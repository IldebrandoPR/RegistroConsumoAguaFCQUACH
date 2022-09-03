#ConsumoAguaApp.py

import streamlit as st
import pandas as pd
import numpy as np
from gsheetsdb import connect
#
st.title('Consumo de agua en FCQ')
#

# Create a connection object.
DATE_COLUMN = 'Fecha'
sheet_url = st.secrets["public_gsheets_url"]
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache
def load_data(nrows):
    data = pd.read_csv(sheet_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
data = load_data(5)
st.subheader('Raw data')
st.write(data)

# Print results.
#st.write(rows)
#for row in rows:
#    st.write(f"{row.name} has a :{row.pet}:")
