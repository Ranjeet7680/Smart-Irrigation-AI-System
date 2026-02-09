"""
Setup Script - Run this to complete the entire project setup
"""

import subprocess
import sys
import os

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def run_step(step_name, command):
    """Run a setup step"""
    print(f"▶️  {step_name}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {step_name} - SUCCESS\n")
            return True
        else:
            print(f"❌ {step_name} - FAILED")
            print(f"Error: {result.stderr}\n")
            return False
    except Exception as e:
        print(f"❌ {step_name} - ERROR: {str(e)}\n")
        return False

def main():
    """Main setup function"""
    print_header("🌾 SMART IRRIGATION SYSTEM - SETUP")
    
    print("This script will:")
    print("1. Install Python dependencies")
    print("2. Generate synthetic agricultural data")
    print("3. Train the ML model")
    print("4. Test the prediction system")
    print("5. Launch the web application\n")
    
    input("Press Enter to continue...")
    
    # Step 1: Install dependencies
    print_header("STEP 1: Installing Dependencies")
    success = run_step(
        "Installing requirements",
        f"{sys.executable} -m pip install -q -r requirements.txt"
    )
    if not success:
        print("⚠️  Installation failed. Please install manually: pip install -r requirements.txt")
        return
    
    # Step 2: Generate data
    print_header("STEP 2: Generating Agricultural Data")
    success = run_step(
        "Generating 2000 data samples",
        f"{sys.executable} src/data_generation.py"
    )
    if not success:
        print("⚠️  Data generation failed.")
        return
    
    # Step 3: Train model
    print_header("STEP 3: Training ML Model")
    success = run_step(
        "Training Random Forest model",
        f"{sys.executable} src/model_training.py"
    )
    if not success:
        print("⚠️  Model training failed.")
        return
    
    # Step 4: Test predictions
    print_header("STEP 4: Testing Prediction System")
    success = run_step(
        "Running prediction tests",
        f"{sys.executable} src/prediction.py"
    )
    if not success:
        print("⚠️  Prediction test failed.")
        return
    
    # Success summary
    print_header("✅ SETUP COMPLETE!")
    
    print("📊 Project Status:")
    print("  ✅ Dependencies installed")
    print("  ✅ Data generated (data/irrigation_data.csv)")
    print("  ✅ Model trained (models/irrigation_model.pkl)")
    print("  ✅ Visualizations created (outputs/*.png)")
    print("  ✅ System tested and working\n")
    
    print("🚀 Next Steps:")
    print("  1. Run the web app: streamlit run src/app.py")
    print("  2. Review documentation: PROJECT_REPORT.md")
    print("  3. Check quick start guide: QUICK_START.md")
    print("  4. Prepare presentation: PRESENTATION_GUIDE.md\n")
    
    # Ask to launch app
    launch = input("Would you like to launch the web application now? (y/n): ")
    
    if launch.lower() == 'y':
        print("\n🌐 Launching Streamlit app...")
        print("Press Ctrl+C to stop the server\n")
        os.system("streamlit run src/app.py")
    else:
        print("\n📝 To launch later, run: streamlit run src/app.py")
    
    print("\n" + "="*60)
    print("  Thank you for using Smart Irrigation System! 🌾")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
