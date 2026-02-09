"""
Simple test to verify Analytics page works
Run with: streamlit run src/test_analytics.py
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from analytics_enhanced import show_enhanced_analytics

st.set_page_config(
    page_title="Analytics Test",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Test Page")

# Show analytics
show_enhanced_analytics()
