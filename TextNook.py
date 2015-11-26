# #code goes here
# #importing required files
from bs4 import BeautifulSoup
import urllib2

#accessing required URL
url = "https://textnook.wordpress.com"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
#print soup.prettify()

#opening a file to store the required information
infile = open("solution.txt", "w")

#Task 1 -- To store the title of all the posts in the file named solution.txt
for everything in soup.find_all("h1", {"class" : "entry-title"}):
	temp = ''.join(everything.findAll(text=True))
	infile.write(temp.encode('utf8') + "\n")
#End of Task 1

infile.close();