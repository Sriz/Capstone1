# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:03:50 2023

@author: srizn
"""

import openai
import streamlit as st
from streamlit_chat import message

openai_api_key = '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'




def friends_bot(HeaderMsg, IntroMsg, PromptMsg, temp):
        st.header(HeaderMsg)
        IntroMsg
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
            {"role": "system", "content": PromptMsg}
            ]
        #if ownFlag == False:
         #   with st.expander(ExpanderMsg):
          #      st.image(ExpanderImageLink, width = 250)
        if prompt := st.chat_input():
            openai.api_key = openai_api_key
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages, temperature = temp)
            msg = response.choices[0].message
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg.content)
            
            total_tokens = response.usage.total_tokens
            
            cost = total_tokens * 0.002 / 1000
            return(cost)
            #st.write('Cost: $',cost)
        



def main():
    with st.container():
        #st.title('Unified Bot Management Streamlit App')
        with st.sidebar:
            st.image('https://openclipart.org/image/400px/307415', width = 200)
            #choice = st.sidebar.selectbox("Who would you like to chat with?", Pages)
            #temp = st.slider('Select temperature value', min_value = 0, max_value = 20)
            
            with st.form("my_form"):
               st.write("Create your own bot")
               BotName = st.text_input("Enter your bot name")
               temp = st.slider("Select temperature value", min_value = 0, max_value = 20)
               prompt_value = st.text_input('Enter a description of the chat bot (prompt).')
               file = st.file_uploader('Upload a file', label_visibility="visible")
               #checkbox_val = st.checkbox("Form checkbox")
               submitted = st.form_submit_button("Submit")
        
        
        cost = friends_bot("Let's chat with", BotName, prompt_value, temp)
       
        st.sidebar.write('Cost: $', cost)
                   
       

    
    
        
    
    
if __name__ == "__main__":
    main()    
      
        