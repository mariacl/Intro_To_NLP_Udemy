
# coding: utf-8

# In[1]:

import nltk


# In[2]:

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")


# In[4]:

md_22 = md[:22]


# In[5]:

md_22


# In[6]:

for word in md_22:
    if word.isalpha():
        print word


# In[7]:

for word in md_22:
    print word.lower()


# In[10]:

norm = [word.lower() for word in md_22 if word.isalpha()]


# In[11]:

norm


# In[12]:

porter = nltk.PorterStemmer()


# In[19]:

my_list = ["cat", "cats", "lie", "lying","run","running", "city","cities","month","monthly","woman", "women"]


# In[20]:

my_list


# In[21]:

for word in my_list:
    print porter.stem(word)


# In[22]:

lancaster = nltk.LancasterStemmer()


# In[24]:

for word in my_list:
    print lancaster.stem(word)


# In[25]:

wnlem = nltk.WordNetLemmatizer()


# In[26]:

for word in my_list:
    print wnlem.lemmatize(word)


# In[ ]:



