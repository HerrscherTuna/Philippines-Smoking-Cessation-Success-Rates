import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PH Smoking Cessation Dashboard", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("cleaned_cessation_data.csv")

df = load_data()


st.sidebar.header("Filter Data")
gender_filter = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
res_filter = st.sidebar.multiselect("Select Residence", options=df["Residence"].unique(), default=df["Residence"].unique())

filtered_df = df[(df["Gender"].isin(gender_filter)) & (df["Residence"].isin(res_filter))]

st.title("🇵🇭 Smoking Cessation Success Rates")
st.markdown("### Analyzing Data from GATS Philippines 2021")


col1, col2, col3 = st.columns(3)
col1.metric("Total Quit Attempts Analyzed", len(filtered_df))
col2.metric("Avg Age of Respondent", int(filtered_df["Age"].mean()))
col3.metric("Primary Method", "Quit Alone")


c1, c2 = st.columns(2)

with c1:

    st.subheader("Cessation Success Duration")
    fig1 = px.bar(filtered_df['Success_Unit'].value_counts().reset_index(), 
                  x='Success_Unit', y='count', color='Success_Unit',
                  labels={'count': 'Number of People', 'Success_Unit': 'Duration'},
                  template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

with c2:

    st.subheader("Demographics by Gender")
    fig2 = px.pie(filtered_df, names='Gender', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Methods Used: Counseling vs. Residence")
fig3 = px.histogram(filtered_df, x="Residence", color="Counseling", barmode="group",
                    labels={"Counseling": "Used Clinic Counseling?"})
st.plotly_chart(fig3, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("**Data Source:** [GATS Philippines 2021](https://extranet.who.int/ncdsmicrodata/index.php/catalog/956/related-materials)")
st.sidebar.write("**Data Dictionary:**")
st.sidebar.caption("1. Success_Unit: Duration of abstinence.")
st.sidebar.caption("2. Counseling: Visited cessation clinic.")
st.sidebar.caption("3. Quit_Alone: Stopped without medical help.")