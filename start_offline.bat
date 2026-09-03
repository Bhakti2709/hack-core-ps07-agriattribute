@echo off
title AgriAttribute AI - Offline Mode
color 0B
cd /d "%~dp0"
python -m streamlit run app.py --server.port 8505
pause
