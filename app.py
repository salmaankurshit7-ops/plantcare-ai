import streamlit as st
import tensorflow as tf
import numpy as np

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# GLOBAL STYLING
# ---------------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --ink: #17241e;
    --muted: #6b7a72;
    --paper: #f6f5ef;
    --card: rgba(255,255,255,0.88);
    --line: rgba(23,36,30,0.10);
    --accent: #2d6a4f;
    --accent-2: #d8a756;
    --deep: #102a21;
    --success: #2e7d5a;
    --danger: #b65f52;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f7f9f7;
    color: var(--ink);
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp p,
.stApp label,
.stApp .stMarkdown {
    color: var(--ink);
}

.hero,
.hero h1,
.hero p,
.hero .eyebrow,
.hero .hero-note {
    color: #ffffff !important;
}

.hero .eyebrow {
    color: #f1dbab !important;
}

.hero .hero-note {
    color: rgba(255,255,255,0.88) !important;
}

.card h3,
.feature-card h3,
.info-card h3,
.process-card h3 {
    color: #1b3b2d !important;
}

.card p,
.feature-card p,
.info-card p,
.process-card p {
    color: #5a6a62 !important;
}


.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1320px;
}

[data-testid="stSidebar"] {
    background: #0f241c;
    border-right: 1px solid rgba(255,255,255,0.07);
}

[data-testid="stSidebar"] * {
    color: #eef7f1 !important;
}

.brand {
    padding: 10px 4px 26px 4px;
}

.brand-mark {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #d8a756, #f0d18c);
    color: #15231d;
    font-size: 22px;
    font-weight: 700;
    box-shadow: 0 10px 25px rgba(0,0,0,0.20);
    margin-bottom: 10px;
}

.brand-name {
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: -0.02em;
}

.brand-sub {
    color: #a9b8af !important;
    font-size: 0.82rem;
    line-height: 1.5;
    margin-top: 2px;
}

.nav-label {
    color: #82978b !important;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.68rem;
    font-weight: 700;
    margin: 6px 0 8px;
}

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 30px;
    padding: 58px 56px;
    background:
        radial-gradient(circle at 92% 18%, rgba(216,167,86,0.30), transparent 20%),
        radial-gradient(circle at 78% 80%, rgba(112,171,135,0.24), transparent 24%),
        linear-gradient(135deg, #0e3023 0%, #194635 52%, #275d48 100%);
    color: white;
    box-shadow: 0 28px 55px rgba(16,42,33,0.22);
    margin-bottom: 28px;
}

.hero::after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -100px;
    bottom: -120px;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 50%;
}

.eyebrow {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #f1dbab;
    margin-bottom: 12px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 4.1rem;
    line-height: 1.0;
    letter-spacing: -0.04em;
    margin: 0 0 16px 0;
    max-width: 720px;
}

.hero p {
    max-width: 720px;
    color: rgba(255,255,255,0.86);
    font-size: 1.08rem;
    line-height: 1.75;
    margin-bottom: 0;
}

.hero-note {
    margin-top: 24px;
    display: inline-block;
    padding: 9px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.13);
    font-size: 0.8rem;
    color: rgba(255,255,255,0.82);
}

.section-kicker {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.72rem;
    font-weight: 700;
    color: #74857d;
    margin-top: 10px;
    margin-bottom: 6px;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 2.05rem;
    color: var(--ink);
    margin: 0 0 18px 0;
}

.card {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 14px 35px rgba(16,42,33,0.06);
}

.feature-card {
    min-height: 176px;
}

.feature-number {
    color: var(--accent-2);
    font-weight: 700;
    font-size: 0.76rem;
    letter-spacing: 0.16em;
}

.feature-card h3,
.card h3 {
    color: #1b3b2d;
    margin: 8px 0 8px 0;
}

.card p {
    color: var(--muted);
    line-height: 1.7;
}


[data-testid="stFileUploader"] section {
    background: #ffffff !important;
    border: 1px dashed #91a99b !important;
    border-radius: 18px !important;
}

[data-testid="stFileUploader"] section * {
    color: #41554b !important;
}

[data-testid="stFileUploader"] button {
    color: #18332a !important;
}

.stAlert p {
    color: inherit !important;
}

.process-card {
    min-height: 190px;
    background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(245,249,244,0.96));
}

.process-index {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: #c8d3cd;
    line-height: 1;
}

.upload-card {
    background: rgba(255,255,255,0.88);
    border: 1px dashed rgba(45,106,79,0.28);
    border-radius: 24px;
    padding: 26px;
}

.result-shell {
    border-radius: 26px;
    overflow: hidden;
    background: white;
    border: 1px solid var(--line);
    box-shadow: 0 18px 40px rgba(16,42,33,0.08);
}

.result-top {
    padding: 28px;
    background: linear-gradient(135deg, #102a21, #1b4b37);
    color: white;
}

.result-eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.70);
    font-weight: 700;
}

.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    margin: 7px 0 8px;
    line-height: 1.1;
}

.result-sub {
    color: rgba(255,255,255,0.78);
    font-size: 0.96rem;
}

.result-body {
    padding: 24px 28px 28px;
}

.metric-label {
    color: #7a8981;
    font-size: 0.74rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
}

.metric-value {
    font-size: 1.65rem;
    font-weight: 700;
    color: #17392a;
    margin-top: 5px;
}

.info-panel {
    background: rgba(255,255,255,0.92);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 22px;
    min-height: 220px;
}

.info-icon {
    display: inline-flex;
    width: 38px;
    height: 38px;
    border-radius: 12px;
    align-items: center;
    justify-content: center;
    background: #edf5ef;
    margin-bottom: 8px;
    font-size: 18px;
}

.info-panel h3 {
    margin: 5px 0 9px;
    color: #1b3b2d;
}

.info-panel p {
    margin: 0;
    color: var(--muted);
    line-height: 1.7;
}

.info-panel ul {
    padding-left: 20px;
    color: var(--muted);
    line-height: 1.7;
}

.notice {
    border-radius: 16px;
    padding: 15px 18px;
    background: #f0f5f1;
    border-left: 4px solid #6d8d7d;
    color: #4a5e54;
    font-size: 0.88rem;
    line-height: 1.6;
}

.healthy-notice {
    border-left-color: #4f8f6c;
    background: #edf7f0;
}

.warning-notice {
    border-left-color: #b66d4c;
    background: #fbf1ea;
}

.footer {
    text-align: center;
    color: #819088;
    font-size: 0.78rem;
    padding: 36px 0 12px;
}

.small-muted {
    color: #78877f;
    font-size: 0.84rem;
}

/* Streamlit widget polish */
.stButton > button {
    border-radius: 13px;
    min-height: 44px;
    font-weight: 700;
    border: 1px solid rgba(45,106,79,0.15);
}

.stButton > button[kind="primary"] {
    background: #173f2e;
    border: 1px solid #173f2e;
    color: white;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(16,42,33,0.12);
}

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.78);
    border-radius: 16px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# CLASS NAMES
# ---------------------------------------------------------

CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]


# ---------------------------------------------------------
# DISEASE INFORMATION
# ---------------------------------------------------------

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "description": "A fungal disease affecting apple leaves and fruit.",
        "symptoms": ["Olive, brown, or dark leaf lesions", "Scabby lesions on fruit"],
        "management": "Remove infected plant debris where practical and follow locally recommended disease-management practices.",
        "prevention": "Maintain orchard sanitation, good airflow, and regular monitoring."
    },
    "Apple___Black_rot": {
        "description": "A fungal disease that can affect apple leaves, branches, and fruit.",
        "symptoms": ["Dark leaf spots", "Dead tissue", "Dark lesions on fruit"],
        "management": "Remove infected material where practical and maintain good plant sanitation.",
        "prevention": "Prune for airflow and regularly remove diseased debris."
    },
    "Apple___Cedar_apple_rust": {
        "description": "A fungal disease affecting apple foliage and fruit.",
        "symptoms": ["Yellow to orange leaf spots", "Rust-like lesions"],
        "management": "Monitor affected plants and follow locally recommended disease-management practices.",
        "prevention": "Use resistant cultivars where available and maintain good sanitation."
    },
    "Apple___healthy": {
        "description": "The model classified this apple leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal plant care and monitor the leaf regularly.",
        "prevention": "Maintain good watering, nutrition, airflow, and sanitation."
    },
    "Blueberry___healthy": {
        "description": "The model classified this blueberry leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and regular monitoring.",
        "prevention": "Maintain suitable growing conditions and good sanitation."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "A fungal disease that produces powder-like growth on plant surfaces.",
        "symptoms": ["White or gray powdery growth", "Leaf distortion", "Reduced plant vigor"],
        "management": "Improve airflow and follow locally recommended disease-management practices.",
        "prevention": "Avoid overly dense foliage and monitor plants regularly."
    },
    "Cherry_(including_sour)___healthy": {
        "description": "The model classified this cherry leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal plant care and monitoring.",
        "prevention": "Maintain airflow, sanitation, and proper watering."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "description": "A fungal disease that primarily affects corn leaves.",
        "symptoms": ["Long gray or tan lesions", "Lesions developing along leaves"],
        "management": "Use appropriate locally recommended crop-management and disease-control practices.",
        "prevention": "Use resistant varieties where available and manage crop residue appropriately."
    },
    "Corn_(maize)___Common_rust_": {
        "description": "A fungal disease that causes rust-colored pustules on corn leaves.",
        "symptoms": ["Small reddish-brown pustules", "Rust-colored spots on foliage"],
        "management": "Monitor disease development and follow local recommendations when control is necessary.",
        "prevention": "Use resistant varieties where available and monitor fields regularly."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "A fungal disease of corn characterized by elongated leaf lesions.",
        "symptoms": ["Large elongated gray-green lesions", "Tan leaf lesions"],
        "management": "Use resistant varieties and follow locally recommended disease-management practices.",
        "prevention": "Maintain field sanitation and suitable crop-management practices."
    },
    "Corn_(maize)___healthy": {
        "description": "The model classified this corn leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and monitoring.",
        "prevention": "Maintain crop hygiene and regular field scouting."
    },
    "Grape___Black_rot": {
        "description": "A fungal disease affecting grape leaves, shoots, and fruit.",
        "symptoms": ["Brown leaf spots", "Dark lesions on developing fruit"],
        "management": "Remove infected plant material where practical and maintain canopy airflow.",
        "prevention": "Maintain sanitation, canopy management, and regular scouting."
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "A complex grapevine disease associated with wood-inhabiting pathogens.",
        "symptoms": ["Leaf discoloration", "Reduced vine vigor", "Fruit and growth symptoms"],
        "management": "Remove severely affected material where practical and follow local vineyard guidance.",
        "prevention": "Use good pruning and vineyard sanitation practices."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "A grape leaf disease that causes visible lesions and foliage damage.",
        "symptoms": ["Dark leaf spots", "Progressive foliage damage"],
        "management": "Maintain airflow and sanitation and follow local recommendations.",
        "prevention": "Monitor foliage regularly and maintain good canopy management."
    },
    "Grape___healthy": {
        "description": "The model classified this grape leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal vineyard care.",
        "prevention": "Maintain canopy airflow, sanitation, and routine monitoring."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "A serious citrus disease associated with bacterial infection and insect-vector transmission.",
        "symptoms": ["Mottled yellowing", "Asymmetrical leaf discoloration", "Reduced plant vigor"],
        "management": "Follow local citrus-health guidance and recommended vector and plant-management practices.",
        "prevention": "Use healthy planting material and monitor plants and vector populations."
    },
    "Peach___Bacterial_spot": {
        "description": "A bacterial disease affecting peach foliage and fruit.",
        "symptoms": ["Small dark leaf spots", "Lesions on fruit"],
        "management": "Maintain good airflow and sanitation and follow locally recommended disease-management practices.",
        "prevention": "Use clean planting material and avoid prolonged leaf wetness."
    },
    "Peach___healthy": {
        "description": "The model classified this peach leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal orchard care.",
        "prevention": "Maintain sanitation, airflow, and regular scouting."
    },
    "Pepper,_bell___Bacterial_spot": {
        "description": "A bacterial disease affecting pepper leaves and fruit.",
        "symptoms": ["Small dark spots on leaves", "Lesions on fruit"],
        "management": "Remove severely affected material where practical and follow local recommendations.",
        "prevention": "Use clean planting material and reduce prolonged leaf wetness."
    },
    "Pepper,_bell___healthy": {
        "description": "The model classified this pepper leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and monitoring.",
        "prevention": "Maintain sanitation, proper irrigation, and airflow."
    },
    "Potato___Early_blight": {
        "description": "A fungal disease commonly associated with dark lesions on potato leaves.",
        "symptoms": ["Brown circular lesions", "Concentric rings may appear", "Leaf yellowing"],
        "management": "Remove severely affected plant material where practical and follow local disease-management guidance.",
        "prevention": "Use healthy planting material, sanitation, and suitable crop rotation."
    },
    "Potato___Late_blight": {
        "description": "A destructive disease of potato caused by Phytophthora infestans.",
        "symptoms": ["Dark water-soaked lesions", "Rapid browning", "Possible white growth under humid conditions"],
        "management": "Take prompt management action according to local late-blight recommendations.",
        "prevention": "Use healthy planting material, monitor disease conditions, and reduce prolonged leaf wetness."
    },
    "Potato___healthy": {
        "description": "The model classified this potato leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and monitoring.",
        "prevention": "Use healthy planting material and maintain sanitation."
    },
    "Raspberry___healthy": {
        "description": "The model classified this raspberry leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and monitoring.",
        "prevention": "Maintain airflow, sanitation, and suitable watering."
    },
    "Soybean___healthy": {
        "description": "The model classified this soybean leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop management and monitoring.",
        "prevention": "Maintain crop hygiene and regular scouting."
    },
    "Squash___Powdery_mildew": {
        "description": "A fungal disease characterized by powdery growth on squash leaves.",
        "symptoms": ["White powdery patches", "Yellowing", "Reduced leaf performance"],
        "management": "Improve airflow and follow local disease-management recommendations.",
        "prevention": "Avoid dense foliage and monitor plants frequently."
    },
    "Strawberry___Leaf_scorch": {
        "description": "A fungal leaf disease affecting strawberry foliage.",
        "symptoms": ["Dark purple or brown spots", "Scorched-looking foliage"],
        "management": "Remove affected material where practical and follow local recommendations.",
        "prevention": "Maintain sanitation and avoid prolonged leaf wetness."
    },
    "Strawberry___healthy": {
        "description": "The model classified this strawberry leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal crop care and monitoring.",
        "prevention": "Maintain sanitation, airflow, and suitable irrigation."
    },
    "Tomato___Bacterial_spot": {
        "description": "A bacterial disease affecting tomato foliage and fruit.",
        "symptoms": ["Small dark leaf spots", "Yellowing", "Fruit lesions"],
        "management": "Remove severely affected material where practical and follow local recommendations.",
        "prevention": "Use clean planting material and reduce prolonged foliage wetness."
    },
    "Tomato___Early_blight": {
        "description": "A fungal disease commonly affecting tomato leaves.",
        "symptoms": ["Brown circular lesions", "Concentric rings", "Progressive yellowing"],
        "management": "Remove affected foliage where practical, maintain airflow, and follow local recommendations.",
        "prevention": "Maintain sanitation, avoid prolonged leaf wetness, and monitor regularly."
    },
    "Tomato___Late_blight": {
        "description": "A rapidly developing tomato disease caused by Phytophthora infestans.",
        "symptoms": ["Dark water-soaked lesions", "Rapid browning of foliage"],
        "management": "Act promptly and follow locally recommended late-blight management practices.",
        "prevention": "Use healthy planting material and reduce prolonged foliage wetness."
    },
    "Tomato___Leaf_Mold": {
        "description": "A fungal disease favored by humid conditions.",
        "symptoms": ["Yellow areas on leaves", "Olive or brown growth on leaf undersides"],
        "management": "Improve ventilation and reduce humidity around foliage.",
        "prevention": "Maintain good spacing and airflow."
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "A fungal disease that primarily affects tomato leaves.",
        "symptoms": ["Small circular leaf spots", "Dark margins", "Pale centers"],
        "management": "Remove affected foliage where practical and maintain sanitation.",
        "prevention": "Avoid prolonged leaf wetness and remove infected debris."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "description": "A pest infestation caused by tiny spider mites feeding on plant tissue.",
        "symptoms": ["Fine pale speckling", "Yellowing or bronzing", "Possible webbing"],
        "management": "Inspect leaf undersides and follow integrated pest-management practices.",
        "prevention": "Monitor plants regularly and protect beneficial organisms."
    },
    "Tomato___Target_Spot": {
        "description": "A fungal tomato disease producing characteristic circular lesions.",
        "symptoms": ["Brown circular lesions", "Concentric rings may develop"],
        "management": "Maintain airflow, remove affected material where practical, and follow local recommendations.",
        "prevention": "Reduce prolonged foliage wetness and maintain sanitation."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "A viral disease of tomato associated with whitefly transmission.",
        "symptoms": ["Leaf curling", "Yellowing", "Stunting", "Reduced growth"],
        "management": "Follow local integrated pest-management and plant-health guidance.",
        "prevention": "Use healthy planting material and monitor vector populations."
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "A viral disease that can produce mosaic patterns and reduced plant vigor.",
        "symptoms": ["Mottled or mosaic leaf patterns", "Leaf distortion", "Reduced growth"],
        "management": "Remove infected material where appropriate and maintain tool and hand sanitation.",
        "prevention": "Use clean planting material and avoid spreading plant sap between plants."
    },
    "Tomato___healthy": {
        "description": "The model classified this tomato leaf as healthy.",
        "symptoms": ["No major disease symptoms were identified by the model."],
        "management": "Continue normal plant care and monitor the plant regularly.",
        "prevention": "Maintain airflow, sanitation, balanced watering, and routine scouting."
    }
}


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------

def clean_name(name):
    return name.replace("___", " — ").replace("_", " ").replace("  ", " ").strip()


def confidence_label(confidence):
    if confidence >= 90:
        return "High model confidence"
    if confidence >= 70:
        return "Moderate model confidence"
    return "Low model confidence"


# ---------------------------------------------------------
# MODEL LOADING - COMPATIBLE WITH STREAMLIT 1.22.0
# ---------------------------------------------------------

@st.cache(allow_output_mutation=True)
def load_model():
    return tf.keras.models.load_model("trained_model.h5")


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

def model_prediction(test_image):
    model = load_model()

    image = tf.keras.preprocessing.image.load_img(
        test_image,
        target_size=(128, 128)
    )

    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])

    prediction = model.predict(input_arr, verbose=0)

    result_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction)) * 100

    top_indices = np.argsort(prediction[0])[-3:][::-1]

    top_predictions = []
    for index in top_indices:
        top_predictions.append(
            (
                CLASS_NAMES[int(index)],
                float(prediction[0][int(index)]) * 100
            )
        )

    return result_index, confidence, top_predictions


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown("""
<div class="brand">
    <div class="brand-mark">🌿</div>
    <div class="brand-name">PlantCare AI</div>
    <div class="brand-sub">AI-powered plant health intelligence</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="nav-label">Workspace</div>', unsafe_allow_html=True)

app_mode = st.sidebar.radio(
    "Navigation",
    ["Home", "Disease Recognition", "About"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("<div class='small-muted'>38-class CNN classification</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if app_mode == "Home":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">Plant health intelligence</div>
        <h1>Know what your plant needs.</h1>
        <p>
            PlantCare AI turns a single leaf photograph into an intelligent
            plant-health assessment using a trained convolutional neural network,
            followed by clear disease insights and practical guidance.
        </p>
        <div class="hero-note">38 plant-health classes • image-based AI</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">Inside the platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">From image to insight.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("01", "AI Detection", "A CNN analyzes visual patterns in the uploaded leaf image."),
        ("02", "Confidence", "See the model's strongest predicted class and top alternatives."),
        ("03", "Disease Insight", "Understand the condition through concise, class-specific information."),
        ("04", "Take Action", "Review general management and prevention guidance."),
    ]

    for col, (number, title, text) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(f"""
            <div class="card feature-card">
                <div class="feature-number">{number}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">The experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">A simple four-step workflow.</div>', unsafe_allow_html=True)

    p1, p2, p3, p4 = st.columns(4)
    process = [
        ("01", "Upload", "Choose a clear image of the plant leaf."),
        ("02", "Analyze", "The trained CNN evaluates the image."),
        ("03", "Understand", "See the predicted class and model confidence."),
        ("04", "Act", "Read symptoms, management, and prevention guidance.")
    ]

    for col, (number, title, text) in zip([p1, p2, p3, p4], process):
        with col:
            st.markdown(f"""
            <div class="card process-card">
                <div class="process-index">{number}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Ready to analyze a leaf?</h3>
        <p>
            Open <b>Disease Recognition</b> in the sidebar to upload an image
            and run the trained model.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# DISEASE RECOGNITION
# ---------------------------------------------------------

elif app_mode == "Disease Recognition":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">AI analysis workspace</div>
        <h1>See what your leaf is telling you.</h1>
        <p>
            Upload a clear image, run the trained classifier, and explore the
            model's prediction together with practical plant-health context.
        </p>
    </div>
    """, unsafe_allow_html=True)

    upload_col, result_col = st.columns([0.95, 1.05], gap="large")

    with upload_col:
        st.markdown('<div class="section-kicker">Step 01</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-heading">Upload a leaf</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="upload-card">
            <h3>Bring a clear image into the workspace.</h3>
            <p class="small-muted">
                Best results come from a well-lit leaf image with the leaf clearly visible.
            </p>
        </div>
        """, unsafe_allow_html=True)

        test_image = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"]
        )

        if test_image is not None:
            st.image(
                test_image,
                caption="Uploaded leaf",
                use_column_width=True
            )

            st.markdown(
                f"<div class='small-muted'>Ready to analyze • {test_image.name}</div>",
                unsafe_allow_html=True
            )

        else:
            st.info("Upload a JPG, JPEG, or PNG image to begin.")

    with result_col:
        st.markdown('<div class="section-kicker">Step 02</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-heading">Run AI analysis</div>', unsafe_allow_html=True)

        if test_image is None:
            st.markdown("""
            <div class="card">
                <h3>Your result will appear here.</h3>
                <p>
                    Once an image is uploaded, PlantCare AI will classify it into
                    one of the 38 trained plant-health classes.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button("Analyze Leaf"):
                with st.spinner("Analyzing leaf image..."):
                    result_index, confidence, top_predictions = model_prediction(test_image)

                predicted_class = CLASS_NAMES[result_index]
                display_name = clean_name(predicted_class)
                info = DISEASE_INFO.get(predicted_class)
                is_healthy = "healthy" in predicted_class.lower()

                if is_healthy:
                    st.markdown("""
                    <div class="notice healthy-notice">
                        <b>Healthy classification</b><br>
                        The model classified this image as a healthy leaf.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="notice warning-notice">
                        <b>Potential issue detected</b><br>
                        The model identified a disease or pest-related class.
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown(f"""
                <div class="result-shell">
                    <div class="result-top">
                        <div class="result-eyebrow">AI analysis complete</div>
                        <div class="result-title">{display_name}</div>
                        <div class="result-sub">{confidence_label(confidence)}</div>
                    </div>
                    <div class="result-body">
                        <div class="metric-label">Model confidence</div>
                        <div class="metric-value">{confidence:.2f}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.progress(min(max(confidence / 100.0, 0.0), 1.0))

                st.markdown('<div class="section-kicker">Model output</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-heading">Top predictions</div>', unsafe_allow_html=True)

                for rank, (prediction_name, probability) in enumerate(top_predictions, 1):
                    st.markdown(
                        f"**{rank}. {clean_name(prediction_name)}** — {probability:.2f}%"
                    )
                    st.progress(min(max(probability / 100.0, 0.0), 1.0))

                if info:
                    st.markdown('<div class="section-kicker">Plant intelligence</div>', unsafe_allow_html=True)
                    st.markdown('<div class="section-heading">Understand the result.</div>', unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="info-panel">
                        <div class="info-icon">◌</div>
                        <h3>What is it?</h3>
                        <p>{info['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    i1, i2 = st.columns(2, gap="medium")

                    symptom_html = "".join([f"<li>{item}</li>" for item in info["symptoms"]])

                    with i1:
                        st.markdown(f"""
                        <div class="info-panel">
                            <div class="info-icon">!</div>
                            <h3>Symptoms</h3>
                            <ul>{symptom_html}</ul>
                        </div>
                        """, unsafe_allow_html=True)

                    with i2:
                        st.markdown(f"""
                        <div class="info-panel">
                            <div class="info-icon">+</div>
                            <h3>Management</h3>
                            <p>{info['management']}</p>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="info-panel">
                        <div class="info-icon">✓</div>
                        <h3>Prevention</h3>
                        <p>{info['prevention']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("""
                    <div class="notice">
                        <b>Important:</b> Model confidence is the probability assigned by the
                        classifier to the selected class. It should not be interpreted as a
                        definitive agricultural diagnosis.
                    </div>
                    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

elif app_mode == "About":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">About the product</div>
        <h1>Where deep learning meets plant health.</h1>
        <p>
            PlantCare AI combines a trained convolutional neural network with
            a clean application layer that turns a model prediction into useful context.
        </p>
    </div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2, gap="large")

    with a1:
        st.markdown("""
        <div class="card">
            <h3>The model</h3>
            <p>
                A convolutional neural network processes plant-leaf images and
                classifies them across 38 plant-health categories.
            </p>
            <p>
                The application uses the trained model saved in
                <b>trained_model.h5</b> and performs prediction on a 128 × 128
                RGB image input.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with a2:
        st.markdown("""
        <div class="card">
            <h3>The application layer</h3>
            <p>
                After the classifier returns its result, the app maps the predicted
                class to a curated information layer containing an explanation,
                symptoms, general management guidance, and prevention guidance.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">Technology</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Built with a focused stack.</div>', unsafe_allow_html=True)

    t1, t2, t3, t4 = st.columns(4)
    tech = [
        ("Python", "Application logic and prediction pipeline."),
        ("TensorFlow", "Neural-network inference."),
        ("Keras", "CNN model definition and loading."),
        ("Streamlit", "Interactive web interface.")
    ]

    for col, (title, text) in zip([t1, t2, t3, t4], tech):
        with col:
            st.markdown(f"""
            <div class="card feature-card">
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">Project architecture</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">A clean separation of responsibilities.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
            <b>Leaf image</b> → <b>CNN</b> → <b>38 probabilities</b> →
            <b>highest-probability class</b> → <b>confidence</b> →
            <b>disease information</b> → <b>user interface</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">Dataset note</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p>
            The model's class structure follows the 38-class plant leaf disease
            taxonomy used by the training project. The information shown in this
            interface is intended for educational and decision-support purposes.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class="footer">
    PlantCare AI • Deep Learning for plant health recognition
</div>
""", unsafe_allow_html=True)
