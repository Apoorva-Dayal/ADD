"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                Predict the disease by entering the values !!!!! 

            </p>
        """, unsafe_allow_html=True)

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    number_input_A = st.number_input("Response value",0,2639,value=10)
    A = st.slider("Response", int(df["Response"].min()), int(df["Response"].max()),value=number_input_A)
    number_input_B = st.number_input("Gender",0,1,value=0)
    B = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()),value=number_input_B)
    number_input_C = st.number_input("Age",60,98,value=60)
    C = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()),value=number_input_C)
    number_input_D = st.number_input("PNSAS",6,23,value=6)
    D = st.slider("Peripheral Nervous System Activity Scale", int(df["PNSA"].min()), int(df["PNSA"].max()),value=number_input_D)
    number_input_E = st.number_input("SES",1,5,value=1)
    E = st.slider("SES", int(df["SES"].min()), int(df["SES"].max()),value=number_input_E)
    number_input_F = st.number_input("MMSE",4,30,value=4)
    F = st.slider("MMSE", int(df["MMSE"].min()), int(df["MMSE"].max()),value=number_input_F)
    number_input_G = st.number_input("CDR",0,2,value=0)
    G = st.slider("CDR", int(df["CDR"].min()), int(df["CDR"].max()),number_input_G)
    number_input_H = st.number_input("eTIV",1106,2004,value=1106)
    H = st.slider("eTIV", int(df["eTIV"].min()), int(df["eTIV"].max()),number_input_H)
    number_input_I = st.number_input("nWBV",0.64,0.84,value=0.64)
    I = st.slider("nWBV", float(df["nWBV"].min()), float(df["nWBV"].max()),value=number_input_I)
    number_input_J = st.number_input("ASF",0,1,value=0)
    J = st.slider("ASF",int(df["ASF"].min()), int(df["ASF"].max()),value=number_input_J)
    number_input_K = st.number_input("Group",0,2,value=0)
    K = st.slider("Group",int(df["Group"].min()), int(df["Group"].max()),value=number_input_K)
    
    # VALUE ENTERED BY EEG EXPERT
    # st.write("RESPONSE IS ", A)
    st.write("RESPONSE IS ", A)
    st.write("GENDER IS ", B)
    st.write("AGE IS ", C)
    st.write("PNSAS IS ", D)
    st.write("SES IS ", E)
    st.write("MMSE IS ", F)
    st.write("CDR IS ", G)
    st.write("eTIV IS ", H)
    st.write("nWBV IS ", I)
    st.write("ASF IS ", J)
    st.write("GROUP IS ", K)


    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to regular forgetfulness")
        elif (prediction == 2):
            st.warning("The person is prone to mild Alzhiemer")
        elif (prediction == 3):
            st.warning("The person is prone to clinical Alzhiemer")
        elif (prediction == 4):
            st.warning("The person is prone to chronic Alzhiemer")
        elif (prediction == 5):
            st.warning("The person is prone to severe Alzhiemer")
        else:
            st.success("The person has no Alzheimer")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
