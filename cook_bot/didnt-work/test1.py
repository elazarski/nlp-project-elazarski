# coding: utf-8
from urllib import request
url = "https://www.allrecipes.com/recipes/?page=1"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
raw
from html.parser import HTMLParser
parser = HTMLParser()
parser.feed(raw)
parser
parser.reset
parser.reset()
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)
    def handle_data(self, data):
        print("Encountered data:", data)
        
myparser = MyHTMLParser()
myparser.feed(raw)
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if not tag == "script":
            print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        if not tag == "script":
            print("Encountered an end tag:", tag)
    def handle_data(self, data):
        print("Encountered data:", data)
        
myparser = MyHTMLParser()
myparser.feed(raw)
class MyHTMLParser(HTMLParser):
    lasttag = ""
    def handle_starttag(self, tag, attrs):
        if not tag == "script":
            print("Encountered a start tag:", tag)
            lasttag = tag
    def handle_endtag(self, tag):
        if not tag == "script":
            print("Encountered an end tag:", tag)
    def handle_data(self, data):
        if lasttag != "script":
            print("Encountered data:", data)
        
from queue import LifoQueue
class MyHTMLParser(HTMLParser):
    lasttag = LifoQueue()
    def handle_starttag(self, tag, attrs):
        if not tag == "script":
            print("Encountered a start tag:", tag)
            lasttag.put(tag)
    def handle_endtag(self, tag):
        if not tag == "script":
            print("Encountered an end tag:", tag)
            lasttag.pop()
    def handle_data(self, data):
        if lasttag.get() != "script":
            print("Encountered data:", data)
        
myparser = MyHTMLParser()
myparser.feed(raw)
class MyHTMLParser(HTMLParser):
    prev_tag = LifoQueue()
    def handle_starttag(self, tag, attrs):
        if tag != "script":
            print("Encountered a start tag:", tag)
        prev_tag.put(tag)
    def handle_endtag(self, tag):
        if tag != "script":
            print("Encountered an end tag:", tag)
        prev_tag.pop()
    def handle_data(self, data):
        if prev_tag.get() != "script":
            print("Encountered data:", data)
        
myparser = MyHTMLParser()
myparser.feed(raw)
class MyHTMLParser(HTMLParser):
    
    def __init__(self, *, covert_charrefs=True):
        self.prev_tag = LifoQueue()
        self.convert_charrefs = convert_charrefs
        self.reset()
    
    def handle_starttag(self, tag, attrs):
        if tag != "script":
            print("Encountered a start tag:", tag)
        self.prev_tag.put(tag)
    def handle_endtag(self, tag):
        if tag != "script":
            print("Encountered an end tag:", tag)
        self.prev_tag.pop()
    def handle_data(self, data):
        if self.prev_tag.get() != "script":
            print("Encountered data:", data)
        
myparser = MyHTMLParser()
class MyHTMLParser(HTMLParser):
    
    def __init__(self, *, convert_charrefs=True):
        self.prev_tag = LifoQueue()
        self.convert_charrefs = convert_charrefs
        self.reset()
    
    def handle_starttag(self, tag, attrs):
        if tag != "script":
            print("Encountered a start tag:", tag)
        self.prev_tag.put(tag)
    def handle_endtag(self, tag):
        if tag != "script":
            print("Encountered an end tag:", tag)
        self.prev_tag.pop()
    def handle_data(self, data):
        if self.prev_tag.get() != "script":
            print("Encountered data:", data)
        
myparser = MyHTMLParser()
myparser.feed(raw)
from bs4 import BeautifulSoup
soup = BeautifulSoup(raw, 'html.parser')
soup.prettify()
soup.title
soup.title.name
soup.title.string
soup.p
soup.findall('div')
soup.find_all('div')
soup.find_all('div', attrs='class')
soup.find_all('div', attrs='center-buttons')
soup.find_all('div', attrs='fixed-recipe-card')
soup.find_all('article', attrs='fixed-recipe-card')
soup.find('article', attrs='fixed-recipe-card')
soup.find_next('article', attrs='fixed-recipe-card')
soup.find_next('article')
soup.find_all_next('article', attrs='fixed-recipe-card')
soup.find_all('article', attrs='fixed-recipe-card')
