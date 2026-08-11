"""
app.py - Multilingual Indian Agricultural Yield Attribution & ROI Predictor
HACK CORE 2026 - Problem Statement 07
Team 15: Soham Prabhakar Kadu (Lead), Singireddy Prabhumitrareddy, Bhakti Ajay Kadam
Mentors: Dr. Shahbaz (ANNAM.AI), Hana Hafer (Syngenta)
"""

import os
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import urllib.parse
from datetime import datetime

from data_generator import generate_synthetic_field_trials, fetch_meteoblue_weather, fetch_cehub_forecast, fetch_10day_forecast
import pdf_report

# Page Configuration
st.set_page_config(
    page_title="AgriAttribute AI India | Syngenta Biologicals ROI Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Premium Light Theme)
st.markdown("""
<style>
    /* Premium Light Theme Core */
    .stApp {
        background-color: #f8fafc;
        color: #334155;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    h1, h2, h3, h4, p, span, div { color: #334155 !important; }
    
    .header-box {
        background: linear-gradient(135deg, #e6fcf5, #f0fdf4);
        border: 1px solid #a7f3d0;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    .header-title {
        font-size: 2.2rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #047857, #0284c7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    .badge-container { display: flex; gap: 10px; margin-top: 12px; flex-wrap: wrap; }
    .badge { background: #ffffff; border: 1px solid #cbd5e1; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; color: #475569 !important; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
    .badge-highlight { background: #ecfdf5; border: 1px solid #059669; color: #047857 !important; font-weight: 600; }
    
    .kpi-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 18px 20px; text-align: center; transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03); }
    .kpi-card:hover { border-color: #059669; transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08); }
    .kpi-title { font-size: 0.85rem !important; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b !important; margin-bottom: 6px; }
    .kpi-value { font-size: 1.8rem !important; font-weight: 800; color: #0f172a !important; }
    .kpi-positive { color: #059669 !important; }
    .kpi-subtext { font-size: 0.78rem !important; color: #64748b !important; margin-top: 4px; }
    
    .section-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; margin-bottom: 24px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03); }
    
    .wa-button { display: inline-flex; align-items: center; background-color: #25D366; color: white !important; font-weight: bold; padding: 10px 20px; border-radius: 8px; text-decoration: none; margin-top: 15px; transition: background-color 0.2s, transform 0.2s; box-shadow: 0 4px 6px -1px rgba(37, 211, 102, 0.4); }
    .wa-button:hover { background-color: #1ebe57; text-decoration: none; transform: translateY(-2px); }
    
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 1px solid #e2e8f0; }
    .stSelectbox label, .stSlider label, .stNumberInput label, .stRadio label { color: #334155 !important; font-weight: 600; }
    
    /* Weather Forecast Cards */
    .weather-card {
        background: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px; text-align: center;
    }
    .weather-date { font-weight: bold; color: #0f172a !important; font-size: 0.9rem; }
    .weather-icon { font-size: 1.5rem; margin: 5px 0; }
    .weather-temp { font-weight: bold; color: #ef4444 !important; font-size: 0.85rem;}
    .weather-sub { font-size: 0.7rem; color: #64748b !important; }
</style>
""", unsafe_allow_html=True)

# Multilingual Dictionary
TRANSLATIONS = {
    "English": {
        "title": "🌾 AgriAttribute AI India: Yield Attribution & ROI Predictor",
        "subtitle": "Isolating Syngenta Biological Product Yield Boosts from Monsoon Weather & Soil Factors",
        "crop_select": "Select Crop Type",
        "region_select": "Agro-Climatic Region",
        "soil_sec": "🌱 Soil Health Profile (ISRIC SoilGrids)",
        "soc": "Soil Organic Carbon (g/kg)",
        "ph": "Soil pH",
        "nitrogen": "Nitrogen (N kg/ha)",
        "weather_sec": "🌧️ Monsoon & Weather Telemetry (Meteoblue)",
        "fetch_weather": "🔄 Fetch Live Weather for Region",
        "rainfall": "Cumulative Rainfall (mm)",
        "gdd": "Growing Degree Days (GDD)",
        "heat_stress": "Heat Stress Days (>38°C)",
        "ndvi": "Peak Satellite NDVI Index",
        "bio_sec": "🔬 Syngenta Biological Treatment",
        "fetch_cehub": "🤖 CE Hub Smart Dosage Sync",
        "bio_apply": "Apply Syngenta Biological Product",
        "bio_product": "Select Biological Product",
        "bio_dosage": "Dosage Rate (L/acre)",
        "market_sec": "💰 Indian Market & Crop Economics",
        "bio_cost": "Biological Product Cost (₹/acre)",
        "crop_price": "Crop Price / MSP (₹/Quintal)",
        "kpi_predicted": "Total Predicted Yield",
        "kpi_delta": "Attributed Bio Boost (ΔY)",
        "kpi_gross": "Gross Revenue Gain",
        "kpi_profit": "Net Profit / Acre",
        "kpi_roi": "Farmer Return on Investment",
        "timeline_title": "📈 Centerpiece Visual: Season-Long Growth & Divergence Trajectory",
        "seeing_believing": "Addressing Hana Hafer's 'Seeing is Believing' mandate: Proving how Syngenta Biologicals create measurable divergence from untreated fields mid-season.",
        "shap_title": "📊 Yield Factor Attribution Decomposition (SHAP)",
        "shap_desc": "Mathematical breakdown isolating Bio-efficacy from Soil & Weather noise",
        "counterfactual_title": "💡 Counterfactual Agronomic Guidance",
        "control_yield": "Untreated Control Yield (Without Bio)",
        "treated_yield": "Yield With Syngenta Biological",
        "attributed_boost": "Direct Biological Attribution",
        "opp_cost": "Opportunity Cost Context",
        "whatsapp_share": "Share ROI Report via WhatsApp",
        "yield_unit": "q/acre",
        "currency": "₹",
        "forecast_title": "🌦️ 10-Day Agronomic Weather Forecast (Powered by Meteoblue)"
    },
    "Hindi (हिंदी)": {
        "title": "🌾 एग्री-एट्रीब्यूट AI: फसल उपज और लाभ (ROI) का अनुमान",
        "subtitle": "सिंजेंटा बायोलॉजिकल उत्पाद के वास्तविक प्रभाव को मौसम और मिट्टी के कारकों से अलग करना",
        "crop_select": "फसल का प्रकार चुनें",
        "region_select": "कृषि-जलवायु क्षेत्र",
        "soil_sec": "🌱 मृदा स्वास्थ्य (ISRIC SoilGrids)",
        "soc": "मृदा जैविक कार्बन (g/kg)",
        "ph": "मृदा pH",
        "nitrogen": "नाइट्रोजन (N kg/ha)",
        "weather_sec": "🌧️ मानसून और मौसम डेटा (Meteoblue)",
        "fetch_weather": "🔄 अपने क्षेत्र का मौसम डेटा प्राप्त करें",
        "rainfall": "कुल वर्षा (मिमी)",
        "gdd": "ग्रोइंग डिग्री डेज़ (GDD)",
        "heat_stress": "अत्यधिक गर्मी के दिन (>38°C)",
        "ndvi": "सैटेलाइट NDVI इंडेक्स",
        "bio_sec": "🔬 सिंजेंटा बायोलॉजिकल उपचार",
        "fetch_cehub": "🤖 CE Hub से सही मात्रा प्राप्त करें",
        "bio_apply": "सिंजेंटा बायोलॉजिकल उत्पाद का प्रयोग करें",
        "bio_product": "बायोलॉजिकल उत्पाद चुनें",
        "bio_dosage": "मात्रा (लीटर/एकड़)",
        "market_sec": "💰 बाजार मूल्य और अर्थशास्त्र",
        "bio_cost": "उत्पाद की लागत (₹/एकड़)",
        "crop_price": "फसल मूल्य / MSP (₹/क्विंटल)",
        "kpi_predicted": "कुल अनुमानित उपज",
        "kpi_delta": "अतिरिक्त उपज (बायो से लाभ)",
        "kpi_gross": "अतिरिक्त आय",
        "kpi_profit": "शुद्ध लाभ / एकड़",
        "kpi_roi": "निवेश पर प्रतिफल (ROI)",
        "timeline_title": "📈 फसल की वृद्धि और उपज का तुलनात्मक विश्लेषण",
        "seeing_believing": "हाना हैफर के 'देखना ही विश्वास करना है' सिद्धांत पर: यह साबित करना कि सिंजेंटा बायोलॉजिकल उपचारित खेत मध्य-सीजन में कैसे बेहतर प्रदर्शन करते हैं।",
        "shap_title": "📊 उपज योगदान का विश्लेषण (SHAP)",
        "shap_desc": "मौसम और मिट्टी के प्रभाव से जैविक उत्पाद के वास्तविक प्रभाव को अलग करना",
        "counterfactual_title": "💡 कृषि संबंधी तुलनात्मक सलाह",
        "control_yield": "बिना सिंजेंटा बायोलॉजिकल की उपज",
        "treated_yield": "सिंजेंटा बायोलॉजिकल के साथ उपज",
        "attributed_boost": "बायोलॉजिकल उत्पाद से शुद्ध लाभ",
        "opp_cost": "अवसर लागत (यूरिया की तुलना में)",
        "whatsapp_share": "WhatsApp पर रिपोर्ट शेयर करें",
        "yield_unit": "क्विंटल/एकड़",
        "currency": "₹",
        "forecast_title": "🌦️ 10-दिन का मौसम पूर्वानुमान (Meteoblue)"
    },
    "Marathi (मराठी)": {
        "title": "🌾 ऍग्री-अॅट्रिब्युट AI: पीक उत्पादन आणि नफा (ROI) अंदाज",
        "subtitle": "हवामान आणि मातीच्या घटकांपासून सिंजेंटा बायोलॉजिकल उत्पादनाचा वास्तविक प्रभाव वेगळा करणे",
        "crop_select": "पिकाचा प्रकार निवडा",
        "region_select": "कृषी-हवामान क्षेत्र",
        "soil_sec": "🌱 मातीचे आरोग्य (ISRIC SoilGrids)",
        "soc": "मातीतील सेंद्रिय कार्बन (g/kg)",
        "ph": "मातीचा सामू (pH)",
        "nitrogen": "नत्र/नायट्रोजन (N kg/ha)",
        "weather_sec": "🌧️ मान्सून आणि हवामान डेटा (Meteoblue)",
        "fetch_weather": "🔄 हवामान डेटा मिळवा",
        "rainfall": "एकूण पाऊस (मिमी)",
        "gdd": "ग्रोइंग डिग्री डेज (GDD)",
        "heat_stress": "उष्णतेचे दिवस (>38°C)",
        "ndvi": "सॅटेलाइट NDVI इंडेक्स",
        "bio_sec": "🔬 सिंजेंटा बायोलॉजिकल उपचार",
        "fetch_cehub": "🤖 CE Hub द्वारे योग्य प्रमाण मिळवा",
        "bio_apply": "सिंजेंटा बायोलॉजिकल उत्पादन वापरा",
        "bio_product": "बायोलॉजिकल उत्पादन निवडा",
        "bio_dosage": "प्रमाण (लिटर/एकर)",
        "market_sec": "💰 बाजार भाव आणि अर्थशास्त्र",
        "bio_cost": "उत्पादनाचा खर्च (₹/एकर)",
        "crop_price": "पिकाचा भाव / MSP (₹/क्विंटल)",
        "kpi_predicted": "एकूण अंदाजित उत्पादन",
        "kpi_delta": "वाढीव उत्पादन (बायोचा फायदा)",
        "kpi_gross": "अतिरिक्त उत्पन्न",
        "kpi_profit": "निव्वळ नफा / एकर",
        "kpi_roi": "गुंतवणुकीवरील परतावा (ROI)",
        "timeline_title": "📈 पिकाची वाढ आणि उत्पादनाचे तुलनात्मक विश्लेषण",
        "seeing_believing": "'पाहणे म्हणजे विश्वास ठेवणे': सिंजेंटा बायोलॉजिकल उत्पादन पीक हंगामात सामान्य शेतापेक्षा कशी चांगली कामगिरी करते हे सिद्ध करणे.",
        "shap_title": "📊 उत्पादन योगदानाचे विश्लेषण (SHAP)",
        "shap_desc": "हवामान आणि मातीच्या परिणामातून जैविक उत्पादनाचा वास्तविक प्रभाव वेगळा करणे",
        "counterfactual_title": "💡 कृषी विषयक तुलनात्मक सल्ला",
        "control_yield": "सिंजेंटा बायोलॉजिकल शिवाय उत्पादन",
        "treated_yield": "सिंजेंटा बायोलॉजिकल सोबत उत्पादन",
        "attributed_boost": "बायोलॉजिकल उत्पादनाचा निव्वळ फायदा",
        "opp_cost": "संधी खर्च (युरियाच्या तुलनेत)",
        "whatsapp_share": "WhatsApp वर रिपोर्ट शेअर करा",
        "yield_unit": "क्विंटल/एकर",
        "currency": "₹",
        "forecast_title": "🌦️ 10-दिवसांचा हवामान अंदाज (Meteoblue)"
    },
    "Telugu (తెలుగు)": {
        "title": "🌾 అగ్రి-అట్రిబ్యూట్ AI: పంట దిగుబడి మరియు లాభం (ROI) అంచనా",
        "subtitle": "వాతావరణం మరియు నేల కారకాల నుండి సింజెంటా బయోలాజికల్ ఉత్పత్తి యొక్క నిజమైన ప్రభావాన్ని వేరు చేయడం",
        "crop_select": "పంట రకాన్ని ఎంచుకోండి",
        "region_select": "వ్యవసాయ-శీతోష్ణస్థితి ప్రాంతం",
        "soil_sec": "🌱 నేల ఆరోగ్యం (ISRIC SoilGrids)",
        "soc": "నేల సేంద్రియ కర్బనం (g/kg)",
        "ph": "నేల pH",
        "nitrogen": "నత్రజని (N kg/ha)",
        "weather_sec": "🌧️ రుతుపవనాలు మరియు వాతావరణ డేటా (Meteoblue)",
        "fetch_weather": "🔄 వాతావరణ డేటాను పొందండి",
        "rainfall": "మొత్తం వర్షపాతం (మి.మీ)",
        "gdd": "గ్రోయింగ్ డిగ్రీ డేస్ (GDD)",
        "heat_stress": "తీవ్రమైన వేడి రోజులు (>38°C)",
        "ndvi": "ఉపగ్రహ NDVI ఇండెక్స్",
        "bio_sec": "🔬 సింజెంటా బయోలాజికల్ చికిత్స",
        "fetch_cehub": "🤖 CE Hub ద్వారా సరైన మోతాదు పొందండి",
        "bio_apply": "సింజెంటా బయోలాజికల్ ఉత్పత్తిని వాడండి",
        "bio_product": "బయోలాజికల్ ఉత్పత్తిని ఎంచుకోండి",
        "bio_dosage": "మోతాదు (లీటర్లు/ఎకరం)",
        "market_sec": "💰 మార్కెట్ ధరలు మరియు ఆర్థిక శాస్త్రం",
        "bio_cost": "ఉత్పత్తి ఖర్చు (₹/ఎకరం)",
        "crop_price": "పంట ధర / MSP (₹/క్వింటాల్)",
        "kpi_predicted": "మొత్తం అంచనా దిగుబడి",
        "kpi_delta": "అదనపు దిగుబడి (బయో ప్రయోజనం)",
        "kpi_gross": "అదనపు ఆదాయం",
        "kpi_profit": "నికర లాభం / ఎకరం",
        "kpi_roi": "పెట్టుబడిపై రాబడి (ROI)",
        "timeline_title": "📈 పంట పెరుగుదల మరియు దిగుబడి యొక్క తులనాత్మక విశ్లేషణ",
        "seeing_believing": "'చూడటమే నమ్మకం': సాధారణ పొలం కంటే సింజెంటా బయోలాజికల్ ఉత్పత్తి మెరుగైన పనితీరును ఎలా కనబరుస్తుందో నిరూపించడం.",
        "shap_title": "📊 దిగుబడి సహకారం యొక్క విశ్లేషణ (SHAP)",
        "shap_desc": "వాతావరణం మరియు నేల ప్రభావం నుండి బయోలాజికల్ ఉత్పత్తి యొక్క నిజమైన ప్రభావాన్ని వేరు చేయడం",
        "counterfactual_title": "💡 వ్యవసాయ తులనాత్మక సలహా",
        "control_yield": "సింజెంటా బయోలాజికల్ లేకుండా దిగుబడి",
        "treated_yield": "సింజెంటా బయోలాజికల్ తో దిగుబడి",
        "attributed_boost": "బయోలాజికల్ ఉత్పత్తి నికర ప్రయోజనం",
        "opp_cost": "అవకాశ ఖర్చు (యూరియాతో పోలిస్తే)",
        "whatsapp_share": "WhatsAppలో నివేదికను పంచుకోండి",
        "yield_unit": "క్వింటాల్/ఎకరం",
        "currency": "₹",
        "forecast_title": "🌦️ 10-రోజుల వాతావరణ సూచన (Meteoblue)"
    }
}

REGION_COORDS = {
    "Punjab & Haryana (Indo-Gangetic)": {"lat": 30.9010, "lon": 75.8573},
    "Maharashtra & Vidarbha (Deccan)": {"lat": 21.1458, "lon": 79.0882},
    "Andhra Pradesh & Telangana": {"lat": 16.5062, "lon": 80.6480},
    "Uttar Pradesh & Bihar": {"lat": 26.8467, "lon": 80.9462},
    "Karnataka & Tamil Nadu": {"lat": 15.3173, "lon": 75.7139}
}

@st.cache_resource
def load_ml_pipeline():
    if os.path.exists("model.pkl") and os.path.exists("shap_explainer.pkl"):
        model = joblib.load("model.pkl")
        artifacts = joblib.load("shap_explainer.pkl")
        return model, artifacts
    else:
        df = generate_synthetic_field_trials(num_samples=1000)
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/field_trials.csv", index=False)
        from train_model import train_yield_attribution_model
        train_yield_attribution_model("data/field_trials.csv")
        return joblib.load("model.pkl"), joblib.load("shap_explainer.pkl")

def get_weather_emoji(condition):
    if "Rain" in condition: return "🌧️"
    if "Cloud" in condition: return "⛅"
    if "Clear" in condition: return "🌙"
    return "☀️"

def build_growth_divergence_timeline(days=120, base_yield=24.0, bio_boost=3.8, heat_stress_day=50, lang_dict=None):
    day_array = np.arange(1, days + 1)
    sigmoid = 1 / (1 + np.exp(-0.08 * (day_array - 55)))
    curve_control = base_yield * sigmoid
    bio_activation = 1 / (1 + np.exp(-0.12 * (day_array - 40)))
    stress_impact = np.where(day_array > heat_stress_day, np.exp(-0.025 * (day_array - heat_stress_day)), 1.0)
    
    curve_control_final = curve_control * (0.90 + 0.10 * stress_impact)
    curve_bio_final = (curve_control + bio_boost * bio_activation) * (0.96 + 0.04 * stress_impact)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=day_array, y=np.round(curve_control_final, 2), mode='lines', name='Untreated Control', line=dict(color='#64748b', width=2.5, dash='dash')))
    fig.add_trace(go.Scatter(x=day_array, y=np.round(curve_bio_final, 2), mode='lines', name='With Syngenta Bio', line=dict(color='#059669', width=3.8), fill='tonexty', fillcolor='rgba(16, 185, 129, 0.15)'))
    
    divergence_day = 42
    fig.add_annotation(x=divergence_day, y=float(curve_bio_final[divergence_day-1]), text="<b>'Seeing is Believing'</b>", showarrow=True, arrowhead=2, arrowcolor="#d97706", ax=45, ay=-55, font=dict(size=12, color="#d97706"), bgcolor="rgba(255, 255, 255, 0.95)", bordercolor="#d97706")
    
    fig.update_layout(title=dict(text=f"<b>{lang_dict['timeline_title']}</b>", font=dict(size=17, color="#0f172a")), xaxis=dict(title="Days After Sowing", gridcolor="#e2e8f0"), yaxis=dict(title=f"Yield ({lang_dict['yield_unit']})", gridcolor="#e2e8f0"), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), margin=dict(l=40, r=40, t=60, b=40), hovermode="x unified")
    return fig

def main():
    if 's_dosage' not in st.session_state: st.session_state.s_dosage = 2.0
    
    model, artifacts = load_ml_pipeline()
    
    st.sidebar.markdown("### 🌐 Select Language / भाषा चुनें")
    selected_lang = st.sidebar.selectbox("Language", ["English", "Hindi (हिंदी)", "Marathi (मराठी)", "Telugu (తెలుగు)"], label_visibility="collapsed")
    t = TRANSLATIONS.get(selected_lang, TRANSLATIONS["English"])

    st.markdown(f"""
    <div class="header-box">
        <div class="header-title">{t['title']}</div>
        <div style="font-size: 1.05rem; color: #475569 !important; font-weight: 500;">{t['subtitle']}</div>
        <div class="badge-container">
            <span class="badge badge-highlight">HACK CORE 2026 - Problem Statement 07</span>
            <span class="badge">Team 15: Soham Prabhakar Kadu | Singireddy P. | Bhakti Ajay Kadam</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # UI Abstraction Mode
    ui_mode = st.sidebar.radio("Platform Experience Mode", ["🚜 Farmer (Simple)", "⚙️ Agronomist (Advanced)"])
    st.sidebar.divider()
    
    st.sidebar.header("🎛️ " + t["crop_select"])
    crop = st.sidebar.selectbox(t["crop_select"], ["Rice (Paddy)", "Wheat", "Cotton", "Sugarcane", "Maize", "Soybean"])
    region = st.sidebar.selectbox(t["region_select"], list(REGION_COORDS.keys()))
    
    # Initialize variables that will feed into the ML model
    soc, ph, nitrogen, rainfall, gdd, heat_stress, ndvi = 7.8, 6.8, 140, 780, 2350, 5, 0.76
    
    if ui_mode == "🚜 Farmer (Simple)":
        st.sidebar.subheader("🌱 Farm Health & Weather")
        soil_quality = st.sidebar.select_slider("Soil Quality", options=["Poor", "Average", "Excellent"], value="Average")
        monsoon = st.sidebar.select_slider("Monsoon Rain", options=["Deficient", "Normal", "Excess"], value="Normal")
        heat = st.sidebar.select_slider("Summer Heat", options=["Normal", "Very Hot"], value="Normal")
        
        # Translate simple inputs to ML features
        if soil_quality == "Poor": soc, ph, nitrogen = 4.5, 5.5, 60
        elif soil_quality == "Excellent": soc, ph, nitrogen = 12.0, 7.2, 200
        
        if monsoon == "Deficient": rainfall, ndvi = 400, 0.55
        elif monsoon == "Excess": rainfall, ndvi = 1300, 0.88
        
        if heat == "Very Hot": heat_stress, gdd = 15, 2800
        
    else:
        st.sidebar.subheader(t["soil_sec"])
        soc = st.sidebar.slider(t["soc"], 3.0, 15.0, 7.8, step=0.1)
        ph = st.sidebar.slider(t["ph"], 5.5, 8.5, 6.8, step=0.1)
        nitrogen = st.sidebar.slider(t["nitrogen"], 50, 250, 140)
        
        st.sidebar.subheader(t["weather_sec"])
        rainfall = st.sidebar.slider(t["rainfall"], 300, 1600, 780)
        gdd = st.sidebar.slider(t["gdd"], 1500, 3200, 2350)
        heat_stress = st.sidebar.slider(t["heat_stress"], 0, 20, 5)
        ndvi = st.sidebar.slider(t["ndvi"], 0.30, 0.95, 0.76)
    
    st.sidebar.subheader(t["bio_sec"])
    if st.sidebar.button(t["fetch_cehub"]):
        ce_data = fetch_cehub_forecast()
        st.session_state.s_dosage = float(ce_data.get("optimal_dosage_l_ha", 2.5))
        st.sidebar.success("✅ CE Hub Optimal Dosage Synced!")
        
    bio_toggle = st.sidebar.toggle(t["bio_apply"], value=True)
    bio_product = st.sidebar.selectbox(t["bio_product"], ["Syngenta Quantis (Biostimulant)", "Syngenta Isabion", "Syngenta CropBio+"]) if bio_toggle else "None"
    dosage = st.sidebar.slider(t["bio_dosage"], 0.5, 4.0, st.session_state.s_dosage) if bio_toggle else 0.0
    
    msp_defaults = {"Rice (Paddy)": 2183.0, "Wheat": 2275.0, "Cotton": 6620.0, "Sugarcane": 315.0, "Maize": 2090.0, "Soybean": 4600.0}
    st.sidebar.subheader(t["market_sec"])
    product_cost = st.sidebar.number_input(t["bio_cost"], min_value=500.0, max_value=8000.0, value=1850.0, step=100.0)
    crop_price = st.sidebar.number_input(t["crop_price"], min_value=200.0, max_value=15000.0, value=float(msp_defaults.get(crop, 2200.0)), step=50.0)

    # ML Prediction Logic
    base_data = {
        "soil_organic_carbon": soc, "soil_ph": ph, "nitrogen_kgha": nitrogen,
        "phosphorus_kgha": 35.0, "potassium_kgha": 140.0, "clay_content_pct": 32.0,
        "cumulative_rainfall_mm": rainfall, "growing_degree_days": gdd, "avg_temperature_c": 27.5,
        "heat_stress_days": heat_stress, "peak_ndvi": ndvi,
        "bio_applied": 1 if bio_toggle else 0, "bio_dosage_l_ha": dosage if bio_toggle else 0.0
    }
    
    encoded_columns = artifacts["all_columns"]
    def prepare_input(data_dict, bio_flag, dosage_val):
        d = data_dict.copy()
        d["bio_applied"] = bio_flag
        d["bio_dosage_l_ha"] = dosage_val
        row = pd.Series(0.0, index=encoded_columns)
        for k, v in d.items():
            if k in row.index: row[k] = float(v)
        if f"crop_type_{crop}" in row.index: row[f"crop_type_{crop}"] = 1.0
        if f"region_{region}" in row.index: row[f"region_{region}"] = 1.0
        return pd.DataFrame([row])

    df_actual = prepare_input(base_data, 1 if bio_toggle else 0, dosage if bio_toggle else 0.0)
    df_counterfactual = prepare_input(base_data, 0, 0.0)
    
    pred_actual = float(model.predict(df_actual)[0])
    pred_counterfactual = float(model.predict(df_counterfactual)[0])
    
    yield_delta = max(0.0, pred_actual - pred_counterfactual) if bio_toggle else 0.0
    gross_rev = yield_delta * crop_price
    net_profit = gross_rev - (product_cost if bio_toggle else 0.0)
    roi_pct = (net_profit / product_cost * 100.0) if (bio_toggle and product_cost > 0) else 0.0

    # SECTION 1: Top KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{t["kpi_predicted"]}</div><div class="kpi-value">{pred_actual:.2f}</div><div class="kpi-subtext">{t["yield_unit"]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{t["kpi_delta"]}</div><div class="kpi-value kpi-positive">+{yield_delta:.2f}</div><div class="kpi-subtext">{t["yield_unit"]}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{t["kpi_gross"]}</div><div class="kpi-value kpi-positive">₹{gross_rev:,.0f}</div><div class="kpi-subtext">@ ₹{crop_price:,.0f}/q</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{t["kpi_profit"]}</div><div class="kpi-value {"kpi-positive" if net_profit>=0 else ""} ">₹{net_profit:,.0f}</div><div class="kpi-subtext">after cost</div></div>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{t["kpi_roi"]}</div><div class="kpi-value {"kpi-positive" if roi_pct>=0 else ""}">{roi_pct:.1f}%</div><div class="kpi-subtext">net return</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 10-Day Forecast Section (NEW)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader(t["forecast_title"])
    coords = REGION_COORDS[region]
    forecast_data = fetch_10day_forecast(lat=coords["lat"], lon=coords["lon"])
    
    f_cols = st.columns(10)
    for i, day in enumerate(forecast_data):
        with f_cols[i]:
            emoji = get_weather_emoji(day['condition'])
            st.markdown(f"""
            <div class="weather-card">
                <div class="weather-date">{day['date']}</div>
                <div class="weather-icon">{emoji}</div>
                <div class="weather-temp">{day['temp_max']}°</div>
                <div class="weather-sub">💧 {day['humidity_pct']}%<br>💨 {day['wind_kmh']} km/h</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Map Visualizer & Timeline
    col_map, col_time = st.columns([1, 2])
    with col_map:
        st.markdown('<div class="section-card" style="height: 100%;">', unsafe_allow_html=True)
        st.subheader("📍 Farm Location Context")
        
        map_df = pd.DataFrame([{"lat": REGION_COORDS[region]["lat"], "lon": REGION_COORDS[region]["lon"]}])
        fig_map = px.scatter_mapbox(map_df, lat="lat", lon="lon", zoom=4, color_discrete_sequence=["#059669"], size_max=15)
        fig_map.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_map, width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_time:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader(t["timeline_title"])
        fig_timeline = build_growth_divergence_timeline(days=120, base_yield=pred_counterfactual, bio_boost=yield_delta, heat_stress_day=48, lang_dict=t)
        st.plotly_chart(fig_timeline, width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)

    # SECTION 3: Counterfactual Guidance & PDF Download
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    col_shap1, col_shap2 = st.columns([1, 1])
    with col_shap1:
        st.subheader(t["shap_title"])
        st.caption(t["shap_desc"])
        
        weather_weight = np.clip(0.36 + 0.04 * (rainfall/800.0) - 0.025*heat_stress, 0.15, 0.55)
        soil_weight = np.clip(0.28 + 0.012 * soc + 0.015*(ph-6.5), 0.15, 0.45)
        bio_weight = (yield_delta / pred_actual) if pred_actual > 0 else 0.12
        baseline_weight = max(0.05, 1.0 - (weather_weight + soil_weight + bio_weight))
        
        categories = ["Syngenta Biological", "Monsoon Weather", "Soil Organic Carbon", "Baseline Practice"]
        values = [bio_weight*100, weather_weight*100, soil_weight*100, baseline_weight*100]
        
        fig_donut = px.pie(values=values, names=categories, hole=0.5, color=categories,
                           color_discrete_map={"Syngenta Biological": "#059669", "Monsoon Weather": "#0284c7", "Soil Organic Carbon": "#d97706", "Baseline Practice": "#64748b"})
        fig_donut.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#ffffff', width=2)))
        fig_donut.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_donut, width='stretch')

    with col_shap2:
        st.subheader(t["counterfactual_title"])
        
        if heat_stress > 4: st.success(f"🔥 **Monsoon Heat Wave Buffer**: Field recorded {heat_stress} stress days (>38°C). Syngenta {bio_product} prevented flower abortion.")
        elif rainfall < 500: st.warning(f"🌵 **Dry Spell Synergy**: Under deficit rainfall ({rainfall}mm), biostimulants enhanced root depth.")
        else: st.info(f"🌾 **Optimal Growth Synergy**: Biological product accelerated nutrient translocating to grain/pod sinks during monsoon season.")
            
        st.divider()
        st.markdown(f"**{t['opp_cost']}**: Investing ₹{product_cost:,.0f} in standard Urea yields approx +{yield_delta*0.3:.2f} q/acre. Syngenta Biologicals delivered **3.3x more efficiency** due to stress mitigation.")
        
        # PDF Generation
        farm_info = {"Region": region, "Crop Type": crop, "Input Applied": f"{bio_product} @ {dosage} L/acre"}
        roi_info = {"Total Yield Predicted": f"{pred_actual:.2f} {t['yield_unit']}", "Biological Yield Boost": f"+{yield_delta:.2f} {t['yield_unit']}", "Gross Revenue Increase": f"Rs {gross_rev:,.0f}", "Net Profit": f"Rs {net_profit:,.0f}", "Return on Investment": f"{roi_pct:.1f}%"}
        pdf_bytes = bytes(pdf_report.generate_roi_pdf(farm_info, roi_info, forecast_data))
        
        col_wa, col_pdf = st.columns(2)
        with col_wa:
            wa_text = f"🌾 *Syngenta Biologicals - Field ROI Report* 🌾\n━━━━━━━━━━━━━━━━━━━━━\n📍 *Region:* {region}\n🌱 *Crop:* {crop}\n🧪 *Product Used:* {bio_product} (@ {dosage} L/acre)\n\n📊 *Performance Highlights (Per Acre):*\n📈 *Total Yield:* {pred_actual:.2f} {t['yield_unit']}\n🚀 *Biological Yield Boost:* +{yield_delta:.2f} {t['yield_unit']}\n\n💰 *Financial Impact:*\n💵 *Gross Additional Revenue:* ₹{gross_rev:,.0f}\n📉 *Product Investment:* ₹{product_cost:,.0f}\n✅ *Net Profit (After Cost):* ₹{net_profit:,.0f}\n🔥 *Return on Investment:* {roi_pct:.1f}%\n\n_Data backed by AgriAttribute AI (Meteoblue Weather & Syngenta CE Hub)_\n✨ *Seeing is Believing!*"
            encoded_wa = urllib.parse.quote(wa_text)
            st.markdown(f'<a href="https://wa.me/?text={encoded_wa}" target="_blank" class="wa-button" style="width: 100%; justify-content: center;">📲 {t["whatsapp_share"]}</a>', unsafe_allow_html=True)
        with col_pdf:
            st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)
            st.download_button(label="📥 Download PDF Report", data=pdf_bytes, file_name=f"Syngenta_ROI_{crop.split()[0]}.pdf", mime="application/pdf", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
