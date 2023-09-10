import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model

# Set the page to wide mode
st.set_page_config(layout="wide")

# Title for the web app
st.title("Perform Descriptive Statistics Application")
st.markdown("<strong>The application reads the first <em>ROW</em> in your file as the <em>Column Title (Variable Name)</em> for each <em>COLUMN</em> in the dataset. So make sure that the first <em>ROW</em> in your file is the name of each <em>Column Title (Variable Name)</em> in the dataset. Also, make sure that every cell in your file is Valid (all cells are filled and there are no duplicates) for better analysis.</strong>", unsafe_allow_html=True)
st.markdown("<strong>This application allows you to Perform Descriptive Statistics, such as Grouping Column names, and see the Descriptive Statistics visualization Results (Sum, Mean, Median, etc). This can helps businesses, industry, trade, and other sectors.</strong>", unsafe_allow_html=True)

# Upload file
file_format = st.radio('Select file format:', ('csv', 'excel'), key='file_format')
dataset = st.file_uploader(label = '')

use_defo = st.checkbox('Use example Dataset')
if use_defo:
    dataset = r'day.csv'
    st.write("[Dataset Explanation Link](https://drive.google.com/file/d/16l1-ObGv6n3j0qUwy6VyY4BOmTCzmCqO/view?usp=sharing)")

if dataset:
    if file_format == 'csv' or use_defo:
        df = pd.read_csv(dataset)
    else:
        df = pd.read_excel(dataset)

    # Display the DataFrame
    st.write("Dataset:")
    st.dataframe(df)

    # Select the target variable (y) and the independent variables (X)
    independent_variables = st.multiselect("Select Independent Variables (X) ~ groupby", df.columns.tolist())
    target_variable = st.selectbox("Select the Target Variable (y)", df.columns)

    if st.button("Perform Descriptive Statistic"):
        a = df.groupby(independent_variables)[target_variable].sum()
        st.markdown("<br>", unsafe_allow_html=True)

        st.write(a.describe(include="all"))
        st.markdown("<br>", unsafe_allow_html=True)

        st.write("= = = =")
        # SUM
        st.write(f"Sum Table with column: {independent_variables} , {target_variable}")
        st.dataframe(a, width=9999)
        st.markdown("<br>", unsafe_allow_html=True)

        if len(independent_variables) == 1:
            st.write(f"Sum Bar Chart with column: {independent_variables} , {target_variable}")
            st.bar_chart(a, width=9999)

        st.write("= = = =")    
        # Mean
        st.write(f"Mean Table with column: {independent_variables} , {target_variable}")
        b = df.groupby(independent_variables)[target_variable].mean()
        b = round(b, 2)
        st.dataframe(b, width=9999)
        st.markdown("<br><br>", unsafe_allow_html=True)

        if len(independent_variables) == 1:
            st.write(f"Mean Bar Chart with column: {independent_variables} , {target_variable}")
            st.bar_chart(b, width=9999)

        st.write("= = = =")
        #Median
        st.write(f"Median Table with column: {independent_variables} , {target_variable}")
        c = df.groupby(independent_variables)[target_variable].median()
        c = round(c, 2)
        st.dataframe(c, width=9999)
        st.markdown("<br><br>", unsafe_allow_html=True)

        if len(independent_variables) == 1:
            st.write(f"Median Bar Chart with column: {independent_variables} , {target_variable}")
            st.bar_chart(c, width=9999)

st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <a href="https://www.linkedin.com/in/glenhans/" style="text-align: center; font-size: 24px;"> Connect with me😄 </a>
    </div>
    """, unsafe_allow_html=True)
