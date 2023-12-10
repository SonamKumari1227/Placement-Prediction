
import pandas as pd
import streamlit as st
import pickle


st.title('Placement Predictor')
mymodel=pickle.load(open('Placement.pkl','rb'))


name = st.text_input("Enter your name (required)")
print(name)
if not name:
  st.warning("Please fill out so required fields")
def chekPlacement(m1,m2,m3,m4):
        res=mymodel.predict([[m1,m2,m3,m4]])
        return res

m1=st.number_input("Enter SSC_Percentage")
m2=st.number_input("Enter hSC_Percentage")
m3=st.number_input("Enter degree_Percentage")
m4=st.number_input("Enter emp_test_Percentage")



if st.button("output"):
    
    res=chekPlacement(m1,m2,m3,m4)
    st.write(res[0])