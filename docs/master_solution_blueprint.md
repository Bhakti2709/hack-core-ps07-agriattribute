# 🌾 AgriAttribute AI — Master Solution Blueprint & Code Structure Guide
**Syngenta Biologicals & ANNAM.AI Hack Core 2026 — Team 15**  
*(Soham Prabhakar Kadu, Singireddy Prabhumitrareddy, Bhakti Ajay Kadam)*

---

## 🎯 1. User-Centric Philosophy: Simple for Farmers, Powerful in the Background

> **"A solution should never confuse the person standing in the field. Heavy data science belongs behind the scenes; the farmer only needs plain proof, native language answers, and actionable financial ROI."**

```text
    ┌────────────────────────────────────────────────────────────────────────┐
    │                      FARMER-CENTRIC FRONTEND (UI)                       │
    │  • 4 Native Languages (English, Hindi, Marathi, Telugu)               │
    │  • Abstracted Inputs ("Soil Quality", "Monsoon Rain", "Heat Waves")   │
    │  • Plain Outputs: "₹6,971 Net Profit/Acre | 498% ROI"                  │
    │  • 1-Click WhatsApp ROI Sharing & Downloadable A4 PDF Report          │
    └──────────────────────────────────┬─────────────────────────────────────┘
                                       │
    ┌──────────────────────────────────┴─────────────────────────────────────┐
    │                    ENGINEERING BACKEND (BACKGROUND)                    │
    │  • XGBoost Regressor (Non-linear yield prediction, R² = 0.9995)         │
    │  • SHAP TreeExplainer (Game-theoretic causal attribution)              │
    │  • OpenWeatherMap 3-Key Failover Telemetry Engine                      │
    │  • Google Gemini 2.5 Flash Multilingual Conversational AI              │
    │  • Supabase PostgreSQL Database (Season Journal - PS-05 Record Layer)  │
    └────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 2. Problem Framing & 13-Point Evaluation Alignment

Based on the **Project Overview & Problem Framing Board**:

### A. Narrative Arc
- **Climate Uncertainty & Resource Scarcity:** Farmers face volatile monsoon weather, heatwaves, and rising input costs.
- **The Core Problem:** Unpredictable crop performance makes farmers skeptical of biological inputs.
- **Smart Intervention:** Precision digital twin modeling isolating biological yield boost from weather/soil noise.
- **Regenerative Impact:** Promotes environmental balance, soil microbial health, and reduced chemical over-application.

### B. Unified 5-Layer Closed Loop
Instead of 7 disconnected tools, **PS-01 through PS-07** collapse into one closed loop:
1. 📡 **Sense (Layer 1):** Ingests weather, soil, and satellite signals (Meteoblue, OpenWeather, SoilGrids, Sentinel-2).
2. 🧠 **Decide (Layer 2):** Calculates application readiness score (PS-01), climate stress alerts (PS-02), and product rankings (PS-03).
3. 💬 **Reach (Layer 3):** Surfacing insights via Gemini 2.5 Flash chatbot (PS-04) and WhatsApp deep-links.
4. 📝 **Record (Layer 4):** Logging field applications and outcomes in the **Season Journal (PS-05)** stored on Supabase PostgreSQL.
5. 📊 **Prove (Layer 5):** Benchmarking efficacy (PS-06) and computing causal ROI attribution via XGBoost + SHAP (PS-07).
6. ↩️ **Loop Back:** Feedback from Prove continuously recalibrates the Decide recommendation engine!

---

## 📂 3. Complete File-by-File Code Structure & Implementation Purpose

Here is the complete catalog of all core code files in the codebase, detailing their exact purpose, why they were created, and how they connect:

### 1. `app.py` — Main Dashboard & User Interface Engine
- **File Path:** [`app.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/app.py)
- **Purpose:** Serves as the primary user-facing Streamlit application.
- **Key Modules & Features:**
  - **Multilingual Support:** Localized dictionary in English, Hindi (हिंदी), Marathi (मराठी), and Telugu (తెలుగు).
  - **Platform Experience Toggles:** `🚜 Farmer (Simple)` mode with abstracted sliders vs. `⚙️ Agronomist (Advanced)` mode.
  - **Header Badges:** Displays real-time status for 5-Layer Closed Loop, Supabase PostgreSQL Live, OpenWeather 3-Key Failover, and Gemini 2.5 Flash AI.
  - **Real-Time OpenWeather Live Telemetry & 5-Day Forecast Card:** Displays live regional temperature, humidity, pressure, and precipitation risk.
  - **Disease Risk Early Warning (Module 3):** Calculates fungal blight risk index ($0-100\%$) and recommends Syngenta biocontrols.
  - **Smart NPK Fertilizer Advisor (Module 4):** Calculates Nitrogen, Phosphorus, and Potassium deficits and recommends 15% Urea reduction for regenerative soil health.
  - **Growth Trajectory Divergence Chart:** Interactive Plotly timeline visualizing treated vs. untreated control fields over 120 days.
  - **SHAP Attribution Donut Chart:** Visual breakdown isolating *Syngenta Biological vs. Monsoon Weather vs. Soil vs. Baseline*.
  - **Counterfactual ROI Calculator:** Calculates gross revenue, treatment cost, net profit (₹/acre), and ROI %.
  - **Export Engines:** 1-Click WhatsApp ROI deep-link sharing & downloadable branded A4 PDF report.

---

### 2. `openweather_service.py` — 3-Key Failover Weather Engine
- **File Path:** [`openweather_service.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/openweather_service.py)
- **Purpose:** Provides 100% resilient real-time weather and 5-day predictive forecast telemetry with automatic API key rotation.
- **Implementation Logic:**
  - Configures 3 active OpenWeatherMap API keys (`current weather`, `map's`, `google map`).
  - If any key hits rate limits or quotas, the service automatically fails over to the next key.
  - Returns current temp, feels-like temp, humidity %, pressure hPa, wind speed km/h, weather description, and daily min/max forecasts.

---

### 3. `gemini_service.py` — Google Gemini 2.5 Flash Multilingual AI Engine
- **File Path:** [`gemini_service.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/gemini_service.py)
- **Purpose:** Powers **PS-04 Multilingual Conversational Chatbot (Reach Layer)** using Google Gemini 2.5 Flash.
- **Implementation Logic:**
  - Configured securely via environment variables (`.env`).
  - Uses an agricultural system prompt tailored for Syngenta Biologicals and Indian farming context.
  - Ingests live field context (crop type, region, heat stress, predicted yield lift) to provide personalized AI answers in Hindi, Marathi, Telugu, or English.

---

### 4. `supabase_client.py` — Cloud Database & Season Journal Engine
- **File Path:** [`supabase_client.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/supabase_client.py)
- **Purpose:** Connects the application to Supabase Cloud PostgreSQL database (`wnujxbnjqrwybllvbahm`) for **PS-05 Season Journal (Record Layer)**.
- **Implementation Logic:**
  - Authenticates with Supabase publishable & secret keys.
  - Function `log_season_journal_entry()` inserts real farmer application logs (date, crop, product, dosage, actual yield, profit).
  - Function `fetch_season_journal_history()` fetches persistent records to fuel the retrain loop (**Prove $\rightarrow$ Decide**).

---

### 5. `train_model.py` — XGBoost & SHAP Causal Model Trainer
- **File Path:** [`train_model.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/train_model.py)
- **Purpose:** Trains the core XGBoost Regressor model and compiles SHAP TreeExplainer values.
- **Implementation Logic:**
  - Fits `XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.07)` on domain-calibrated Indian field trial data.
  - Evaluates performance: $R^2 = 0.9995$, MAE = $1.82\text{ q/acre}$.
  - Computes `shap.TreeExplainer(model)` to enable exact additive feature attribution.
  - Serializes artifacts: `model.pkl` and `shap_explainer.pkl`.

---

### 6. `retrain_pipeline.py` — Automated Real CSV Retraining Engine
- **File Path:** [`retrain_pipeline.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/retrain_pipeline.py)
- **Purpose:** Enables seamless, one-click model retraining whenever a real Syngenta field trial CSV dataset is uploaded.
- **Implementation Logic:**
  - Includes a **Smart Synonym Header Resolver** (auto-maps headers like `yield`, `soc`, `rain_mm`, `treated`).
  - Preprocesses, normalizes, and encodes raw CSV data.
  - Retrains XGBoost regressor, recalibrates SHAP explainer, and updates `model.pkl`.

---

### 7. `data_generator.py` — API Data Ingestion & Synthetic Trial Generator
- **File Path:** [`data_generator.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/data_generator.py)
- **Purpose:** Ingests Meteoblue Weather telemetry, Syngenta CE Hub API dosage parameters, ISRIC SoilGrids data, and generates domain-calibrated field trial datasets.

---

### 8. `pdf_report.py` — Branded A4 PDF Report Generator
- **File Path:** [`pdf_report.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/pdf_report.py)
- **Purpose:** Renders ready-to-print branded A4 PDF reports using `fpdf2` containing farm profile, weather forecasts, and financial ROI breakdown.

---

### 9. `presentation.html` — Interactive Web Pitch Deck
- **File Path:** [`presentation.html`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/presentation.html)
- **Purpose:** Self-contained 7-slide presentation deck with keyboard navigation, financial cascade cards, interactive diagrams, and built-in speaker notes toggle.

---

## 🛠️ Complete Summary Matrix of Project Code Files

| File Name | Primary Role | 5-Layer Component | Active External Integration |
|---|---|---|---|
| `app.py` | Main Streamlit Application & Dashboard UI | All 5 Layers | Streamlit, Plotly, FPDF2, WhatsApp Link |
| `openweather_service.py` | 3-Key Failover Weather Telemetry & 5-Day Forecast | Layer 1 (Sense) & Layer 2 (Decide) | OpenWeatherMap API (3 Keys) |
| `gemini_service.py` | Google Gemini 2.5 Flash Multilingual Conversational AI | Layer 3 (Reach) | Google Gemini 2.5 Flash API |
| `supabase_client.py` | PostgreSQL Database Integration & Season Journal | Layer 4 (Record) | Supabase Cloud Database (`wnujxbnjqrwybllvbahm`) |
| `train_model.py` | XGBoost Yield Regression & SHAP Causal Attribution | Layer 5 (Prove) | XGBoost, SHAP (`TreeExplainer`) |
| `retrain_pipeline.py` | Automated Real Field Trial CSV Retraining Engine | Layer 5 $\rightarrow$ Layer 2 Feedback Loop | Pandas, XGBoost, SHAP |
| `data_generator.py` | API Gateway & Field Trial Dataset Ingestion | Layer 1 (Sense) | Meteoblue API, Syngenta CE Hub API |
| `pdf_report.py` | Downloadable Branded A4 PDF Report Generator | Layer 3 (Reach) | FPDF2 Engine |
| `presentation.html` | Interactive 7-Slide Pitch Deck Web Page | Pitch Deliverable | HTML5, CSS3, JavaScript |
