import json
import requests


class Translation:
    """ Get a single a single chapter or ayah. """

    def __init__(self):
        """Initialize"""

        self.api_1 = 'https://api.quran.com/api/v4/resources/translations'
        self.api_2 = 'https://api.quran.com/api/v4/quran/translations'

    def list_translations(self, lang="en"):
        """Get list of available translations.""" 

        response = requests.get(f"{self.api_1}?language={lang}")
        return json.loads(response.text)

    def get_tchapter(self, chapter_number, translation_id=20):
        """Get information of a specific translation.""" 

        response = requests.get(f"{self.api_2}/{translation_id}?chapter_number={chapter_number}")
        return json.loads(response.text)
    
    def get_tverse(self, verse_key, translation_id=20):
        """Get translation of a specific ayah."""

        response = requests.get(f"{self.api_2}/{translation_id}?verse_key={verse_key}")
        return json.loads(response.text)