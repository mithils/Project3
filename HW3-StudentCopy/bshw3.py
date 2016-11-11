# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
import operator
from bs4 import BeautifulSoup
import re
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
x = open('project3.html','w')
soup_99 = BeautifulSoup(r.text, 'html.parser')
print (soup_99.prettify())
changes = soup_99.prettify() #Initializes changes varialbe to have prettify
text_replace = changes.replace('student', 'AMAZING student') #Replaces string with another string
img_replace = text_replace.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'media/test1.jpg')
logo_replace = img_replace.replace('logo2.png', 'media/logo.png') #Replaces an image with another image
x.write(logo_replace)
x.close()
