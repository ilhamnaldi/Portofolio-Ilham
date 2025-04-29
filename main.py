import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Sidebar for navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150)
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Projects", "Skills", "Experience", "Contact"])

# Main content
if page == "Home":
    st.title("Welcome to Ilham's Portfolio")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300", width=300)
    
    with col2:
        st.header("About Me")
        st.write("""
        Hello! I'm a passionate developer with expertise in web development, 
        data science, and machine learning. I love building applications that solve real-world problems.
        
        This portfolio showcases some of my projects and skills.
        """)
        
        with open("assets/CV Ilham Rinaldi_0125.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="CV Ilham Rinaldi_0125.pdf",
                mime="application/pdf"
        )

elif page == "Projects":
    st.title("My Projects")

    # Project: Interactive Sales Dashboard with Matplotlib
    with st.expander("Project: Interactive Sales Dashboard (Matplotlib)"):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("https://via.placeholder.com/150/0af/fff.png?text=Sales+Chart", width=150)
        with col2:
            st.subheader("Interactive Sales Dashboard (Matplotlib)")
            st.write("This dashboard shows monthly sales trends by region using matplotlib.")
            st.write("**Technologies used:** Python, Pandas, Matplotlib, Streamlit")

        # Sample data
        data = {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 3,
            "Region": ["West"] * 6 + ["Central"] * 6 + ["East"] * 6,
            "Sales": [250, 300, 280, 350, 400, 420, 200, 230, 210, 280, 310, 330, 180, 220, 200, 260, 290, 310]
        }
        df = pd.DataFrame(data)

        # Interactivity
        selected_region = st.selectbox("Select Region", df["Region"].unique())
        filtered_df = df[df["Region"] == selected_region]

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(filtered_df["Month"], filtered_df["Sales"], marker='o', linestyle='-')
        ax.set_title(f"Monthly Sales in {selected_region} Region")
        ax.set_xlabel("Month")
        ax.set_ylabel("Sales")
        ax.grid(True)

        st.pyplot(fig)

elif page == "Skills":
    st.title("My Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Programming Languages")
        for skill, level in [("Python", 90), ("SQL", 80)]:
            st.write(f"{skill}")
            st.progress(level)
    
    with col2:
        st.subheader("Frameworks & Tools")
        for skill, level in [("React", 85), ("Django", 80), ("Docker", 75), ("AWS", 70)]:
            st.write(f"{skill}")
            st.progress(level)

elif page == "Experience":
    st.title("Work Experience")

    with st.container():
        st.subheader("Upstream Operation Lead at PT. Elevasi Agri Indonesia (Elevarm)")
        st.write("May 2023 – Present")
        st.write("""
        - Created SOPs for all core business functions.
        - Managed Yarnen (financing) projects averaging 650M IDR/month.
        - Built internal tools for manufacturing, inventory, and bookkeeping (3B+ IDR recorded).
        - Developed Yarnen scoring system for KYC, reducing overdue projects by 40%.
        - Led 7 team members; reported to CTO.
        """)

    with st.container():
        st.subheader("Business Development at PT. Elevasi Agri Indonesia (Elevarm)")
        st.write("June 2022 – May 2023")
        st.write("""
        - Designed farmer journey and funnel for 10,000+ farmers.
        - Piloted Yarnen program (8.2B IDR GMV, 2,500+ farmers).
        - Analyzed 89 commodities’ models; led market expansion in Java regions.
        """)

    with st.container():
        st.subheader("Business Development at PT. Neura Cipta Nusantara (Neurafarm)")
        st.write("May 2021 – May 2022")
        st.write("""
        - Piloted trading and partnership programs (350M+ IDR GMV).
        - Launched agri-inputs consignment with 45 stores (550M+ IDR GMV).
        - First full-time employee; reported to CEO.
        """)

    with st.container():
        st.subheader("Business Development at Perum Jasa Tirta II")
        st.write("Aug 2020 – Feb 2021")
        st.write("""
        - Learned ISO 31000, Malcolm Baldrige, and KPKU scoring.
        - Produced 10+ internal GCG and risk videos.
        - Mentored by senior Risk Manager.
        """)

    with st.container():
        st.subheader("CEO & Founder at Garfaria")
        st.write("Sep 2018 – Dec 2020")
        st.write("""
        - Led 4-member team; built hydroponic system for 1,000 plant sites.
        - Secured 20M IDR grant from Ministry of Education & Culture.
        """)

    with open("assets/CV Ilham Rinaldi_0125.pdf", "rb") as file:
        st.download_button(
            label="📄 Download CV Ilham Rinaldi",
            data=file,
            file_name="CV_Ilham_Rinaldi.pdf",
            mime="application/pdf"
        )


elif page == "Contact":
    st.title("Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success("Thank you for your message! I'll get back to you soon.")
    
    st.header("Connect with me")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/ilhamrinaldi/)")
    with col2:
        st.markdown("[GitHub](https://github.com/ilhamnaldi)")

# Footer
st.markdown("---")
st.markdown("© 2025 My Portfolio. All rights reserved.")
