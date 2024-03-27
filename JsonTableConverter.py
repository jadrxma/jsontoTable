import streamlit as st
import pandas as pd
import json

# Title of your Streamlit app
st.title("JSON to Table Converter")

# File uploader allows user to add their own JSON
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])
if uploaded_file is not None:
    # Read the file and load it as JSON
    data = json.load(uploaded_file)
    
    # Assuming the JSON structure is as described, convert it to a DataFrame
    # We'll first normalize the JSON to create a flat table
    records = []
    for item in data:
        record = item['data']  # This extracts the data object
        record['id'] = item['id']  # Add the 'id' field to the record
        records.append(record)
    
    df = pd.DataFrame.from_records(records)
    
    # Display the DataFrame as a table in the Streamlit app
    st.table(df)

