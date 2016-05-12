
# coding: utf-8

# In[1]:

import nltk


# In[2]:

text ="I walked to the cafe to buy coffee before work."


# In[3]:

text


# In[4]:

tokens = nltk.word_tokenize(text)


# In[5]:

tokens


# In[6]:

nltk.pos_tag(tokens)


# In[8]:

nltk.help.upenn_tagset()


# In[9]:

nltk.pos_tag(nltk.word_tokenize("I will have desert."))


# In[10]:

nltk.pos_tag(nltk.word_tokenize("They will desert us."))


# In[14]:

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")


# In[23]:

md_norm = [word.lower() for word in md if word.isalpha()]


# In[24]:

md_tags = nltk.pos_tag(md_norm, tagset="universal")


# In[25]:

md_tags[:5]


# In[29]:

md_nouns = [word[0] for word in md_tags if word[1] == "NOUN"]


# In[30]:

md_nouns[:20]


# In[31]:

nouns_fd = nltk.FreqDist(md_nouns)


# In[33]:

nouns_fd.most_common(10)


# In[ ]:



