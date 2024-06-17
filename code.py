
import streamlit as st

# Main body of content

st.title("MANISH SRI SAI SURYA **ROUTHU**")

# Create a navigation bar with links to different sections of the app
st.sidebar.header("Navigation")
nav_option = st.sidebar.radio("", ["ABOUT ME", "EDUCATION", "RESEARCH", "EXPERIENCE", "SKILLS AND PROOF OF WORK", "PROJECTS"])

# Profile links
github_link = 'https://github.com/manishFromShambala'
linkedin_link = 'https://linkedin.com/in/manishcse456 '
leetcode_link = 'https://leetcode.com/u/manishShambala/'
geeksforgeeks_link = 'https://www.geeksforgeeks.org/user/mxr8f3nd/'

# Add the links to the sidebar
st.sidebar.markdown("### Connect with me:")
st.sidebar.write("Phone Number: +1 (216)-575-8862")
st.sidebar.write("Email: manishshambala@gmail.com")
st.sidebar.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=GitHub)]({github_link})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=LinkedIn)]({linkedin_link})")
st.sidebar.markdown(f"[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-blue?style=flat-square&logo=LeetCode)]({leetcode_link})")
st.sidebar.markdown(f"[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Profile-blue?style=flat-square&logo=GeeksforGeeks)]({geeksforgeeks_link})")



# Define the content for each section
if nav_option == "ABOUT ME":
    st.header("Computer Science Graduate skilled in Coding, Artificial Intelligence and Machine Learning")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("<div style='text-align: justify;'>Computer Science graduate with a specialization in Artificial Intelligence and Machine Learning. Proficient in C++ and Python coding, with experience in machine learning algorithms and deep learning frameworks, excels in collaborative team environments. My expertise includes developing innovative AI solutions, evident in projects like a chatbot for a coffee shop and a deep learning model for pest detection in farmland. My research contributions delve into NLP and deep learning optimization, showcasing my dedication to advancing AI technologies. My blend of technical skills and practical experience positions me as a valuable asset in driving AI advancements.<\div>", unsafe_allow_html=True)
    with col2:
        st.image("Profile_Image.jpeg")
    
elif nav_option == "EDUCATION":
    st.header("Education")
    
    st.markdown("<h3><a href='https://case.edu' style='color:black;text-decoration:none;'>Case Western Reserve University</a></h3>", unsafe_allow_html=True)
    st.write("**Master of Science - Computer Science**")
    st.write("**GPA:** 3.75 / 4")
    st.write("**Award:** **Seigal Lifelong Learning Scholarship** of **25%** of Tuition fee")
    st.write("**Coursework:** Machine Learning, Data Mining, Computer Vision, Contemporary Issues in Big Data, Designing High Performant Systems for Artificial Intelligence, High-Performance Data and Computing, Database Systems, Software Engineering, Computer security, and Computer Networks.")


elif nav_option == "RESEARCH":
    st.header("Research")
    st.subheader("Analysis of linguistic and math features for classification of math word problems: Insights and future direction")
    
    st.write("**Role:** Research Assistant ")
    st.write("**Research paper ID:** AR-TENLT-HYBD-090723-300 ")
    st.markdown("**Link to PDF:** [<img src='https://ijmas.iraj.in//images/pdf_icon.png' alt='PDF Logo' style='width:20px;'>](research_paper.pdf)", unsafe_allow_html=True)
    st.markdown("**Link to website:** [<img src='web_logo.jpeg' alt='PDF Logo' style='width:20px;'>](https://ijmas.iraj.in//paper_detail.php?paper_id=20128&nameAnalysis_of_Linguistics_and_Math_Features_for_Classification_of_Math_Word_Problems:_Insights_and_Future_Direction)", unsafe_allow_html=True)
    st.write("**Research Description:** The research investigates linguistic structures and mathematical elements within math word problems for classification. It aims to identify key features influencing problem categorization, employing machine learning techniques. Insights gained will guide future directions, potentially improving automated problem-solving systems and enhancing math education strategies for students' comprehension and problem-solving skills.")

    research_paper_link="http://ijmas.iraj.in//paper_detail.php?paper_id=20128&nameAnalysis_of_Linguistics_and_Math_Features_for_Classification_of_Math_Word_Problems:_Insights_and_Future_Direction"

elif nav_option == 'EXPERIENCE':
    st.header("Experience - Academic Internships")
    # Data Science Internship
    st.subheader("Personifwy (05/2022 - 07/2022)")
    st.write ("**Data Science Intern**")
    st.write("• Developed and deployed an AI-powered chatbot for a coffee shop using Dialogflow and Python, increasing customer engagement by approximately 30% and streamlining customer service interactions by a quarter.")
    st.write("• Implemented natural language processing (NLP) techniques within the Python framework to enable the chatbot to understand user queries, extract relevant information, and generate appropriate responses.")
    st.write("• Collaborated effectively with the team to overcome technical hurdles and ensure successful project completion, earning recognition for problem-solving skills and adaptability.")


    # IoT Internship
    st.subheader("Apsis Solutions (05/2022 - 08/2022)")
    st.write("**IoT Internship**")
    st.write("• Developed a deep learning model (ResNet-50) for pest detection in farmland using drone-mounted sensors and imagery, achieving 76% accuracy.")
    st.write("• Integrated the model with a drone control system to enable real-time, targeted pesticide application. This innovative approach significantly reduced pesticide usage by 40%, leading to increased crop yield by 10% and minimized environmental impact.")
    st.write("• Utilized Python libraries like TensorFlow & OpenCV.")
        
elif nav_option == "SKILLS AND PROOF OF WORK":
    col1, col2 = st.columns([2,1])
    with col1:
            
        st.header("Skills")
        # Programming Languages
        st.subheader("Programming Languages")
        programming_languages = """
        - C
        - C++
        - Python
        - SQL
        - R (Basic)
        """
        st.markdown(programming_languages)

        # Data Analytics and Visualization
        st.subheader("Data Analytics and Visualization")
        data_analytics_visualization = """
        - Analytics Tools:
        - Excel
        - Power BI
        - Tableau
        - Analysis Python Libraries:
        - Pandas
        - Numpy
        - Statistical Analysis:
        - Scipy
        - Statsmodels
        - Visualization Python Libraries:
        - Matplotlib
        - Seaborn
        - Plotly
        - Data Engineering:
        - Understanding of data pipelines, ETL (Extract, Transform, Load) processes, and data warehousing concepts.
        """
        st.markdown(data_analytics_visualization)

        # Artificial Intelligence
        st.subheader("Artificial Intelligence")
        ai_skills = """
        - Machine Learning:
        - Scikit-learn
        - Scipy
        - Deep Learning:
        - TensorFlow
        - Keras
        - Pytorch
        - Computer Vision:
        - OpenCV
        - Natural Language Processing:
        - NLTK
        - SpaCy
        - Frameworks:
        - Fastai
        - Hugging Face Transformers
        - Gradio
        - Langchain
        - Web Interface Development:
        - Flask
        - Streamlit
        """
        st.markdown(ai_skills)
    
        with col2:
            st.header("Proof of work")
            st.write("github link")

elif nav_option == "PROJECTS":
    st.header("Projects")

    # Header
    st.title("Project Showcase")

    # Project 1: Pistachio Classification
    st.subheader("Project 1: Pistachio Classification")
    st.write("""
    - Explored image classification in a computer vision course.
    - Used ImageNet and VGG16 with Python libraries.
    - Preprocessed images, trained the model, and evaluated accuracy.
    - Achieved 91% accuracy in identifying pistachio types.
    - Potential improvements: Explore other algorithms, analyze larger datasets, consider real-world applications.
    """)

    # Project 2: Amazon Customer Satisfaction Prediction
    st.subheader("Project 2: Amazon Customer Satisfaction Prediction")
    st.write("""
    - Analyzed customer sentiment and predicted satisfaction.
    - Implemented the BERT model for NLP.
    - Preprocessed text data and trained the model.
    - Achieved 72% accuracy in predicting customer satisfaction.
    - Potential improvements: Experiment with different NLP models, analyze additional sentiment factors, build an interactive feedback system.
    """)

    # Project 3: Melanoma Classification
    st.subheader("Project 3: Melanoma Classification")
    st.write("""
    - Explored early melanoma detection through image analysis.
    - Developed a model using deep learning techniques.
    - Collaborated with medical professionals for clinical relevance.
    - Contributed to early detection with promising accuracy.
    - Potential improvements: Expand dataset, refine model, integrate with medical diagnosis system.
    """)

    # Project 4: Optimizing Bank Marketing Campaigns
    st.subheader("Project 4: Optimizing Bank Marketing Campaigns")
    st.write("""
    - Undertook a course project analyzing a dataset from a Portuguese bank's marketing campaigns, focusing on term deposit subscriptions.
    - Utilized SparkML to implement a predictive model, aiming to optimize marketing strategies and reduce costs.
    - Defined schema, processed data, and conducted exploratory data analysis on real time data, addressing issues like negative balances and null values.
    - Successfully applied machine learning techniques in a controlled environment, demonstrating proficiency in SparkML.
    - Enhanced data preprocessing skills and gained practical experience in implementing predictive models for marketing optimization.
    """)
