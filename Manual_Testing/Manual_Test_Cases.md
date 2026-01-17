# 📊 Manual Test Execution Report
### AI Crop Disease Detection System | STQA Project

---

## 📝 Execution Summary
| Metric | Details |
| :--- | :--- |
| **Test Lead** | Muhammad Taha |
| **Project** | AI Corp Disease Detection |
| **Execution Date** | January 17, 2026 |
| **Total Test Cases** | 25 |
| **Passed** | 25 |
| **Failed** | 0 |
| **Pass Rate** | 100% |
| **Coverage** | 95% |

---

## 🏗️ Detailed Test Execution Matrix

| ID | Module | Scenario | Steps | Expected Result | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | **UI/UX** | Application Launch | Open app from icon | Splash screen → Dashboard | **PASSED** |
| **TC-02** | **IoT** | Sensor Data Display | Navigate to Sensors | Real-time Temp/Hum/Soil data | **PASSED** |
| **TC-03** | **IoT** | Manual Refresh | Click refresh icon | Force latest cloud data update | **PASSED** |
| **TC-04** | **Data** | Historical View | Open History tab | List of past 50 readings | **PASSED** |
| **TC-05** | **Core** | Camera Capture | Click camera button | Stable image preview window | **PASSED** |
| **TC-06** | **AI** | Disease Analysis | Upload leaf photo | Detected name + Confidence % | **PASSED** |
| **TC-07** | **AI** | Invalid Input | Upload non-leaf img | "Not a plant image" error | **PASSED** |
| **TC-08** | **System** | Performance | Upload 20MB file | Auto-handling / Error notice | **PASSED** |
| **TC-09** | **Data** | Predict History | View past analyses | List of identified diseases | **PASSED** |
| **TC-10** | **Chatbot** | English Support | Ask crop advice | AI response in English | **PASSED** |
| **TC-11** | **Chatbot** | Urdu Support | Ask in Urdu text | AI response in Urdu text | **PASSED** |
| **TC-12** | **Utils** | Text Translation | Use translate tool | EN text → Urdu conversion | **PASSED** |
| **TC-13** | **IoT** | ESP32-CAM Upload | Trigger capture | Image sync to Cloudinary | **PASSED** |
| **TC-14** | **IoT** | Remote Feed | View latest cam | Show most recent IoT photo | **PASSED** |
| **TC-15** | **API** | `/health` Check | Call backend API | Status 200 OK | **PASSED** |
| **TC-16** | **API** | `/status` Check | Call model status | Returns "Model Loaded" | **PASSED** |
| **TC-17** | **API** | Ping Latency | Request `/ping` | Fast response (<200ms) | **PASSED** |
| **TC-18** | **Core** | Offline Support | Toggle No Internet | Data served from local cache | **PASSED** |
| **TC-19** | **Cloud** | Firebase Sync | Update sensor node | Immediate Dashboard sync | **PASSED** |
| **TC-20** | **Alerts** | SMS Notification | Soil Moisture > 2800 | Receive emergency SMS alert | **PASSED** |
| **TC-21** | **Social** | WhatsApp Bot | Send "reading" | Auto-reply with sensor data | **PASSED** |
| **TC-22** | **i18n** | Language Toggle | Click EN/UR btn | Instant UI language swap | **PASSED** |
| **TC-23** | **Themes** | Dark Mode Sync | Toggle Dark Mode | Full UI theme color inversion | **PASSED** |
| **TC-24** | **IoT** | Serial Stream | Plug ESP32 via USB | Data stream to local console | **PASSED** |
| **TC-25** | **Backend** | Load Handling | 100 concurrent reqs | All requests handled safely | **PASSED** |

---

## 📈 Final Verdict
> **STATUS: APPROVED FOR PRODUCTION**
>
> Integrated testing across IoT, AI, and Manual workflows confirms the system is stable. All major navigation paths and core functionalities perform according to specifications with zero critical gaps identified during manual execution.

---
*Generated for the University of Layyah Department of CS | STQA Documentation*
