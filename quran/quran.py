import json
import requests


class Quran:
    """ Class designed to fetch one complete translation, tafsir, recitation or ayah text of whole Quran. """

    def __init__(self):
        """Initialize"""

        self.api = 'https://api.quran.com/api/v4/quran' 
    
    def get_chapter(self, chapter_number, script=1):
        """Get script of a specific surah."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"

        response = requests.get(f"{self.api}/verses/{script}?chapter_number={chapter_number}")
        return json.loads(response.text)

    def get_juz(self, juz_number, script=1):
        """Get script of a specific juz."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"        

        response = requests.get(f"{self.api}/verses/{script}?juz_number={juz_number}")
        return json.loads(response.text)

    def get_page(self, page_number, script=1):
        """Get script of a specific page."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"

        response = requests.get(f"{self.api}/verses/{script}?page_number={page_number}")
        return json.loads(response.text)

    def get_hizb(self, hizb_number, script=1):
        """Get script of a specific hizab."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"

        response = requests.get(f"{self.api}/verses/{script}?hizb_number={hizb_number}")
        return json.loads(response.text)    

    def get_rub(self, rub_number, script=1):
        """Get script of a specific rub."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"

        response = requests.get(f"{self.api}/verses/{script}?rub_number={rub_number}")
        return json.loads(response.text)  

    def get_verse(self, verse_key, script=1):
        """Get script of a specific verse."""
        if script == 1:
            script = "imlaei"
        elif script == 2:
            script = "imlaei_simple"
        elif script == 3:
            script = "indopak"
        elif script == 4:
            script = "uthmani"
        elif script == 5:
            script = "uthmani_simple"
        elif script == 6:
            script = "uthmani_tajweed"

        response = requests.get(f"{self.api}/verses/{script}?verse_key={verse_key}")
        return json.loads(response.text)   