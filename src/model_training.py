"""
Model Training Script for Smart Irrigation System
Trains a Random Forest Regressor to predict irrigation requirements
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os

# Set style for plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

def load_data(filepath='../data/irrigation_data.csv'):
    """Load the irrigation dataset"""
    print("📂 Loading data...")
    df = pd.read_csv(filepath)
    print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def preprocess_data(df):
    """
    Preprocess data for ML model
    - Encode categorical variables
    - Split features and target
    """
    print("\n🔧 Preprocessing data...")
    
    # Create a copy
    df_processed = df.copy()
    
    # Drop date column (not needed for prediction)
    df_processed = df_processed.drop('Date', axis=1)
    
    # Encode categorical variables
    label_encoders = {}
    
    for col in ['Crop_Type', 'Soil_Type']:
        le = LabelEncoder()
        df_processed[col] = le.fit_transform(df_processed[col])
        label_encoders[col] = le
        print(f"  ✓ Encoded {col}")
    
    # Split features and target
    X = df_processed.drop('Irrigation_Needed_Liters', axis=1)
    y = df_processed['Irrigation_Needed_Liters']
    
    print(f"✅ Features shape: {X.shape}")
    print(f"✅ Target shape: {y.shape}")
    
    return X, y, label_encoders

def train_model(X_train, y_train):
    """Train Random Forest Regressor"""
    print("\n🤖 Training Random Forest Model...")
    
    # Initialize model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    # Train model
    model.fit(X_train, y_train)
    
    print("✅ Model trained successfully!")
    
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    print("\n📊 Evaluating Model Performance...")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n" + "=" * 50)
    print("MODEL PERFORMANCE METRICS")
    print("=" * 50)
    print(f"R² Score:                  {r2:.4f}")
    print(f"Mean Absolute Error:       {mae:.2f} liters")
    print(f"Root Mean Squared Error:   {rmse:.2f} liters")
    print(f"Mean Squared Error:        {mse:.2f}")
    print("=" * 50)
    
    return y_pred, {'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2}

def plot_results(y_test, y_pred, feature_importance, feature_names):
    """Create visualization plots"""
    print("\n📈 Creating visualizations...")
    
    # Create output directory
    os.makedirs('../outputs', exist_ok=True)
    
    # 1. Actual vs Predicted
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, edgecolors='k')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Irrigation (Liters)', fontsize=12)
    plt.ylabel('Predicted Irrigation (Liters)', fontsize=12)
    plt.title('Actual vs Predicted Irrigation Requirements', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../outputs/actual_vs_predicted.png', dpi=300, bbox_inches='tight')
    print("  ✓ Saved: actual_vs_predicted.png")
    plt.close()
    
    # 2. Feature Importance
    plt.figure(figsize=(10, 6))
    feature_imp_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': feature_importance
    }).sort_values('Importance', ascending=True)
    
    plt.barh(feature_imp_df['Feature'], feature_imp_df['Importance'], color='steelblue')
    plt.xlabel('Importance', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.title('Feature Importance in Irrigation Prediction', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('../outputs/feature_importance.png', dpi=300, bbox_inches='tight')
    print("  ✓ Saved: feature_importance.png")
    plt.close()
    
    # 3. Residual Plot
    plt.figure(figsize=(10, 6))
    residuals = y_test - y_pred
    plt.scatter(y_pred, residuals, alpha=0.5, edgecolors='k')
    plt.axhline(y=0, color='r', linestyle='--', lw=2)
    plt.xlabel('Predicted Irrigation (Liters)', fontsize=12)
    plt.ylabel('Residuals', fontsize=12)
    plt.title('Residual Plot', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../outputs/residuals.png', dpi=300, bbox_inches='tight')
    print("  ✓ Saved: residuals.png")
    plt.close()
    
    print("✅ All visualizations saved to ../outputs/")

def save_model(model, label_encoders):
    """Save trained model and encoders"""
    print("\n💾 Saving model and encoders...")
    
    # Create models directory
    os.makedirs('../models', exist_ok=True)
    
    # Save model
    joblib.dump(model, '../models/irrigation_model.pkl')
    print("  ✓ Model saved: irrigation_model.pkl")
    
    # Save label encoders
    joblib.dump(label_encoders, '../models/label_encoders.pkl')
    print("  ✓ Encoders saved: label_encoders.pkl")
    
    print("✅ Model artifacts saved successfully!")

def main():
    """Main training pipeline"""
    print("🌾 Smart Irrigation System - Model Training")
    print("=" * 50)
    
    # Load data
    df = load_data()
    
    # Preprocess data
    X, y, label_encoders = preprocess_data(df)
    
    # Train-test split
    print("\n🔀 Splitting data (80% train, 20% test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"  Training samples: {len(X_train)}")
    print(f"  Testing samples: {len(X_test)}")
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    y_pred, metrics = evaluate_model(model, X_test, y_test)
    
    # Feature importance
    feature_importance = model.feature_importances_
    feature_names = X.columns.tolist()
    
    # Plot results
    plot_results(y_test, y_pred, feature_importance, feature_names)
    
    # Save model
    save_model(model, label_encoders)
    
    print("\n" + "=" * 50)
    print("✅ Training Pipeline Complete!")
    print("=" * 50)
    
    return model, label_encoders, metrics

if __name__ == "__main__":
    model, encoders, metrics = main()
