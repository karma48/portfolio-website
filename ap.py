# streamlit_app.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":rocket:", layout="centered")

# Custom CSS to center align content and slightly adjust the page positioning
st.markdown(
    """
    <style>
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 10px; /* Adjust to move content up */
    }
    .section-image {
        margin: 20px 0;
        max-width: 80%;
        border-radius: 10px;
    }
    .skills-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
    }
    .skill-card {
        text-align: center;
        max-width: 150px;
        margin-bottom: 20px; /* Spacing between rows */
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #777;
        font-size: 0.9em;
    }
    a.project-link {
        color: black; /* Change link color to black */
        text-decoration: none; /* Remove underline */
    }
    a.project-link:hover {
        color: #333; /* Optional: Change color on hover */
    }
    .experience-entry, .education-entry {
        text-align: left;
        margin-bottom: 20px;
    }
    .experience-role, .education-degree {
        font-size: 1.2em;
        font-weight: bold;
    }
    .experience-company, .education-university {
        font-size: 1em;
        color: #555;
    }
    .experience-duration {
        font-size: 0.9em;
        color: #777;
    }
    .experience-description, .education-description {
        font-size: 0.9em;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.title("Aryan Nambiar")
st.subheader("ML Engineer")
st.markdown('</div>', unsafe_allow_html=True)

# Tabs for navigation
tabs = st.tabs(["About Me", "Projects", "Skills", "Experience", "Education", "Contact"])

# About Section
with tabs[0]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    
    # Create two columns: one for the image and one for the text
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("Profile Pic.png", caption="Profile Picture", use_column_width=True)  # Replace with your image URL
    
    with col2:
        st.write(
            """
            Hello there.

            I'm an ML Engineer and a Problem-Solver at heart.

            I specialize in computer vision and natural language processing.
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
with tabs[1]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    project_data = [
        {"title": "Marketing Campaign Analysis - A/B Testing", "description": "A deep learning project for image classification.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject1"},
        {"title": "CAPM Web Application", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Car Price Prediction", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Stock Market Analysis and Prediction", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Customer Segmentation using K-Means Clustering Analysis", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Credit Card Fraud Detection", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Music Recommendation System", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Rain Prediction", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Real Estate Price Prediction", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
        {"title": "Twitter Sentiment Analysis", "description": "NLP model for text generation.", "image": "https://via.placeholder.com/250", "link": "https://github.com/yourproject2"},
    ]

    for project in project_data:
        # Create three columns: one for the image, one for spacing, and one for the text
        col1, col_space, col2 = st.columns([1, 0.1, 2])
        
        with col1:
            st.image(project["image"], caption=project["title"], use_column_width=True)
 
        with col2:
            # Styled project title with link, but no blue color or underline
            st.markdown(f'<a href="{project["link"]}" class="project-link"><h3>{project["title"]}</h3></a>', unsafe_allow_html=True)
            st.write(project["description"])
    
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
with tabs[2]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)

    # Skill icons list
    skill_icons = [
        {"name": "Python", "icon": "python.svg"},
        {"name": "TensorFlow", "icon": "python.svg"},
        {"name": "PyTorch", "icon": "python.svg"},
        {"name": "SQL", "icon": "python.svg"},
        {"name": "Keras", "icon": "python.svg"},
        {"name": "Scikit-Learn", "icon": "python.svg"},
    ]

    # Use CSS class structures for skills display
    st.markdown('<div class="skills-row">', unsafe_allow_html=True)
    for skill in skill_icons:
        st.markdown(f'''
            <div class="skill-card">
                <img src="{skill['icon']}" class="section-image" alt="{skill['name']}">
                <p>{skill['name']}</p>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Experience Section
with tabs[3]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    # Experience data
    experience_data = [
        {
            "role": "ML Engineer",
            "company": "Confidential",
            "duration": "Aug 24 - Present",
            "description": "Developed scalable ML models and worked on high-performance algorithms."
        },
        {
            "role": "Trainee - Data Scientist",
            "company": "360DigiTMG",
            "duration": "Jun 24 - Present",
            "description": "Focused on predictive analytics and building data-driven solutions."
        },
         {
            "role": "Intern - Supply Chain Analytics Analyst",
            "company": "Ecolab",
            "duration": "Jan 24 - Apr 24",
            "description": "Focused on predictive analytics and building data-driven solutions."
        },
         {
            "role": "Intern - SEO and Content Writer",
            "company": "Amber",
            "duration": "Apr 23 - Oct 23",
            "description": "Focused on predictive analytics and building data-driven solutions."
        }
    ]

    for experience in experience_data:
        st.markdown(
            f"""
            <div class="experience-entry">
                <div class="experience-role">{experience["role"]}</div>
                <div class="experience-company">{experience["company"]}</div>
                <div class="experience-duration">{experience["duration"]}</div>
                <div class="experience-description">{experience["description"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Education Section
with tabs[4]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    # Education data
    education_data = [
        {
            "degree": "B.Tech. - Information Technology",
            "university": "Ajeenkya DY Patil University",
            "description": """Specialized in Data Science with skills in Machine Learning and Big Data.
            Experienced in building models to make predictions, creating clear data visualizations, and finding useful patterns in large amounts of data.
            Comfortable using various tools to turn raw data into practical insights for better decision-making."""
        }
    ]

    for education in education_data:
        st.markdown(
            f"""
            <div class="education-entry">
                <div class="education-degree">{education["degree"]}</div>
                <div class="education-university">{education["university"]}</div>
                <div class="education-description">{education["description"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
with tabs[5]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    st.write(
        """
        I'm open to connecting! You can reach out through the following platforms:
        - [LinkedIn](https://www.linkedin.com/in/nambiar-aryan/)
        - [GitHub](https://github.com/karma48)
        - [Email](mailto:nambiararyan24@gmail.com)
        - [WhatsApp](https://wa.link/4gis5z)
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Aryan Nambiar</div>', unsafe_allow_html=True)
