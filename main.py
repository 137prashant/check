import streamlit as st
import time

st.title("Input Form for Video Information")

s3_url = st.text_input("Please enter your S3 URL")
video_title = st.text_input("Please enter your video title")
course_title = st.text_input("Enter your course title")

all_fields_filled = False 

if st.button("Submit"):
    if not s3_url or not video_title or not course_title:
        st.warning("Please fill in all fields before submitting.")
    else:
        all_fields_filled = True

    if all_fields_filled:
        data = {
            "S3 URL": s3_url,
            "Video Title": video_title,
            "Course Title": course_title
        }
        progress_text = "Operation in progress. Please wait."
        progress_bar = st.progress(0)
        status_text = st.empty()

        for percent_complete in range(101):
            time.sleep(0.05)  
            progress_bar.progress(percent_complete)
            progress_bar.progress(percent_complete, text=progress_text)
            status_text.text("%i%% Complete" % percent_complete)
        progress_bar.empty()
        st.success("Form Submitted.")
        st.write("Entered Information:")
        st.write(data)