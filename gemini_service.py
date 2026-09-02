"""
gemini_service.py - Google Gemini 2.5 Flash Multimodal AI Engine
PS-04 Reach Layer & Leaf Doctor Diagnostic for Syngenta Biologicals (Team 15 - Hack Core 2026)
"""

import os
import requests
import json
import base64
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

AGRI_SYSTEM_PROMPT = """
You are AgriAttribute AI, an expert agricultural AI assistant powered by Google Gemini and trained for Syngenta Biologicals & Indian agriculture.
Your role:
1. Answer farmer queries conversationally in the user's selected native language (English, Hindi, Marathi, Telugu, Punjabi, Gujarati, Kannada, Tamil, Bengali, Odia).
2. Provide clear, empathetic, practical advice on biological product application timing, stress mitigation (heat waves, dry spells), and soil health.
3. Recommend Syngenta Biological products (Quantis, Isabion, CropBio+) when relevant, explaining their ROI and stress-buffering benefits.
4. Keep answers concise, actionable, and formatted with bullet points and friendly emojis.
"""

def ask_gemini_agri_assistant(user_query: str, language: str = "English", context_info: dict = None) -> dict:
    """
    Queries Google Gemini 2.5 Flash API with agricultural context and language preferences.
    """
    context_str = ""
    if context_info:
        context_str = f"\n[Current Field Context: Region: {context_info.get('region')}, Crop: {context_info.get('crop')}, Product Applied: {context_info.get('product')}, Heat Stress Days: {context_info.get('heat_stress')}, Predicted Yield: {context_info.get('predicted_yield')} q/acre]"

    full_prompt = f"{AGRI_SYSTEM_PROMPT}\n{context_str}\n[Target Language: {language}]\nFarmer Question: {user_query}\n\nAgriAttribute AI Response:"

    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 600
        }
    }
    headers = {"Content-Type": "application/json"}

    try:
        res = requests.post(GEMINI_ENDPOINT, json=payload, headers=headers, timeout=8)
        if res.status_code == 200:
            data = res.json()
            reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            return {
                "status": "Success (Live Gemini 2.5 Flash)",
                "response": reply.strip(),
                "language": language
            }
        else:
            return {
                "status": f"HTTP {res.status_code}",
                "response": f"Gemini API Notice: Received response code {res.status_code}.",
                "language": language
            }
    except Exception as e:
        return {
            "status": f"Error: {e}",
            "response": f"Namaste! For your crop in this season, applying Syngenta Biologicals (Quantis/Isabion) during early stress windows boosts root depth and preserves flower retention.",
            "language": language
        }

def diagnose_crop_disease_image(image_bytes: bytes, mime_type: str = "image/jpeg", crop_name: str = "Crop", language: str = "English") -> dict:
    """
    Analyzes an uploaded leaf photo using Gemini 2.5 Flash Multimodal Vision API.
    Diagnoses crop diseases, pest symptoms, and recommends Syngenta biological treatments.
    """
    try:
        b64_data = base64.b64encode(image_bytes).decode('utf-8')
        prompt = f"""
You are an expert plant pathologist and agronomist for Syngenta Biologicals in India.
A farmer has uploaded a leaf / plant photo of {crop_name}.
Please:
1. Identify any visible symptoms (fungal spots, blast, blight, rust, leaf scorch, or pest stress).
2. Give a clear, practical diagnosis in {language}.
3. Recommend immediate treatment steps and explain how Syngenta biologicals (e.g., Quantis for heat/drought stress, Isabion for amino acid vigor, or bio-fungicides) can help revive crop health.
Keep it empathetic, clear, and actionable in bullet points with friendly emojis.
"""
        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": mime_type, "data": b64_data}}
                ]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 800
            }
        }
        headers = {"Content-Type": "application/json"}
        res = requests.post(GEMINI_ENDPOINT, json=payload, headers=headers, timeout=12)
        if res.status_code == 200:
            data = res.json()
            reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            return {
                "status": "Success (Gemini 2.5 Flash Vision)",
                "diagnosis": reply.strip(),
                "language": language
            }
        else:
            return {
                "status": f"HTTP {res.status_code}",
                "diagnosis": f"Notice: Leaf analysis service returned status {res.status_code}.",
                "language": language
            }
    except Exception as e:
        return {
            "status": f"Error: {e}",
            "diagnosis": "Unable to process image. Please ensure image is a clear close-up of the crop leaf.",
            "language": language
        }

if __name__ == "__main__":
    print("Testing Gemini 2.5 Flash Service...")
    res = ask_gemini_agri_assistant("When should I apply Quantis on Paddy in Vidarbha?", "English")
    print("Status:", res['status'])
    print("Response Length:", len(res['response']))
