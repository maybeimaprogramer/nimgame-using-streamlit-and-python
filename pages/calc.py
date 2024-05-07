import streamlit as st
# with st.form(key='my_form_to_submit'):
a:int = st.number_input("Enter a number 1 ")
b:int = st.number_input("Enter a number 2")
  #  submit_button = st.form_submit_button(label='Submit')
# if submit_button:
if a and b:
    sum:int=int(a) + int(b)
    st.write("the sum is",sum)
    def add (a:int,b:int) -> int:
       return a+b
    st.write("the sum is",add(int(a),int(b)))
