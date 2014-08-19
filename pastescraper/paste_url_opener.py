#pastebin scraper exe!cuter!
import webbrowser

PASTES = "pastes.txt"

def openUrls(pastes):
	"""
	Takes in pastes file and opens each url in a tab
	"""
	pastes = open(pastes, "r+")
	count = 0
	for url in pastes:
		webbrowser.open_new_tab(url)
		count += 1
		print "Opened " + str(count) + " url's so far"



# import timeit
# import threading
# import pastebinscraper

# #start time
# orig_start = timeit.timeit()
# start = timeit.timeit()
# #first scrape

# #other times
# while True:
# 	current = timeit.timeit()
# 	if current > start+1300:
#         start = timeit.time()


openUrls(PASTES)