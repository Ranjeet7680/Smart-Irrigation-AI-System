"""
Prediction Module for Smart Irrigation System
Makes irrigation predictions using the trained model
"""

import joblib
import numpy as np
import pandas as pd

class IrrigationPredictor:
    """Class to handle irrigation predictions"""
    
    def __init__(self, model_path='../models/irrigation_model.pkl', 
                 encoders_path='../models/label_encoders.pkl'):
        """
        Initialize predictor with trained model
        
        Parameters:
        model_path (str): Path to saved model
        encoders_path (str): Path to saved label encoders
        """
        try:
            self.model = joblib.load(model_path)
            self.label_encoders = joblib.load(encoders_path)
            print("✅ Model loaded successfully!")
        except FileNotFoundError:
            print("❌ Model files not found. Please train the model first.")
            raise
    
    def predict(self, crop_type, soil_type, temperature, humidity, 
                rainfall, soil_moisture):
        """
        Predict irrigation requirement
        
        Parameters:
        crop_type (str): Type of crop
        soil_type (str): Type of soil
        temperature (float): Temperature in Celsius
        humidity (float): Humidity percentage
        rainfall (float): Rainfall in mm
        soil_moisture (float): Soil moisture percentage
        
        Returns:
        float: Predicted irrigation requirement in liters
        """
        
        # Encode categorical variables
        crop_encoded = self.label_encoders['Crop_Type'].transform([crop_type])[0]
        soil_encoded = self.label_encoders['Soil_Type'].transform([soil_type])[0]
        
        # Create feature array
        features = np.array([[
            crop_encoded,
            soil_encoded,
            temperature,
            humidity,
            rainfall,
            soil_moisture
        ]])
        
        # Make prediction
        prediction = self.model.predict(features)[0]
        
        # Ensure non-negative
        prediction = max(0, prediction)
        
        return round(prediction, 2)
    
    def get_recommendation(self, irrigation_amount):
        """
        Get irrigation recommendation based on predicted amount
        
        Parameters:
        irrigation_amount (float): Predicted irrigation in liters
        
        Returns:
        dict: Recommendation details
        """
        
        if irrigation_amount < 10:
            status = "Low Priority"
            color = "🟢"
            recommendation = "Minimal irrigation needed. Soil has adequate moisture."
            water_saved = "Excellent! You're conserving water effectively."
        elif irrigation_amount < 25:
            status = "Medium Priority"
            color = "🟡"
            recommendation = "Moderate irrigation recommended within 24 hours."
            water_saved = "Good water management. Continue monitoring."
        elif irrigation_amount < 40:
            status = "High Priority"
            color = "🟠"
            recommendation = "Significant irrigation needed. Water within 12 hours."
            water_saved = "Ensure adequate water supply for optimal crop health."
        else:
            status = "Critical"
            color = "🔴"
            recommendation = "Immediate irrigation required! Crops need water urgently."
            water_saved = "High water demand. Consider drip irrigation for efficiency."
        
        return {
            'status': status,
            'color': color,
            'recommendation': recommendation,
            'water_saved': water_saved
        }
    
    def batch_predict(self, df):
        """
        Make predictions for multiple samples
        
        Parameters:
        df (pandas.DataFrame): DataFrame with input features
        
        Returns:
        numpy.array: Array of predictions
        """
        
        # Encode categorical variables
        df_encoded = df.copy()
        df_encoded['Crop_Type'] = self.label_encoders['Crop_Type'].transform(df['Crop_Type'])
        df_encoded['Soil_Type'] = self.label_encoders['Soil_Type'].transform(df['Soil_Type'])
        
        # Make predictions
        predictions = self.model.predict(df_encoded)
        
        # Ensure non-negative
        predictions = np.maximum(0, predictions)
        
        return predictions

def test_predictor():
    """Test the predictor with sample inputs"""
    print("\n🧪 Testing Irrigation Predictor...")
    print("=" * 50)
    
    predictor = IrrigationPredictor()
    
    # Test cases
    test_cases = [
        {
            'name': 'Hot dry day with rice',
            'crop_type': 'Rice',
            'soil_type': 'Clay',
            'temperature': 38,
            'humidity': 30,
            'rainfall': 0,
            'soil_moisture': 15
        },
        {
            'name': 'Moderate day with wheat',
            'crop_type': 'Wheat',
            'soil_type': 'Loamy',
            'temperature': 25,
            'humidity': 60,
            'rainfall': 5,
            'soil_moisture': 30
        },
        {
            'name': 'Rainy day with cotton',
            'crop_type': 'Cotton',
            'soil_type': 'Sandy',
            'temperature': 22,
            'humidity': 80,
            'rainfall': 25,
            'soil_moisture': 40
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n📋 Test Case {i}: {test['name']}")
        print("-" * 50)
        
        irrigation = predictor.predict(
            test['crop_type'],
            test['soil_type'],
            test['temperature'],
            test['humidity'],
            test['rainfall'],
            test['soil_moisture']
        )
        
        recommendation = predictor.get_recommendation(irrigation)
        
        print(f"Crop: {test['crop_type']} | Soil: {test['soil_type']}")
        print(f"Temp: {test['temperature']}°C | Humidity: {test['humidity']}%")
        print(f"Rainfall: {test['rainfall']}mm | Soil Moisture: {test['soil_moisture']}%")
        print(f"\n{recommendation['color']} Irrigation Needed: {irrigation} liters")
        print(f"Status: {recommendation['status']}")
        print(f"💡 {recommendation['recommendation']}")
    
    print("\n" + "=" * 50)
    print("✅ Testing complete!")

if __name__ == "__main__":
    test_predictor()
