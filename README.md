# quran.py
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Blue_Python_3.8_Shield_Badge.svg">
An easy to use API wrapper for Quran.com written in Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install. ([Git](https://git-scm.com/downloads) required as well.)

```bash
pip install git+https://github.com/Jadtz/quran.py.git
```

## Usage

```python
from quran.verses import Verses
vrs = Verses()

vrs.get_chapter() # returns complete chapter from Quran.
vrs.get_juz() # returns all verses from a specific juz(1-30).
vrs.get_page() # returns all verses of a specific Madani Mushaf page(1 to 604).
vrs.get_hizb() # returns all verses from a specific Hizb( half(1-60).
vrs.get_rub() # returns all verses of a specific Rub number(1-240).
vrs.get_verse() # returns a specific ayah with key.
#example for verse key, "10:5" is 5th ayah of 101th surah.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
