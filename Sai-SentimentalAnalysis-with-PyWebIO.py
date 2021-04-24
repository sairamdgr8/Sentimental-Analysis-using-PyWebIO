#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install gradio


# In[2]:


#import gradio as gr
from textblob import TextBlob
from pywebio.platform.flask import webio_view
from flask import Flask,send_from_directory
from pywebio.input import *
from pywebio.output import *

# In[3]:

app=Flask(__name__)

def sentiment_analysis():
    text=input("enter text to know whether the tweet ie positive or negative or neutral: ",type='text')
    x=TextBlob(text)
    
    sentiment_polarity=x.sentiment.polarity
    
    #sentiment_polarity_output=[(0,["positive","negative","nuetral"])]
    
    if sentiment_polarity>0:
        put_text("The given tweet looks : positive")
    elif sentiment_polarity<0:
        put_text("The given tweet looks : negative")
    elif sentiment_polarity==0:
        put_text("The given tweet looks : neutral")
        
app.add_url_rule('/predict','webio_view',webio_view(sentiment_analysis),
                 methods=['GET','POST','OPTIONS'])



#app.run(host='localhost',port=80)

if __name__="__main__":
    parser
    
        
        
        
        
        
        
        
            
    
    
    
    
    
    
    
    
    
    
    



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






#if __name__=='__main__':
#    sentiment_analysis()
    
    

# In[ ]:




