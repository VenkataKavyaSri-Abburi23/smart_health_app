# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:12:43 2025

@author: abbur
"""

# stress_detector_app.py
import streamlit as st

st.set_page_config(page_title="Stress & Fatigue Detector", layout="centered")

st.title("🧠 Smart Stress & Fatigue Detection System")
st.write("This app estimates your stress level based on physiological indicators. Real-time smartwatch integration coming soon!")

st.header("📲 Input Your Vitals (simulated from smartwatch)")

# Simulated inputs – later these will be fetched from your smartwatch
heart_rate = st.number_input("💓 Heart Rate (bpm)", min_value=40, max_value=200, value=85)
breathing_rate = st.number_input("🌬️ Breathing Rate (breaths/min)", min_value=5, max_value=40, value=16)
sleep_hours = st.number_input("😴 Sleep Duration (last night in hours)", min_value=0.0, max_value=12.0, value=6.5)
steps = st.number_input("🚶 Steps Taken Today", min_value=0, max_value=30000, value=5000)
age = st.number_input("🎂 Age (optional)", min_value=10, max_value=100, value=25)

# Prediction logic
stress_level = ""
recommendation = ""

if st.button("🧠 Analyze Stress Level"):
    if heart_rate > 100 and sleep_hours < 5 and steps < 2000:
        stress_level = "🔴 High Stress"
        recommendation = "⚠️ Take a break, rest well tonight, and consider breathing exercises."
    elif heart_rate > 90 or sleep_hours < 6 or steps < 4000:
        stress_level = "🟠 Medium Stress"
        recommendation = "🧘‍♂️ You may be a bit fatigued. Try walking or meditating."
    else:
        stress_level = "🟢 Low Stress"
        recommendation = "✅ You seem well-rested. Keep up the good work!"

    st.subheader("🧪 Result")
    st.success(f"**Stress Level:** {stress_level}")
    st.info(recommendation)

# Future integration placeholder
st.markdown("---")
st.caption("📡 Real-time vitals from smartwatch (Google Fit API) will auto-fill these fields soon.")
