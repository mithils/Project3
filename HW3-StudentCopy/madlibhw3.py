# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import random
import nltk
import re
import pprint
nltk.download('punkt')
from nltk.book import *
from nltk import word_tokenize, sent_tokenize
print("START*******")
text = text2[:50]
print (text)
print("\n\nEND*******")
