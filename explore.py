import streamlit as st

def show_explore_page():

    with st.container():
        st.header(":violet[Let's explore more about Mindfullness and Mental Wellbeing!]")
        st.markdown("  ")
        st.markdown("Here's a list of resources about mental health in software industry")
        
    st.write(" ")

    with st.container():
        st.subheader("Books")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://m.media-amazon.com/images/I/41qfPgTdcPL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg")
            st.markdown("[Hope and help your nerves](%s)" % "https://www.amazon.com/Hope-Help-Your-Nerves-Anxiety/dp/0593201906?dchild=1&keywords=Hope+and+Help+for+Your+Nerves&qid=1623358416&sr=8-1&linkCode=ll1&tag=mental-health-books-06-20&linkId=af1ef0403d4f6e0489cc63749fce7b2f&language=en_US&ref_=as_li_ss_tl&ascsubtag=a127bd67-4a0b-4c70-a37d-d4466692d38c&correlationId=a127bd67-4a0b-4c70-a37d-d4466692d38c")
        with col2:
            st.image("https://m.media-amazon.com/images/I/41T-XHe8-EL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg")
            st.markdown("[The Body Keeps the Score](%s)" % "https://www.amazon.com/Hope-Help-Your-Nerves-Anxiety/dp/0593201906?dchild=1&keywords=Hope+and+Help+for+Your+Nerves&qid=1623358416&sr=8-1&linkCode=ll1&tag=mental-health-books-06-20&linkId=af1ef0403d4f6e0489cc63749fce7b2f&language=en_US&ref_=as_li_ss_tl&ascsubtag=a127bd67-4a0b-4c70-a37d-d4466692d38c&correlationId=a127bd67-4a0b-4c70-a37d-d4466692d38c")
        with col3:
            st.image("https://m.media-amazon.com/images/I/41gpJRAQ3CL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg")
            st.markdown("[50 Things To Do Before Seeing a Psychiatrist](%s)" % "https://www.amazon.com/dp/099849660X/ref=sspa_dk_detail_3?psc=1&pd_rd_i=099849660X&pd_rd_w=wrrhv&content-id=amzn1.sym.eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_p=eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_r=CV8DME0A1PAFRN3Y4GVK&pd_rd_wg=Fnb8F&pd_rd_r=eefcca0a-cf2e-4a4b-a37c-6abe8a96fa51&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw")
     
    st.write(" ") 
    
    with st.container():
        st.subheader("Articles")
        st.markdown("[A Programmers Guide To Stress - By Daragh Byrne](%s)"%"http://codingmindfully.com/a-programmers-guide-to-stress/")
        st.markdown("[Are You More Than Okay: The State Of Mental Health In Tech In 2016 - By Julia Nguyen](%s)"%"https://modelviewculture.com/pieces/are-you-more-than-okay-the-state-of-mental-health-in-tech-in-2016")
        st.markdown("[How To Keep Your Mental Health In Check When You Work From Home - By WeWorkRemotely](%s)"%"https://weworkremotely.com/how-to-keep-your-mental-health-in-check-when-you-work-from-home")
        st.markdown("[Encouraging Wellness in a Remote Workpalce - By Desi Rottman](%s)"%"https://dev.to/desi/encouraging-wellness-in-a-remote-workplace-17m5")
        st.markdown("[Do Not Disturb - By Joe Bell](%s)"%"https://joebell.co.uk/blog/do-not-disturb/")
        st.markdown("[Intro To Meditation For Coders - By Abe Dolinger](%s)"%"https://dev.to/256hz/intro-to-meditation-for-coders-1p6f")
    
    st.write(" ")
    with st.container():
        st.subheader("Applications")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://www.verywellmind.com/thmb/ZWddbIwSXKItZuGACLHN9D8TrEg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-5c796d62c9e77c000136a710.png")
            st.markdown("[Headspace](%s)" % "https://www.headspace.com/")
            
            st.image("https://www.verywellmind.com/thmb/7FMBXI_BMkCq36tAYMvArzzpR8E=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-1-5c796daa46e0fb00011bf2dd.png")
            st.markdown("[Insight Timer](%s)" % "https://insighttimer.com/")
 
        with col2:
            st.image("https://www.verywellmind.com/thmb/sdTg8tGwXoJZBipaNe_BihSGPCo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-5c796de846e0fb0001edc7fb.png")
            st.markdown("[Smiling mind](%s)" % "https://www.smilingmind.com.au/")

            st.image("https://www.verywellmind.com/thmb/gnd5GbPrdZisGB0eqsJ4VPnvSQg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-1-5c796ed646e0fb000140a417.png")
            st.markdown("[Stop, Breathe, Think](%s)" % "https://www.stopbreathethink.com/")
  
        with col3:
            st.image("https://www.verywellmind.com/thmb/TlNBV1cNEvDcgAbzVBWbn6fD134=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-5c796f06c9e77c00011c835e.png")
            st.markdown("[Calm](%s)" % "https://www.calm.com/")
            
            st.image("https://www.verywellmind.com/thmb/2OO_h-J7KRTGvSg1dWHfiSSLcRA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1200x630wa-1-5c796f3146e0fb0001a98381.png")
            st.markdown("[Aura](%s)" % "https://www.aurahealth.io/")
  
    
    st.write("  ")
    st.write("  ")
    with st.container():
        st.subheader("Organizations")
        st.markdown("[Hack Mental Health - The intersection of mental health and technology](%s)"%"https://www.hackmentalhealth.care/")
        st.markdown("[OSMI - Open Sourcing Mental Illness is a non-profit, corporation dedicated to raising awareness, educating, and providing resources to support mental wellness in the tech and open source communities](%s)"%"https://osmihelp.org/")
        st.markdown("[SelfCare.Tech - A repository of self-care resources for developers & others](%s)"%"http://selfcare.tech/")
        st.markdown("[MHPrompt - Let's start a conversation about mental health in tech](%s)"%"http://mhprompt.org/")
        st.markdown("[Everybody Has A Brain - Everybody Has A Brain is about creating opportunities for dialogue around personal mental health](%s)"%"http://everybodyhasabrain.com/")
        st.markdown("[](%s)"%"")

    st.write("  ")

    with st.container():
        st.subheader("Podcasts")
        st.markdown("[Emotional Intelligence And Ethics In Tech - By April Wensel in the Happy Porch podcast](%s)"%"http://happyporchradio.com/season-4-episode-3-april-wensel/")
        st.markdown("[Jerk Programmer To Compassionate Coder - By April Wensel in the Ardent Development podcast](%s)"%"http://ardentdev.com/011-jerk-programmer-compassionate-coder-april-wensel")

    st.write("  ")

    with st.container():
        st.subheader("Conferences")
        st.markdown("[Computing And Mental Health - Bringing together communities](%s)"%"http://mentalhealth.media.mit.edu/")
        st.markdown("[Anxiety Tech](%s)"%"http://www.anxietytech.com/")
       
    st.write("  ")

    st.divider()
    with st.container():
        st.caption("A project by B.Tech EXTC students.")