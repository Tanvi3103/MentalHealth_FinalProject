import streamlit as st
import pickle
import numpy as np 


with open('pickle_model.pkl', 'rb') as file:
    model = pickle.load(file)
  


def show_predict_page():
    st.title("Prediction")

    benefits_0=("I don't know","No","Not eligible for coverage","Yes") 
    coverage_1=("I am not sure","No","Yes")
    resources_2=("I don't know","No","Yes")
    leave_3=("I don't know","Neither easy nor difficult","Somewhat difficult","Somewhat easy","Very difficult","Very easy")
    consequences_m_4=('Maybe', 'No', 'Yes')
    consequences_h_5=( 'Maybe', 'No', 'Yes', "I don't know")
    attitute_6=( 'No', 'Yes')
    consequences_for_coworkers_7=('No', 'Yes')
    previous_employers_8=('No', 'Yes')
    benefits_previous_employer_9=("I don't know", 'No, none did', 'Some did', 'Yes, they all did')
    options_10=('I was aware of some','N/A (not currently aware)', 'No, I only became aware later', 'Yes, I was aware of all of them')
    formal_discussion_wellness_11=("I don't know", 'None did', 'Some did', 'Yes, they all did' )
    anonymity_12=("I don't know", 'No', 'Sometimes', 'Yes, always')  
    consequences_m_previous_employer_13=( "I don't know", 'None of them', 'Some of them', 'Yes, all of them')
    willingness_14=("I don't know", 'No, at none of my previous employers', 'Some of my previous employers', 'Yes, at all of my previous employers')
    attitute_previous_employer_15=("I don't know", 'None did', 'Some did', 'Yes, they all did' )
    consequences_for_coworkers_previous_employer_16=('None of them', 'Some of them', 'Yes, all of them')
    potential_employer_interview_17=('Maybe', 'No', 'Yes')
    hurt_your_career_18=('Maybe', "No, I don't think it would", 'No, it has not', 'Yes, I think it would', 'Yes, it has')
    attitue_coworkers_19=('Maybe', "No, I don't think they would", 'No, they do not', 'Yes, I think they would', 'Yes, they do')
    willingness_to_share_20=( 'Neutral', 'Not applicable to me (I do not have a mental illness)', 'Not open at all', 'Somewhat not open', 'Somewhat open', 'Very open')
    observation_21=('Maybe/Not sure', 'No', 'Yes, I experienced', 'Yes, I observed')
    family_history_22=("I don't know", 'No', 'Yes')
    past_history_23=( 'Maybe', 'No', 'Yes')
    current_state_24=('Maybe', 'No', 'Yes')
    treatment_26=("Yes","No")
    interference_27=('Never', 'Not applicable to me', 'Often', 'Rarely', 'Sometimes')
    interference_when_not_trated_28=('Never', 'Not applicable to me', 'Often', 'Rarely', 'Sometimes')
    gender_29=('Female', 'Male', 'Other')
    country_of_residence_30=( 'Australia', 'Canada', 'Germany', 'Netherlands', 'Other', 'United Kingdom', 'United States of America')
    country_of_work_31=('Australia', 'Canada', 'Germany', 'Netherlands', 'Other', 'Sweden', 'United Kingdom', 'United States of America')

    X= np.zeros(shape=(1, 120))

    benefits=st.selectbox("Does your employer provide mental health benefits as part of healthcare coverage?",benefits_0)
    coverage=st.selectbox("Do you know the options for mental health care available under your employer-provided coverage?",coverage_1)
    resources=st.selectbox("Does your employer offer resources to learn more about mental health concerns and options for seeking help?",resources_2)
    leave=st.selectbox("If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:",leave_3)
    consequences_m=st.selectbox("Do you think that discussing a mental health disorder with your employer would have negative consequences?",consequences_m_4)
    consequences_h=st.selectbox("Do you think that discussing a physical health issue with your employer would have negative consequences?",consequences_h_5)
    attitute=st.selectbox("Do you feel that your employer takes mental health as seriously as physical health?",attitute_6)
    consequences_for_coworkers=st.selectbox("Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?",consequences_for_coworkers_7)
    previous_employers=st.selectbox("Do you have previous employers?",previous_employers_8)
    benefits_previous_employer=st.selectbox("Have your previous employers provided mental health benefits?",benefits_previous_employer_9)
    options=st.selectbox("Were you aware of the options for mental health care provided by your previous employers?",options_10)
    formal_discussion_wellness=st.selectbox("Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?",formal_discussion_wellness_11)
    anonymity=st.selectbox("Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?",anonymity_12)
    consequences_m_previous_employer=st.selectbox("Do you think that discussing a mental health disorder with previous employers would have negative consequences?",consequences_m_previous_employer_13)
    willingness=st.selectbox("Would you have been willing to discuss a mental health issue with your direct supervisor(s)?",willingness_14)
    attitute_previous_employer=st.selectbox("Did you feel that your previous employers took mental health as seriously as physical health?",attitute_previous_employer_15)
    consequences_for_coworkers_previous_employer=st.selectbox("Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces?",consequences_for_coworkers_previous_employer_16)
    potential_employer_interview=st.selectbox("Would you bring up a mental health issue with a potential employer in an interview?",potential_employer_interview_17)
    hurt_your_career=st.selectbox("Do you feel that being identified as a person with a mental health issue would hurt your career?",hurt_your_career_18)
    attitue_coworkers=st.selectbox("Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?",attitue_coworkers_19)
    willingness_to_share=st.selectbox("How willing would you be to share with friends and family that you have a mental illness?",willingness_to_share_20)
    observation=st.selectbox("Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?",observation_21)
    family_history=st.selectbox("Do you have a family history of mental illness?",family_history_22)
    past_history=st.selectbox("Have you had a mental health disorder in the past",past_history_23)
    current_state=st.selectbox("Do you currently have a mental health disorder?",current_state_24)
    treatment=st.selectbox("Have you ever sought treatment for a mental health issue from a mental health professional?",treatment_26)
    interference=st.selectbox("If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?",interference_27)
    interference_when_not_trated=st.selectbox("If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?",interference_when_not_trated_28)
    gender=st.selectbox("What is your gender?",gender_29)
    country_of_residence=st.selectbox("What country do you live in?",country_of_residence_30)
    country_of_work=st.selectbox("What country do you work in?",country_of_work_31)

    pred= st.button("predict")

    if pred:
        pred = model.predict(X)
        st.subheader(f"The prediction is {pred[0]}")
        