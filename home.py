import streamlit as st

def show_home_page():

    with st.container():
        st.subheader(":violet[Mental health Predictor]")

    st.header("**:violet[Welcome!]**")
    #st.divider()

    col1, col2 = st.columns(2)

    with st.container():
        with col1:
            st.image("Resources/img1.png")
            st.subheader(":violet[Take a quiz]")
            st.markdown("Please feel free to take this simple quiz to find out about your mental health. And don't worry, your data is in safe hands!")

        
        with col2:
            st.image("Resources/img2.png")
            st.subheader(":violet[Explore]")
            st.markdown("Your one stop solution to start learning about mental health, mindfulness and wellbeing.")

    st.write("  ")

    st.divider()
    with st.container():
        st.caption("A project by B.Tech EXTC students.")