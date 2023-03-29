import streamlit as st
import json
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV David Maimoun.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | David Maimoun"
NAME = "David Maimoun"
DESCRIPTION = "Bioinformatician & Data Scientist"
EMAIL = "davidmaimoun@hotmail.com"
PHONE = "0527810255"
PAGE_ICON = ":wave:"
URL_PROJECT1 = "https://backtrack.streamlit.app/"
URL_PROJECT2 = "https://movie-finder.streamlit.app/"
URL_PROJECT3 = "https://datavision.streamlit.app/"
URL_PROJECT4 = "https://heartdisease-pred.streamlit.app/"
URL_PROJECT5 = "https://diabetes-pred.streamlit.app/"
URL_PROJECT6 = "https://cryptoprice.streamlit.app/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.write("""
<style>

   .description {
      font-weight: 100;
      letter-spacing: 1px;
      margin-bottom: 8px;
   }
  
   
   div[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
      box-shadow: 0 0 12px rgb(235,235,235);
      border-radius: 22px;
      padding: 28px 18px;
   }

   .btn {
      color: rgb(45, 63, 113);
      background-color: white;
      border-radius: 3px;
      padding: 4px 8px;
      border: 1px solid rgb(45, 63, 113);
      margin-top: 24px;
      transition: .1s;
   }
   .btn:hover{
      background-color: rgb(45, 63, 113);
      color: white !important;
      text-decoration: none;

   }


</style>
""", unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
   PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

def load_lottiefile(filepath: str):
   with open(filepath, "r") as f:
      return json.load(f)

def returnLottie(path):
   return st_lottie(
      load_lottiefile(path),
      speed=1,
      reverse=False,
      loop=True,
      quality="medium", # medium ; high
      # renderer="svg", # canvas
      height=None,
      width=None,
      key=None,
   )

# --- HERO SECTION --- 
col1, col2 = st.columns([.5,1], gap="medium")
with col1:
   st.image(profile_pic, width=200)

with col2:
   st.title(NAME)
   st.markdown(f"<h5 class='description'>{DESCRIPTION}</h5>", unsafe_allow_html=True)
  
   st.markdown(f"""
      <h6>📞 {PHONE}</h6>
      <h6><a href='mailto:{EMAIL}'>📫 {EMAIL}</a></h6>
   """, unsafe_allow_html=True)

   st.download_button(
      label=" 📄 Download Resume",
      data=PDFbyte,
      file_name=resume_file.name,
      mime="application/octet-stream",
   )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.markdown("""
      <div style="height:1px;border:none;color:#CCC;background-color:#CCC;" ></div> 
      """, unsafe_allow_html=True)
st.write(
   """
      - ✔️ Experience in extracting and visualize data.\n
      - ✔️ Strong hands on experience and knowledge in Python and R.\n
      - ✔️ Good understanding of statistical principles and their applications.\n
      - ✔️ Excellent team-player and displaying strong sense of initiative on tasks.\n
   """, unsafe_allow_html=True
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.markdown("""
      <div style="height:1px;border:none;color:#CCC;background-color:#CCC;" ></div> 
      """, unsafe_allow_html=True)
st.write(
   """
      - 👩‍💻 Data Analysis: Python (Numpy, Pandas), R, Bash.\n
      - 📊 Data Visualization: Plotly, Seaborn, Geographical Plotting.\n
      - 📈 Machine Learning modeling and prediction.\n
      - 🧬 Genome Analysis: Sequencing Quality Control, Assembly, Mapping.\n
      - 🦠 Pathogen Detection: cg/wgMLST, MS Tree, Virulence/Resistance Factors. \n
      - 🌐 Web Front-End: HTML, CSS, JS, ReactJS.\n
      - 🗄️ Databases & Back-End: ExpressJS, MongoDB, MySQL.\n       
   """
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.markdown(
   """
      <h5>
         🧫 Head of Bioinformatics department at the Ministry of Health, Jerusalem.
      </h5>
   """,unsafe_allow_html=True
)
st.markdown("<p class='date'>01/2022 - Present</p>", unsafe_allow_html=True)
col1, col2 = st.columns([1,3], gap="small")
with col1:
   returnLottie("assets/moh.json")
with col2:
   st.write(
      """
      - ✔️ In charge of finding new solutions to improve pathogens detections in the country.\n
      - ✔️ Detect pathogens profile better & faster.\n
      - ✔️ Improve the detection speed from hours to minutes.\n
      - ✔️ Create tutorials to promote the usage of scripts in the laboratory work routine by the researchers.\n
      """
   )

# --- JOB 2
st.write('\n')
st.markdown(
   """
      <h5>
         🔬 The Wohl Institute for Translational Medicine (Hadassah Ein Karem).
      </h5>
   """,unsafe_allow_html=True
)
st.markdown("<p class='date'>2019 - 2021</p>", unsafe_allow_html=True)
col1, col2 = st.columns([1,3], gap="small")
with col1:
   returnLottie("assets/hadassah.json")
with col2:
   st.write(
      """
         - ✔️ Operating the state of the art imaging devices.\n
         - ✔️ Analysis & Summarize the raw data.\n
         - ✔️ In charge of devices maintenance.\n
      """
   )

# --- JOB 3
st.write('\n')
st.markdown(
   """
      <h5>
         💻 Qeezz ltd, Mobile & Web Application.
      </h5>
   """,unsafe_allow_html=True
)
st.markdown("<p class='date'>2019</p>", unsafe_allow_html=True)
col1, col2 = st.columns([1,3], gap="small")
with col1:
   returnLottie("assets/qeezz.json")
with col2:
   st.write(
      """
         - ✔️ iOS/Android Mobile development.\n
         - ✔️ Web site development & maintenance.\n
         - ✔️ Api Calling.\n
      """
   )

# --- JOB 4
st.write('\n')
st.markdown(
   """
      <h5>
         🥼 Hadassah Ein Kerem, Cardiology.
      </h5>
   """,unsafe_allow_html=True
)
st.markdown("<p class='date'>2015 - 2017</p>", unsafe_allow_html=True)
col1, col2 = st.columns([1,3], gap="small")
with col1:
   returnLottie("assets/microscope.json")
with col2:
   st.write(
      """
         - ✔️ Build a model for atherosclerosis.\n
         - ✔️ Analysis of the plaque formation in arteries.\n
         - ✔️ Treatment testing.\n
      """
   )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

# Project 1
with st.container():
   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
      """
         <h5>
            Project 1: BacTrack
         </h5>
      """,unsafe_allow_html=True
      )
      st.markdown("<p class='date'>Data Visualization & Manipulation > Epidemiology</p>", unsafe_allow_html=True)
      st.write(
            f"""
            Bacteria called Neisseria meningitidis cause meningococcal disease.
            Three of these serogroups (types) cause most of the illness and death.
            It is vital to detect them as soon as possible, and check their distribution/spread in the country.
            <br>
            <a target="_blank" href={URL_PROJECT1}>
               <button class='btn'>
                  Launch BacTrack ! 
               </button>
            </a>
            """,unsafe_allow_html=True
         )
     
   with col2:
      st.markdown("<br>",unsafe_allow_html=True)
      returnLottie("assets/project1.json")

   st.markdown("<br>",unsafe_allow_html=True)

# Project 2
with st.container():
   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
      """
         <h5>
            Project 2: CLAPP! The Movie Finder
         </h5>
      """,unsafe_allow_html=True
      )
      st.markdown("<p class='date'>Suggestion Algorithm</p>", unsafe_allow_html=True)
      st.write(f"""
            If you are tired to spend the whole evening looking for a movie to see, try this CLAPP!
            Enter a movie title and the app will suggest you more movies based on similar 
            genre. 
            You can filter a search by director name, genre and released date if you want more
            accuracies... Enjoy your evening!
            <br>
            <a target='_blank' href={URL_PROJECT3}>
               <button class='btn'>
                  Launch CLAPP ! 
               </button>
            </a>
            """,unsafe_allow_html=True
         )
   with col2:
         st.markdown("<br>",unsafe_allow_html=True)
         returnLottie("assets/movie.json")

   st.markdown("<br>",unsafe_allow_html=True)

# Project 3
with st.container():
   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
      """
         <h5>
            Project 3: DataVision (🚧 in development)
         </h5>
      """,unsafe_allow_html=True
      )
      st.markdown("<p class='date'>Data Manipulation & Data Visualization</p>", unsafe_allow_html=True)
      st.write(
            """
            This App will help you to get informations on your dataset.
            Manipulating your data, handling Null values, drawing charts like line, bar, pie charts, 
            geographical plots and even buildind Machine Learning Model, without a line of code! All
            in one nice and user friendly app.
            <br>
            <a target="_blank" href={URL_PROJECT3}>
               <button class='btn'>
                  Launch Data Vision ! 
               </button>
            </a>
            """,unsafe_allow_html=True
         )
   with col2:
      st.markdown("<br>",unsafe_allow_html=True)
      returnLottie("assets/data-analysis.json")

   st.markdown("<br>",unsafe_allow_html=True)

# Project 4
with st.container():
   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
      """
         <h5>
            Project 4: Heart Disease Predictor
         </h5>
      """,unsafe_allow_html=True
      )
      st.markdown("<p class='date'>Machine Learning > Logistic Regression</p>", unsafe_allow_html=True)
      st.write(
            f"""
            As a new researcher in the cardiology department, I was stunted to see how many people
            live with heart disease, knowing that stroke could strike at any time.
            Here, I used the power of Machine Learning to predict the chance somebody get a stroke.
            <br>
            <a target="_blank" href={URL_PROJECT4}>
               <button class='btn'>
                  Launch H.D.Predictor ! 
               </button>
            </a>
            """,unsafe_allow_html=True
         )
   with col2:
         st.markdown("<br>",unsafe_allow_html=True)
         returnLottie("assets/project2.json")

   st.markdown("<br>",unsafe_allow_html=True)

# Project 5
with st.container():
   st.markdown(
   """
      <h5>
         Project 5: Diabetes Predictor
      </h5>
   """,unsafe_allow_html=True
   )
   st.markdown("<p class='date'>Machine Learning > Support Vector Machines</p>", unsafe_allow_html=True)
   col1, col2 = st.columns([3,1])

   with col1:
      st.write(
            f"""
            Diabetes, another disease that affects millions people worlwide, is a major cause of blindness, 
            kidney failure, heart attacks, stroke and lower limb amputation.
            In this project, I am using the Support Vector Machine model to build a system that 
            can predict whether a person has diabetes or not. 
            <br>
               <a target="_blank" href={URL_PROJECT5}>
                  <button class='btn'>
                     Launch Diabetes Predictor ! 
                  </button>
               </a>
               """,unsafe_allow_html=True
         )
   with col2:
         returnLottie("assets/diabetes.json")

   st.markdown("<br>",unsafe_allow_html=True)

# Project 6
with st.container():
   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
      """
         <h5>
            Project 6: Binance Crypto Price
         </h5>
      """,unsafe_allow_html=True
      )
      st.markdown("<p class='date'>Data Manipulation > Finance & Crypto</p>", unsafe_allow_html=True)
      st.write(f"""
            I wanted to test the power of Python and Streamlit to check in real time
            the price of the different cryptocurrencies.
            <br>
            <a target="_blank" href={URL_PROJECT6}>
               <button class='btn'>
                  Launch BCP App ! 
               </button>
            </a>
            """,unsafe_allow_html=True
         )
   with col2:
         returnLottie("assets/crypto.json")
