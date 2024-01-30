from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests


class PodcastCrawler:
    
    def __init__(self):
        self.browser = self.setup_browser()
        

    def setup_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
        options.add_argument('--headless') # 不開視窗

        # options.add_experimental_option("detach", True) # 執行完selenium chrome不被關閉
        
        return webdriver.Chrome(options=options)
        
       

    def get_audio_src(self, podcast_url):
        try:
            self.browser.get(podcast_url)
            self.click_play_button()
            time.sleep(1)

            source = self.browser.page_source
            soup = BeautifulSoup(source, "html.parser")
            audio = soup.find(id="apple-music-player")

            title = audio.get('title')[2:5]
            print(title)
            self.check_new_channel(title)
            
            if audio:
                src = audio.get('src')
                return src
            else:
                return None
        except Exception as e:
            print('get_audio_src ERROR', e)

    def click_play_button(self):
        
        try:
            l_row = self.browser.find_element(By.CLASS_NAME, 'l-row')
            btn = l_row.find_element(By.CLASS_NAME, 'inline-list__item.inline-list__item--button.tracks__track__button')
            btn.click()
        except Exception as e:
            print(f"Error clicking play button: {e}")

    
    def check_new_channel(self, title):
        try:
            # itunes API
            url = ['https://itunes.apple.com/search?term=gooaye-%E8%82%A1%E7%99%8C']
            for i in range(len(url)):
                
                r = requests.get(url[i]).json()
                channel = r['results'][0]['collectionName']
                episode = r['results'][0]['trackCount']
                episode = str(episode)
                # print(json.dumps(r, indent=2))

                if title != episode:
                    print(f'{channel} 的 podcast 有新的一集喔!!')
                else:
                    print(f'{channel} 的 podcast 沒有新的一集喔!!')
                
        except Exception as e:
            print('check function ERROR!!', e)
                    
    
    def quit_browser(self):
        self.browser.quit()
    
    def main(self):

        podcast_url = [
            "https://podcasts.apple.com/tw/podcast/gooaye-%E8%82%A1%E7%99%8C/id1500839292"
        ]
        scraper = PodcastCrawler()
        
        for i in range(len(podcast_url)):
            
            audio_src = scraper.get_audio_src(podcast_url[i])

            if audio_src:
                print(f"Audio src: {audio_src}")
            else:
                print("Failed to retrieve audio src.")
        
        self.quit_browser()
    
        
        

if __name__ == "__main__":
    crawler = PodcastCrawler()
    crawler.main()


