import pandas as pd
import numpy as np
import pickle

import streamlit as st
pickle_in=open('di.pkl','rb')
lm=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
       BMI,DiabetesPedigreeFunction,Age):
    

    prediction=lm.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
       BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return (prediction)



def main():
    st.title('Varsha home')
    html_temp=""
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies=float(st.text_input("Pregnancies",0))
    Glucose=float(st.text_input("Glucose",0))
    BloodPressure=float(st.text_input("BloodPressure",0))
    SkinThickness=float(st.text_input("SkinThickness",0))

    Insulin=float(st.text_input("Insulin",0))
    BMI=float(st.text_input("BMI",0))
    DiabetesPedigreeFunction=float(st.text_input("DiabetesPedigreeFunction",0))
    Age=float(st.text_input("Age",0))
    result=0
    y=""
    if st.button("Predict"):
        
        result=predict_note_authentication(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
       BMI,DiabetesPedigreeFunction,Age)
       
        
        if result[0]==0:
           y="The person is non Diabetic"
        else:
            y="The person is Diabetic"  
        print(y) 
            
    st.success((format(y)))    
    if(st.button("about")):
        st.text("Lets Learn")
        st.text("built")

    



if __name__=='__main__':
     main()