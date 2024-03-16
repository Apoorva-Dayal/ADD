"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Alzheimer Detection by AAP")

    # Add image to the home page
    st.image("./images/Alzheimer image.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
            Alzheimer's disease is a progressive neurodegenerative disorder that primarily affects cognition, leading to memory loss, impaired reasoning, and changes in behavior. It is the most common cause of dementia, a syndrome characterized by a decline in cognitive function severe enough to interfere with daily life. Named after Dr. Alois Alzheimer, who first described the condition in 1906, Alzheimer's disease has become a significant global health concern due to its prevalence and the profound impact it has on individuals and their families.
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Causes and Risk Factors:
Genetics: While most cases of Alzheimer's disease occur sporadically, genetic factors play a role, particularly in familial cases. Mutations in certain genes, such as the amyloid precursor protein (APP), presenilin 1 (PSEN1), and presenilin 2 (PSEN2), have been linked to early-onset familial Alzheimer's disease.<br>
Age: Advancing age is the greatest risk factor for Alzheimer's disease. The prevalence of the condition increases significantly with age, particularly after the age of 65.<br>
Environmental Factors: Certain environmental factors, such as traumatic brain injury, cardiovascular disease, diabetes, and low educational attainment, have been associated with an increased risk of Alzheimer's disease. """, unsafe_allow_html=True)