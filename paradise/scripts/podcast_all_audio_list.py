import requests
import xml.etree.ElementTree as ET
from paradise.common.mp3_downloader import download_mp3


class PodcastFeed:
    def __init__(self, term):
        self.term = term
        self.channel = None
        self.episode = None
        self.feed_url = None
        self.audio_list = []


        self.get_podcast_info()

    def get_podcast_info(self):
        # self.turn => channel name
        url = f'https://itunes.apple.com/search?term={self.term}'
        r = requests.get(url).json()

        if 'results' in r and len(r['results']) > 0:
            result = r['results'][0]
            self.channel = result.get('collectionName')
            self.episode = result.get('trackCount')
            self.feed_url = result.get('feedUrl')

    def get_audio_list(self):
        if self.feed_url is not None:
            response = requests.get(self.feed_url)

            if response.status_code == 200:
                xml_content = response.text
                root = ET.fromstring(xml_content)

                enclosures = root.findall('.//enclosure')

                for enclosure in enclosures:
                    url_attribute = enclosure.attrib.get('url')
                    self.audio_list.append(url_attribute)
                
                return self.audio_list
            else:
                print(f"Failed to retrieve XML file. Status code: {response.status_code}")
        else:
            print("Feed URL is not available.")

        return []  # if feed_url is None，return empty list
    
    def download(self):

        for i in range(0, len(audio_list)):
            
            download_mp3(self.audio_list[i],f'mp3/{len(audio_list)-i}.mp3')


term_to_search = 'gooaye-%E8%82%A1%E7%99%8C'
podcast_feed = PodcastFeed(term_to_search)
audio_list = podcast_feed.get_audio_list()

print('Audio List:',len(audio_list))

download = podcast_feed.download()
