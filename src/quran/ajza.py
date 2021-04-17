import json
import requests

class Ajza:
    """Ajza/juzs list"""

    def __init__(self):
        """Initialize"""
        
        self.api = 'https://api.quran.com/api/v4/juzs' 

    def juzs_list(self, lang='en'):
        """Get list of all ajza/juzs"""

        response = requests.get(f"{self.api}?language={lang}")
        return json.loads(response.text)

    def get_ijuz(self, juz_id, lang='en'):
        """Get details of a single juz."""

        response = requests.get(f"{self.api}/{juz_id}?language={lang}")
        return json.loads(response.text)