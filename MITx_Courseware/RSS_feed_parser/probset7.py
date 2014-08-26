# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class NewsStory:
    
    def __init__(self,guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title
    
    def getSubject(self):
        return self.subject
    
    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link
    
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
        #self.text = " winn lose , wine's loses WINnnerwin."
    def isWordIn(self,text):
        text = text.lower()
        #print text
        for punctuation in string.punctuation:
            text = text.replace(punctuation, " ")
        text = text.split(" ")
        if self.word in text:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())
    
class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())
    
class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self,story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self,story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
    
class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self,story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
        
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
        
    def evaluate(self,story):
 #       if self.phrase in story.getSubject():
  #          return True
   #     elif self.phrase in story.getTitle():
    #        return True
     #   elif self.phrase in story.getSummary():
      #      return True
       # else:
        #    return False
        return self.phrase in story.getTitle() or self.phrase in story.getSummary() or self.phrase in story.getSubject()

gjh = NewsStory('', '', "something something new york city", '', '')

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    #return stories
    storylist = []
    #print stories
    #print triggerlist
    for story in stories:
        for trig in triggerlist:
            if trig.evaluate(story):
                storylist.append(story)
    
    return set(storylist)

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTriggerF(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    if triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
    
    elif triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
                                        
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
        
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(params[0])
        
    elif triggerType == "PHRASE":
        phrase = ""
        for i in params:
            phrase += i + " "
        triggerMap[name] = PhraseTrigger(phrase)
            
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[str(params[0])], triggerMap[params[1]])

        
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[str(params[0])], triggerMap[params[1]])
        
    return triggerMap[name]        
                                                
        
def makeTrigger(triggerMap, triggerType, params, name):
    triggerTypeStr = triggerType.capitalize() + "Trigger"    
    if triggerType == 'PHRASE':
        trigger = eval(triggerTypeStr + "('" + ' '.join(params) + "')")
    elif triggerType in ['TITLE', 'SUBJECT', 'SUMMARY']:
        trigger = eval(triggerTypeStr + "('" + ''.join(params) + "')")
    else:        
        newParams = []
        for param in params:
            newParams.append("triggerMap['" + param + "']")
            
        trigger = eval(triggerTypeStr + "(" + ','.join(newParams) + ")")
        
    triggerMap[name] = trigger        
    return trigger


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    #print triggerfile.readlines()
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])
    
    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        #triggerlist = readTriggerConfig("C:/Users/Jordan/Desktop/triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)
    
    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("My RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

