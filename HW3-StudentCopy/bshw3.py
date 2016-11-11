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
##Part A
list_a = []
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find_all('div', {'class' : 'field-item even'})
for  word in title:
    if word.p:
        soup.append(word.text.replace('student', 'AMAZING student'))
print (soup)

##Part B
title_1 = soup.find_all('div', {'class' : 'field-item even'})
for picture in title_1:
    if picture.img:
        soup.append
##Part C
