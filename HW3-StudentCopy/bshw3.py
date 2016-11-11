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
changes = soup_99.prettify()
text_replace = changes.replace('student', 'AMAZING student')
img_replace = text_replace.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'media/test1.jpg')
logo_replace = img_replace.replace('logo2.png', 'media/logo.png')

##
##
####Part A
##list_a = []
##soup = BeautifulSoup(r.text, 'html.parser')
##title = soup.find_all('div', {'class' : 'field-item even'})
##for word in title:
##    if word.p:
##        soup.append(word.text.replace('student', 'AMAZING student'))
##title_1 = soup.find_all('a', {'class': 'menu__link'})
##for side in title_1:
##    if side['href']:
##        soup.append(side.text.replace('student', 'AMAZING student'))        
###print (soup)
##
####Part B
##
##title_1 = soup.find_all('div', {'class' : 'field-item even'})
##old_image_src = 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg'
##new = soup.prettify()
##new_image = new.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'test1.jpg')
###print (new_image)
####Part C
x.write(logo_replace)
#x.write(img_replace)
#x.write(logo_replace)
x.close()
