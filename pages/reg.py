import streamlit as st
with st.form(key='my_form_to_submit'):
    st.write('Please fill out the form below')
    name = st.text_input('Name')
    email = st.text_input('Email')

    password = st.text_input('password',type=('password'))
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    pass