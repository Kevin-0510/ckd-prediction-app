import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    file_path = "ckd-dataset-v2.csv"  # Make sure the file is in the same directory as your Streamlit app
    df = pd.read_csv(file_path)

    # Ensure Patient ID column exists (if not, create one)
    if "patient_id" not in df.columns:
        df["patient_id"] = df.index + 1  # Assign unique IDs

    return df

df = load_data()  # Load the data once


# Function to get patient details
def get_patient_details(patient_id):
    patient_data = df[df["patient_id"] == patient_id]  # Filter by ID

    if patient_data.empty:
        return {"error": "Patient ID not found."}

    # Extract CKD Stage & Condition
    ckd_stage = patient_data["stage"].values[0]  # CKD Stage
    ckd_condition = patient_data["class"].values[0]  # CKD or Not

    return {
        "Patient ID": patient_id,
        "CKD Stage": ckd_stage,
        "Condition": ckd_condition
    }


# 🎯 **Streamlit UI**
st.title("🔍 CKD Stage & Condition Finder")

# User Input for Patient ID
patient_id = st.number_input("Enter Patient ID:", min_value=1, step=1)

if st.button("Find CKD Stage"):
    result = get_patient_details(patient_id)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"✅ Patient ID: {result['Patient ID']}")
        st.info(f"📌 CKD Stage: {result['CKD Stage']}")
        st.warning(f"⚠️ Condition: {result['Condition']}")  # Shows CKD or Not CKD
