import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Tarasankar Paul",
    page_icon="📊",
    layout="wide"
)

# --- SIDEBAR ---
st.sidebar.title("Tarasankar Paul")
st.sidebar.caption("Data Engineer")

section = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Skills", "Projects", "Experience", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit")

# --- HOME ---
if section == "Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("Tarasankar Paul")
        st.subheader("Data Engineer | AWS | Spark | ETL")

        st.write("""
        I build scalable data pipelines, optimize big data systems, 
        and turn raw data into reliable, production-grade platforms.
        """)

        st.markdown("### 🚀 What I Do")
        st.write("""
        - Design large-scale ETL pipelines  
        - Optimize Spark jobs (TB-scale data)  
        - Build real-time streaming systems  
        - Work with AWS + Snowflake ecosystems  
        """)

    with col2:
        st.image("https://via.placeholder.com/250", caption="Profile Photo")

    st.markdown("---")

    # Metrics section
    col1, col2, col3 = st.columns(3)
    col1.metric("Experience", "5+ Years")
    col2.metric("Data Processed", "1TB+")
    col3.metric("Projects", "10+")

# --- ABOUT ---
elif section == "About":
    st.header("About Me")

    st.write("""
    I'm a Data Engineer focused on building efficient and scalable data systems.
    
    Over the years, I've worked on large-scale data processing, handled real-time
    streaming pipelines, and optimized distributed systems for performance.
    """)

    st.markdown("### 💡 Core Strengths")
    st.write("""
    - Distributed data processing  
    - Data pipeline architecture  
    - Performance tuning in Spark  
    - Cloud-native solutions (AWS)  
    """)

# --- SKILLS ---
elif section == "Skills":
    st.header("Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Languages")
        st.write("""
        - Python  
        - SQL  
        """)

    with col2:
        st.subheader("Big Data")
        st.write("""
        - Spark  
        - PySpark  
        - Kafka  
        """)

    with col3:
        st.subheader("Cloud & Tools")
        st.write("""
        - AWS (S3, Glue, EMR)  
        - Snowflake  
        - dbt  
        - Airflow  
        """)

# --- PROJECTS ---
elif section == "Projects":
    st.header("Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔹 Real-Time Data Pipeline")
        st.write("""
        Built using Spark Structured Streaming and Kafka to process live user events.
        """)

        st.subheader("🔹 CDC Pipeline")
        st.write("""
        Designed a pipeline to handle insert, update, delete events efficiently.
        """)

    with col2:
        st.subheader("🔹 Data Lake on AWS")
        st.write("""
        Built scalable data lake using S3, Glue, Athena.
        """)

        st.subheader("🔹 Spark Optimization")
        st.write("""
        Improved job performance using partitioning, broadcast joins, and caching.
        """)

# --- EXPERIENCE ---
elif section == "Experience":
    st.header("Experience")

    st.subheader("Data Engineer")
    st.caption("Company Name | 2021 - Present")

    st.write("""
    - Built large-scale ETL pipelines processing TB-level data  
    - Reduced job runtime by optimizing Spark transformations  
    - Designed real-time streaming pipelines  
    """)

    st.markdown("---")

    st.subheader("Associate Data Engineer")
    st.caption("Previous Company | 2019 - 2021")

    st.write("""
    - Developed batch pipelines using PySpark  
    - Worked on SQL-based transformations  
    - Supported data warehouse systems  
    """)

# --- CONTACT ---
elif section == "Contact":
    st.header("Contact")

    st.write("📧 Email: your_email@gmail.com")
    st.write("🔗 LinkedIn: https://linkedin.com/in/your-profile")
    st.write("💻 GitHub: https://github.com/your-username")

    st.markdown("### 📄 Resume")
    with open("resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Tarasankar_Paul_Resume.pdf",
            mime="application/pdf"
        )

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Tarasankar Paul | Built with Streamlit")
