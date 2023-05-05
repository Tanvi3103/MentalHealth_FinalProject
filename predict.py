import streamlit as st
import pickle
import numpy as np 


with open('pickle_model.pkl', 'rb') as file:
    model = pickle.load(file)
  

def show_predict_page():

    # Title 
    st.title("Take a quick test")

    benefits_0=("I don't know","No","Not eligible for coverage","Yes")  #0 to 3
    coverage_1=("I am not sure","No","Yes") # 4 to 6
    resources_2=("I don't know","No","Yes") # 7 to 9 
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

    X= np.zeros(shape=(120))


    #Q8
    consequences_for_coworkers=st.selectbox("Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?",consequences_for_coworkers_7)
    if (consequences_for_coworkers=="No"):
        X[0]=1 
    else:
        X[0]=0   

    #Q26
    treatment=st.selectbox("Have you ever sought treatment for a mental health issue from a mental health professional?",treatment_26)
    if (treatment=="Yes"):
        X[1]=1
    else:
        X[1]=0   
    
    # Q1
    benefits=st.selectbox("Does your employer provide mental health benefits as part of healthcare coverage?",benefits_0)

    if (benefits=="I don't know"):
        X[2]=1
    elif (benefits=="No"):
        X[3]=1
    elif (benefits=="Not eligible for coverage"):
        X[4]=1   
    else:
        X[5]=1         

    #Q2
    coverage=st.selectbox("Do you know the options for mental health care available under your employer-provided coverage?",coverage_1)
    if (coverage=="I am not sure"):
        X[6]=1
    elif (coverage=="No"):
        X[7]=1 
    else:
        X[8]=1   

    #Q3
    resources=st.selectbox("Does your employer offer resources to learn more about mental health concerns and options for seeking help?",resources_2)
    if (resources=="I don't know"):
        X[9]=1
    elif (resources=="No"):
        X[10]=1 
    else:
        X[11]=1   

    #Q4
    leave=st.selectbox("If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:",leave_3)
    if (leave=="I don't know"):
        X[12]=1
    elif (leave=="Neither easy nor difficult"):
        X[13]=1
    elif (leave=="Somewhat difficult"):
        X[14]=1  
    elif (leave=="Somewhat easy"):
        X[15]=1 
    elif (leave=="Very difficult"):
        X[16]=1   
    else:
        X[17]=1   

    #Q5
    consequences_m=st.selectbox("Do you think that discussing a mental health disorder with your employer would have negative consequences?",consequences_m_4)
    if (consequences_m=="Maybe"):
        X[18]=1
    elif (consequences_m=="No"):
        X[19]=1  
    else:
        X[20]=1   

    #Q6
    consequences_h=st.selectbox("Do you think that discussing a physical health issue with your employer would have negative consequences?",consequences_h_5)
    if (consequences_h=="Maybe"):
        X[21]=1
    elif (consequences_h=="No"):
        X[22]=1
    elif (consequences_h=="Yes"):
        X[23]=1   
    else:
        X[24]=1   

    #Q7
    attitude=st.selectbox("Do you feel that your employer takes mental health as seriously as physical health?",attitute_6)
    if (attitude=="No"):
        X[25]=1
    else:
        X[26]=1   

    #Q9
    previous_employers=st.selectbox("Do you have previous employers?",previous_employers_8)
    if (previous_employers=="No"):
        X[27]=1 
    else:
        X[28]=1 

    #Q10
    benefits_previous_employer=st.selectbox("Have your previous employers provided mental health benefits?",benefits_previous_employer_9)
    if (benefits_previous_employer=="I don't know"):
        X[29]=1
    elif (benefits_previous_employer=="No, none did"):
        X[30]=1
    elif (benefits_previous_employer=="Some did"):
        X[31]=1   
    else:
        X[32]=1   

    #Q11
    options=st.selectbox("Were you aware of the options for mental health care provided by your previous employers?",options_10)
    if (benefits=="I don't know"):
        X[33]=1
    elif (benefits=="No"):
        X[34]=1
    elif (benefits=="Not eligible for coverage"):
        X[35]=1   
    else:
        X[36]=1   
    
    #Q12
    formal_discussion_wellness=st.selectbox("Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?",formal_discussion_wellness_11)
    if (formal_discussion_wellness=="I was aware of some"):
        X[37]=1
    elif (formal_discussion_wellness=="N/A (not currently aware)"):
        X[38]=1
    elif (formal_discussion_wellness=="No, I only became aware later"):
        X[39]=1   
    else:
        X[40]=1   

    #Q13
    anonymity=st.selectbox("Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?",anonymity_12)
    if (anonymity=="I don't know"):
        X[41]=1
    elif (anonymity=="Sometimes"):
        X[42]=1
    elif (anonymity=="Yes"):
        X[43]=1   
    else:
        X[44]=1   

    #Q14
    consequences_m_previous_employer=st.selectbox("Do you think that discussing a mental health disorder with previous employers would have negative consequences?",consequences_m_previous_employer_13)
    if (consequences_m_previous_employer=="I don't know"):
        X[45]=1
    elif (consequences_m_previous_employer=="None of them"):
        X[46]=1
    elif (consequences_m_previous_employer=="Some of them"):
        X[47]=1   
    else:
        X[48]=1   

    #Q15
    willingness=st.selectbox("Would you have been willing to discuss a mental health issue with your direct supervisor(s)?",willingness_14)
    if (willingness=="I don't know"):
        X[49]=1
    elif (willingness=="No, at none of my previous employers"):
        X[50]=1
    elif (willingness=="Some of my previous employers"):
        X[51]=1   
    else:
        X[52]=1   
    
    #Q16
    attitute_previous_employer=st.selectbox("Did you feel that your previous employers took mental health as seriously as physical health?",attitute_previous_employer_15)
    if (attitute_previous_employer=="I don't know"):
        X[53]=1
    elif (attitute_previous_employer=="None did"):
        X[54]=1
    elif (attitute_previous_employer=="Some did"):
        X[55]=1   
    else:
        X[56]=1   

    #Q17
    consequences_for_coworkers_previous_employer=st.selectbox("Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces?",consequences_for_coworkers_previous_employer_16)
    if (consequences_for_coworkers_previous_employer=="None of them"):
        X[57]=1
    elif (consequences_for_coworkers_previous_employer=="Some of them"):
        X[58]=1
    else:
        X[59]=1   
    
    #Q18
    potential_employer_interview=st.selectbox("Would you bring up a mental health issue with a potential employer in an interview?",potential_employer_interview_17)
    if (potential_employer_interview=="Maybe"):
        X[60]=1
    elif (potential_employer_interview=="No"):
        X[61]=1
    else:
        X[62]=1   

    #Q19
    hurt_your_career=st.selectbox("Do you feel that being identified as a person with a mental health issue would hurt your career?",hurt_your_career_18)
    if (hurt_your_career=="Maybe"):
        X[63]=1
    elif ( hurt_your_career=="No, I don't think it would"):
        X[64]=1
    elif ( hurt_your_career=="No, it has not"):
        X[65]=1  
    elif ( hurt_your_career=="Yes, I think it would"):
        X[66]=1   
    else:
        X[67]=1   

    #Q20    
    attitue_coworkers=st.selectbox("Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?",attitue_coworkers_19)
    if (attitue_coworkers=="Maybe"):
        X[68]=1
    elif (attitue_coworkers=="No, I don't think it would"):
        X[69]=1
    elif (attitue_coworkers=="No, it has not"):
        X[70]=1  
    elif (attitue_coworkers=="Yes, I think it would"):
        X[71]=1   
    elif (attitue_coworkers=="Yes, I think it would"):
        X[72]=1   
    else:
        X[73]=1 

    #Q21
    willingness_to_share=st.selectbox("How willing would you be to share with friends and family that you have a mental illness?",willingness_to_share_20)
    if (willingness_to_share=="Neutral"):
        X[74]=1
    elif (willingness_to_share=="Not applicable to me (I do not have a mental illness)"):
        X[75]=1
    elif (willingness_to_share=="Not open at all"):
        X[76]=1
    elif (willingness_to_share=="Somewhat not open"):
        X[77]=1   
    elif (willingness_to_share=="Somewhat open"):
        X[78]=1
    else:
        X[79]=1   

    #Q22
    observation=st.selectbox("Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?",observation_21)
    if (observation=="Maybe/Not sure"):
        X[80]=1
    elif (observation=="No"):
        X[81]=1
    elif (observation=="Yes, I experienced"):
        X[82]=1   
    else:
        X[83]=1   

    #Q23
    family_history=st.selectbox("Do you have a family history of mental illness?",family_history_22)
    if (family_history=="I don't know"):
        X[84]=1
    elif (family_history=="No"):
        X[85]=1
    else:
        X[86]=1   

    #Q24   
    past_history=st.selectbox("Have you had a mental health disorder in the past",past_history_23)
    if (past_history=="Maybe"):
        X[87]=1
    elif (past_history=="No"):
        X[88]=1   
    else:
        X[89]=1   

    #Q25
    current_state=st.selectbox("Do you currently have a mental health disorder?",current_state_24)
    if (current_state=="Maybe"):
        X[90]=1
    elif (current_state=="No"):
        X[91]=1   
    else:
        X[92]=1  

    #Q27
    interference=st.selectbox("If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?",interference_27)
    if (interference=="Never"):
        X[93]=1
    elif (interference=="Not applicable to me"):
        X[94]=1
    elif (interference=="Often"):
        X[95]=1 
    elif (interference=="Rarely"):
        X[96]=1   
    else:
        X[97]=1   

    #Q28
    interference_when_not_trated=st.selectbox("If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?",interference_when_not_trated_28)
    if (interference_when_not_trated=="Never"):
        X[98]=1
    elif (interference_when_not_trated=="Not applicable to me"):
        X[99]=1
    elif (interference_when_not_trated=="Often"):
        X[100]=1 
    elif (interference_when_not_trated=="Rarely"):
        X[101]=1   
    else:
        X[102]=1 

    #Q29
    gender=st.selectbox("What is your gender?",gender_29)
    if (gender=="Male"):
        X[103]=1
    elif (gender=="Female"):
        X[104]=1
    else:
        X[105]=1   

    #Q30
    country_of_residence=st.selectbox("What country do you live in?",country_of_residence_30)
    if (country_of_residence=="Australia"):
        X[106]=1
    elif (country_of_residence=="Canada"):
        X[107]=1
    elif (country_of_residence=="Germany"):
        X[108]=1
    elif (country_of_residence=="Netherlands"):
        X[109]=1 
    elif (country_of_residence=="Other"):
        X[110]=1 
    elif (country_of_residence=="United Kingdom"):
        X[111]=1   
    else:
        X[112]=1   

    #Q31
    country_of_work=st.selectbox("What country do you work in?",country_of_work_31)
    if (country_of_work=="Australia"):
        X[113]=1
    elif (country_of_work=="Canada"):
        X[114]=1
    elif (country_of_residence=="Germany"):
        X[115]=1
    elif (country_of_work=="Netherlands"):
        X[116]=1 
    elif (country_of_work=="Other"):
        X[117]=1 
    elif (country_of_work=="United Kingdom"):
        X[119]=1   
    else:
        X[120]=1   

    final_arr=[X]

    pred= st.button("predict")

    if pred:
        pred = model.predict(final_arr)

        st.subheader(f"The prediction is {pred}")
        