"""
localization.py - Centralized Full Platform Translation & Internationalization System
AgriAttribute AI — Syngenta Biologicals & ANNAM.AI Hack Core 2026 (Team 15)

Supports:
- English (en)
- Hindi / हिंदी (hi)
- Marathi / मराठी (mr)
- Telugu / తెలుగు (te)

Features:
- Global t(key, lang, **kwargs) lookup with safe fallback to English
- Dedicated translators for crops, regions, seasons, weather, and soil options
- Comprehensive coverage of 100% of visible UI strings, charts, tabs, hero cards, and alerts
"""

# Language key mapping
LANG_MAP = {
    "English": "en",
    "Hindi (हिंदी)": "hi",
    "Marathi (मराठी)": "mr",
    "Telugu (తెలుగు)": "te",
    "en": "en",
    "hi": "hi",
    "mr": "mr",
    "te": "te"
}

TRANSLATIONS = {
    "en": {
        "agmark_expander_title": "🏛️ Explore All Indian Commodity Groups (Official Agmarknet 2.0 Marketplace)",
        "agmark_caption": "Live APMC Mandi modal prices, official Govt MSP 2026-27, and daily arrival volumes across all 6 national commodity classifications (agmarknet.gov.in/home):",
        "agmark_tab_cereals": "🌾 Cereals (7)",
        "agmark_tab_oilseeds": "🌻 Oil Seeds (7)",
        "agmark_tab_pulses": "🥣 Pulses (5)",
        "agmark_tab_fibre": "🧵 Fibre Crops (1)",
        "agmark_tab_veg": "🥦 Vegetables & Sugar (4)",
        "agmark_card_msp": "Govt MSP:",
        "agmark_card_perishable": "Perishable",
        "agmark_card_vs_msp": "vs MSP",
        "agmark_card_arrival": "Arrival:",
        "agmark_card_72h": "72h:",
        # App Header & Meta
        
        "radar_map_title": "🛰️ Interactive Weather Radar & Field Satellite Map",
        "proof_sources_expander": "🏛️ Verified Government Citations, CACP MSP Formulas & ICAR Sources",
        "share_weather_wa_btn": "📲 Share Weather & Spray Window via WhatsApp",
        "kcc_cert_btn": "📄 Download Official KCC Bank Certificate (PDF)",
        "soil_card_title": "🏛️ Official 12-Parameter Indian Soil Health Card",
        "soil_card_subtitle": "Calibrated with Ministry of Agriculture standards (soilhealth.dac.gov.in)",
        "crop_detection_conf": "Crop Detection Confidence",
        "detected_crop": "Detected Plant Species",
        "lesion_surface_area_pct": "Lesion Surface Area (%)",
        "severity_level": "Infection Severity Stage",
        "optimal_dosage_l_ha": "Optimal Dosage Rate (L/ha)",
        "product_applied": "Biological Product Applied",
        "yield_actual_q_acre": "Observed Harvest Yield (q/acre)",
        "farmer_notes": "Field Observations & Notes",
        "dosage_l_acre": "Dosage (L/acre)",
        "net_profit_rs": "Net Profit Benefit (₹)",
        "crop_type": "Crop Type",
        "region": "Agro-Climatic Belt",
        "status": "System Status",
        "temp_c": "Temperature (°C)",
        "rain_prob": "Precipitation Probability (%)",
        "all_columns": "Model Feature Space",
        "created_at": "Logged At",
        "description": "Weather Sky Condition",
        "mae": "Mean Absolute Error (MAE)",
        "rmse": "Root Mean Squared Error (RMSE)",
        "r2": "Coefficient of Determination (R²)",
        "metrics": "Model Diagnostics",
        "message": "Agronomic Message",
        "response": "Gemini Expert Recommendation",

        "title": "🌾 AgriAttribute AI: Farmer Decision Platform",
        "subtitle": "“Before you act, know why. After you act, know whether it worked.”",
        "badge_hack": "HACK CORE 2026 - PS07",
        "badge_team": "Team 15: Soham P. Kadu | Singireddy P. | Bhakti A. Kadam",
        "badge_loop": "📐 Unified Closed Loop",
        "badge_db": "⚡ Supabase PostgreSQL Live",
        "badge_ai": "🤖 Gemini 2.5 Flash AI Active",

        # Location Intelligence
        "loc_title": "Agro-Climatic Farm Location",
        "loc_detect_btn": "🛰️ Detect GPS Location",
        "loc_verified": "✅ Farm GPS Verified: {region}",
        "loc_change_belt": "Change Agro-Climatic Belt:",
        "belt_punjab": "Punjab & Haryana",
        "belt_vidarbha": "Maharashtra & Vidarbha",
        "belt_andhra": "Andhra & Telangana",
        "belt_up": "Uttar Pradesh & Bihar",
        "belt_karnataka": "Karnataka & Tamil Nadu",

        # Regional Crops Section
        "crop_sec_heading": "🌱 What is Commonly Cultivated in {region}?",
        "crop_sec_caption": "Visual agricultural intelligence based on regional ICAR acreage surveys. Tap a crop card to explore your field:",
        "acreage_share": "{share}% Regional Acreage",
        "active_field_badge": "ACTIVE FIELD",
        "select_crop_btn": "Select {crop}",
        "map_expander": "🗺️ Explore National Crop Concentration Map for {crop}",
        "map_caption": "Visualizing national cultivation density for {crop}. Larger and deeper emerald circles indicate higher regional cultivation share.",
        "map_title": "National Cultivation Concentration: {crop}",
        "map_hover_concentration": "Concentration of {crop}:",
        "map_hover_top": "Top Cultivated:",

        # Sidebar
        "sidebar_lang_title": "Select Language / भाषा चुनें",
        "sidebar_mode_title": "Experience Mode",
        "mode_farmer": "🚜 Farmer Mode (Action-Oriented)",
        "mode_agronomist": "⚙️ Agronomist Mode (Expert Analytics)",
        "sidebar_active_field": "Active Field:",
        "sidebar_location": "Location:",
        "sidebar_farm_health": "🌱 Farm Health & Weather",
        "soil_quality": "Soil Quality",
        "opt_poor": "Poor",
        "opt_average": "Average",
        "opt_excellent": "Excellent",
        "monsoon_rain": "Monsoon Rain",
        "opt_deficient": "Deficient",
        "opt_normal": "Normal",
        "opt_excess": "Excess",
        "summer_heat": "Summer Heat",
        "opt_very_hot": "Very Hot",

        # Agronomist Sliders
        "soil_sec": "🌱 Soil Health Profile (ISRIC SoilGrids)",
        "soc": "Soil Organic Carbon (g/kg)",
        "ph": "Soil pH",
        "nitrogen": "Nitrogen (N kg/ha)",
        "weather_sec": "🌧️ Weather & Climate Context",
        "rainfall": "Cumulative Rainfall (mm)",
        "gdd": "Growing Degree Days (GDD)",
        "heat_stress": "Heat Stress Days (>38°C)",
        "ndvi": "Peak Satellite NDVI Index",

        # Retrain Section
        "retrain_sec": "📤 Retrain Model on Real Data",
        "retrain_uploader": "Upload Syngenta Field Trial CSV",
        "retrain_success": "✅ Retrained on {samples} samples!\nR² Score: {r2}",
        "retrain_error": "❌ Retrain Notice: {msg}",

        # Biological Section
        "bio_sec": "🔬 Syngenta Biological Intervention",
        "sync_dosage_btn": "🤖 Sync Optimal Dosage",
        "sync_dosage_success": "✅ CE Hub Optimal Dosage Synced!",
        "apply_bio_toggle": "Apply Syngenta Biological",
        "select_product": "Select Product",
        "dosage_rate": "Dosage Rate (L/acre)",

        # Market Section
        "market_sec": "💰 Market Economics & Prices",
        "product_cost": "Product Cost (₹/acre)",
        "crop_price": "Crop Price / MSP (₹/Quintal)",

        # Hero Decision Card
        "decision_field_title": "📍 {region} • {crop} Field Decision",
        "action_apply": "✅ RECOMMENDED ACTION: APPLY {product} TODAY",
        "action_delay": "⚠️ RECOMMENDED ACTION: DELAY APPLICATION 1 DAY (HEAT / RAIN RISK)",
        "why_title": "💡 Plain Reason (Why this recommendation?):",
        "why_readiness": "Crop & Soil Readiness: Field readiness score is {score}/100 (Optimal root absorption window).",
        "why_weather": "Weather Telemetry: Live temp is {temp}°C ({desc}). Rain probability next 24h is {prob}%.",
        "why_stress": "Stress Buffering: Field has {days} heat stress days (>38°C). Biological treatment buffers flower abortion.",
        "financial_benefit_title": "Expected Financial Benefit",
        "financial_range": "Expected Range: ₹{low} – ₹{high}",
        "confidence_badge": "Confidence: High (95% CI)",

        # Navigation Tabs
        "tab_decision": "🌦️ Today's Decision & Weather",
        "tab_counter": "⚖️ Counterfactual (Act vs Do Nothing)",
        "tab_disease": "🩺 Disease Risk & NPK Advisor",
        "tab_memory": "📖 My Farm Memory (Journal)",
        "tab_prove": "📊 Outcome & Attribution Proof",
        "tab_ai": "💬 Conversational AI Assistant",
        "tab_expert": "⚙️ Agronomist & Expert Studio",

        # Tab 1: Decision & Weather
        "tab1_heading": "🌦️ Live Field Telemetry & 5-Day Agronomic Forecast",
        "ow_active_banner": "🌐 OpenWeather Live Telemetry Active",
        "ow_key_label": "Active Key:",
        "ow_feels_like": "Feels",
        "ow_rh": "RH",
        "ow_wind": "Wind",
        "ow_rain_prob": "Rain",

        # Tab 2: Counterfactual
        "tab2_heading": "⚖️ Decision Comparison: What Happens If I Act vs Do Nothing?",
        "tab2_caption": "Using counterfactual modeling to simulate expected harvest outcomes under identical weather & soil conditions.",
        "cf_without_title": "❌ WITHOUT INTERVENTION (Do Nothing)",
        "cf_with_title": "✅ WITH SYNGENTA BIOLOGICAL (Apply Today)",
        "cf_exp_yield": "Expected Yield: {yield_val} {unit}",
        "cf_exp_revenue": "Expected Gross Revenue: ₹{rev} / acre",
        "cf_vulnerable": "⚠️ Field remains vulnerable to summer heat stress ({days} days >38°C).",
        "cf_boost_tag": "(+{boost} boost)",
        "cf_investment_profit": "Product Investment: ₹{cost} | NET PROFIT: +₹{profit} / acre",

        # Tab 3: Disease & NPK & LeafVision
        "tab3_heading": "⚡ Real-Time Field Intelligence: Disease Risk & Smart NPK Advisor",
        "dis_warning_title": "🩺 Disease Risk & Biocontrol Warning",
        "dis_high_risk": "⚠️ **High Disease Risk Index ({risk}%)**: High humidity detected. Fungal blight risk for {crop}.",
        "dis_high_rec": "💡 **Syngenta Rec:** Apply **Syngenta Quantis / Biostimulant** + Bio-fungicide within 5 days.",
        "dis_low_risk": "✅ **Low Disease Risk Index ({risk}%)**: Crop canopy is healthy with optimal chlorophyll.",
        "npk_title": "🧪 Smart NPK Soil Health Advisor",
        "npk_baseline": "Soil Baseline:",
        "npk_deficit": "Target Deficit:",
        "npk_caption": "🌱 **Regenerative Soil Balancing:** Reduce synthetic Urea by 15% when combined with Syngenta Biostimulants.",
        "lv_heading": "🍃 LeafVision Edge Diagnostic (LABA-SNU Foundation Model)",
        "lv_caption": "Self-supervised vision foundation model pre-trained on 540,000+ agricultural leaf images. Runs 100% locally on edge hardware with 0 cloud token cost.",
        "lv_uploader": "Upload or Capture Field Leaf Sample",
        "lv_sample_caption": "Field Sample: {crop}",
        "lv_analyzing": "LeafVision extracting self-supervised visual features...",
        "lv_pathology": "Pathology: {diag}",
        "lv_pathogen": "Pathogen:",
        "lv_confidence": "Confidence: {conf}% | Edge Latency: {lat}ms",
        "lv_symptoms": "Symptoms:",
        "lv_prescription": "🔬 Syngenta Biological Prescription:",
        "lv_loss_prevention": "🛡️ Prevents up to {loss}% yield loss (~{amt} q/acre)",
        "lv_error": "LeafVision analysis note: {msg}",

        # Tab 4: Farm Memory
        "tab4_heading": "📖 My Farm Memory (Season Journal)",
        "tab4_caption": "Powered by Supabase PostgreSQL Database (wnujxbnjqrwybllvbahm) — Preserving your field history across seasons.",
        "mem_field_name": "Crop & Field Name",
        "mem_product": "Product Applied",
        "mem_dosage": "Dosage Applied (L/acre)",
        "mem_observed_yield": "Observed Yield (q/acre)",
        "mem_notes": "Farmer Field Notes",
        "mem_notes_default": "Applied during early flower initiation stage. Favorable root response.",
        "mem_save_btn": "📝 Save to Supabase Farm Memory",
        "mem_save_success_remote": "✅ Logged successfully to Supabase PostgreSQL Database!",
        "mem_save_success_local": "✅ Recorded in local Farm Memory!",
        "mem_history_title": "📜 Historical Farm Memory Log",
        "mem_actual_yield": "Actual Yield:",
        "mem_net_profit": "Net Profit:",

        # Tab 5: Outcome & Attribution
        "tab5_heading": "📊 Plain Outcome Attribution: What Contributed to My Crop Result?",
        "attr_breakdown_title": "Yield Attribution Factor Breakdown",
        "attr_baseline": "Baseline Harvest Without Biological",
        "attr_weather": "Monsoon & Climate Impact (Heat/Rain Buffer)",
        "attr_soil": "Soil Organic Profile (SOC & Nutrients)",
        "attr_bio": "Syngenta Biological Attributed Lift",
        "attr_summary_title": "Financial Attribution Summary",
        "attr_cost": "Product Investment Cost",
        "attr_profit": "Net Profit to Farmer",
        "attr_roi": "Return on Investment (ROI)",
        "download_pdf_btn": "📥 Download A4 PDF",
        "share_wa_btn": "📲 Share via WhatsApp",
        "wa_template_header": "🌾 *Syngenta Biologicals - Field ROI Report* 🌾",
        "wa_total_yield": "📈 *Total Yield:*",
        "wa_bio_boost": "🚀 *Biological Boost:*",
        "wa_net_profit": "💰 *Net Profit:*",
        "wa_roi": "🔥 *Farmer ROI:*",
        "wa_tagline": "✨ *Seeing is Believing!*",

        # Tab 6: Conversational AI
        "tab6_heading": "💬 Ask AgriAttribute AI Assistant (Powered by Google Gemini 2.5 Flash)",
        "tab6_caption": "Native Multilingual AI Assistant configured for {lang}. Ask questions about timing, weather, or products.",
        "ai_input_label": "Ask any question about your field:",
        "ai_input_default": "Why is {product} recommended for {crop} under {days} heat stress days?",
        "ai_ask_btn": "🤖 Ask Gemini AI",
        "ai_connecting": "Connecting to Google Gemini 2.5 Flash API...",
        "ai_response_title": "🤖 AgriAttribute AI (Gemini 2.5 Flash Response):",

        # Tab 7: Agronomist Studio
        "tab7_heading": "⚙️ Agronomist & Model Diagnostics Studio",
        "ag_r2": "XGBoost R² Score",
        "ag_rmse": "RMSE Error",
        "ag_mae": "MAE Error",
        "ag_samples": "Field Samples",
        "chart_title": "📈 Mid-Season Growth Trajectory & Divergence",
        "chart_xaxis": "Days After Sowing",
        "chart_yaxis": "Yield (q/acre)",
        "chart_control": "Untreated Field",
        "chart_bio": "With Syngenta Bio",
        "chart_annotation": "'Seeing is Believing' Boost",

        # Common Units
        "yield_unit": "q/acre",
        "currency": "₹"
    },

    "hi": {
        "agmark_expander_title": "🏛️ सभी भारतीय कृषि जींस समूह देखें (आधिकारिक Agmarknet 2.0 मंडी)",
        "agmark_caption": "निदेशालय विपणन एवं निरीक्षण (agmarknet.gov.in) से वास्तविक समय मंडी थोक भाव, न्यूनतम समर्थन मूल्य (MSP) और दैनिक आवक:",
        "agmark_tab_cereals": "🌾 अनाज (7)",
        "agmark_tab_oilseeds": "🌻 तिलहन (7)",
        "agmark_tab_pulses": "🥣 दालें (5)",
        "agmark_tab_fibre": "🧵 रेशा / कपास (1)",
        "agmark_tab_veg": "🥦 सब्जियां व गन्ना (4)",
        "agmark_card_msp": "सरकारी MSP:",
        "agmark_card_perishable": "नाशवान",
        "agmark_card_vs_msp": "MSP तुलना",
        "agmark_card_arrival": "दैनिक आवक:",
        "agmark_card_72h": "72 घंटे:",
        # App Header & Meta
        "title": "🌾 एग्री-एट्रीब्यूट AI: किसान निर्णय मंच",
        "subtitle": "“कदम उठाने से पहले कारण जानें। कदम उठाने के बाद परिणाम सिद्ध करें।”",
        "badge_hack": "हैक कोर 2026 - PS07",
        "badge_team": "टीम 15: सोहम काडू | सिंगीरेड्डी पी. | भक्ति कदम",
        "badge_loop": "📐 एकीकृत क्लोज्ड लूप",
        "badge_db": "⚡ सुपबेस पोस्टग्रेएसक्यूएल लाइव",
        "badge_ai": "🤖 जेमिनी 2.5 फ्लैश AI सक्रिय",

        # Location Intelligence
        "loc_title": "कृषि-जलवायु प्रक्षेत्र स्थान",
        "loc_detect_btn": "🛰️ जीपीएस द्वारा खेत खोजें",
        "loc_verified": "✅ खेत जीपीएस सत्यापित: {region}",
        "loc_change_belt": "कृषि-जलवायु क्षेत्र बदलें:",
        "belt_punjab": "पंजाब व हरियाणा",
        "belt_vidarbha": "महाराष्ट्र व विदर्भ",
        "belt_andhra": "आंध्र व तेलंगाना",
        "belt_up": "उत्तर प्रदेश व बिहार",
        "belt_karnataka": "कर्नाटक व तमिलनाडु",

        # Regional Crops Section
        "crop_sec_heading": "🌱 {region} में आमतौर पर क्या उगाया जाता है?",
        "crop_sec_caption": "क्षेत्रीय ICAR रकबा सर्वेक्षण पर आधारित कृषि बुद्धिमत्ता। अपनी फसल चुनने के लिए कार्ड पर टैप करें:",
        "acreage_share": "{share}% क्षेत्रीय रकबा",
        "active_field_badge": "सक्रिय प्रक्षेत्र",
        "select_crop_btn": "{crop} चुनें",
        "map_expander": "🗺️ {crop} का राष्ट्रीय फसल सघनता मानचित्र देखें",
        "map_caption": "{crop} की राष्ट्रीय खेती सघनता। बड़े और गहरे हरे वृत्त उस क्षेत्र में अधिक रकबे को दर्शाते हैं।",
        "map_title": "राष्ट्रीय फसल सघनता: {crop}",
        "map_hover_concentration": "{crop} की सघनता:",
        "map_hover_top": "प्रमुख फसलें:",

        # Sidebar
        "sidebar_lang_title": "Select Language / भाषा चुनें",
        "sidebar_mode_title": "अनुभव मोड",
        "mode_farmer": "🚜 किसान मोड (कार्रवाई-उन्मुख)",
        "mode_agronomist": "⚙️ कृषि वैज्ञानिक मोड (विशेषज्ञ विश्लेषण)",
        "sidebar_active_field": "सक्रिय फसल:",
        "sidebar_location": "स्थान:",
        "sidebar_farm_health": "🌱 खेत का स्वास्थ्य व मौसम",
        "soil_quality": "मिट्टी की गुणवत्ता",
        "opt_poor": "कमजोर",
        "opt_average": "मध्यम",
        "opt_excellent": "उत्कृष्ट",
        "monsoon_rain": "मानसूनी वर्षा",
        "opt_deficient": "कम",
        "opt_normal": "सामान्य",
        "opt_excess": "अधिक",
        "summer_heat": "ग्रीष्मकालीन गर्मी",
        "opt_very_hot": "अत्यधिक गर्म",

        # Agronomist Sliders
        "soil_sec": "🌱 मृदा स्वास्थ्य प्रोफाइल (ISRIC SoilGrids)",
        "soc": "मृदा जैविक कार्बन (g/kg)",
        "ph": "मृदा pH",
        "nitrogen": "नाइट्रोजन (N kg/ha)",
        "weather_sec": "🌧️ मौसम एवं जलवायु स्थिति",
        "rainfall": "कुल वर्षा (mm)",
        "gdd": "ग्रोइंग डिग्री डेज़ (GDD)",
        "heat_stress": "अत्यधिक गर्मी के दिन (>38°C)",
        "ndvi": "सैटेलाइट NDVI इंडेक्स",

        # Retrain Section
        "retrain_sec": "📤 वास्तविक फील्ड डेटा पर मॉडल पुनः प्रशिक्षित करें",
        "retrain_uploader": "सिंजेंटा फील्ड ट्रायल CSV अपलोड करें",
        "retrain_success": "✅ {samples} नमूनों पर मॉडल पुनः प्रशिक्षित!\nR² स्कोर: {r2}",
        "retrain_error": "❌ पुनः प्रशिक्षण सूचना: {msg}",

        # Biological Section
        "bio_sec": "🔬 सिंजेंटा जैविक (बायोलॉजिकल) उपचार",
        "sync_dosage_btn": "🤖 CE Hub से सटीक मात्रा सिंक करें",
        "sync_dosage_success": "✅ CE Hub से अनुशंसित मात्रा प्राप्त हुई!",
        "apply_bio_toggle": "सिंजेंटा जैविक उत्पाद का प्रयोग करें",
        "select_product": "जैविक उत्पाद चुनें",
        "dosage_rate": "प्रयोग दर (लीटर/एकड़)",

        # Market Section
        "market_sec": "💰 बाजार मूल्य और अर्थशास्त्र",
        "product_cost": "उत्पाद लागत (₹/एकड़)",
        "crop_price": "फसल का बाजार भाव / MSP (₹/क्विंटल)",

        # Hero Decision Card
        "decision_field_title": "📍 {region} • {crop} खेत निर्णय",
        "action_apply": "✅ अनुशंसित कार्रवाई: आज {product} का प्रयोग करें",
        "action_delay": "⚠️ अनुशंसित कार्रवाई: प्रयोग 1 दिन टालें (गर्मी / बारिश जोखिम)",
        "why_title": "💡 सीधा कारण (यह सलाह क्यों दी गई है?):",
        "why_readiness": "फसल व मिट्टी की तैयारी: फील्ड तैयारी स्कोर {score}/100 है (जड़ों द्वारा अवशोषण के लिए अनुकूल समय)।",
        "why_weather": "मौसम टेलीमेट्री: वर्तमान तापमान {temp}°C ({desc}) है। अगले 24 घंटों में बारिश की संभावना {prob}% है।",
        "why_stress": "तनाव रोधक: खेत में {days} दिन अत्यधिक गर्मी (>38°C) रही है। जैविक उत्पाद फूलों को झड़ने से बचाता है।",
        "financial_benefit_title": "अनुमानित शुद्ध वित्तीय लाभ",
        "financial_range": "अनुमानित दायरा: ₹{low} – ₹{high}",
        "confidence_badge": "सटीकता: उच्च (95% CI)",

        # Navigation Tabs
        "tab_decision": "🌦️ आज का निर्णय व मौसम",
        "tab_counter": "⚖️ तुलना: दवा डालें बनाम कुछ न करें",
        "tab_disease": "🩺 रोग जोखिम व NPK सलाहकार",
        "tab_memory": "📖 मेरा खेत स्मृति रजिस्टर (जर्नल)",
        "tab_prove": "📊 परिणाम व लाभ का प्रमाण",
        "tab_ai": "💬 किसान AI सहायक",
        "tab_expert": "⚙️ कृषि वैज्ञानिक विशेषज्ञ स्टूडियो",

        # Tab 1: Decision & Weather
        "tab1_heading": "🌦️ लाइव मौसम टेलीमेट्री और 5-दिवसीय कृषि पूर्वानुमान",
        "ow_active_banner": "🌐 ओपनवेदर लाइव टेलीमेट्री सक्रिय",
        "ow_key_label": "सक्रिय कुंजी:",
        "ow_feels_like": "महसूस",
        "ow_rh": "नमी",
        "ow_wind": "हवा",
        "ow_rain_prob": "बारिश",

        # Tab 2: Counterfactual
        "tab2_heading": "⚖️ निर्णय तुलना: जैविक उपचार करने बनाम कुछ न करने का परिणाम",
        "tab2_caption": "समान मौसम व मिट्टी में फसल कटाई परिणामों का वैज्ञानिक सिमुलेशन।",
        "cf_without_title": "❌ बिना उपचार के (कुछ न करने पर)",
        "cf_with_title": "✅ सिंजेंटा जैविक उपचार के साथ (आज छिड़काव)",
        "cf_exp_yield": "अनुमानित उपज: {yield_val} {unit}",
        "cf_exp_revenue": "अनुमानित कुल आय: ₹{rev} / एकड़",
        "cf_vulnerable": "⚠️ फसल गर्मी के तनाव ({days} दिन >38°C) के प्रति संवेदनशील रहेगी।",
        "cf_boost_tag": "(+{boost} अतिरिक्त उपज)",
        "cf_investment_profit": "उत्पाद निवेश: ₹{cost} | शुद्ध मुनाफा: +₹{profit} / एकड़",

        # Tab 3: Disease & NPK & LeafVision
        "tab3_heading": "⚡ वास्तविक समय प्रक्षेत्र सूचना: रोग जोखिम और स्मार्ट NPK सलाहकार",
        "dis_warning_title": "🩺 रोग जोखिम और सुरक्षा चेतावनी",
        "dis_high_risk": "⚠️ **उच्च रोग जोखिम सूचकांक ({risk}%)**: अधिक नमी दर्ज। {crop} में फफूंद झुलसा का खतरा।",
        "dis_high_rec": "💡 **सिंजेंटा सलाह:** 5 दिनों के भीतर **सिंजेंटा Quantis / बायोस्टिमुलेंट** + बायो-फफूंदनाशक का प्रयोग करें।",
        "dis_low_risk": "✅ **कम रोग जोखिम ({risk}%)**: फसल की पत्तियां स्वस्थ और क्लोरोफिल उत्तम है।",
        "npk_title": "🧪 स्मार्ट NPK मृदा पोषण सलाहकार",
        "npk_baseline": "वर्तमान मिट्टी पोषक तत्व:",
        "npk_deficit": "आवश्यक अतिरिक्त खुराक:",
        "npk_caption": "🌱 **संतुलित मृदा स्वास्थ्य:** सिंजेंटा बायोस्टिमुलेंट के साथ रासायनिक यूरिया में 15% की कमी की जा सकती है।",
        "lv_heading": "🍃 लीफ-विज़न एज निदान (LABA-SNU फाउंडेशन मॉडल)",
        "lv_caption": "5,40,000+ कृषि पत्तियों पर प्रशिक्षित स्व-पर्यवेक्षित विज़न मॉडल। बिना किसी क्लाउड लागत के स्थानीय स्तर पर त्वरित परिणाम।",
        "lv_uploader": "खेत की पत्ती का फोटो अपलोड करें या खींचें",
        "lv_sample_caption": "फील्ड पत्ती नमूना: {crop}",
        "lv_analyzing": "लीफ-विज़न पत्तियों के रोग लक्षणों का विश्लेषण कर रहा है...",
        "lv_pathology": "रोग निदान: {diag}",
        "lv_pathogen": "रोगजनक (पैथोजन):",
        "lv_confidence": "विश्वसनीयता: {conf}% | प्रतिक्रिया समय: {lat}ms",
        "lv_symptoms": "देखे गए लक्षण:",
        "lv_prescription": "🔬 सिंजेंटा जैविक उपचार नुस्खा:",
        "lv_loss_prevention": "🛡️ {loss}% तक संभावित नुकसान से सुरक्षा (~{amt} क्विंटल/एकड़)",
        "lv_error": "लीफ-विज़न विश्लेषण टिप्पणी: {msg}",

        # Tab 4: Farm Memory
        "tab4_heading": "📖 मेरा खेत स्मृति रजिस्टर (सीज़न जर्नल)",
        "tab4_caption": "सुपबेस पोस्टग्रेएसक्यूएल डेटाबेस द्वारा संचालित — सीज़न दर सीज़न आपके खेत का रिकॉर्ड सुरक्षित।",
        "mem_field_name": "फसल व खेत का नाम",
        "mem_product": "उपयोग किया गया उत्पाद",
        "mem_dosage": "उपयोग की गई मात्रा (लीटर/एकड़)",
        "mem_observed_yield": "प्राप्त वास्तविक उपज (क्विंटल/एकड़)",
        "mem_notes": "किसान के अपने अनुभव / नोट्स",
        "mem_notes_default": "शुरुआती फूल आने की अवस्था में छिड़काव किया गया। जड़ों का विकास बहुत बढ़िया रहा।",
        "mem_save_btn": "📝 सुपबेस खेत डायरी में सहेजें",
        "mem_save_success_remote": "✅ सुपबेस पोस्टग्रेएसक्यूएल क्लाउड में सफलतापूर्वक दर्ज!",
        "mem_save_success_local": "✅ स्थानीय खेत मेमोरी में दर्ज!",
        "mem_history_title": "📜 पिछले सीज़न का फील्ड रिकॉर्ड",
        "mem_actual_yield": "वास्तविक उपज:",
        "mem_net_profit": "शुद्ध लाभ:",

        # Tab 5: Outcome & Attribution
        "tab5_heading": "📊 स्पष्ट परिणाम श्रेय: मेरी फसल वृद्धि में किस घटक का कितना योगदान था?",
        "attr_breakdown_title": "उपज योगदान घटकों का विश्लेषण",
        "attr_baseline": "मूल उपज (बिना जैविक उपचार के)",
        "attr_weather": "मानसून व मौसम प्रभाव (गर्मी/वर्षा रोधक)",
        "attr_soil": "मृदा जैविक प्रोफाइल (कार्बन व पोषक तत्व)",
        "attr_bio": "सिंजेंटा जैविक उत्पाद से शुद्ध अतिरिक्त लाभ",
        "attr_summary_title": "वित्तीय परिणाम सारांश",
        "attr_cost": "उत्पाद निवेश लागत",
        "attr_profit": "किसान को शुद्ध मुनाफा",
        "attr_roi": "निवेश पर प्रतिफल (ROI)",
        "download_pdf_btn": "📥 A4 PDF रिपोर्ट डाउनलोड करें",
        "share_wa_btn": "📲 WhatsApp पर रिपोर्ट शेयर करें",
        "wa_template_header": "🌾 *सिंजेंटा बायोलॉजिकल्स - प्रक्षेत्र ROI रिपोर्ट* 🌾",
        "wa_total_yield": "📈 *कुल अनुमानित उपज:*",
        "wa_bio_boost": "🚀 *जैविक उत्पाद से लाभ:*",
        "wa_net_profit": "💰 *शुद्ध मुनाफा:*",
        "wa_roi": "🔥 *किसान ROI:*",
        "wa_tagline": "✨ *प्रत्यक्ष को प्रमाण की क्या आवश्यकता!*",

        # Tab 6: Conversational AI
        "tab6_heading": "💬 एग्री-एट्रीब्यूट AI सहायक से पूछें (Google Gemini 2.5 Flash संचालित)",
        "tab6_caption": "आपकी पसंदीदा भाषा {lang} में तैयार देशी AI सलाहकार। छिड़काव समय, मौसम या उत्पाद संबंधी प्रश्न पूछें।",
        "ai_input_label": "अपने खेत के बारे में कोई भी प्रश्न पूछें:",
        "ai_input_default": "{days} दिन गर्मी के तनाव में {crop} के लिए {product} का छिड़काव क्यों फायदेमंद है?",
        "ai_ask_btn": "🤖 जेमिनी AI से सलाह लें",
        "ai_connecting": "Google Gemini 2.5 Flash से संपर्क हो रहा है...",
        "ai_response_title": "🤖 एग्री-एट्रीब्यूट AI (जेमिनी 2.5 फ्लैश उत्तर):",

        # Tab 7: Agronomist Studio
        "tab7_heading": "⚙️ कृषि वैज्ञानिक एवं मॉडल विश्लेषण स्टूडियो",
        "ag_r2": "XGBoost R² स्कोर",
        "ag_rmse": "RMSE त्रुटि",
        "ag_mae": "MAE त्रुटि",
        "ag_samples": "फील्ड नमूने",
        "chart_title": "📈 फसल वृद्धि व जैविक प्रभाव का प्रक्षेपवक्र",
        "chart_xaxis": "बुवाई के बाद के दिन",
        "chart_yaxis": "उपज क्षमता (क्विंटल/एकड़)",
        "chart_control": "अनुपचारित खेत (कंट्रोल)",
        "chart_bio": "सिंजेंटा जैविक उपचारित",
        "chart_annotation": "'प्रत्यक्ष प्रमाण' अतिरिक्त उपज",

        # Common Units
        "yield_unit": "क्विंटल/एकड़",
        "currency": "₹"
    },

    "mr": {
        "agmark_expander_title": "🏛️ सर्व भारतीय कृषी कमोडिटी गट पहा (अधिकृत Agmarknet 2.0 बाजारपेठ)",
        "agmark_caption": "विपणन आणि तपासणी संचालनालय (agmarknet.gov.in) कडून थेट बाजारभाव, हमीभाव (MSP) आणि दैनिक आवक:",
        "agmark_tab_cereals": "🌾 अन्नधान्ये (7)",
        "agmark_tab_oilseeds": "🌻 गळीत धान्ये (7)",
        "agmark_tab_pulses": "🥣 कडधान्ये (5)",
        "agmark_tab_fibre": "🧵 कापूस (1)",
        "agmark_tab_veg": "🥦 भाजीपाला व ऊस (4)",
        "agmark_card_msp": "सरकारी हमीभाव:",
        "agmark_card_perishable": "नाशवंत",
        "agmark_card_vs_msp": "हमीभाव तुलना",
        "agmark_card_arrival": "दैनिक आवक:",
        "agmark_card_72h": "72 तास:",
        # App Header & Meta
        "title": "🌾 ऍग्री-अॅट्रिब्युट AI: शेतकरी निर्णय मंच",
        "subtitle": "“कृती करण्यापूर्वी कारण जाणून घ्या. कृती केल्यानंतर परिणाम सिद्ध करा.”",
        "badge_hack": "हॅक कोर २०२६ - PS07",
        "badge_team": "टीम १५: सोहम काडू | सिंगीरेड्डी पी. | भक्ती कदम",
        "badge_loop": "📐 एकात्मिक क्लोज्ड लूप",
        "badge_db": "⚡ सुपबेस पोस्टग्रेएसक्यूएल थेट",
        "badge_ai": "🤖 जेमिनी २.५ फ्लॅश AI सक्रिय",

        # Location Intelligence
        "loc_title": "कृषी-हवामान शेत स्थान",
        "loc_detect_btn": "🛰️ GPS द्वारे शेत शोधा",
        "loc_verified": "✅ शेत GPS सत्यापित: {region}",
        "loc_change_belt": "कृषी-हवामान पट्टा बदला:",
        "belt_punjab": "पंजाब आणि हरियाणा",
        "belt_vidarbha": "महाराष्ट्र आणि विदर्भ",
        "belt_andhra": "आंध्र आणि तेलंगणा",
        "belt_up": "उत्तर प्रदेश आणि बिहार",
        "belt_karnataka": "कर्नाटक आणि तामिळनाडू",

        # Regional Crops Section
        "crop_sec_heading": "🌱 {region} मध्ये प्रामुख्याने काय पिकवले जाते?",
        "crop_sec_caption": "प्रादेशिक ICAR क्षेत्र पाहणीवर आधारित कृषी बुद्धिमत्ता. आपल्या शेतातील पीक निवडण्यासाठी कार्डवर टॅप करा:",
        "acreage_share": "{share}% प्रादेशिक क्षेत्र",
        "active_field_badge": "सक्रिय शेत",
        "select_crop_btn": "{crop} निवडा",
        "map_expander": "🗺️ {crop} चे राष्ट्रीय पीक घनता नकाशा पाहा",
        "map_caption": "{crop} ची राष्ट्रीय लागवड घनता. मोठे आणि गडद हिरवे वर्तुळ त्या भागातील जास्त लागवड दर्शवतात.",
        "map_title": "राष्ट्रीय पीक घनता: {crop}",
        "map_hover_concentration": "{crop} चे प्रमाण:",
        "map_hover_top": "प्रमुख पिके:",

        # Sidebar
        "sidebar_lang_title": "Select Language / भाषा निवडा",
        "sidebar_mode_title": "अनुभव मोड",
        "mode_farmer": "🚜 शेतकरी मोड (कृती-केंद्रित)",
        "mode_agronomist": "⚙️ कृषी तज्ज्ञ मोड (सखोल विश्लेषण)",
        "sidebar_active_field": "सक्रिय पीक:",
        "sidebar_location": "स्थान:",
        "sidebar_farm_health": "🌱 शेताचे आरोग्य आणि हवामान",
        "soil_quality": "मातीची प्रत",
        "opt_poor": "कमकुवत",
        "opt_average": "मध्यम",
        "opt_excellent": "उत्कृष्ट",
        "monsoon_rain": "पावसाचे प्रमाण",
        "opt_deficient": "कमी",
        "opt_normal": "सामान्य",
        "opt_excess": "भरपूर",
        "summer_heat": "उन्हाची तीव्रता",
        "opt_very_hot": "अतिउष्ण",

        # Agronomist Sliders
        "soil_sec": "🌱 मातीचे आरोग्य (ISRIC SoilGrids)",
        "soc": "मातीतील सेंद्रिय कर्ब (g/kg)",
        "ph": "मातीचा सामू (pH)",
        "nitrogen": "नत्र / नायट्रोजन (N kg/ha)",
        "weather_sec": "🌧️ हवामान आणि निसर्ग स्थिती",
        "rainfall": "एकूण पाऊस (mm)",
        "gdd": "ग्रोइंग डिग्री डेज (GDD)",
        "heat_stress": "उष्णतेचे दिवस (>38°C)",
        "ndvi": "उपग्रह NDVI निर्देशांक",

        # Retrain Section
        "retrain_sec": "📤 प्रत्यक्ष फील्ड डेटावर मॉडेल पुन्हा प्रशिक्षित करा",
        "retrain_uploader": "सिंजेंटा फील्ड ट्रायल CSV अपलोड करा",
        "retrain_success": "✅ {samples} नमुन्यांवर मॉडेल पुन्हा प्रशिक्षित!\nR² स्कोअर: {r2}",
        "retrain_error": "❌ री-ट्रेन सूचना: {msg}",

        # Biological Section
        "bio_sec": "🔬 सिंजेंटा जैविक (बायोलॉजिकल) उपाय",
        "sync_dosage_btn": "🤖 CE Hub वरून योग्य प्रमाण मिळवा",
        "sync_dosage_success": "✅ CE Hub वरून शिफारस केलेले प्रमाण सिंक झाले!",
        "apply_bio_toggle": "सिंजेंटा जैविक उत्पादनाचा वापर करा",
        "select_product": "जैविक उत्पादन निवडा",
        "dosage_rate": "वापरण्याचे प्रमाण (लिटर/एकर)",

        # Market Section
        "market_sec": "💰 बाजारभाव आणि अर्थशास्त्र",
        "product_cost": "उत्पादन खर्च (₹/एकर)",
        "crop_price": "बाजारभाव / हमीभाव MSP (₹/क्विंटल)",

        # Hero Decision Card
        "decision_field_title": "📍 {region} • {crop} शेत निर्णय",
        "action_apply": "✅ शिफारस केलेली कृती: आज {product} चा वापर करा",
        "action_delay": "⚠️ शिफारस केलेली कृती: वापर १ दिवस पुढे ढकला (उष्णता / पावसाचा धोका)",
        "why_title": "💡 सोपे कारण (हा सल्ला का दिला आहे?):",
        "why_readiness": "पीक व मातीची सज्जता: शेताची सज्जता {score}/100 आहे (मुळांवाटे शोषण होण्यासाठी अत्यंत अनुकूल वेळ).",
        "why_weather": "थेट हवामान: सध्याचे तापमान {temp}°C ({desc}) आहे. पुढील २४ तासांत पावसाची शक्यता {prob}% आहे.",
        "why_stress": "ताण सहनशीलता: शेताने {days} दिवस अतिउष्णता (>38°C) अनुभवली आहे. जैविक उत्पादनामुळे फुलगळ रोखली जाते.",
        "financial_benefit_title": "अपेक्षित निव्वळ आर्थिक फायदा",
        "financial_range": "अपेक्षित कक्षा: ₹{low} – ₹{high}",
        "confidence_badge": "अचूकता: उच्च (95% CI)",

        # Navigation Tabs
        "tab_decision": "🌦️ आजचा निर्णय आणि हवामान",
        "tab_counter": "⚖️ तुलना: औषध फवारले विरूद्ध काहीच नाही केले",
        "tab_disease": "🩺 रोग धोका आणि NPK सल्लागार",
        "tab_memory": "📖 शेतकरी रोजनिशी (जर्नल)",
        "tab_prove": "📊 उत्पादकता व नफ्याचा पुरावा",
        "tab_ai": "💬 शेतकरी AI सल्लागार",
        "tab_expert": "⚙️ कृषी तज्ज्ञ व मॉडेल स्टुडिओ",

        # Tab 1: Decision & Weather
        "tab1_heading": "🌦️ थेट हवामान निरीक्षण आणि ५ दिवसांचा कृषी अंदाज",
        "ow_active_banner": "🌐 ओपनवेदर थेट हवामान सक्रिय",
        "ow_key_label": "सक्रिय की:",
        "ow_feels_like": "जाणवणारे",
        "ow_rh": "आर्द्रता",
        "ow_wind": "वारा",
        "ow_rain_prob": "पाऊस",

        # Tab 2: Counterfactual
        "tab2_heading": "⚖️ निर्णयाची तुलना: जैविक उपाय केल्यास काय होईल आणि न केल्यास काय?",
        "tab2_caption": "समान हवामान व मातीत पीक कापणीच्या संभाव्य निकालांचे वैज्ञानिक विश्लेषण.",
        "cf_without_title": "❌ उपाय न केल्यास (काहीही न करता)",
        "cf_with_title": "✅ सिंजेंटा जैविक उपायासह (आज फवारणी)",
        "cf_exp_yield": "अपेक्षित उत्पादन: {yield_val} {unit}",
        "cf_exp_revenue": "अपेक्षित एकूण उत्पन्न: ₹{rev} / एकर",
        "cf_vulnerable": "⚠️ पीक उन्हाच्या ताणास ({days} दिवस >38°C) बळी पडण्याची शक्यता कायम आहे.",
        "cf_boost_tag": "(+{boost} वाढीव उत्पादन)",
        "cf_investment_profit": "औषध गुंतवणूक: ₹{cost} | निव्वळ नफा: +₹{profit} / एकर",

        # Tab 3: Disease & NPK & LeafVision
        "tab3_heading": "⚡ थेट शेत बुद्धिमत्ता: रोगाचा धोका आणि स्मार्ट NPK सल्लागार",
        "dis_warning_title": "🩺 रोगाचा धोका आणि पीक संरक्षण चेतावणी",
        "dis_high_risk": "⚠️ **जास्त रोग धोका निर्देशांक ({risk}%)**: हवेतील जास्त दमटपणामुळे {crop} मध्ये करपा/बुरशीचा धोका.",
        "dis_high_rec": "💡 **सिंजेंटा सल्ला:** ५ दिवसांच्या आत **सिंजेंटा Quantis / बायोस्टिम्युलंट** + बुरशीनाशकाचा वापर करा.",
        "dis_low_risk": "✅ **कमी रोग धोका ({risk}%)**: पिकाची पाने सशक्त असून हरितद्रव्य उत्तम आहे.",
        "npk_title": "🧪 स्मार्ट NPK माती पोषण सल्लागार",
        "npk_baseline": "सध्याचे जमिनीतील पोषण:",
        "npk_deficit": "आवश्यक अतिरिक्त मात्रा:",
        "npk_caption": "🌱 **संतुलित जमीन आरोग्य:** सिंजेंटा बायोस्टिम्युलंट वापरल्यास रासायनिक युरियामध्ये १५% बचत होऊ शकते.",
        "lv_heading": "🍃 लीफ-व्हिजन एज निदान (LABA-SNU फाउंडेशन मॉडेल)",
        "lv_caption": "५,४०,०००+ कृषी पानांवर प्रशिक्षित सखोल संगणक दृष्टी मॉडेल. कोणत्याही इंटरनेट खर्चाशिवाय आपल्या फोनवर सेकंदात निकाल.",
        "lv_uploader": "शेतातील पानाचा फोटो अपलोड करा किंवा काढा",
        "lv_sample_caption": "फील्ड पानाचा नमुना: {crop}",
        "lv_analyzing": "लीफ-व्हिजन पानातील रोग लक्षणांचा शोध घेत आहे...",
        "lv_pathology": "रोग निदान: {diag}",
        "lv_pathogen": "रोगजंतू (पॅथोजेन):",
        "lv_confidence": "विश्वासार्हता: {conf}% | वेग: {lat}ms",
        "lv_symptoms": "दिसलेली लक्षणे:",
        "lv_prescription": "🔬 सिंजेंटा जैविक उपाययोजना:",
        "lv_loss_prevention": "🛡️ {loss}% संभाव्य नुकसान टळू शकते (~{amt} क्विंटल/एकर)",
        "lv_error": "लीफ-व्हिजन तपासणी नोंद: {msg}",

        # Tab 4: Farm Memory
        "tab4_heading": "📖 माझी शेत रोजनिशी (हंगाम जर्नल)",
        "tab4_caption": "सुपबेस पोस्टग्रेएसक्यूएल डेटाबेसद्वारे संरक्षित — पिढ्यानपिढ्या आपल्या शेताचा इतिहास सुरक्षित.",
        "mem_field_name": "पीक आणि शेताचे नाव",
        "mem_product": "वापरलेले उत्पादन",
        "mem_dosage": "वापरलेले प्रमाण (लिटर/एकर)",
        "mem_observed_yield": "प्रत्यक्ष मिळालेले उत्पादन (क्विंटल/एकर)",
        "mem_notes": "शेतकऱ्याचे स्वतःचे अनुभव / नोंदी",
        "mem_notes_default": "फुलोरा लागण्याच्या सुरुवातीला फवारणी केली. मुळांची वाढ आणि फुटवे खूप चांगले झाले.",
        "mem_save_btn": "📝 सुपबेस शेत रोजनिशीत जतन करा",
        "mem_save_success_remote": "✅ सुपबेस पोस्टग्रेएसक्यूएल क्लाऊडवर यशस्वीरीत्या नोंदवले!",
        "mem_save_success_local": "✅ स्थानिक शेत मेमरीमध्ये नोंदवले!",
        "mem_history_title": "📜 मागील हंगामातील नोंदी",
        "mem_actual_yield": "प्रत्यक्ष उत्पादन:",
        "mem_net_profit": "निव्वळ नफा:",

        # Tab 5: Outcome & Attribution
        "tab5_heading": "📊 प्रत्यक्ष परिणाम श्रेय: माझ्या पीक उत्पादनात नेमका कशाचा किती वाटा होता?",
        "attr_breakdown_title": "उत्पादनातील घटकांचे नेमके विश्लेषण",
        "attr_baseline": "नैसर्गिक मूळ उत्पादन (जैविक उपायाशिवाय)",
        "attr_weather": "हवामान आणि पाऊस प्रभाव (उष्णता/पाणी ताण रक्षण)",
        "attr_soil": "मातीचा सेंद्रिय दर्जा (कर्ब आणि पोषण)",
        "attr_bio": "सिंजेंटा जैविक उत्पादनामुळे झालेली वाढ",
        "attr_summary_title": "आर्थिक नफा सारांश",
        "attr_cost": "उत्पादन खरेदी खर्च",
        "attr_profit": "शेतकऱ्याचा निव्वळ नफा",
        "attr_roi": "गुंतवणुकीवरील परतावा (ROI)",
        "download_pdf_btn": "📥 A4 PDF अहवाल डाउनलोड करा",
        "share_wa_btn": "📲 WhatsApp वर अहवाल पाठवा",
        "wa_template_header": "🌾 *सिंजेंटा बायोलॉजिकल्स - प्रक्षेत्र नफा अहवाल* 🌾",
        "wa_total_yield": "📈 *एकूण उत्पादन:*",
        "wa_bio_boost": "🚀 *जैविक उत्पादनामुळे वाढ:*",
        "wa_net_profit": "💰 *निव्वळ नफा:*",
        "wa_roi": "🔥 *शेतकरी परतावा (ROI):*",
        "wa_tagline": "✨ *प्रत्यक्ष पाहिले की विश्वास बसतो!*",

        # Tab 6: Conversational AI
        "tab6_heading": "💬 ऍग्री-अॅट्रिब्युट AI सहाय्यकाशी बोला (Google Gemini 2.5 Flash)",
        "tab6_caption": "{lang} भाषेसाठी विशेष तयार केलेला डिजिटल कृषी तज्ज्ञ. फवारणी, हवामान किंवा औषधांविषयी प्रश्न विचारा.",
        "ai_input_label": "आपल्या शेतीविषयी कोणताही प्रश्न विचारा:",
        "ai_input_default": "{days} दिवस अतिउष्णतेमध्ये {crop} साठी {product} फवारणी करणे का फायदेशीर आहे?",
        "ai_ask_btn": "🤖 जेमिनी AI कडून सल्ला घ्या",
        "ai_connecting": "Google Gemini 2.5 Flash कडून उत्तर मिळवत आहे...",
        "ai_response_title": "🤖 ऍग्री-अॅट्रिब्युट AI (जेमिनी २.५ फ्लॅश उत्तर):",

        # Tab 7: Agronomist Studio
        "tab7_heading": "⚙️ कृषी तज्ज्ञ आणि मॉडेल विश्लेषण स्टुडिओ",
        "ag_r2": "XGBoost R² अचूकता स्कोअर",
        "ag_rmse": "RMSE त्रुटी",
        "ag_mae": "MAE त्रुटी",
        "ag_samples": "फील्ड नमुने",
        "chart_title": "📈 पीक वाढीचा आलेख आणि जैविक उपायांचा फरक",
        "chart_xaxis": "पेरणीनंतरचे दिवस",
        "chart_yaxis": "उत्पादन क्षमता (क्विंटल/एकर)",
        "chart_control": "उपचार न केलेले शेत (कंट्रोल)",
        "chart_bio": "सिंजेंटा जैविक उपचार केलेले",
        "chart_annotation": "'प्रत्यक्ष पुरावा' अतिरिक्त उत्पादन",

        # Common Units
        "yield_unit": "क्विंटल/एकर",
        "currency": "₹"
    },

    "te": {
        "agmark_expander_title": "🏛️ అన్ని భారతీయ వ్యవసాయ వస్తువుల సమూహాలు (అధికారిక Agmarknet 2.0 మార్కెట్)",
        "agmark_caption": "మార్కెటింగ్ డైరెక్టరేట్ (agmarknet.gov.in) నుండి ప్రత్యక్ష మార్కెట్ ధరలు, MSP మరియు రోజువారీ రాకలు:",
        "agmark_tab_cereals": "🌾 తృణధాన్యాలు (7)",
        "agmark_tab_oilseeds": "🌻 నూనెగింజలు (7)",
        "agmark_tab_pulses": "🥣 పప్పుధాన్యాలు (5)",
        "agmark_tab_fibre": "🧵 పత్తి (1)",
        "agmark_tab_veg": "🥦 కూరగాయలు & చెరకు (4)",
        "agmark_card_msp": "ప్రభుత్వ MSP:",
        "agmark_card_perishable": "పాడైపోయేవి",
        "agmark_card_vs_msp": "MSP పోలిక",
        "agmark_card_arrival": "రాక:",
        "agmark_card_72h": "72 గం:",
        # App Header & Meta
        "title": "🌾 అగ్రి-అట్రిబ్యూట్ AI: రైతు నిర్ణయ వేదిక",
        "subtitle": "“చర్య తీసుకునే ముందు ఎందుకు అని తెలుసుకోండి. తీసుకున్న తర్వాత ఫలితం నిరూపించండి.”",
        "badge_hack": "హ్యాక్ కోర్ 2026 - PS07",
        "badge_team": "టీమ్ 15: సోహమ్ కాడు | సింగిరెడ్డి పి. | భక్తి కదం",
        "badge_loop": "📐 సమగ్ర క్లోజ్డ్ లూప్",
        "badge_db": "⚡ సుపాబేస్ పోస్ట్‌గ్రేస్ లైవ్",
        "badge_ai": "🤖 జెమిని 2.5 ఫ్లాష్ AI యాక్టివ్",

        # Location Intelligence
        "loc_title": "వ్యవసాయ-శీతోష్ణస్థితి ప్రాంతం",
        "loc_detect_btn": "🛰️ GPS ద్వారా పొలం గుర్తించండి",
        "loc_verified": "✅ పొలం GPS ధృవీకరించబడింది: {region}",
        "loc_change_belt": "వ్యవసాయ ప్రాంతాన్ని మార్చండి:",
        "belt_punjab": "పంజాబ్ & హర్యానా",
        "belt_vidarbha": "మహారాష్ట్ర & విదర్భ",
        "belt_andhra": "ఆంధ్ర & తెలంగాణ",
        "belt_up": "ఉత్తరప్రదేశ్ & బీహార్",
        "belt_karnataka": "కర్ణాటక & తమిళనాడు",

        # Regional Crops Section
        "crop_sec_heading": "🌱 {region} లో సాధారణంగా ఏ పంటలు సాగు చేస్తారు?",
        "crop_sec_caption": "ప్రాంతీయ ICAR సర్వే ఆధారిత వ్యవసాయ సమాచారం. మీ పంటను ఎంచుకోవడానికి కార్డ్‌పై నొక్కండి:",
        "acreage_share": "{share}% ప్రాంతీయ విస్తీర్ణం",
        "active_field_badge": "ప్రస్తుత పొలం",
        "select_crop_btn": "{crop} ఎంచుకోండి",
        "map_expander": "🗺️ {crop} కోసం జాతీయ పంట సాంద్రత మ్యాప్ చూడండి",
        "map_caption": "{crop} జాతీయ సాగు సాంద్రత. పెద్ద మరియు ముదురు ఆకుపచ్చ వృత్తాలు ఎక్కువ విస్తీర్ణాన్ని సూచిస్తాయి.",
        "map_title": "జాతీయ పంట సాంద్రత: {crop}",
        "map_hover_concentration": "{crop} సాంద్రత:",
        "map_hover_top": "ప్రధాన పంటలు:",

        # Sidebar
        "sidebar_lang_title": "Select Language / భాషను ఎంచుకోండి",
        "sidebar_mode_title": "అనుభవ మోడ్",
        "mode_farmer": "🚜 రైతు మోడ్ (చర్య-కేంద్రీకృతం)",
        "mode_agronomist": "⚙️ వ్యవసాయ శాస్త్రవేత్త మోడ్ (లోతైన విశ్లేషణ)",
        "sidebar_active_field": "ప్రస్తుత పంట:",
        "sidebar_location": "ప్రాంతం:",
        "sidebar_farm_health": "🌱 పొలం ఆరోగ్యం & వాతావరణం",
        "soil_quality": "నేల నాణ్యత",
        "opt_poor": "తక్కువ",
        "opt_average": "మధ్యస్థం",
        "opt_excellent": "ఉత్తమం",
        "monsoon_rain": "వర్షపాతం",
        "opt_deficient": "తక్కువ",
        "opt_normal": "సాధారణం",
        "opt_excess": "ఎక్కువ",
        "summer_heat": "ఎండ తీవ్రత",
        "opt_very_hot": "చాలా ఎక్కువ",

        # Agronomist Sliders
        "soil_sec": "🌱 నేల ఆరోగ్య ప్రొఫైల్ (ISRIC SoilGrids)",
        "soc": "నేల సేంద్రీయ కర్బనం (g/kg)",
        "ph": "నేల pH",
        "nitrogen": "నత్రజని (N kg/ha)",
        "weather_sec": "🌧️ వాతావరణ పరిస్థితులు",
        "rainfall": "మొత్తం వర్షపాతం (mm)",
        "gdd": "గ్రోయింగ్ డిగ్రీ డేస్ (GDD)",
        "heat_stress": "తీవ్ర ఎండ రోజులు (>38°C)",
        "ndvi": "ఉపగ్రహ NDVI సూచిక",

        # Retrain Section
        "retrain_sec": "📤 నిజమైన ఫీల్డ్ డేటాతో మోడల్ రీ-ట్రైన్ చేయండి",
        "retrain_uploader": "సింజెంటా ఫీల్డ్ ట్రయల్ CSV అప్‌లోడ్ చేయండి",
        "retrain_success": "✅ {samples} నమూనాలతో రీ-ట్రైన్ పూర్తయింది!\nR² స్కోర్: {r2}",
        "retrain_error": "❌ రీ-ట్రైన్ నోటీసు: {msg}",

        # Biological Section
        "bio_sec": "🔬 సింజెంటా బయోలాజికల్ చికిత్స",
        "sync_dosage_btn": "🤖 CE Hub ద్వారా సరైన మోతాదు పొందండి",
        "sync_dosage_success": "✅ CE Hub సరైన మోతాదు సింక్ చేయబడింది!",
        "apply_bio_toggle": "సింజెంటా బయోలాజికల్ ఉత్పత్తిని వాడండి",
        "select_product": "ఉత్పత్తిని ఎంచుకోండి",
        "dosage_rate": "మోతాదు రేటు (లీటరు/ఎకరం)",

        # Market Section
        "market_sec": "💰 మార్కెట్ ధరలు & ఆర్థిక విశ్లేషణ",
        "product_cost": "ఉత్పత్తి ఖర్చు (₹/ఎకరం)",
        "crop_price": "పంట ధర / MSP (₹/క్వింటాల్)",

        # Hero Decision Card
        "decision_field_title": "📍 {region} • {crop} పొలం నిర్ణయం",
        "action_apply": "✅ సిఫార్సు చేసిన చర్య: ఈరోజు {product} ను ఉపయోగించండి",
        "action_delay": "⚠️ సిఫార్సు చేసిన చర్య: వాడకాన్ని 1 రోజు వాయిదా వేయండి (ఎండ / వర్షం ప్రమాదం)",
        "why_title": "💡 స్పష్టమైన కారణం (ఈ సిఫార్సు ఎందుకు?):",
        "why_readiness": "పంట & నేల సంసిద్ధత: ఫీల్డ్ సంసిద్ధత స్కోర్ {score}/100 (వేర్లు గ్రహించడానికి అత్యంత అనుకూల సమయం).",
        "why_weather": "వాతావరణ సమాచారం: ప్రస్తుత ఉష్ణోగ్రత {temp}°C ({desc}). రాబోయే 24 గంటల్లో వర్షం అవకాశం {prob}%.",
        "why_stress": "ఒత్తిడి నిరోధకత: పొలంలో {days} రోజులు తీవ్రమైన వేడి (>38°C) ఉంది. బయోలాజికల్ చికిత్స పూత రాలడాన్ని నివారిస్తుంది.",
        "financial_benefit_title": "ఆశించే నికర ఆర్థిక ప్రయోజనం",
        "financial_range": "అంచనా పరిధి: ₹{low} – ₹{high}",
        "confidence_badge": "ఖచ్చితత్వం: ఎక్కువ (95% CI)",

        # Navigation Tabs
        "tab_decision": "🌦️ నేటి నిర్ణయం & వాతావరణం",
        "tab_counter": "⚖️ పోలిక: మందు వాడితే vs ఏమీ చేయకపోతే",
        "tab_disease": "🩺 తెగుళ్ల ప్రమాదం & NPK సలహాదారు",
        "tab_memory": "📖 నా పొలం జ్ఞాపకాలు (జర్నల్)",
        "tab_prove": "📊 ఫలితం & లాభం రుజువు",
        "tab_ai": "💬 రైతు AI సహాయకుడు",
        "tab_expert": "⚙️ శాస్త్రవేత్త & మోడల్ స్టూడియో",

        # Tab 1: Decision & Weather
        "tab1_heading": "🌦️ లైవ్ ఫీల్డ్ సమాచారం మరియు 5-రోజుల వ్యవసాయ సూచన",
        "ow_active_banner": "🌐 ఓపెన్‌వెదర్ లైవ్ సమాచారం యాక్టివ్",
        "ow_key_label": "యాక్టివ్ కీ:",
        "ow_feels_like": "అనిపించేది",
        "ow_rh": "తేమ",
        "ow_wind": "గాలి",
        "ow_rain_prob": "వర్షం",

        # Tab 2: Counterfactual
        "tab2_heading": "⚖️ నిర్ణయ పోలిక: బయోలాజికల్ వాడితే ఏమవుతుంది మరియు వాడకపోతే ఏమవుతుంది?",
        "tab2_caption": "ఒకే వాతావరణం మరియు నేలలో ఆశించే దిగుబడి ఫలితాల శాస్త్రీయ అనుకరణ.",
        "cf_without_title": "❌ జోక్యం లేకుండా (ఏమీ చేయకపోతే)",
        "cf_with_title": "✅ సింజెంటా బయోలాజికల్ తో (ఈరోజే వాడితే)",
        "cf_exp_yield": "ఆశించే దిగుబడి: {yield_val} {unit}",
        "cf_exp_revenue": "ఆశించే మొత్తం ఆదాయం: ₹{rev} / ఎకరం",
        "cf_vulnerable": "⚠️ పొలం తీవ్రమైన ఎండ ఒత్తిడికి ({days} రోజులు >38°C) గురయ్యే ప్రమాదం ఉంది.",
        "cf_boost_tag": "(+{boost} అదనపు దిగుబడి)",
        "cf_investment_profit": "మందు ఖర్చు: ₹{cost} | నికర లాభం: +₹{profit} / ఎకరం",

        # Tab 3: Disease & NPK & LeafVision
        "tab3_heading": "⚡ రియల్-టైమ్ ఫీల్డ్ ఇంటెలిజెన్స్: తెగుళ్ల ప్రమాదం మరియు స్మార్ట్ NPK సలహాదారు",
        "dis_warning_title": "🩺 తెగుళ్ల ప్రమాదం & బయో-కంట్రోల్ హెచ్చరిక",
        "dis_high_risk": "⚠️ **అధిక తెగుళ్ల ప్రమాద సూచిక ({risk}%)**: అధిక తేమ గుర్తించబడింది. {crop} లో శిలీంధ్ర తెగులు వచ్చే అవకాశం ఉంది.",
        "dis_high_rec": "💡 **సింజెంటా సలహా:** 5 రోజుల్లోపు **సింజెంటా Quantis / బయోస్టిమ్యులెంట్** + బయో-ఫంగిసైడ్ పిచికారీ చేయండి.",
        "dis_low_risk": "✅ **తక్కువ తెగుళ్ల ప్రమాదం ({risk}%)**: పంట ఆకులు ఆరోగ్యంగా ఉన్నాయి మరియు క్లోరోఫిల్ సరైన స్థాయిలో ఉంది.",
        "npk_title": "🧪 స్మార్ట్ NPK నేల ఆరోగ్య సలహాదారు",
        "npk_baseline": "ప్రస్తుత నేల పోషకాలు:",
        "npk_deficit": "కావాల్సిన అదనపు మోతాదు:",
        "npk_caption": "🌱 **పునరుత్పత్తి నేల సమతుల్యత:** సింజెంటా బయోస్టిమ్యులెంట్‌తో కలిపి వాడినప్పుడు యూరియాను 15% తగ్గించవచ్చు.",
        "lv_heading": "🍃 లీఫ్-విజన్ ఎడ్జ్ డయాగ్నోస్టిక్స్ (LABA-SNU ఫౌండేషన్ మోడల్)",
        "lv_caption": "5,40,000+ ఆకులపై శిక్షణ పొందిన విజన్ మోడల్. ఇంటర్నెట్ అవసరం లేకుండా మీ పరికరంలోనే తక్షణ రోగ నిర్ధారణ.",
        "lv_uploader": "పొలంలోని ఆకు ఫోటో అప్‌లోడ్ చేయండి లేదా తీయండి",
        "lv_sample_caption": "పొలం ఆకు నమూనా: {crop}",
        "lv_analyzing": "లీఫ్-విజన్ ఆకు తెగుళ్ల లక్షణాలను విశ్లేషిస్తోంది...",
        "lv_pathology": "వ్యాధి నిర్ధారణ: {diag}",
        "lv_pathogen": "తెగులు కారకం:",
        "lv_confidence": "ఖచ్చితత్వం: {conf}% | వేగం: {lat}ms",
        "lv_symptoms": "గమనించిన లక్షణాలు:",
        "lv_prescription": "🔬 సింజెంటా బయోలాజికల్ పరిష్కారం:",
        "lv_loss_prevention": "🛡️ {loss}% వరకు పంట నష్టాన్ని నివారిస్తుంది (~{amt} క్వింటాల్/ఎకరం)",
        "lv_error": "లీఫ్-విజన్ విశ్లేషణ గమనిక: {msg}",

        # Tab 4: Farm Memory
        "tab4_heading": "📖 నా పొలం జ్ఞాపకాలు (సీజన్ జర్నల్)",
        "tab4_caption": "సుపాబేస్ పోస్ట్‌గ్రేస్ క్లౌడ్ డేటాబేస్ ఆధారితం — మీ పొలం చరిత్ర సీజన్ల వారీగా భద్రపరచబడుతుంది.",
        "mem_field_name": "పంట మరియు పొలం పేరు",
        "mem_product": "వాడిన ఉత్పత్తి",
        "mem_dosage": "వాడిన మోతాదు (లీటరు/ఎకరం)",
        "mem_observed_yield": "వచ్చిన అసలు దిగుబడి (క్వింటాల్/ఎకరం)",
        "mem_notes": "రైతు సొంత అనుభవాలు / నోట్స్",
        "mem_notes_default": "పూత ప్రారంభ దశలో పిచికారీ చేశాము. వేర్ల పెరుగుదల చాలా బాగుంది.",
        "mem_save_btn": "📝 సుపాబేస్ ఫార్మ్ మెమరీలో సేవ్ చేయండి",
        "mem_save_success_remote": "✅ సుపాబేస్ క్లౌడ్ డేటాబేస్‌లో విజయవంతంగా నమోదు చేయబడింది!",
        "mem_save_success_local": "✅ స్థానిక ఫార్మ్ మెమరీలో నమోదు చేయబడింది!",
        "mem_history_title": "📜 మునుపటి సీజన్ రికార్డులు",
        "mem_actual_yield": "అసలు దిగుబడి:",
        "mem_net_profit": "నికర లాభం:",

        # Tab 5: Outcome & Attribution
        "tab5_heading": "📊 స్పష్టమైన ఫలితం కేటాయింపు: నా పంట దిగుబడిలో దేని వాటా ఎంత?",
        "attr_breakdown_title": "దిగుబడి కారణాల పూర్తి విశ్లేషణ",
        "attr_baseline": "సహజ దిగుబడి (బయోలాజికల్ లేకుండా)",
        "attr_weather": "వర్షపాతం & వాతావరణ ప్రభావం (ఎండ/నీటి ఒత్తిడి రక్షణ)",
        "attr_soil": "నేల సేంద్రీయ నాణ్యత (కర్బనం & పోషకాలు)",
        "attr_bio": "సింజెంటా బయోలాజికల్ ఉత్పత్తి వల్ల అదనపు పెరుగుదల",
        "attr_summary_title": "ఆర్థిక లాభం సారాంశం",
        "attr_cost": "ఉత్పత్తి పెట్టుబడి ఖర్చు",
        "attr_profit": "రైతుకు నికర లాభం",
        "attr_roi": "పెట్టుబడిపై రాబడి (ROI)",
        "download_pdf_btn": "📥 A4 PDF నివేదిక డౌన్‌లోడ్ చేసుకోండి",
        "share_wa_btn": "📲 WhatsApp లో నివేదిక పంపండి",
        "wa_template_header": "🌾 *సింజెంటా బయోలాజికల్స్ - పొలం ROI నివేదిక* 🌾",
        "wa_total_yield": "📈 *మొత్తం దిగుబడి:*",
        "wa_bio_boost": "🚀 *బయోలాజికల్ అదనపు దిగుబడి:*",
        "wa_net_profit": "💰 *నికర లాభం:*",
        "wa_roi": "🔥 *రైతు ROI:*",
        "wa_tagline": "✨ *చూస్తేనే నమ్ముతారు!*",

        # Tab 6: Conversational AI
        "tab6_heading": "💬 అగ్రి-అట్రిబ్యూట్ AI ని అడగండి (Google Gemini 2.5 Flash ఆధారితం)",
        "tab6_caption": "మీ భాష {lang} లో రూపొందించబడిన డిజిటల్ వ్యవసాయ సహాయకుడు. సమయం, వాతావరణం లేదా ఉత్పత్తుల గురించి అడగండి.",
        "ai_input_label": "మీ పొలం గురించి ఏదైనా ప్రశ్న అడగండి:",
        "ai_input_default": "{days} తీవ్రమైన ఎండ రోజులలో {crop} కొరకు {product} వాడటం వల్ల కలిగే ప్రయోజనం ఏమిటి?",
        "ai_ask_btn": "🤖 జెమిని AI ని అడగండి",
        "ai_connecting": "Google Gemini 2.5 Flash తో కనెక్ట్ అవుతోంది...",
        "ai_response_title": "🤖 అగ్రి-అట్రిబ్యూట్ AI (జెమిని 2.5 ఫ్లాష్ సమాధానం):",

        # Tab 7: Agronomist Studio
        "tab7_heading": "⚙️ వ్యవసాయ శాస్త్రవేత్త & మోడల్ డయాగ్నోస్టిక్స్ స్టూడియో",
        "ag_r2": "XGBoost R² ఖచ్చితత్వం",
        "ag_rmse": "RMSE లోపం",
        "ag_mae": "MAE లోపం",
        "ag_samples": "ఫీల్డ్ నమూనాలు",
        "chart_title": "📈 పంట పెరుగుదల పథం మరియు బయోలాజికల్ వ్యత్యాసం",
        "chart_xaxis": "విత్తిన తర్వాత రోజులు",
        "chart_yaxis": "దిగుబడి సామర్థ్యం (క్వింటాల్/ఎకరం)",
        "chart_control": "మందు వాడని పొలం (కంట్రోల్)",
        "chart_bio": "సింజెంటా బయో వాడిన పొలం",
        "chart_annotation": "'ప్రత్యక్ష రుజువు' అదనపు దిగుబడి",

        # Common Units
        "yield_unit": "క్వింటాల్/ఎకరం",
        "currency": "₹"
    }
}

# Crop Name Localizations
CROP_TRANSLATIONS = {
    "Rice (Paddy)": {
        "en": "Rice (Paddy)",
        "hi": "चावल (धान)",
        "mr": "भात (धान)",
        "te": "వరి (ధాన్యం)"
    },
    "Wheat": {
        "en": "Wheat",
        "hi": "गेहूं",
        "mr": "गहू",
        "te": "గోధుమ"
    },
    "Cotton": {
        "en": "Cotton",
        "hi": "कपास",
        "mr": "कापूस",
        "te": "పత్తి"
    },
    "Sugarcane": {
        "en": "Sugarcane",
        "hi": "गन्ना",
        "mr": "ऊस",
        "te": "చెరకు"
    },
    "Maize": {
        "en": "Maize",
        "hi": "मक्का",
        "mr": "मका",
        "te": "మొక్కజొన్న"
    },
    "Soybean": {
        "en": "Soybean",
        "hi": "सोयाबीन",
        "mr": "सोयाबीन",
        "te": "సోయాబీన్"
    },
    "Groundnut (Peanut)": {
        "en": "Groundnut (Peanut)",
        "hi": "मूंगफली",
        "mr": "भुईमूग",
        "te": "వేరుశెనగ"
    },
    "Mustard / Rapeseed": {
        "en": "Mustard / Rapeseed",
        "hi": "सरसों / राई",
        "mr": "मोहरी",
        "te": "ఆవాలు"
    },
    "Gram / Chickpea (Chana)": {
        "en": "Gram / Chickpea (Chana)",
        "hi": "चना",
        "mr": "हरभरा (चना)",
        "te": "శనగలు"
    },
    "Tur / Pigeon Pea (Arhar)": {
        "en": "Tur / Pigeon Pea (Arhar)",
        "hi": "अरहर (तुअर)",
        "mr": "तूर (अरहर)",
        "te": "కందులు"
    },
    "Onion": {
        "en": "Onion",
        "hi": "प्याज",
        "mr": "कांदा",
        "te": "ఉల్లిపాయ"
    },
    "Tomato": {
        "en": "Tomato",
        "hi": "टमाटर",
        "mr": "टोमॅटो",
        "te": "టమోటా"
    }
}

# Agro-Climatic Region Localizations
REGION_TRANSLATIONS = {
    "Punjab & Haryana (Indo-Gangetic)": {
        "en": "Punjab & Haryana (Indo-Gangetic)",
        "hi": "पंजाब और हरियाणा (सिंधु-गंगा मैदान)",
        "mr": "पंजाब आणि हरियाणा (सिंधू-गंगा खोरे)",
        "te": "పంజాబ్ & హర్యానా (సింధు-గంగా మైదానం)"
    },
    "Maharashtra & Vidarbha (Deccan)": {
        "en": "Maharashtra & Vidarbha (Deccan)",
        "hi": "महाराष्ट्र और विदर्भ (दक्कन का पठार)",
        "mr": "महाराष्ट्र आणि विदर्भ (दख्खनचे पठार)",
        "te": "మహారాష్ట్ర & విదర్భ (దక్కన్ పీఠభూమి)"
    },
    "Andhra Pradesh & Telangana": {
        "en": "Andhra Pradesh & Telangana",
        "hi": "आंध्र प्रदेश और तेलंगाना",
        "mr": "आंध्र प्रदेश आणि तेलंगणा",
        "te": "ఆంధ్రప్రదేశ్ & తెలంగాణ"
    },
    "Uttar Pradesh & Bihar": {
        "en": "Uttar Pradesh & Bihar",
        "hi": "उत्तर प्रदेश और बिहार",
        "mr": "उत्तर प्रदेश आणि बिहार",
        "te": "ఉత్తరప్రదేశ్ & బీహార్"
    },
    "Karnataka & Tamil Nadu": {
        "en": "Karnataka & Tamil Nadu",
        "hi": "कर्नाटक और तमिलनाडु",
        "mr": "कर्नाटक आणि तामिळनाडू",
        "te": "కర్ణాటక & తమిళనాడు"
    }
}

# Crop Season Translations
SEASON_TRANSLATIONS = {
    "Kharif Season": {
        "en": "Kharif Season",
        "hi": "खरीफ मौसम",
        "mr": "खरीप हंगाम",
        "te": "ఖరీఫ్ సీజన్"
    },
    "Rabi Season": {
        "en": "Rabi Season",
        "hi": "रबी मौसम",
        "mr": "रब्బీ हंगाम",
        "te": "రబీ సీజన్"
    },
    "Annual Crop": {
        "en": "Annual Crop",
        "hi": "वार्षिक फसल",
        "mr": "वार्षिक पीक",
        "te": "వార్షిక పంట"
    },
    "Kharif/Rabi": {
        "en": "Kharif/Rabi",
        "hi": "खरीफ / रबी",
        "mr": "खरीप / रब्बी",
        "te": "ఖరీఫ్ / రబీ"
    },
    "Rabi/Kharif": {
        "en": "Rabi/Kharif",
        "hi": "रबी / खरीफ",
        "mr": "रब्बी / खरीप",
        "te": "రబీ / ఖరీఫ్"
    },
    "Kharif/Zaid": {
        "en": "Kharif/Zaid",
        "hi": "खरीफ / ज़ायद",
        "mr": "खरीप / झैद",
        "te": "ఖరీఫ్ / జైద్"
    }
}

# Crop Description Translations
CROP_DESC_TRANSLATIONS = {
    "Primary rainfed oilseed crop": {
        "en": "Primary rainfed oilseed crop",
        "hi": "मुख्य वर्षा-आधारित तिलहन फसल",
        "mr": "पावसावर अवलंबून असणारे मुख्य गळीत धान्य",
        "te": "ప్రధాన వర్షాధార నూనెగింజల పంట"
    },
    "Intercropped rainfed pulse": {
        "en": "Intercropped rainfed pulse",
        "hi": "अंतर्वर्ती वर्षा-आधारित दलहन",
        "mr": "आंतरपीक पावसावर आधारित कडधान्य",
        "te": "అంతరపంటగా వర్షాధార పప్పుదినుసు"
    },
    "Commercial bulb cash crop": {
        "en": "Commercial bulb cash crop",
        "hi": "व्यावसायिक कंद नकदी फसल",
        "mr": "व्यावसायिक कंदवर्गीय नगदी पीक",
        "te": "వాణిజ్య దుంప నగదు పంట"
    },
    "Dominant black cotton soil cash crop": {
        "en": "Dominant black cotton soil cash crop",
        "hi": "काली मिट्टी की प्रमुख नकदी फसल",
        "mr": "काळीच्या कसदार जमिनीतले मुख्य नगदी पीक",
        "te": "నల్లరేగడి నేలలో ప్రధాన వాణిజ్య పంట"
    },
    "Eastern Vidarbha wetland cultivation": {
        "en": "Eastern Vidarbha wetland cultivation",
        "hi": "पूर्वी विदर्भ की प्रमुख दलदली फसल",
        "mr": "पूर्व विदर्भातील भातशेतीचा मुख्य पट्टा",
        "te": "తూర్పు విదర్భ చిత్తడి నేలల ప్రధాన పంట"
    },
    "Western Maharashtra irrigated belt": {
        "en": "Western Maharashtra irrigated belt",
        "hi": "पश्चिमी महाराष्ट्र का सिंचित गन्ना क्षेत्र",
        "mr": "पश्चिम महाराष्ट्रातील बागायती पट्टा",
        "te": "పశ్చిమ మహారాష్ట్ర సాగునీటి ప్రాంతపు పంట"
    },
    "Major Rabi foodgrain staple": {
        "en": "Major Rabi foodgrain staple",
        "hi": "प्रमुख रबी खाद्यान्न फसल",
        "mr": "रब्बी हंगामातील मुख्य अन्नधान्य पीक",
        "te": "ప్రధాన రబీ ఆహార ధాన్య పంట"
    },
    "Major Kharif cereal staple": {
        "en": "Major Kharif cereal staple",
        "hi": "प्रमुख खरीफ अनाज फसल",
        "mr": "खरीप हंगामातील मुख्य अन्नधान्य",
        "te": "ప్రధాన ఖరీఫ్ ధాన్యపు పంట"
    },
    "Commercial cash crop rotation": {
        "en": "Commercial cash crop rotation",
        "hi": "व्यावसायिक नकदी फसल चक्र",
        "mr": "व्यावसायिक नगदी पीक फेरपालट",
        "te": "వాణిజ్య పంటల మార్పిడి సాగు"
    },
    "Diversification grain & feed crop": {
        "en": "Diversification grain & feed crop",
        "hi": "फसल विविधीकरण व पशु आहार फसल",
        "mr": "पीक फेरपालट आणि चारा पीक",
        "te": "పంటల మార్పిడి మరియు దాణా పంట"
    },
    "Irrigated agro-industrial staple": {
        "en": "Irrigated agro-industrial staple",
        "hi": "सिंचित कृषि-औद्योगिक फसल",
        "mr": "बागायती कृषी-औद्योगिक पीक",
        "te": "సాగునీటి ఆధారిత వ్యవసాయ-పారిశ్రామిక పంట"
    },
    "High acreage monsoon staple": {
        "en": "High acreage monsoon staple",
        "hi": "विशाल रकबे वाली मुख्य मानसूनी फसल",
        "mr": "मोठ्या क्षेत्रावरील मुख्य मान्सून पीक",
        "te": "అత్యధిక విస్తీర్ణంలో సాగయ్యే ప్రధాన పంట"
    },
    "Black soil commercial cash crop": {
        "en": "Black soil commercial cash crop",
        "hi": "काली मिट्टी की व्यावसायिक नकदी फसल",
        "mr": "काळीच्या जमिनीतील व्यावसायिक नगदी पीक",
        "te": "నల్లరేగడి నేలల వాణిజ్య పంట"
    },
    "Commercial feed & industrial crop": {
        "en": "Commercial feed & industrial crop",
        "hi": "व्यावसायिक पशु आहार व औद्योगिक फसल",
        "mr": "औद्योगिक आणि पशुखाद्य पीक",
        "te": "వాణిజ్య దాణా మరియు పారిశ్రామిక పంట"
    },
    "Key agro-industrial cash crop": {
        "en": "Key agro-industrial cash crop",
        "hi": "प्रमुख कृषि-औद्योगिक नकदी फसल",
        "mr": "महत्त्वाचे कृषी-औद्योगिक नगदी पीक",
        "te": "కీలక వ్యవసాయ-పారిశ్రామిక వాణిజ్య పంట"
    },
    "Monsoon basin food staple": {
        "en": "Monsoon basin food staple",
        "hi": "नदी घाटी का प्रमुख मानसूनी भोजन",
        "mr": "नदी खोऱ्यातील मुख्य मान्सून पीक",
        "te": "నదీ పరీవాహక ప్రధాన ఆహార పంట"
    },
    "Eastern UP & North Bihar specialty": {
        "en": "Eastern UP & North Bihar specialty",
        "hi": "पूर्वी उप्र व उत्तर बिहार की विशेषता",
        "mr": "पूर्व युपी व उत्तर बिहारचे विशेष पीक",
        "te": "తూర్పు యూపీ & ఉత్తర బీహార్ ప్రత్యేక పంట"
    },
    "River basin irrigated cash crop": {
        "en": "River basin irrigated cash crop",
        "hi": "नदी घाटी सिंचित नकदी फसल",
        "mr": "नदी खोऱ्यातील बागायती नगदी पीक",
        "te": "నదీ పరీవాహక సాగునీటి వాణిజ్య పంట"
    },
    "Cauvery & Tungabhadra basin staple": {
        "en": "Cauvery & Tungabhadra basin staple",
        "hi": "कावेरी व तुंगभद्रा घाटी की प्रमुख फसल",
        "mr": "कावेरी व तुंगभद्रा खोऱ्यातील मुख्य पीक",
        "te": "కావేరి & తుంగభద్ర పరివాహక ప్రధాన పంట"
    },
    "Dryland commercial grain production": {
        "en": "Dryland commercial grain production",
        "hi": "शुष्क भूमि व्यावसायिक अनाज उत्पादन",
        "mr": "कोरडवाहू व्यावसायिक धान्य उत्पादन",
        "te": "మెట్టభూమి వాణిజ్య ధాన్యపు సాగు"
    },
    "Southern black cotton soil belt": {
        "en": "Southern black cotton soil belt",
        "hi": "दक्षिण भारत का काली मिट्टी कपास क्षेत्र",
        "mr": "दक्षिण भारतातील काळ्या मातीचा पट्टा",
        "te": "దక్షిణ నల్లరేగడి పత్తి సాగు ప్రాంతం"
    }
}

# Weather Description Localizations
WEATHER_DESC_TRANSLATIONS = {
    "clear sky": {"en": "Clear Sky", "hi": "साफ आसमान", "mr": "निरभ्र आकाश", "te": "స్వచ్ఛమైన ఆకాశం"},
    "few clouds": {"en": "Few Clouds", "hi": "हल्के बादल", "mr": "अंशतः ढगाळ", "te": "తేలికపాటి మేఘాలు"},
    "scattered clouds": {"en": "Scattered Clouds", "hi": "बिखरे बादल", "mr": "विखुरलेले ढग", "te": "చెదురుమదురు మేఘాలు"},
    "broken clouds": {"en": "Broken Clouds", "hi": "बादल छाए रहेंगे", "mr": "ढगाळ वातावरण", "te": "దట్టమైన మేఘాలు"},
    "overcast clouds": {"en": "Overcast", "hi": "घने बादल", "mr": "पूर्ण ढगाळ", "te": "పూర్తిగా మేఘావృతం"},
    "light rain": {"en": "Light Rain", "hi": "हल्की बारिश", "mr": "हलका पाऊस", "te": "తేలికపాటి వర్షం"},
    "moderate rain": {"en": "Moderate Rain", "hi": "मध्यम वर्षा", "mr": "मध्यम पाऊस", "te": "మోస్తరు వర్షం"},
    "heavy rain": {"en": "Heavy Rain", "hi": "भारी बारिश", "mr": "मुसळधार पाऊस", "te": "భారీ వర్షం"},
    "thunderstorm": {"en": "Thunderstorm", "hi": "गरज के साथ बारिश", "mr": "वादळी पाऊस", "te": "ఉరుములతో కూడిన వర్షం"},
    "drizzle": {"en": "Drizzle", "hi": "बूंदाबांदी", "mr": "रिमझिम पाऊस", "te": "చిరుజల్లులు"},
    "haze": {"en": "Haze", "hi": "धुंध", "mr": "धुकट वातावरण", "te": "పొగమంచు"}
}


# 24 Official Agmarknet 2.0 Commodity Multilingual Mappings
COMMODITY_TRANSLATIONS = {
    "Bajra(Pearl Millet/Cumbu)": {"en": "Bajra (Pearl Millet)", "hi": "बाजरा", "mr": "बाजरी", "te": "సజ్జలు"},
    "Barley(Jau)": {"en": "Barley (Jau)", "hi": "जौ", "mr": "जव", "te": "యావలు"},
    "Jowar(Sorghum)": {"en": "Jowar (Sorghum)", "hi": "ज्वार", "mr": "ज्वारी", "te": "జొన్నలు"},
    "Maize": {"en": "Maize (Corn)", "hi": "मक्का", "mr": "मका", "te": "మొక్కజొన్న"},
    "Paddy(Common)": {"en": "Paddy (Rice)", "hi": "चावल (धान)", "mr": "भात (धान)", "te": "వరి (ధాన్యం)"},
    "Ragi(Finger Millet)": {"en": "Ragi (Finger Millet)", "hi": "रागी (मडुआ)", "mr": "नाचणी (रागी)", "te": "రాగులు"},
    "Wheat": {"en": "Wheat", "hi": "गेहूं", "mr": "गहू", "te": "గోధుమలు"},
    "Cotton": {"en": "Cotton", "hi": "कपास", "mr": "कापूस", "te": "పత్తి"},
    "Copra": {"en": "Copra (Dry Coconut)", "hi": "खोपरा (सूखा नारियल)", "mr": "खोबरं (कोपरा)", "te": "కొబ్బరి (కొప్రా)"},
    "Groundnut": {"en": "Groundnut (Peanut)", "hi": "मूंगफली", "mr": "भुईमूग", "te": "వేరుశెనగ"},
    "Mustard": {"en": "Mustard (Sarson)", "hi": "सरसों / राई", "mr": "मोहरी", "te": "ఆవాలు"},
    "Safflower": {"en": "Safflower (Kardi)", "hi": "कुसुम (करड़ी)", "mr": "करडई", "te": "కుసుమలు"},
    "Sesamum(Sesame,Gingelly,Til)": {"en": "Sesame (Til)", "hi": "तिल", "mr": "तीळ", "te": "నువ్వులు"},
    "Soyabean": {"en": "Soybean", "hi": "सोयाबीन", "mr": "सोयाबीन", "te": "సోయాబీన్"},
    "Sunflower/Sunflower Seed": {"en": "Sunflower", "hi": "सूरजमुखी", "mr": "सूर्यफूल", "te": "పొద్దుతిరుగుడు"},
    "Sugarcane": {"en": "Sugarcane", "hi": "गन्ना", "mr": "ऊस", "te": "చెరకు"},
    "Bengal Gram(Gram)(Whole)": {"en": "Bengal Gram (Chana)", "hi": "चना (साबुत)", "mr": "हरभरा (चना)", "te": "శనగలు"},
    "Black Gram(Urd Beans)(Whole)": {"en": "Black Gram (Urad)", "hi": "उड़द (साबुत)", "mr": "उडीद", "te": "మినుములు"},
    "Green Gram(Moong)(Whole)": {"en": "Green Gram (Moong)", "hi": "मूंग (साबुत)", "mr": "मूग", "te": "పెసలు"},
    "Lentil(Masur)(Whole)": {"en": "Lentil (Masur)", "hi": "मसूर (साबुत)", "mr": "मसूर", "te": "మసూర్ పప్పు"},
    "Red gram/Arhar/Tur(whole)": {"en": "Red Gram (Tur/Arhar)", "hi": "अरहर (तुअर)", "mr": "तूर (अरहर)", "te": "కందులు"},
    "Onion": {"en": "Onion", "hi": "प्याज", "mr": "कांदा", "te": "ఉల్లిపాయ"},
    "Potato": {"en": "Potato", "hi": "आलू", "mr": "बटाटा", "te": "బంగాళాదుంప"},
    "Tomato": {"en": "Tomato", "hi": "टमाटर", "mr": "टोमॅटो", "te": "టమోటా"}
}

def t_commodity(name: str, lang: str = "English") -> str:
    """Translates any Agmarknet commodity name into the active language."""
    code = get_lang_code(lang)
    for k, v in COMMODITY_TRANSLATIONS.items():
        if k.lower() in name.lower() or name.lower() in k.lower():
            return v.get(code, v.get("en", name))
    return name

def get_lang_code(lang_str: str) -> str:
    """Resolves language string to short code 'en', 'hi', 'mr', or 'te'."""
    return LANG_MAP.get(lang_str, "en")

def t(key: str, lang: str = "English", **kwargs) -> str:
    """
    Centralized translation function.
    Returns localized string for the specified key and language.
    Falls back gracefully to English if key is not found.
    Performs safe string formatting with kwargs.
    """
    code = get_lang_code(lang)
    lang_dict = TRANSLATIONS.get(code, TRANSLATIONS["en"])
    text = lang_dict.get(key, TRANSLATIONS["en"].get(key, key))
    
    format_kwargs = dict(kwargs)
    if "lang" not in format_kwargs:
        format_kwargs["lang"] = lang
        
    try:
        return text.format(**format_kwargs)
    except Exception:
        return text

def t_crop(crop_name: str, lang: str = "English") -> str:
    """Translates crop name to selected language, supporting all 24 Indian commodities."""
    code = get_lang_code(lang)
    if crop_name in CROP_TRANSLATIONS:
        return CROP_TRANSLATIONS[crop_name].get(code, crop_name)
    return t_commodity(crop_name, lang)

def t_region(region_name: str, lang: str = "English") -> str:
    """Translates agro-climatic region name to selected language."""
    code = get_lang_code(lang)
    return REGION_TRANSLATIONS.get(region_name, {}).get(code, region_name)

def t_season(season_name: str, lang: str = "English") -> str:
    """Translates season name."""
    code = get_lang_code(lang)
    return SEASON_TRANSLATIONS.get(season_name, {}).get(code, season_name)

def t_crop_desc(desc: str, lang: str = "English") -> str:
    """Translates crop agronomic description."""
    code = get_lang_code(lang)
    return CROP_DESC_TRANSLATIONS.get(desc, {}).get(code, desc)

def t_weather_desc(desc: str, lang: str = "English") -> str:
    """Translates live weather description."""
    code = get_lang_code(lang)
    desc_clean = str(desc).strip().lower()
    for k, v in WEATHER_DESC_TRANSLATIONS.items():
        if k in desc_clean:
            return v.get(code, desc)
    return desc
