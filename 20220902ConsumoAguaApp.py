#ConsumoAguaApp.py

import streamlit as st
import pandas as pd
import numpy as np
from gsheetsdb import connect
#
st.title('Consumo de agua en FCQ')
#

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
#st.write(rows)
for row in rows:
    st.write([row.Fecha])
