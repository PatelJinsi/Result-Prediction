import streamlit as st
import requests

st.title(" Result Predictor ")

lastGrade=st.slider("Last Grade" ,0,100,7)
studyHours=st.slider("Study Hours",0,24,4)


if st.button("Predict"):
    url="http://127.0.0.1:4000/predict"
    
    data = {
        "last grade" : lastGrade,
        "study hours" : studyHours,
        }
    
    response=requests.post(url,json=data)
    result=response.json()
    
    if result['prediction'] == 1:
        st.success("You will pass")
    else :
        st.error("not likely to be pass")