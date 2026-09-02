# 🌾 AgriAttribute AI — Master List of Resources & Assets
**Syngenta Biologicals & ANNAM.AI Hack Core 2026 — Team 15**  
*(Soham Prabhakar Kadu, Singireddy Prabhumitrareddy, Bhakti Ajay Kadam)*

---

## 🌐 1. External APIs & Telemetry Services

| Service Name | API Endpoint | Credentials / Keys Used | Purpose & Role |
|---|---|---|---|
| **Google Gemini API** | `https://generativelanguage.googleapis.com/v1beta/` | `Configured via .env` | **PS-04 Multilingual Conversational AI:** Powers Gemini 2.5 Flash for native conversational Q&A in 10 Indian languages. |
| **Meteoblue Weather API** | `https://www.meteoblue.com/en/weather-api/dataset-api/` | `Configured via .env` | Live 10-day agronomic weather forecasts, GDD, cumulative rainfall, & heat stress telemetry. |
| **OpenWeatherMap API** | `https://api.openweathermap.org/data/2.5/` | `Configured via .env (3-Key Failover)` | Real-time weather telemetry (Temp, Humidity, Pressure, Wind) & 5-day predictive forecast with **3-key failover**. |
| **Syngenta CE Hub API** | `https://services.cehub.syngenta-ais.com/swagger/` | `Configured via .env` | Biological product recommendations, optimal application dosage (L/acre), and target crop parameters. |
| **ISRIC SoilGrids Database** | `https://soilgrids.org` (REST API) | Public REST API (No Key Required) | Baseline Soil Organic Carbon (SOC g/kg), soil pH, clay content %, and N-P-K profiles across 5 Indian zones. |
| **Sentinel-2 Remote Sensing** | Sentinel-2 Earth Observation Data | Open Access Data | Peak Satellite NDVI Index for mid-season crop canopy greenness and vigor telemetry. |

---

## ⚡ 2. Cloud Infrastructure & Databases

| Service Name | Project / URL | Access Credentials | Purpose & Role |
|---|---|---|---|
| **Supabase Cloud Database** | **Project:** `wnujxbnjqrwybllvbahm`<br>**URL:** `https://wnujxbnjqrwybllvbahm.supabase.co` | `Configured via .env` | **PostgreSQL + PostGIS Database:** Persists Season Journal entries (PS-05), field profiles, and retrain loop history. |

---

## 🤖 3. Machine Learning & Explainable AI Stack

| Technology / Library | Artifact File | Specs / Accuracy | Purpose & Role |
|---|---|---|---|
| **XGBoost Regressor** (`xgboost`) | `model.pkl` | $R^2 = 0.9995$, MAE = $1.82\text{ q/acre}$ | Non-linear yield prediction capturing environmental stress buffering by Syngenta Biologicals. |
| **SHAP TreeExplainer** (`shap`) | `shap_explainer.pkl` | Game-Theoretic Decomposition | Mathematically isolates biological yield contribution ($\Delta Y$) from monsoon weather & soil noise. |

---

## 📂 4. Source Code Modules & Repository Structure

- **GitHub Repository:** [`soham0777/hack-core-ps07-agriattribute`](https://github.com/soham0777/hack-core-ps07-agriattribute)
- **Local Path:** [`C:\Users\kadus\.gemini\antigravity\scratch\hack-core-ps07-agriattribute`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute)

| File Name | Purpose & Implementation |
|---|---|
| [`app.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/app.py) | **Main Streamlit Dashboard:** Multilingual UI (EN, HI, MR, TE), 5-Layer closed loop banner, OpenWeather telemetry, Disease Risk warning, NPK advisor, PDF export & WhatsApp sharing. |
| [`openweather_service.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/openweather_service.py) | **OpenWeather Engine:** Automatic 3-key failover rotation pulling live current weather and 5-day predictive forecasts. |
| [`supabase_client.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/supabase_client.py) | **Supabase Engine:** Connects to PostgreSQL `wnujxbnjqrwybllvbahm` database for Season Journal logging & history. |
| [`data_generator.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/data_generator.py) | **Data Pipeline:** Integrates Meteoblue, CE Hub, SoilGrids, and domain-calibrated Indian field trial dataset. |
| [`train_model.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/train_model.py) | **ML Training Pipeline:** Trains XGBoost regressor & compiles SHAP TreeExplainer. |
| [`pdf_report.py`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/pdf_report.py) | **PDF Engine:** Generates downloadable A4 ROI reports using FPDF2. |
| [`requirements.txt`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/requirements.txt) | **Dependencies:** `streamlit`, `xgboost`, `shap`, `plotly`, `pandas`, `numpy`, `scikit-learn`, `joblib`, `requests`, `fpdf2`, `supabase`. |

---

## 📄 5. Strategic Documentation & Presentation Deliverables

| Artifact File | Description & Link |
|---|---|
| **Interactive HTML Pitch Deck** | [`presentation.html`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/presentation.html) — 7-slide pitch deck with keyboard navigation & speaker notes. |
| **Master Pitch Deck Guide** | [`presentation_guide.md`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/presentation_guide.md) — Slide-by-slide pitch scripts & judge Q&A defense guide. |
| **Unified Closed-Loop Concept Note** | [`concept_note.md`](file:///C:/Users/kadus/.gemini/antigravity/scratch/hack-core-ps07-agriattribute/concept_note.md) — Reframe of PS-01 through PS-07 into a 5-layer loop (*Sense, Decide, Reach, Record, Prove*). |
| **Master Technical Requirements** | [`unified_platform_requirements.md`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/unified_platform_requirements.md) — SQL schemas, API specs, & scoring math. |
| **13-Point Product Strategy** | [`product_strategy_13points.md`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/product_strategy_13points.md) — Alignment with handwritten evaluation points. |
| **Smart Precision Suite Guide** | [`smart_precision_suite_guide.md`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/smart_precision_suite_guide.md) — Disease risk scoring & NPK balancing algorithms. |
| **Master Implementation Plan** | [`implementation_plan.md`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/implementation_plan.md) — Architecture rollout plan. |
| **Live Dashboard Preview Widget** | [`platform_preview.html`](file:///C:/Users/kadus/.gemini/antigravity/brain/bbcb53e3-f5f4-42cc-9427-df81a6290ab6/platform_preview.html) — Inline chat preview widget. |
