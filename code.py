
import streamlit as st
from streamlit_option_menu import option_menu


# Profile links
github_link = 'https://github.com/manishFromShambala'
linkedin_link = 'https://linkedin.com/in/manishcse456 '
leetcode_link = 'https://leetcode.com/u/manishShambala/'
geeksforgeeks_link = 'https://www.geeksforgeeks.org/user/mxr8f3nd/'

# Add the links to the sidebar
st.sidebar.markdown("### Connect with me:")
st.sidebar.write("Email: manishshambala@gmail.com")


# Custom HTML for horizontal arrangement with Bootstrap icons and custom colors
st.sidebar.markdown(f"""
    <style>
        .profile-link {{
            background-color: #ff4c4b;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: center;
            color: #fff;
            text-decoration: none;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .profile-link img {{
            width: 40px;
            height: 40px;
            margin-bottom: 10px;
            border-radius: 50%;
            background-color: #fff;
            padding: 5px;
        }}
        .profile-link span {{
            font-size: 18px;
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}
    </style>
    <a href="{github_link}" target="_blank" class="profile-link" >
        <img src="https://icons.getbootstrap.com/assets/icons/github.svg">
        <span style = "color: #fff">GitHub</span>
    </a>
    <a href="{linkedin_link}" target="_blank" class="profile-link" >
        <img src="https://icons.getbootstrap.com/assets/icons/linkedin.svg">
        <span style = "color: #fff">LinkedIn</span>
    </a>
    <a href="{leetcode_link}" target="_blank" class="profile-link" >
        <img src="https://icons.getbootstrap.com/assets/icons/file-code.svg">
        <span style = "color: #fff">LeetCode</span>
    </a>
    <a href="{geeksforgeeks_link}" target="_blank" class="profile-link" >
        <img src="https://icons.getbootstrap.com/assets/icons/code-slash.svg">
        <span style = "color: #fff">GeeksforGeeks</span>
    </a>
    """, unsafe_allow_html=True)

# st.sidebar.write("Email: manishshambala@gmail.com")
# st.sidebar.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=GitHub)]({github_link})")
# st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=LinkedIn)]({linkedin_link})")
# st.sidebar.markdown(f"[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-blue?style=flat-square&logo=LeetCode)]({leetcode_link})")
# st.sidebar.markdown(f"[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Profile-blue?style=flat-square&logo=GeeksforGeeks)]({geeksforgeeks_link})")


# Main body of content

st.title("MANISH SRI SAI SURYA **ROUTHU**")
selected = option_menu(
    menu_title=None,
    options=["About", "Education", "Research", "Experience", "Skills", "Projects", "Certifications"],
    icons=["person-fill", "mortarboard-fill", "search", "code-slash", "person-fill-gear", "folder-fill",  "file-earmark-text"],
    orientation="horizontal"
)
# icons.getbootstrap.com -> website for icons

# Define the content for each section
if selected=="About":
    st.write(f'<h1 style="color:#ff4c4b;">About Me</h1>', unsafe_allow_html=True)
    st.subheader("Computer Science graduate with a strong command of programming languages and a passion for applying AI to develop innovative applications")
    # col1, col2 = st.columns([2,1])
    # with col1:
    st.markdown("<div style='text-align: justify;'>Computer Science graduate with a specialization in Artificial Intelligence and Machine Learning. Proficient in C++ and Python coding, with experience in machine learning algorithms and deep learning frameworks, excels in collaborative team environments. My expertise includes developing innovative AI solutions, evident in projects like a chatbot for a coffee shop and a deep learning model for pest detection in farmland. My research contributions delve into NLP and deep learning optimization, showcasing my dedication to advancing AI technologies. My blend of technical skills and practical experience positions me as a valuable asset in driving AI advancements.<\div>", unsafe_allow_html=True)
    # with col2:
    #     st.image("profile_Image.jpeg")
    
if selected=="Education":
    st.write(f'<h1 style="color:#ff4c4b;">Education</h1>', unsafe_allow_html=True)
    
    st.markdown("<h3><a href='https://case.edu' style='color:black;text-decoration:none;'>Case Western Reserve University</a></h3>", unsafe_allow_html=True)
    st.write("**Master of Science - Computer Science**")
    st.write("**GPA:** 3.75 / 4")
    st.write("**Award:** **Seigal Lifelong Learning Scholarship** of **25%** of Tuition fee")
    st.write("**Coursework:** Machine Learning, Data Mining, Computer Vision, Contemporary Issues in Big Data, Designing High Performant Systems for Artificial Intelligence, High-Performance Data and Computing, Database Systems, Software Engineering, Computer security, and Computer Networks.")

    st.markdown("<h3><a href='https://case.edu' style='color:black;text-decoration:none;'>SRKR Engineering College, Bhimavaram</a></h3>", unsafe_allow_html=True)
    st.write("**Bachelor of Technology - Computer Science and Engineering**")
    st.write("**CGPA:** 8.65 / 10")

if selected=="Research":
    st.write(f'<h1 style="color:#ff4c4b;">Research</h1>', unsafe_allow_html=True)
    st.subheader("Analysis of linguistic and math features for classification of math word problems: Insights and future direction")
    
    st.write("**Role:** Research Assistant ")
    st.write("**Research paper ID:** AR-TENLT-HYBD-090723-300 ")
    st.markdown("**Link to PDF:** [<img src='https://ijmas.iraj.in//images/pdf_icon.png' alt='PDF Logo' style='width:20px;'>](research_paper.pdf)", unsafe_allow_html=True)
    st.markdown("**Link to website:** [<img src='web_logo.jpeg' alt='PDF Logo' style='width:20px;'>](https://ijmas.iraj.in//paper_detail.php?paper_id=20128&nameAnalysis_of_Linguistics_and_Math_Features_for_Classification_of_Math_Word_Problems:_Insights_and_Future_Direction)", unsafe_allow_html=True)
    st.write("**Research Description:** The research investigates linguistic structures and mathematical elements within math word problems for classification. It aims to identify key features influencing problem categorization, employing machine learning techniques. Insights gained will guide future directions, potentially improving automated problem-solving systems and enhancing math education strategies for students' comprehension and problem-solving skills.")

    research_paper_link="http://ijmas.iraj.in//paper_detail.php?paper_id=20128&nameAnalysis_of_Linguistics_and_Math_Features_for_Classification_of_Math_Word_Problems:_Insights_and_Future_Direction"

if selected=="Experience":
    st.write(f'<h1 style="color:#ff4c4b;">Experience - Research Assistantship</h1>', unsafe_allow_html=True)
    # Graduate Research Assistantship
    st.subheader("Case Western Reserve University (01/2023 - 05/2023)")
    st.write ("**Graduate Research Assistantship**")
    st.write("Worked under the assistance of Dr. Shilpa Kadam on various machine and deep learning models for research in developing language based mathematical problem distinctions which further will be useful in determining the level of the problem.")

    st.subheader("Case Western Reserve University (05/2024 - Present)")
    st.write("**Graduate Research Assistantship**")
    st.write("Optimizing the attention mechanism, a key component in Transformers that power many large language models (LLMs). The attention mechanism analyzes relationships between words, but it can be computationally expensive. Our goal is to streamline it within Transformers, making LLMs more efficient while maintaining their accuracy.")

    st.write(f'<h1 style="color:#ff0066;">Experience - Academic Internships</h1>', unsafe_allow_html=True)
    # Data Science Internship
    st.subheader("Personifwy (05/2022 - 07/2022)")
    st.write ("**Data Science Intern**")
    st.write("• Developed and deployed an AI-powered chatbot for a coffee shop using Dialogflow and Python, increasing customer engagement by approximately 30% and streamlining customer service interactions by a quarter.")
    st.write("• Implemented natural language processing (NLP) techniques within the Python framework to enable the chatbot to understand user queries, extract relevant information, and generate appropriate responses.")
    st.write("• Collaborated effectively with the team to overcome technical hurdles and ensure successful project completion, earning recognition for problem-solving skills and adaptability.")


    # IoT Internship
    st.subheader("Apsis Solutions (05/2022 - 08/2022)")
    st.write("**IoT Intern**")
    st.write("• Developed a deep learning model (ResNet-50) for pest detection in farmland using drone-mounted sensors and imagery, achieving 76% accuracy.")
    st.write("• Integrated the model with a drone control system to enable real-time, targeted pesticide application. This innovative approach significantly reduced pesticide usage by 40%, leading to increased crop yield by 10% and minimized environmental impact.")
    st.write("• Utilized Python libraries like TensorFlow & OpenCV.")
        
if selected=="Skills": 
    st.write(f'<h1 style="color:#ff4c4b;">Skills</h1>', unsafe_allow_html=True)
    st.subheader("Programming Languages")
    st.write("C, C++, Python, SQL, R (Basic)")

    st.subheader("Data Analytics and Visualization")
    st.write("""
    - **Analytics Tools**: Excel, Power BI, Tableau
    - **Analysis Python Libraries**: Pandas, Numpy
    - **Statistical Analysis**: Scipy, Statsmodels
    - **Visualization Python Libraries**: Matplotlib, Seaborn, Plotly
    - **Data Engineering**: Understanding of data pipelines, ETL (Extract, Transform, Load) processes, and data warehousing concepts.
    """)

    st.subheader("Artificial Intelligence")
    st.write("""
    - **Machine Learning**: Scikit-learn, Scipy
    - **Deep Learning**: TensorFlow, Keras, Pytorch
    - **Computer Vision**: OpenCV
    - **Natural Language Processing**: NLTK, SpaCy
    - **Frameworks**: Fastai, Hugging Face Transformers, Gradio, Langchain
    - **Web Interface Development**: Flask, Streamlit
    """)
if selected=="Projects":
    st.write(f'<h1 style="color:#ff4c4b;">Projects</h1>', unsafe_allow_html=True)

    # Project 1: Pistachio Classification
    st.subheader("Project 1: Pistachio Classification")
    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write("""
        - Explored image classification in a computer vision course.
        - Used ImageNet and VGG16 with Python libraries.
        - Preprocessed images, trained the model, and evaluated accuracy.
        - Achieved 91% accuracy in identifying pistachio types.
        - Potential improvements: Explore other algorithms, analyze larger datasets, consider real-world applications.
        """)
    with right_column:
        github_link = "https://github.com/yourusername/amazon-customer-satisfaction-prediction"
        st.markdown(f"""
        <a href="https://github.com/manishFromShambala/Python/tree/main/Pistachio_Classification" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="50">
        </a>
        """, unsafe_allow_html=True)

    # Project 2: Amazon Customer Satisfaction Prediction
    st.subheader("Project 2: Amazon Customer Satisfaction Prediction")
    left_column, right_column = st.columns([5, 1])

    with left_column:
        st.write("""
        - Analyzed customer sentiment and predicted satisfaction.
        - Implemented the BERT model for NLP.
        - Preprocessed text data and trained the model.
        - Achieved 72% accuracy in predicting customer satisfaction.
        - Potential improvements: Experiment with different NLP models, analyze additional sentiment factors, build an interactive feedback system.
        """)

    with right_column:
        github_link = "https://github.com/yourusername/amazon-customer-satisfaction-prediction"
        st.markdown(f"""
        <a href="{github_link}" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="50">
        </a>
        """, unsafe_allow_html=True)
    # Project 3: Melanoma Classification
    st.subheader("Project 3: Melanoma Classification")
    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write("""
        - Explored early melanoma detection through image analysis.
        - Developed a model using deep learning techniques.
        - Collaborated with medical professionals for clinical relevance.
        - Contributed to early detection with promising accuracy.
        - Potential improvements: Expand dataset, refine model, integrate with medical diagnosis system.
        """)
    with right_column:
        github_link = "https://github.com/yourusername/amazon-customer-satisfaction-prediction"
        st.markdown(f"""
        <a href="https://github.com/manishFromShambala/Python/tree/main/Melanoma_Classification" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="50">
        </a>
        """, unsafe_allow_html=True)

    # Project 4: Optimizing Bank Marketing Campaigns
    st.subheader("Project 4: Optimizing Bank Marketing Campaigns")
    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write("""
        - Undertook a course project analyzing a dataset from a Portuguese bank's marketing campaigns, focusing on term deposit subscriptions.
        - Utilized SparkML to implement a predictive model, aiming to optimize marketing strategies and reduce costs.
        - Defined schema, processed data, and conducted exploratory data analysis on real time data, addressing issues like negative balances and null values.
        - Successfully applied machine learning techniques in a controlled environment, demonstrating proficiency in SparkML.
        - Enhanced data preprocessing skills and gained practical experience in implementing predictive models for marketing optimization.
        """)
    with right_column:
        github_link = "https://github.com/yourusername/amazon-customer-satisfaction-prediction"
        st.markdown(f"""
        <a href="https://github.com/manishFromShambala/Python/tree/main/Bank_Marketing_Optimization" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub logo" width="50">
        </a>
        """, unsafe_allow_html=True)

if selected=="Certifications":
    st.write(f'<h1 style="color:#ff4c4b;">Certifications</h1>', unsafe_allow_html=True)
    certifications = [
        {
            "title": "Python Essentials for MLOps",
            "issuer": "Duke University",
            "issued": "Dec 2023",
            "credential_id": "E7CS9KT8XSRB",
            "skills": "",
            "logo": "https://1000logos.net/wp-content/uploads/2017/11/Duke-University-logo.jpg",
            "credential_url": "https://www.coursera.org/account/accomplishments/verify/E7CS9KT8XSRB"
        },

        {
            "title": "Communication and Presentation Skills for Analysts and Managers",
            "issuer": "365 Data Science",
            "issued": "Mar 2024",
            "credential_id": "CC-F66F447B1F",
            "skills": "Presentation Skills, Microsoft PowerPoint, Report Writing",
            "logo": "https://media.trustradius.com/vendor-logos/CX/Cc/8F69BFLI6KXP.JPEG",
            "credential_url": "https://learn.365datascience.com/certificates/CC-F66F447B1F/"
        },

        {
            "title": "Data Cleaning and Preprocessing with pandas",
            "issuer": "365 Data Science",
            "issued": "Mar 2024",
            "credential_id": "CC-1C1B60822A",
            "skills": "Pandas, Data Analytics",
            "logo": "https://media.trustradius.com/vendor-logos/CX/Cc/8F69BFLI6KXP.JPEG",
            "credential_url": "https://learn.365datascience.com/certificates/CC-1C1B60822A/"
        },
        
        {
            "title": "Data Literacy",
            "issuer": "365 Data Science",
            "issued": "Nov 2023",
            "credential_id": "CC-BF19DC93F6",
            "skills": "Business Understanding, Data, Big Data",
            "logo": "https://media.trustradius.com/vendor-logos/CX/Cc/8F69BFLI6KXP.JPEG",
            "credential_url": "https://learn.365datascience.com/certificates/CC-BF19DC93F6/"
        }
    ]

    for cert in certifications:
        logo_col, info_col = st.columns([1, 4])
        with logo_col:
            st.markdown(f"""
            <a href="{cert['credential_url']}" target="_blank">
                <img src="{cert['logo']}" width="50">
            </a>
    """, unsafe_allow_html=True)
        with info_col:
            st.markdown(f"""
            <p style="font-size:24px; font-weight:bold;">{cert['issuer']}</p>
            <p style="font-size:20px;">{cert['title']}</p>
            <p>Issued {cert['issued']}</p>
            <p>Credential ID: {cert['credential_id']}</p>
            """, unsafe_allow_html=True)
            if cert["skills"]:
                st.write(f"Skills: {cert['skills']}")


            # st.markdown(f"[Show credential]({cert['credential_url']})")
            # st.write(f"**{cert['title']}**")
            # st.write(f"*{cert['issuer']}*")
            # st.write(f"Issued {cert['issued']}")
            # st.write(f"Credential ID: {cert['credential_id']}")
            # if cert["skills"]:
            #     st.write(f"Skills: {cert['skills']}")
            # st.markdown(f"[Show credential]({cert['credential_url']})")

