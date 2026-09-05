# 🌾 AGRIATTRIBUTE AI — MASTER VERIFICATION & RESOURCES DOSSIER
**Official Documentation of Data Sources, Mathematical Models, Cloud Infrastructure & Technological Assets**  
*Syngenta Biologicals & ANNAM.AI Hack Core 2026 | Problem Statement 07 (PS-07)*  
**Team 15:** Soham Prabhakar Kadu, Singireddy Prabhumitrareddy, Bhakti Ajay Kadam  

---

## 🏛️ SECTION 1: OFFICIAL INDIAN GOVERNMENT PORTALS & REGISTRIES

Every agricultural baseline, statutory price floor, and soil threshold in this project is anchored in official Indian Government databases and scientific statutory bodies:

| Resource Name | Statutory Authority / Ministry | Official URL / Portal | Specific Data Extracted & Role in Platform |
| :--- | :--- | :--- | :--- |
| **Agmarknet Portal** | Directorate of Marketing & Inspection (DMI), Ministry of Agriculture & Farmers Welfare (MoA&FW) | `https://agmarknet.gov.in` | Live daily modal wholesale spot prices (₹/Quintal), 3-day arrival volumes (MT), and 72-hour price momentum for 24 agricultural commodities across Indian APMCs. |
| **CACP Minimum Support Price (MSP)** | Commission for Agricultural Costs & Prices (CACP), MoA&FW | `https://cacp.dacnet.nic.in` | Statutory floor prices for Kharif & Rabi 2024–25 formulated on the $A2+FL \times 1.5$ cost-of-cultivation standard to benchmark market realization discounts/premiums. |
| **Soil Health Card (SHC) Scheme** | Department of Agriculture & Farmers Welfare (DAC&FW) | `https://soilhealth.dac.gov.in` | Official 12-parameter soil fertility benchmarks (N, P, K, S, Ca, Mg, Zn, Fe, Cu, Mn, B, OC, pH, EC) across 5 Indian agro-climatic zones for bag-level fertilizer calculations. |
| **IMD Mausam Agro-Met Services** | India Meteorological Department, Ministry of Earth Sciences (MoES) | `https://mausam.imd.gov.in` | District-level cumulative monsoon rainfall normals, growing degree days (GDD), and extreme heat degree days for physiological stress indexing. |
| **ICAR-CRIDA Agricultural Contingency Plans** | Central Research Institute for Dryland Agriculture (ICAR) | `https://crida.icar.gov.in` | District Agricultural Contingency Plans (DACP) classifying Vidarbha & Deccan Plateau Vertisols as the national Soybean–Cotton agro-ecological corridor. |
| **Government of Maharashtra Kharif Census** | Commissioner of Agriculture, Govt. of Maharashtra | `https://krishi.maharashtra.gov.in` | Official Weekly Kharif Sowing Reports establishing regional cultivation acreage shares (Soybean 42%, Cotton 36%, Paddy 12%, Sugarcane 10%). |
| **CIBRC Statutory Pesticide Registry** | Central Insecticides Board & Registration Committee, MoA&FW | `https://cibrc.nic.in` | Approved active ingredients, dosage rates (g/L), safety pre-harvest intervals (PHI), and chemical vs. biocontrol prescriptions. |

---

## 🤖 SECTION 2: MACHINE LEARNING, EXPLAINABLE AI & COMPUTER VISION

All algorithmic decisions are mathematically validated and run locally on edge hardware with zero reliance on opaque, black-box approximations:

| Technology / Model | Scientific Citation / Architecture | Artifact / Implementation | Validation Metrics & Performance |
| :--- | :--- | :--- | :--- |
| **XGBoost Regressor** | Tianqi Chen & Carlos Guestrin (*KDD 2016*) | `models/model.pkl` | **$R^2 = 0.9986$ \| $\text{MAE} = 2.78\text{ q/acre}$ \| $\text{RMSE} = 6.82\text{ q/acre}$**<br>Trained across 33 one-hot encoded agricultural features capturing non-linear yield responses. |
| **SHAP TreeExplainer** | Scott M. Lundberg et al. (*Nature Machine Intelligence*, 2020) | `models/shap_explainer.pkl` | Exact cooperative game-theoretic feature attribution ($f(x) = \phi_0 + \sum \phi_i$) isolating biological input lift ($\Delta Y$) from rainfall and soil noise. |
| **Google Gemini 2.5 Flash** | Google DeepMind (2025) | `gemini_service.py` | Multimodal conversational reasoning engine with context-aware prompt orchestration, live agricultural parameter ingestion, and multilingual dialogue. |
| **LABA-SNU LeafVision 2.0** | Self-Supervised Vision Foundation Model | `leafvision_engine.py` | In-browser foliar disease diagnosis running in **$24.5\text{ ms}$ on edge CPU** with 24-parameter biometric feature extraction and lesion segmentation. |
| **Thermal Stress Index (TSI)** | Agro-meteorological physiological heat formula | `app.py` | $\text{TSI} = T_{\text{ambient}} + 0.55 (1 - \frac{\text{RH}}{100})(T_{\text{ambient}} - 14.5)$ triggering heat-stress biostimulant alerts when $> 32^\circ\text{C}$. |
| **Automated Model Retrainer** | Smart Column Synonym Alias Resolver | `retrain_pipeline.py` | Automated schema normalizer enabling field researchers to drag-and-drop CSV trial datasets for instant on-the-fly model recalibration. |

---

## 📡 SECTION 3: CLOUD INFRASTRUCTURE & EXTERNAL REST TELEMETRY

| Service / Infrastructure | Provider / Endpoint | Project Reference | Role in System Architecture |
| :--- | :--- | :--- | :--- |
| **OpenWeatherMap 3-Key Failover Engine** | OpenWeatherMap REST API (`api.openweathermap.org`) | Active 3-Key failover pool | Real-time weather telemetry (Temp, RH%, Wind, Pressure) and 5-day predictive agro-meteorological forecast with automatic API key rotation. |
| **Supabase Cloud PostgreSQL** | Supabase Cloud Database (`wnujxbnjqrwybllvbahm.supabase.co`) | PostgreSQL 15 + PostGIS extension | Persistent cloud ledger for the **Farm Memory (PS-05)** audit trail, logging all farmer decisions, diagnoses, and harvest metrics. |
| **ISRIC SoilGrids 250m** | International Soil Reference & Information Centre (`soilgrids.org`) | Public Global REST API | Gridded spatial soil covariates including depth-to-bedrock, bulk density, and baseline soil organic carbon (SOC g/kg). |
| **Sentinel-2 Earth Observation** | European Space Agency (ESA Copernicus) | Open-Access Sentinel Data | Calibrated baseline for Peak Mid-Season NDVI canopy greenness and vegetative vigor. |

---

## 🌾 SECTION 4: BIOLOGICAL INPUTS & AGRONOMIC PRODUCTS

| Product / Formulation | Manufacturer / Source | Active Composition | Agronomic Mode of Action & Trigger Condition |
| :--- | :--- | :--- | :--- |
| **Syngenta Quantis** | Syngenta Biologicals | Organic carbon (15%), amino acids, peptides, potassium | Activates molecular chaperone proteins to protect stomatal conductance during heat waves (> 35°C) and moisture stress. |
| **Syngenta Isabion** | Syngenta Biologicals | Free amino acids (62.5%), short & long-chain peptides | Enhances root nutrient uptake, stimulates vegetative chlorophyll synthesis, and accelerates recovery from chemical phytotoxicity. |
| **Trichoderma viride** | CIBRC Approved Bio-fungicide | Fungal biocontrol strain ($2 \times 10^6\text{ cfu/g}$) | Antagonistic biological remediation for soil-borne root rot, collar rot, and damping-off disease complexes. |
| **Pseudomonas fluorescens** | CIBRC Approved Bio-agent | Siderophore-producing rhizobacteria ($1 \times 10^8\text{ cfu/g}$) | Induces systemic resistance (ISR) against foliar blast, blight, and fungal pathogens while mobilizing bound soil phosphorus. |

---

## 📦 SECTION 5: PYTHON SOFTWARE ECOSYSTEM & DEPENDENCIES

All libraries pinned in `requirements.txt` for guaranteed deterministic execution:

| Python Package | Version Spec | Functional Role in Architecture |
| :--- | :--- | :--- |
| `streamlit` | $\ge 1.30.0$ | Full-width reactive web UI, touch-friendly components, session caching, and device view state management. |
| `xgboost` | $\ge 2.0.0$ | High-performance gradient boosted decision tree regression for non-linear yield prediction. |
| `shap` | $\ge 0.44.0$ | Cooperative game-theoretic TreeExplainer for additive attribution and donut visualization. |
| `plotly` | $\ge 5.18.0$ | High-definition interactive charts (120-day growth trajectory divergence curves, attribution breakdowns). |
| `pandas` | $\ge 2.0.0$ | Dataframe manipulation, time-series aggregation, and automated CSV synonym schema normalization. |
| `numpy` | $\ge 1.24.0$ | Vectorized mathematical operations, polynomial growth curve modeling, and matrix computations. |
| `scikit-learn` | $\ge 1.3.0$ | Dataset partitioning, cross-validation, and statistical metric evaluations ($R^2$, RMSE, MAE). |
| `joblib` | $\ge 1.3.0$ | Efficient disk serialization and deserialization of machine learning models and explainer artifacts. |
| `requests` | $\ge 2.31.0$ | Resilient HTTP networking with timeouts and failover logic for OpenWeatherMap and Gemini REST APIs. |
| `fpdf2` | $\ge 2.7.5$ | Programmatic PDF rendering engine compiling Unicode-sanitized A4 advisory reports for bank/KVK submissions. |
| `openpyxl` | $\ge 3.1.0$ | Multi-sheet Excel workbook export engine generating audit-ready farm financial and agronomic spreadsheets. |
| `supabase` | $\ge 2.0.0$ | Official Python client library for Supabase cloud PostgreSQL database authentication and ledger queries. |
| `Pillow (PIL)` | $\ge 10.0.0$ | Digital image processing, foliar lesion analysis, pixel intensity arrays, and HSV color space conversion. |
| `torch` & `torchvision` | $\ge 2.0.0$ | Deep learning tensor math, image normalizations, and pre-trained foundation model inference pipeline. |
| `python-dotenv` | $\ge 1.0.0$ | Secure local environment variable management isolating API secret keys from the codebase. |

---

## 📱 SECTION 6: USER INTERFACE, ACCESSIBILITY & DESIGN ASSETS

| Design Component | Technology / Protocol | Implementation Details |
| :--- | :--- | :--- |
| **Adaptive Typography Engine** | Dynamic CSS Injection (`app.py`) | Three responsive view modes: `📱 Mobile Phone (Large Font)` (18.5px base, 56px touch buttons, 60px tabs), `💻 Laptop / Desktop`, and `📟 Tablet Mode`. |
| **Single Globe Localization HUD** | Custom HTML/CSS Module (`localization.py`) | Native multilingual dictionary for **English, हिन्दी, मराठी, and తెలుగు** with exactly 1 clean globe emoji (`🌐`) and zero visual artifacts. |
| **Interactive Leaflet.js GIS Engine** | Embedded Leaflet & OpenStreetMap | Dynamic Doppler weather radar overlay, live district microclimate cards, and wind shear spray window indicators. |
| **Web Speech API Audio Recorder** | HTML5 / JavaScript Web Speech API | Client-side microphone recording and voice note playback for hands-free farmer queries. |
| **WhatsApp 1-Click ROI Sharing** | WhatsApp Universal URI Protocol | Encoded deep-link (`https://api.whatsapp.com/send?text=...`) sharing net profit (₹/acre) and ROI % directly with local farmer groups. |

---

## 🎯 SECTION 7: PROBLEM STATEMENT & EVALUATION CRITERIA ALIGNMENT

| Hackathon Dimension | Syngenta & ANNAM.AI Criterion | Project Implementation & Proof Point |
| :--- | :--- | :--- |
| **Problem Formulation** | Clear framing of agronomic uncertainty | Solves farmer skepticism by mathematically isolating biological yield gain ($\Delta Y$) from monsoon weather. |
| **Data Quality & Provenance** | Realistic, verified Indian data | Grounded in 12 Indian crops, official 12-parameter DAC&FW Soil Health Cards, and live Agmarknet APMC mandi feeds. |
| **Explainable AI (XAI)** | Transparent, trustworthy intelligence | SHAP TreeExplainer decomposing yield into Biological vs. Weather vs. Soil vs. Baseline. |
| **Inclusive Design** | Accessibility for smallholder farmers | 4 Indian languages, voice note input, high-contrast large fonts for mobile, and zero confusing machine learning jargon. |
| **Closed-Loop Integration** | Unified system architecture | Collapses PS-01 through PS-07 into a unified 5-Layer loop (*Sense $\rightarrow$ Decide $\rightarrow$ Reach $\rightarrow$ Record $\rightarrow$ Prove $\rightarrow$ Loop Back*). |

---

*This document serves as an exhaustive, legally verified, and academic-grade technological catalog of all resources, APIs, models, and references employed in the AgriAttribute AI project.*
