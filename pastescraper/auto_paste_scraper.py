#auto pastebin scraper

import time
import pastebin_scraper

START_TIME = time.time()
END_TIME = START_TIME + 38400
LAST_TIME = START_TIME
VECTOR = 1200

pastebin_scraper.run()

while time.time() < END_TIME:
    if LAST_TIME+VECTOR < time.time():
    	pastebin_scraper.run()
    	LAST_TIME = time.time() + VECTOR