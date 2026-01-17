# AI Crop Disease Detection System - STQA Project

This repository contains the comprehensive Software Testing and Quality Assurance (STQA) documentation and artifacts for the AI Crop Disease Detection System.

## 🚀 Project Overview
The system integrates a Flutter mobile app, ESP32 IoT sensors, and a Flask backend to identify 38 crop diseases with 96.7% accuracy using CNN models. It also features a Google Gemini-powered AI chatbot for agricultural guidance.

**Live API Server:** [https://ai-crop-disease-detection.onrender.com](https://ai-crop-disease-detection.onrender.com)

## 📂 Project Structure

- **Backend/**: Contains `main.py` which is the Flask server handling ML inference, IoT data, and chatbot integration.
- **Automation_Testing/**: Contains `test_web.py`, a suite of 11 Playwright automation scripts for End-to-End testing.
- **API_Testing/**: Contains the Postman collection and environment files for testing 10 core API endpoints.
- **Manual_Testing/**: Contains the PDF report detailing 25 manual test cases and their execution results.
- **Report/**: Contains the LaTeX source code (`report.tex`) and visual evidence (API screenshots) for the final project report.

## 🛠️ Technology Stack
- **Frontend**: Flutter 3.16
- **Backend**: Python 3.10, Flask 3.0
- **IoT**: ESP32, DHT11, Soil Moisture Sensors
- **ML/AI**: TensorFlow 2.14, Google Gemini Pro 1.5
- **Testing**: Playwright, Postman, Jira, pytest

## 📊 Quality Metrics
- **Test Pass Rate**: 100% (46/46 cases)
- **API Reliability**: 100%
- **System Uptime**: 99.9%
- **Avg API Response**: 247ms
- **Defects Fixed**: 62.5% (5/8 tracked)

## 📝 Contributors
- **Muhammad Taha**: Manual Testing
- **Maher Sachal**: API & Automation Testing
- **Fasi ul Din**: Defect Tracking
- **Muhammad Asif**: QA Documentation

---
*Submitted for the STQA course at University of Layyah.*
