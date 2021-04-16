import json
import requests

class Chapter:
    """chapters list/info"""

    def __init__(self):
        """Initialize"""

        self.api = 'https://api.quran.com/api/v4/chapters' 

    def chapters_list(self, lang='en'):
        """Get list of chapters"""

        response = requests.get(f"{self.api}?language={lang}")
        return json.loads(response.text)

    def get_ichapter(self, chapter_id, lang='en'):
        """Get details of a single chapter."""

        response = requests.get(f"{self.api}/{chapter_id}?language={lang}")
        return json.loads(response.text)

    def chapter_info(self, chapter_id, lang='en'):
        """Get Chapter Info in specific language. Default to English."""

        response = requests.get(f"{self.api}/{chapter_id}/info?language={lang}")
        return json.loads(response.text)        

