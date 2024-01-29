import os
import requests
from paradise.common.logger import setup_logger


# Instance of the shared logger
logger = setup_logger(__name__)

def download_mp3(url, filepath):
    try:
        logger.info(f"Starting download of MP3 from {url}")

        # Create directory if it does not exist
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            logger.info(f"Created directory for {filepath}")

        # Send an HTTP GET request to download the MP3 file
        response = requests.get(url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the file in 'wb' mode to write binary data
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    # Write the data to the file if there is data
                    if chunk:
                        file.write(chunk)
            logger.info(f"Successfully downloaded MP3 to {filepath}")
            return filepath
        else:
            logger.warning(f"File download failed, URL might be problematic: {url}")
            return 'File download failed, URL might be problematic.'
    except Exception as e:
        logger.error(f"An error occurred during download: {e}")
        return f'An error occurred: {e}'
