# streamlit_app.py
import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon="🍔", layout="centered")

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
            max-width: 80px; /* Adjust max width */
            max-height: 80px; /* Adjust max height */
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
    .experience-duration, .education-duration {
        font-size: 0.9em;
        color: #777;
    }
    
     .experience-description, .education-description {
        font-size: 0.9em;
        margin-top: 5px;
    }
    .experience-description ul {
        /*list-style-type: none;   Optional: Remove bullet points if needed */
        padding-left: 0;
    }
    .experience-description li {
        font-size: 0.9em;  /* Ensure the correct font size */
        line-height: 1.5;   /* Adjust line height for better readability */
    }
    .col1, col_space, col2 {
    display: flex;
    align-items: center; /* Align the text vertically to the center */
}
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.title("Aryan Nambiar")

# Create columns for subheader and button
col1, col2 = st.columns([4, 1])

with col1:
    st.subheader("Machine Learning Engineer")

with col2:
    # Add a button with an external link to your resume
    resume_link = "https://docs.google.com/document/d/17QL8uw3ZrZWHmmXHsmgeh8kNifU4li_IU9GfcTKpECg/edit?usp=sharing"  # Replace with your actual resume link
    st.markdown(f'<a href="{resume_link}" target="_blank"><button style="padding: 8px 16px; background-color: #FF4B4B; color: white; border: none; border-radius: 7px; cursor: pointer;">Resume</button></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# Tabs for navigation
tabs = st.tabs(["About Me", "Projects", "Skills", "Experience", "Education", "Contact"])

# About Section
with tabs[0]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    
    # Create two columns: one for the image and one for the text
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("photo.png", use_column_width=True)  # Replace with your image URL
    
    with col2:
        st.write("""
**Some Things About Me**
- I’m an ML Engineer skilled in supervised and unsupervised learning, currently expanding my knowledge in NLP and computer vision. My goal is to be in the top 1% of AI engineers, working on impactful projects.

- I thrive in startup environments where I can learn fast and contribute meaningfully. Personal growth is key for me—I stay calm, focused, and constantly seek to improve.

- I'm passionate about technology's future and driven to be part of the innovation. I also value sustainability and actively volunteer to make a positive difference in my community.
""")
        st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
with tabs[1]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    project_data = [
        {"title": "Marketing Campaign Analysis", "description": "A/B testing of marketing campaigns to select the optimal advertising platform, regression analysis to predict conversion rates and improve sales performance.", "image": "marketing.png", "link": "https://github.com/karma48/Marketing-Campaign-Analysis-A-B-Testing"},
        {"title": "Financial Analysis- CAPM Web App", "description": "Web application to perform CAPM calculations for stocks with Yahoo Finance data. It calculates expected returns and visualizes the results.", "image": "finance.jpg", "link": "https://github.com/karma48/CAPM"},
        {"title": "Car Price Prediction", "description": "Car price prediction model using Linear Regression using data from Quikr.com. Built a web application with Flask to provide user-friendly predictions based on car details.", "image": "car.jpg", "link": "https://github.com/karma48/Car-Price-Prediction"},
       {"title": "Stock Market Analysis and Prediction", "description": "Analyzes stock data for tech giants like Apple and Amazon, using Python for visualization and LSTM for price prediction.", "image": "stockmarket.jpg", "link": "https://github.com/karma48"},
      {"title": "Customer Segmentation using K-Means Clustering Analysis", "description": "Segment customers based on age, income, and spending behavior from the Mall Customer Segmentation dataset", "image": "customer.jpg", "link": "https://github.com/karma48"},
       {"title": "Credit Card Fraud Detection", "description": "Detecting credit card fraud using a highly imbalanced dataset of anonymized European transactions, applying PCA for feature transformation.", "image": "creditcard.jpg", "link": "https://github.com/karma48"},
       {"title": "Real Estate Price Prediction", "description": "Uses the Bengaluru House Price dataset to build a ML model that predicts property prices based on features like area, location, size, etc.", "image": "real estate.jpg", "link": "https://github.com/karma48"},
      {"title": "Twitter Sentiment Analysis", "description": "Sentiment analysis on company-related tweets using Logistic Regression and XGBoost, applying NLP techniques with libraries like wordcloud and sklearn.", "image": "twitter.jpg", "link": "https://github.com/karma48"},
      {"title": "Music Recommendation System", "description": "", "image": "music.jpg", "link": "https://github.com/karma48"},
      {"title": "Rain Prediction Using ANN", "description": "", "image": "rain.jpg", "link": "https://github.com/karma48"},
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
        {"name": "AWS", "icon": "aws.svg"},
        {"name": "Snowflake", "icon": "snowflake.svg"},
        {"name": "Power BI", "icon": "powerbi.svg"},
        {"name": "SQL", "icon": "sql.svg"},
        {"name": "Python", "icon": "python.svg"},
    ]

    # Create two main columns for the skills
    col1, col2 = st.columns(2)

    # Display skills in alternating columns
    for i, skill in enumerate(skill_icons):
        col = col1 if i % 2 == 0 else col2  # Alternates between the columns
        
        with col:
            # Create sub-columns for image and text alignment
            image_col, text_col = st.columns([1, 4])  # Adjust the ratio as needed
            with image_col:
                st.image(skill['icon'], width=50)  # Enlarged the image size
            with text_col:
                st.markdown(f"<div style='display: flex; align-items: center; height: 50px;'><span style='line-height: 1.5;'>{skill['name']}</span></div>", unsafe_allow_html=True)

# Experience Section
with tabs[3]:
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    # Experience data
    experience_data = [
        {
            "role": "Machine Learning Engineer",
            "company": "Confidential",
            "duration": "Aug '24 - Present",
            "description": ["Working at an early-stage startup, building and integrating AI applications to the product, enhancing product experience."]
        },
        {
            "role": "Trainee - Data Scientist",
            "company": "360DigiTMG",
            "duration": "Jun '24 - Present",
            "description": ["Working as a trainee, building end-to-end Data Science projects according to client requirements."]
        },
        {
            "role": "Intern - Supply Chain Analytics Analyst",
            "company": "Ecolab",
            "duration": "Jan '24 - Apr '24",
            "description": [
                "Worked on 5 projects in analytics and automation, analyzing problems and creating custom solutions according to requirements.",
                "Created dashboards, low-code applications and automated workflows using the Power Platform, increasing efficiency by 17%.",
                "Developed Python automation scripts, speeding up business processes by 15%",
                "Conduct exploratory data analysis (EDA) on logistics data to identify patterns, anomalies, and validate hypotheses.",
                "Performed ad-hoc analysis using SQL and data integration using Azure Data Factory."
            ]
        },
        {
            "role": "Intern - SEO and Content Writer",
            "company": "Amber",
            "duration": "Apr '23 - Oct '23",
            "description": [
                "Wrote and optimized 75+ B2C blogs, driving 300k+ traffic by Oct 2023. Additionally, crafted 100+ property descriptions for international PBSA and optimized search page content for 120+ countries, states, cities, and universities.",
                "Developed 40+ YouTube scripts (short and long-form), pin descriptions, and web stories.",
                "Curated 2.5K+ property reviews for strategic analysis (UGC).",
                "Conducted technical SEO audits and regular content quality assessments.",
                "Created monthly performance dashboards using Looker Studio."
            ]
        }
    ]

    for experience in experience_data:
        description_list_items = "".join([f"<li>{point}</li>" for point in experience["description"]])

        st.markdown(
            f"""
            <div class="experience-entry">
                <div class="experience-role">{experience["role"]}</div>
                <div class="experience-company">{experience["company"]}</div>
                <div class="experience-duration">{experience["duration"]}</div>
                <div class="experience-description">
                    <ul>
                        {description_list_items}
                    </ul>
                </div>
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
            "degree": "Professional Course in Data Science & AI",
            "university": "360DigiTMG",
            "duration": "Jun '24 - Present",
            "description": """Proficient in Data Science with skills in Exploratory Data Analysis, Machine Learning, Deep Learning, NLP, and Computer Vision. Experienced in CRISP-DM methodology, Python, SQL, and data visualization tools like Power BI and Tableau for insightful data-driven solutions.
"""
        },
        {
            "degree": "B.Tech. - Information Technology (Data Science)",
            "university": "Ajeenkya DY Patil University",
            "duration": "Aug '20 - May '24",
            "description": """Skilled in Data Science with expertise in Machine Learning and Big Data. I build predictive models, create insightful data visualizations, and uncover patterns in complex datasets, turning raw data into actionable insights for smarter decisions.
"""
        },

    ]

    for education in education_data:
        st.markdown(
            f"""
            <div class="education-entry">
                <div class="education-degree">{education["degree"]}</div>
                <div class="education-university">{education["university"]}</div>
                <div class="education-duration">{education["duration"]}</div>
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
        - [LinkedIn](https://www.linkedin.com/in/karma48/)
        - [GitHub](https://github.com/karma48)
        - [Email](mailto:nambiararyan24@gmail.com)
        - [WhatsApp](https://wa.link/4gis5z)
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Aryan Nambiar</div>', unsafe_allow_html=True)
