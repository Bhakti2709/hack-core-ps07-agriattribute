# 🌾 AgriAttribute AI — Farmer Decision Platform UX Guide
**Human-Centric Agricultural Design & Experience Architecture**  
*Syngenta Biologicals & ANNAM.AI Hack Core 2026 — Team 15*

---

## 🎯 1. Product North Star & Core Promise

> **"Before you act, know why.  
> After you act, know whether it worked."**

```text
    FARMER MENTAL MODEL:
    OBSERVE ──> UNDERSTAND ──> DECIDE ──> ACT ──> MEASURE ──> LEARN

    SYSTEM ARCHITECTURE:
    SENSE   ──> DECIDE     ──> REACH  ──> RECORD ──> PROVE   ──> LOOP BACK
```

---

## 💡 2. The 8 Core Farmer Questions Answered

1. **What is happening in my field?** $\rightarrow$ *Live weather telemetry from OpenWeatherMap & satellite NDVI canopy greenness.*
2. **What should I do now?** $\rightarrow$ *Clear, unambiguous decision recommendation (e.g., "APPLY QUANTIS TODAY" or "WAIT 1 DAY").*
3. **Why should I do it?** $\rightarrow$ *Plain-language explanation without statistical or ML jargon.*
4. **What happens if I do nothing?** $\rightarrow$ *Counterfactual comparison: Expected yield & revenue WITHOUT intervention vs. WITH intervention.*
5. **What result can I reasonably expect?** $\rightarrow$ *Estimated yield range (e.g. 25.5 – 28.0 q/acre) with realistic confidence levels.*
6. **Did the intervention actually work?** $\rightarrow$ *Causal attribution isolating biological lift ($\Delta Y$) from monsoon weather.*
7. **Did it make financial sense?** $\rightarrow$ *Net Profit per acre (₹) and proven Return on Investment (ROI %).*
8. **What should I do next time?** $\rightarrow$ *Farm Memory (Season Journal) historical insights stored on Supabase PostgreSQL.*

---

## 🌾 3. Mapping PS-01 through PS-07 into 1 Unified Journey

| Capability | Human-Centric Translation | User Journey Stage |
|---|---|---|
| **PS-01 Application Timing** | *"Is now the right time?"* | DECIDE |
| **PS-02 Climate Stress Alert** | *"What could hurt my crop?"* | OBSERVE |
| **PS-03 Product Advisor** | *"Which option fits my field?"* | DECIDE |
| **PS-04 Multilingual AI Chatbot** | *"Explain this to me simply."* | UNDERSTAND |
| **PS-05 Season Journal** | *"Remember what I did."* | RECORD & LEARN |
| **PS-06 Efficacy Benchmark** | *"Did it actually work?"* | MEASURE |
| **PS-07 Yield Attribution & ROI** | *"Did it create measurable value?"* | PROVE |

---

## 🎛 4. Dual Experience Levels (`FARMER MODE` vs `AGRONOMIST MODE`)

### 🚜 Farmer Mode (Action-Oriented & Empathetic)
- **Visuals:** High-contrast cards, large actionable buttons, regional language support (English, Hindi, Marathi, Telugu).
- **Language:** Plain English & native Devanagari/Telugu terminology.
- **Metrics:** Net Profit (₹/acre), Yield Boost (+q/acre), Plain "Why?" bullet points.
- **Complexity:** Zero ML terminology exposed. No "XGBoost", "SHAP", or "hyperparameters".

### ⚙️ Agronomist / Expert Mode (Analytical & Model-Backed)
- **Visuals:** Technical SHAP donut charts, Plotly trajectory curves, SoilGrids NPK sliders.
- **Metrics:** XGBoost $R^2 = 0.9995$, MAE = $1.82\text{ q/acre}$, SHAP feature weights.
- **Data Engineering:** Real Syngenta Field Trial CSV Upload & Automated Retraining Engine.

---

## 🛡️ 5. Technical Preservation Guarantee

The updated user interface strictly preserves and reuses 100% of the underlying codebase:
- `openweather_service.py`: OpenWeatherMap 3-key failover rotation engine.
- `gemini_service.py`: Google Gemini 2.5 Flash API engine (`AQ.Ab8RN6I6...`).
- `supabase_client.py`: Supabase Cloud PostgreSQL client (`wnujxbnjqrwybllvbahm`).
- `train_model.py`: XGBoost regressor & SHAP `TreeExplainer` (`model.pkl`, `shap_explainer.pkl`).
- `retrain_pipeline.py`: Real CSV retraining engine with column synonym resolver.
- `pdf_report.py`: FPDF2 A4 PDF report generator.
- `data_generator.py`: Weather, soil, and CE Hub API data generator.
