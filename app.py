import streamlit as st

st.set_page_config(page_title="Tarasankar Paul | Data Engineer", layout="wide")

Header

st.title("Tarasankar Paul") st.subheader("Data Engineer | AWS | Spark | ETL")

st.write("📍 Kolkata, India") st.write("📞 9830368552 | ✉️ tarasankarpaul03@gmail.com") st.markdown("LinkedIn | GitHub")

Summary

st.header("Professional Summary") st.write(""" Data Engineer with 5 years of experience designing and building scalable ETL pipelines and data warehousing solutions. Expert in AWS, PySpark, and distributed data systems. Strong background in building optimized data pipelines and working with modern data stack including Airflow, dbt, and Snowflake. """)

Skills

st.header("Technical Skills")

col1, col2, col3 = st.columns(3)

with col1: st.subheader("Programming") st.write("- Python\n- SQL\n- Shell Scripting")

with col2: st.subheader("Big Data") st.write("- Apache Spark\n- PySpark\n- Kafka\n- Hadoop\n- Databricks")

with col3: st.subheader("Cloud & Tools") st.write("- AWS (S3, Glue, Redshift, Athena)\n- Airflow\n- Docker\n- Jenkins\n- Tableau")

Experience

st.header("Professional Experience")

st.subheader("Deloitte | Data Engineer (Aug 2024 – Present)") st.write("""

Built scalable serverless ETL pipelines

Optimized Spark jobs using broadcast joins and salting

Worked on Agentic AI system using LangChain & LangGraph """)


st.subheader("Cognizant | Data Engineer (Nov 2022 – Aug 2024)") st.write("""

Built Airflow-based pipelines with AWS EMR

Improved pipeline efficiency by 30%

Implemented SCD Type 2 using dbt """)


st.subheader("TCS | Data Engineer (Mar 2021 – Nov 2022)") st.write("""

Developed PySpark pipelines on Hadoop

Automated monitoring using shell scripts """)


Certifications

st.header("Certifications") st.write("""

AWS Solutions Architect Associate (2024)

AWS Cloud Practitioner (2023)

Databricks Data Engineer Associate (2024) """)


Education

st.header("Education") st.write(""" B.Tech in Computer Science Cooch Behar Government Engineering College CGPA: 7.89 """)

Footer

st.markdown("---") st.write("Built with ❤️ using Streamlit")
