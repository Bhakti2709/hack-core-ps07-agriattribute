@echo off
title AgriAttribute AI - Live Presentation Launcher
color 0A
cd /d "%~dp0"
echo Starting Streamlit Engine...
start "Streamlit Engine" python -m streamlit run app.py --server.port 8505
start "Public Tunnel" python scratch/tunnel_keeper.py
echo Local address: http://localhost:8505
pause
