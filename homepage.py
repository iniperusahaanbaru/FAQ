import streamlit as st
import time

# Set page config for a clean, modern look
st.set_page_config(layout="centered", page_title="Job Finder FAQ")

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def display_faq_talent_pool():
    # Display FAQs for Talent Pool System
    st.write("**FAQ - Talent Pool System**")
    
    faq_talent_pool = {
        "What is this?": (
            "Hello, my name is Hanif Rizkana. I'm a freelance recruiter. "
            "I've experienced both sides as a freelancer and a job seeker. "
            "It's challenging for companies to find the right talent and for job seekers to repeatedly fill out multiple forms, often without responses. "
            "To address this, I created a platform where talents only need to fill out a form once, and then let the right opportunities find them."
        ),
        "How does it work?": (
            "1. Submit Your Profile: Click the join button and fill out the form (it's free).\n"
            "2. Tailored Matches: When companies search for talent, we filter candidates based on their specific needs.\n"
            "3. Job Opportunities: If your skills match, we send your resume to the company and only email you when you're selected."
        ),
        "Who can register for the talent pool?": (
            "Anyone looking for a job can register. Whether you are a recent graduate, a seasoned professional, "
            "or looking to switch careers, our system is designed to help you find the right opportunity."
        ),
        "Is there any cost to join?": (
            "No, it's free, and we aim to keep it free forever."
        ),
        "Can I update my information after joining?": (
            "Yes, you can update your information anytime by filling out the form again with your updated details."
        ),
        "What if I’m no longer looking for a job?": (
            "You can unsubscribe from our talent pool at any time by selecting the 'No' option in the form."
        ),
        "Can I delete my data?": (
            "Yes, just contact us at hanif@qode.world."
        ),
        "How do I know if I’ve been matched with a job?": (
            "You will receive an email notification whenever your profile is matched with a job and has been sent to a recruiter."
        ),
        "Where do the job opportunities come from?": (
            "Currently, our primary partner is Qode (https://qode.world/), but we also source job information from LinkedIn and other social platforms."
        ),
        "How long does it take to get matched with a job?": (
            "The time it takes to get matched with a job varies depending on your profile and the current job openings available. "
            "We strive to match candidates as quickly as possible."
        ),
        "Can I refer friends to the talent pool?": (
            "Yes, we encourage you to refer friends and colleagues to join our talent pool. "
            "The more diverse our talent pool, the better we can match candidates with the right opportunities."
        ),
        "How does this benefit you?": (
            "Yes, we encourage you to refer friends and colleagues to join our talent pool. "
            "The more diverse our talent pool, the better we can match candidates with the right opportunities."
        ),        
        "How can I contact you?": (
            "You can contact me through:\n"
            "WhatsApp: +6285923671003\n"
            "Email: hanif@qode.world\n"
            "Telegram: @Hanif_Recruiter"
        ),
        "What if I have more questions?": (
            "We encourage you to use our chatbot by clicking the button below, "
            "or you can contact me through the provided contact information."
        )
    }

    
    for question, answer in faq_talent_pool.items():
        with st.expander(question):
            st.write(answer)



    st.markdown("""
        <div style='padding-top: 14px;'>
            <a href='https://bit.ly/chatbotfromqa' target='_blank'>
                <button class='chatbot-button'>Ask more here.</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='padding-top: 14px;'>
            <a href='https://bit.ly/form_from_qa' target='_blank'>
                <button class='register-button'>Join! (it's free)</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

display_faq_talent_pool()
