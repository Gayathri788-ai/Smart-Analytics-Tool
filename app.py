import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Analytics Tool", layout="wide")

st.title("🧠 Smart Analytics Tool")

# Upload file
file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Info")
    st.write(df.describe())

    st.subheader("❌ Missing Values")
    st.write(df.isnull().sum())

    # Clean data
    df = df.dropna()

    st.subheader("📈 Visual Analytics")

    num_cols = df.select_dtypes(include='number').columns

    if len(num_cols) > 0:
        col = st.selectbox("Select Column for Analysis", num_cols)

        fig1 = px.histogram(df, x=col, title="Histogram")
        st.plotly_chart(fig1)

        fig2 = px.box(df, y=col, title="Box Plot")
        st.plotly_chart(fig2)

    # Scatter plot
    if len(num_cols) > 1:
        st.subheader("📉 Relationship Analysis")
        fig3 = px.scatter(df, x=num_cols[0], y=num_cols[1])
        st.plotly_chart(fig3)

    st.success("✅ Analysis Completed Successfully!")
