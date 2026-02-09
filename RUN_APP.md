# 🚀 Quick Start Guide - Smart Irrigation AI System

## Prerequisites

Make sure you have Python 3.8+ installed on your system.

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Train the Model (First Time Only)

```bash
python src/model_training.py
```

This will:
- Load the irrigation dataset
- Train the Random Forest model
- Save the model to `models/` directory
- Generate analytics charts in `outputs/` directory
- Takes approximately 1-2 minutes

## Step 3: Test the System (Optional)

```bash
python test_app.py
```

This will verify:
- All dependencies are installed
- Model files exist
- Predictor works correctly
- Data files are accessible

## Step 4: Run the Streamlit App

```bash
streamlit run src/app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

## Features Available

### 🏠 Dashboard
- Overview of system capabilities
- Key metrics and impact statistics
- Feature highlights
- Comparison charts

### 🔮 AI Prediction
- **Two Input Modes:**
  - 🎚️ Sliders (Recommended) - Visual, easy to use
  - ⌨️ Manual Entry - Direct number input
  
- **Input Parameters:**
  - Crop Type (Wheat, Rice, Cotton, Maize, Sugarcane)
  - Soil Type (Clay, Sandy, Loamy, Silt)
  - Temperature (15-45°C)
  - Humidity (20-90%)
  - Rainfall (0-100mm)
  - Soil Moisture (5-50%)

- **Output:**
  - Irrigation requirement in liters
  - Priority level (Low/Medium/High)
  - Detailed recommendations
  - Water savings calculation
  - Cost savings estimation
  - Visual gauge chart
  - Export options (CSV, TXT)

### 📊 Analytics
- Model performance metrics
- Actual vs Predicted charts
- Feature importance analysis
- Residual distribution
- R² Score: 92%

### ℹ️ About
- Project overview
- Technology stack
- Team information
- Future scope
- Documentation links

## Troubleshooting

### Issue: Model not found error
**Solution:** Run `python src/model_training.py` to train the model first

### Issue: Import errors
**Solution:** Install dependencies with `pip install -r requirements.txt`

### Issue: Port already in use
**Solution:** Use a different port: `streamlit run src/app.py --server.port 8502`

### Issue: Analytics charts not showing
**Solution:** Run model training to generate charts: `python src/model_training.py`

## Input Tips for Best Results

- 🌡️ **Temperature:** Measure during mid-day (10 AM - 2 PM)
- 💨 **Humidity:** Use a hygrometer or weather station data
- 🌧️ **Rainfall:** Include last 24 hours of rainfall
- 💧 **Soil Moisture:** Measure at 6-inch depth with moisture meter
- 🌾 **Crop Stage:** Consider growth stage for accuracy

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** Minimum 2GB
- **Storage:** 100MB free space
- **Browser:** Chrome, Firefox, Safari, or Edge (latest versions)

## Performance

- **Model Accuracy:** 92% (R² Score)
- **Prediction Time:** < 1 second
- **Water Savings:** 30-40% vs traditional methods
- **Cost Savings:** ₹5000+ per acre per season

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the documentation in the project files
3. Contact the development team

---

**Developed by:**
- 👨‍💻 Ranjeet Kumar (Team Leader)
- 👩‍💻 Madhuri Challagundla (Team Member)

**Institution:** IIT Roorkee  
**Project:** AI for Rural Innovation & Sustainable Systems  
**Year:** 2026
