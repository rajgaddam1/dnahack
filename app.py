# -*- coding: utf-8 -*-
import streamlit as st
from urllib.parse import urlparse
#import psycopg2
import os
#import pandas as pd
import snowflake.connector
import warnings 
warnings.filterwarnings("ignore")

st.title("DNA Hackathon", anchor=None)

selected_database = st.selectbox("Select the Databse Name", ("None","student", "employee"))
st.write(selected_database)

selected_schema = st.selectbox("Select the Schema Name", ("None","info", "contact"))
st.write(selected_schema)

first_name = st.text_input('Enter your First Name')
st.write(first_name)

last_name = st.text_input('Enter your Last Name')
st.write(last_name)

email_id = st.text_input('Enter your Email')
st.write(email_id)

contact_no = st.text_input('Enter your Contact Number')
st.write(contact_no)

address = st.text_input('Enter your Address')
st.write(address)

if st.button("submit"):
    st.write('Adde to the database')
