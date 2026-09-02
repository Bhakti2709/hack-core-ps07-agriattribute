# 🌾 Step-by-Step Guide: Retraining AgriAttribute AI on Real Syngenta Field Trial Data
**Syngenta Biologicals & ANNAM.AI Hack Core 2026 — Team 15**

---

## 💡 Overview: Is Retraining on Real Data a Standalone Process?

**NO — Retraining on real Syngenta field trial data is NOT a complicated or standalone manual process.**  
We have built an **Automated Data Ingestion & Model Retraining Engine (`retrain_pipeline.py`)** that automatically reads, normalizes column headers, fits the XGBoost Regressor, recalibrates SHAP TreeExplainer values, and updates serialized artifacts (`model.pkl` and `shap_explainer.pkl`).

---

## 🔄 The 4-Step Ingestion & Retraining Lifecycle

```text
[ 1. CSV Data Input ] ──> [ 2. Schema Normalization ] ──> [ 3. XGBoost Fit ] ──> [ 4. SHAP Recalibration ]
 (Upload UI or CLI)      (Matches header synonyms)     (Learns real yield y)     (Saves new model.pkl)
```

---

## 📊 1. Expected CSV File Format (Column Headers)

`retrain_pipeline.py` includes a **Smart Synonym Alias Resolver**. Even if Syngenta's raw field data uses different header names (e.g. `yield` instead of `yield_q_per_acre` or `soc` instead of `soil_organic_carbon`), the engine automatically maps them.

| Required Data Dimension | Standard ML Feature Name | Supported CSV Column Synonyms (Auto-Mapped) |
|---|---|---|
| **Harvest Yield (Target)** | `yield_q_per_acre` | `yield`, `yield_q_acre`, `yield_q_ha`, `yield_t_ha` |
| **Soil Organic Carbon** | `soil_organic_carbon` | `soc`, `organic_carbon`, `soc_g_kg` |
| **Soil pH** | `soil_ph` | `ph`, `soil_ph_level` |
| **Soil Nitrogen** | `nitrogen_kgha` | `nitrogen`, `n_kgha`, `n` |
| **Soil Phosphorus** | `phosphorus_kgha` | `phosphorus`, `p_kgha`, `p` |
| **Soil Potassium** | `potassium_kgha` | `potassium`, `k_kgha`, `k` |
| **Monsoon Rainfall** | `cumulative_rainfall_mm` | `rainfall`, `rain_mm`, `cum_rain` |
| **Growing Degree Days** | `growing_degree_days` | `gdd`, `degree_days` |
| **Heat Stress Days** | `heat_stress_days` | `heat_days`, `days_over_38c` |
| **Peak Satellite NDVI** | `peak_ndvi` | `ndvi`, `sentinel_ndvi` |
| **Biological Applied?** | `bio_applied` | `is_bio`, `bio_flag`, `treated` (0 or 1) |
| **Biological Dosage** | `bio_dosage_l_ha` | `dosage`, `bio_dosage`, `dosage_l_acre` |
| **Crop Type** | `crop_type` | `crop`, `crop_name` |
| **Agro-Climatic Region** | `region` | `state`, `zone`, `location` |

---

## 🛠️ 2. How to Retrain (2 Easy Options)

### Option A: Direct Web UI Drag-and-Drop (Easiest)
1. Open the live dashboard at [http://localhost:8505](http://localhost:8505).
2. On the left sidebar, switch **Platform Experience Mode** to `⚙️ Agronomist (Advanced)`.
3. Scroll to **"📤 Retrain Model on Real Data"**.
4. Drag and drop your Syngenta field trial CSV file (`syngenta_trials_2024.csv`).
5. The system will automatically retrain the XGBoost regressor, update SHAP explanations, and notify you of the new $R^2$ accuracy score and sample count!

### Option B: Command Line (CLI)
Place your CSV file in the `data/` folder and run:
```bash
python retrain_pipeline.py
```

---

## 🧪 3. What Happens Under the Hood During Retraining?

1. **Schema Check:** Fills any missing optional columns with domain defaults (e.g. default SOC = 7.5 g/kg).
2. **Categorical One-Hot Encoding:** Encodes regions and crop types (e.g. Paddy, Wheat, Cotton).
3. **Non-Linear XGBoost Training:** Fits `XGBRegressor` on 80-90% training split to capture stress-buffering interaction effects.
4. **SHAP TreeExplainer Compilation:** Computes exact SHAP values for game-theoretic feature decomposition.
5. **Artifact Serialization:** Overwrites `model.pkl` and `shap_explainer.pkl` so the Streamlit UI immediately renders predictions from your new real-world model.
