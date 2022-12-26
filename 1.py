#!/usr/bin/env python
# coding: utf-8

# In[26]:


import re # regular expression library
import nltk # natural language toolkit library
import string


# In[27]:


original_text = """Artificial intelligence is human like intelligence.
                   It is the study of intelligent artificial agents.
                   Science and engineering to produce intelligent machines.
                   Solve problems and have intelligence.
                   Related to intelligent behavior.
                   Developing of reasoning machines.
                   Learn from mistakes and successes.
                   Artificial Intelligence is related to reasoning in everyday situations."""


# In[28]:


original_text


# In[29]:


original_text = re.sub(r'\s+', ' ', original_text)


# In[46]:


original_text


# In[47]:


nltk.download('punkt')


# In[56]:


nltk.download('stopwords')


# In[76]:


stopwords = nltk.corpus.stopwords.words('english') #these are the words in english that have no value and we are going to remve them
#print(stopwords)
#len(stopwords)


# In[78]:


string.punctuation


# In[83]:


def preprocess(text): # defining our function and it recieves Text as parameter and will do 3 things for us (lower case, tokenize and removal of the punctuation)
    formatted_text = text.lower() # this function lower here makes the texts in Lowercase (firts function)
    
    tokens = [] # made new variable which includes each one of the words we have in the string
    for token in nltk.word_tokenize(formatted_text):
        tokens.append(token)
        #print(tokens)
    
    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation] #check the tokens variable and remove the one that matches in stopwords and that matches in punctuations
    
    
    formatted_text = ' '.join(element for element in tokens)
    
    return formatted_text


# In[84]:


formatted_text = preprocess(original_text) #now make a variable to implement our function to the text we want
formatted_text


# In[ ]:





# In[ ]:




