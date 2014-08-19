#pastebin scraper just because
import re
import urllib2
from BeautifulSoup import BeautifulSoup as BS

def run():
	"""
	scrapes pastebin website for keywords,
	created function for use in autoscraper.
	##can refactor to take in keywords/total pastes to scrape
	"""
	#output file (CHANGE OUTPUT_FILE TO "w+" instead of "a" if you have no pastes.txt or always want a new one)
	OUTPUT = {"password" : [], "secret" : [], "accounts" : []}
	OUTPUT_FILE = open('pastes.txt', 'a+')

	#counter
	COUNT = 0

	#will need soup object to make calls on
	pastebin_archive = BS(urllib2.urlopen("http://freeproxyx.appspot.com/www.pastebin.com/archive"))

	#will iterate through links on page and check if they have a match. 17-523 are past pastes
	#for anchor in pastebing_archive.findAll('a')[15:523:2]:

	#iterates through 44 pastes instead of all as seen above
	for anchor in pastebin_archive.findAll('a')[17:522:2]:
		#url of archived post
		try:
			new_url = "http://freeproxyx.appspot.com/" + (re.search(r'(?<=href="/).*(?=")', str(anchor)).group())
			print new_url
			#create soup and capture content to prevent parsing entire page
			recent_paste_content = BS(urllib2.urlopen(new_url)).findAll('textarea')

			#if content matches query add to set for writing to output_file
			if re.search('minecraft', str(recent_paste_content)) == None:	
				if re.search("password", str(recent_paste_content)) != None and re.search("porn" , str(recent_paste_content)) == None:
					OUTPUT["password"].append(new_url + "\n")
					#lets you know as it's captured
					#print new_url + ' the before mentioned url mentions "password"'
				elif re.search("secret", str(recent_paste_content)) != None and re.search("porn", str(recent_paste_content)) == None:
					OUTPUT["secret"].append(new_url + "\n")
				elif re.search("account", str(recent_paste_content)) != None and re.search("porn", str(recent_paste_content)) == None:
					OUTPUT["accounts"].append(new_url + "\n")
					#print new_url + ' the before mentioned url mentions "secret"'
			COUNT += 1
			print "Scraped " + str(COUNT) + " pastes so far"
		except:
			print "fail on " + new_url
	print
	print
	#write each item to output_file, used set to prevent duplicates 
	print "Writing pastebins containing password"
	for pw in set(OUTPUT["password"]):
		OUTPUT_FILE.write(pw)
		print "Wrote " + str(pw) + " to output_file"

	print "Writing pastebins containing secret"
	for scrt in set(OUTPUT["secret"]):
		OUTPUT_FILE.write(scrt)
		print "Wrote " + str(scrt) + " to output_file"
	OUTPUT_FILE.close()
    #clear space between scrapes






#will need regex to match emails

print
print
print

if __name__ == "__main__":
	run()