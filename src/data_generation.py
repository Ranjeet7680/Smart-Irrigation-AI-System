"""
Data Generation Script for Smart Irrigation System
Generates synthetic agricultural and weather data for ML training
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_irrigation_data(n_samples=2000):
    """
    Generate synthetic irrigation data with realistic patterns
    
    Parameters:
    n_samples (int): Number of data samples to generate
    
    Returns:
    pandas.DataFrame: Generated dataset
    """
    
    # Crop types
    crop_types = ['Wheat', 'Rice', 'Cotton', 'Maize', 'Sugarcane']
    
    # Soil types
    soil_types = ['Clay', 'Sandy', 'Loamy', 'Silt']
    
    # Generate date range
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(n_samples)]
    
    data = []
    
    for i in range(n_samples):
        # Random crop and soil type
        crop = np.random.choice(crop_types)
        soil = np.random.choice(soil_types)
        
        # Weather parameters (realistic ranges)
        temperature = np.random.uniform(15, 45)  # Celsius
        humidity = np.random.uniform(20, 90)  # Percentage
        rainfall = np.random.exponential(5)  # mm (exponential distribution for rainfall)
        rainfall = min(rainfall, 100)  # Cap at 100mm
        
        # Soil moisture (affected by soil type)
        soil_moisture_base = {
            'Clay': 35,
            'Sandy': 15,
            'Loamy': 25,
            'Silt': 30
        }
        soil_moisture = soil_moisture_base[soil] + np.random.uniform(-10, 10)
        
        # Crop water requirement (different for each crop)
        crop_water_req = {
            'Wheat': 25,
            'Rice': 45,
            'Cotton': 30,
            'Maize': 28,
            'Sugarcane': 50
        }
        base_water_req = crop_water_req[crop]
        
        # Calculate irrigation needed based on multiple factors
        # Formula considers: temperature, humidity, rainfall, soil moisture, crop type
        irrigation_needed = base_water_req
        
        # Temperature factor (higher temp = more water)
        if temperature > 35:
            irrigation_needed += 15
        elif temperature > 30:
            irrigation_needed += 10
        elif temperature > 25:
            irrigation_needed += 5
        
        # Humidity factor (lower humidity = more water)
        if humidity < 40:
            irrigation_needed += 10
        elif humidity > 70:
            irrigation_needed -= 5
        
        # Rainfall factor (recent rain = less irrigation)
        if rainfall > 20:
            irrigation_needed -= 20
        elif rainfall > 10:
            irrigation_needed -= 10
        elif rainfall > 5:
            irrigation_needed -= 5
        
        # Soil moisture factor
        if soil_moisture < 20:
            irrigation_needed += 15
        elif soil_moisture > 40:
            irrigation_needed -= 10
        
        # Ensure non-negative
        irrigation_needed = max(0, irrigation_needed)
        
        # Add some random variation
        irrigation_needed += np.random.uniform(-3, 3)
        irrigation_needed = max(0, irrigation_needed)
        
        # Create data point
        data.append({
            'Date': dates[i],
            'Crop_Type': crop,
            'Soil_Type': soil,
            'Temperature_C': round(temperature, 2),
            'Humidity_Percent': round(humidity, 2),
            'Rainfall_mm': round(rainfall, 2),
            'Soil_Moisture_Percent': round(soil_moisture, 2),
            'Irrigation_Needed_Liters': round(irrigation_needed, 2)
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    return df

def save_data(df, filename='../data/irrigation_data.csv'):
    """Save generated data to CSV file"""
    
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")
    print(f"📊 Total samples: {len(df)}")
    print(f"\n📈 Data Statistics:")
    print(df.describe())
    
    # Save data description
    description = """
    Dataset Description: Smart Irrigation System
    ============================================
    
    This dataset contains synthetic agricultural and weather data for irrigation prediction.
    
    Fields:
    -------
    1. Date: Date of observation
    2. Crop_Type: Type of crop (Wheat, Rice, Cotton, Maize, Sugarcane)
    3. Soil_Type: Type of soil (Clay, Sandy, Loamy, Silt)
    4. Temperature_C: Temperature in Celsius (15-45°C)
    5. Humidity_Percent: Relative humidity (20-90%)
    6. Rainfall_mm: Rainfall in millimeters (0-100mm)
    7. Soil_Moisture_Percent: Soil moisture level (5-50%)
    8. Irrigation_Needed_Liters: Target variable - Water needed for irrigation (0-80 liters)
    
    Data Generation Logic:
    ----------------------
    - Base water requirement varies by crop type
    - Temperature increases water need
    - Higher humidity reduces water need
    - Recent rainfall reduces irrigation requirement
    - Low soil moisture increases water need
    - Soil type affects moisture retention
    
    Use Case:
    ---------
    This data is used to train an ML model to predict optimal irrigation amounts
    based on environmental conditions and crop requirements, promoting water conservation
    and sustainable agriculture practices.
    """
    
    with open('../data/data_description.txt', 'w') as f:
        f.write(description)
    
    print("\n✅ Data description saved to ../data/data_description.txt")

if __name__ == "__main__":
    print("🌾 Generating Smart Irrigation Dataset...")
    print("=" * 50)
    
    # Generate data
    df = generate_irrigation_data(n_samples=2000)
    
    # Save data
    save_data(df)
    
    print("\n" + "=" * 50)
    print("✅ Data generation complete!")
