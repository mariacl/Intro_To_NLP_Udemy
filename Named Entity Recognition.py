
# coding: utf-8

# In[1]:

import nltk


# In[2]:

text = open("C:\Users\conchita\Downloads\example.txt").read().decode('utf-8')


# In[3]:

text


# In[4]:

text_tag = nltk.pos_tag(nltk.word_tokenize(text))


# In[5]:

text_ch = nltk.ne_chunk(text_tag)


# In[8]:

text_ch[:10]


# In[9]:

for chunk in text_ch:
    if hasattr(chunk,'label'):
        print chunk.label(), " ".join (c[0] for c in chunk.leaves())


# In[ ]:



