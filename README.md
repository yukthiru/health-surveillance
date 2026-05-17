# health-surveillance
Predictive Public Health Surveillance System

---
What it does
An AI-powered dashboard that monitors disease outbreaks across 10 Indian districts in real time, predicts risk levels, and generates health advisories automatically.
---
Tech Stack
Backend — Python, Flask, Pandas
Frontend — HTML, CSS, JavaScript, Leaflet.js
AI/ML — Prophet (time-series forecasting)
---
How to Run
```bash
# Install libraries
pip install flask pandas flask-cors prophet

# Generate data
py generate\_data.py

# Start server
cd backend
py app.py

# Open frontend/index.html in browser
```
---
Features
🗺️ Interactive India map with color-coded risk levels
🔴 Critical / 🟠 High / 🟡 Medium / 🟢 Low risk per district
🤖 AI-generated health advisories on click
📊 Tracks Dengue, Malaria, Cholera across 10 cities
---
SDG Goal 3 — Good Health and Well-Being
