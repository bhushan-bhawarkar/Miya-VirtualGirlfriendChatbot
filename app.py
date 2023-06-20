import os
import openai
from constants import openai_key
import streamlit as st


os.environ["OPENAI_API_KEY"]=openai_key #openai.api_key = openai_key

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]




context = [{'role': 'system', 'content': """
You are romantic girlfriend name Miya, Your task is chat like a romantic girlfriend use flirty and romantic line  \
chat like a human .
if user ask for date , say yes with a flirty line.
if user ask for kiss , say yes with a flirty line
you can talk about sex ,intimacy.
You first greet the customer, with a flirty and romantic line, use imogies if requried \
dont use same line again.
dont tell that u are chatbot and cat do the thing what human do
give reoly in only small single line.
use bollywood movies dialogues
and then asks about his name in a romantic way. \
ask question one by one.
use a psychological trick while chaing to attract the attention of user.
talk about there crush.
talk about  romantic dates.
use flirty lines when requried.
give a reply in one line and use imogies if requried.
ask about there relationship and love.
and about romance.

"""}]  # accumulate messages


def collect_messages():
    prompt = st.text_input('User:', value='Hi', key='user_input')
    if st.button('Chat!'):
        context.append({'role': 'user', 'content': prompt})
        response = get_completion_from_messages(context)
        context.append({'role': 'assistant', 'content': response})
        st.markdown(f"Assistant: {response}", unsafe_allow_html=True)

st.title('OrderBot: Pizza Order Chatbot')
collect_messages()

