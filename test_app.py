"""
Test script to verify all app functions work correctly
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import plotly.graph_objects as go
        print("✅ Plotly imported successfully")
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
        return False
    
    try:
        from prediction import IrrigationPredictor
        print("✅ IrrigationPredictor imported successfully")
    except ImportError as e:
        print(f"❌ IrrigationPredictor import failed: {e}")
        return False
    
    return True

def test_predictor():
    """Test if predictor can be loaded and used"""
    print("\nTesting predictor...")
    try:
        from prediction import IrrigationPredictor
        predictor = IrrigationPredictor()
        print("✅ Predictor loaded successfully")
        
        # Test prediction
        irrigation = predictor.predict(
            crop_type='Wheat',
            soil_type='Loamy',
            temperature=30.0,
            humidity=60.0,
            rainfall=5.0,
            soil_moisture=25.0
        )
        print(f"✅ Prediction successful: {irrigation} liters")
        
        # Test recommendation
        recommendation = predictor.get_recommendation(irrigation)
        print(f"✅ Recommendation generated: {recommendation['status']}")
        
        return True
    except Exception as e:
        print(f"❌ Predictor test failed: {e}")
        return False

def test_model_files():
    """Test if model files exist"""
    print("\nTesting model files...")
    model_path = os.path.join('models', 'irrigation_model.pkl')
    encoder_path = os.path.join('models', 'label_encoders.pkl')
    
    if os.path.exists(model_path):
        print(f"✅ Model file found: {model_path}")
    else:
        print(f"❌ Model file not found: {model_path}")
        return False
    
    if os.path.exists(encoder_path):
        print(f"✅ Encoder file found: {encoder_path}")
    else:
        print(f"❌ Encoder file not found: {encoder_path}")
        return False
    
    return True

def test_data_files():
    """Test if data files exist"""
    print("\nTesting data files...")
    data_path = os.path.join('data', 'irrigation_data.csv')
    
    if os.path.exists(data_path):
        print(f"✅ Data file found: {data_path}")
        
        # Check if data can be loaded
        try:
            import pandas as pd
            df = pd.read_csv(data_path)
            print(f"✅ Data loaded successfully: {len(df)} rows")
            return True
        except Exception as e:
            print(f"❌ Data loading failed: {e}")
            return False
    else:
        print(f"❌ Data file not found: {data_path}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("SMART IRRIGATION AI SYSTEM - FUNCTION TEST")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Model Files", test_model_files()))
    results.append(("Data Files", test_data_files()))
    results.append(("Predictor", test_predictor()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:20s}: {status}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! The app is ready to run.")
        print("\nTo start the app, run:")
        print("  streamlit run src/app.py")
    else:
        print("⚠️ SOME TESTS FAILED! Please fix the issues above.")
        print("\nIf model files are missing, run:")
        print("  python src/model_training.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
