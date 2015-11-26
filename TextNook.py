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

#Task -- Storing Title, Date, Comments and No of likes of each post in a file named solution.txt
for everything in soup.find_all("aside", {"class" : "widget widget_archive"}):
	title = list() #Storing titles of all blogs in the current month
	date = list() #Date
	comment = list() #Comment
	for link in everything.find_all("a"):
		url = link.get('href')
		content = urllib2.urlopen(url).read()
		soupLink = BeautifulSoup(content)

		#Title
		for everything in soupLink.find_all("h1", {"class" : "entry-title"}):
		 	temp = ''.join(everything.findAll(text=True))
		 	title.append(temp.encode('utf8') + "\n")
		#End of Task 1 

		#Date
		for everything in soupLink.find_all("time", {"class" : "entry-date"}):
			temp = ''.join(everything.findAll(text=True))
			date.append(temp.encode('utf8') + "\n")
		#End of Task 2

		#Commenrs
		for everything in soupLink.find_all("h1", {"class" : "entry-title"}):
			link = everything.find_all('a')[0].get('href')
			content = urllib2.urlopen(link).read()
			soupOpen = BeautifulSoup(content)
			comments = ""
			for i, c in enumerate(soupOpen.find_all("div", {'comment-content'})):
				temp = ''.join(c.find_all(text=True))
				comments +="Comment#%d: "%(i+1)+temp.encode('utf8') + "\n"
			comment.append(comments)
		#End of Task 3
		for i in xrange(len(title)):
			infile.write("Title:"+title[i])
			infile.write("Date:"+date[i])
			infile.write("Comments:\n"+comment[i])
			infile.write("\n\n\n")
infile.close();