
# coding: utf-8

# In[1]:

import nltk
from urllib import urlopen


# In[11]:

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


# In[12]:

html = urlopen(url).read()


# In[13]:

html


# In[6]:

from bs4 import BeautifulSoup
web_str = BeautifulSoup(html).get_text()


# In[7]:

web_str


# In[14]:

from bs4 import BeautifulSoup


# In[15]:

web_str = BeautifulSoup(html).get_text()


# In[16]:

web_str


# In[25]:

start = web_str.find("Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.")


# In[26]:

end = web_str.find("CPython is managed by the non-profit Python Software Foundation.")


# In[27]:

last_sent = len("CPython is managed by the non-profit Python Software Foundation.")


# In[28]:

intro = web_str[start:end+last_sent]


# In[29]:

intro_tokens = nltk.word_tokenize(intro)


# In[30]:

intro_tokens


# In[24]:

print intro_tokens


# In[ ]:



