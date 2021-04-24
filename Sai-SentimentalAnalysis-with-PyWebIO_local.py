#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install gradio


# In[2]:


#import gradio as gr
from textblob import TextBlob
from pywebio.input import *
from pywebio.output import *

# In[3]:

def sentiment_analysis():
    text=input("enter text to know whether the tweet ie positive or negative or neutral: ",type='text')
    x=TextBlob(text)
    
    sentiment_polarity=x.sentiment.polarity
    
    #sentiment_polarity_output=[(0,["positive","negative","nuetral"])]
    
    if sentiment_polarity>0:
        put_text("The given tweet looks:positive")
    elif sentiment_polarity<0:
        put_text("The given tweet looks:negative")
    elif sentiment_polarity==0:
        put_text("The given tweet looks:neutral")
        
            
    
    
    
    
    
    
    
    
    
    
    



#def greet(text):
#    x=TextBlob(text)
#    if x.sentiment.polarity>0:
#        return "The given tweet looks:positive"
#    elif x.sentiment.polarity<0:
#        return "The given tweet looks:negative"
#    else:
#        return "The given tweet looks:neutral"
#iface=gr.Interface(fn=greet,inputs="text",outputs="text")
#iface.launch()






if __name__=='__main__':
    sentiment_analysis()
    
    

# In[ ]:




