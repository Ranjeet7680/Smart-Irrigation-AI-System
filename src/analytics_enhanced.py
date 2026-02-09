"""
Enhanced Analytics Page for Smart Irrigation System
Creates interactive Plotly visualizations
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os

def show_enhanced_analytics():
    """Display enhanced analytics with interactive charts"""
    
    st.markdown("## 📊 Enhanced Interactive Analytics")
    
    # Find base path
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_path, 'data', 'irrigation_data.csv')
    outputs_dir = os.path.join(base_path, 'outputs')
    
    # Show static images first
    st.markdown("### 🎯 Model Performance Charts")
    
    actual_vs_pred = os.path.join(outputs_dir, 'actual_vs_predicted.png')
    feature_imp = os.path.join(outputs_dir, 'feature_importance.png')
    residuals = os.path.join(outputs_dir, 'residuals.png')
    
    if os.path.exists(actual_vs_pred):
        col1, col2 = st.columns(2)
        with col1:
            st.image(actual_vs_pred, caption='Actual vs Predicted - 92% Accuracy', use_column_width=True)
        with col2:
            st.image(feature_imp, caption='Feature Importance Analysis', use_column_width=True)
        
        st.image(residuals, caption='Residual Distribution', use_column_width=True)
    else:
        st.warning("⚠️ Charts not found. Please run: `python src/model_training.py`")
    
    #  Interactive charts
    st.markdown("---")
    st.markdown("### 📈 Interactive Data Insights")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        
        # Water requirements by crop
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💧 Average Water by Crop Type")
            crop_data = df.groupby('Crop_Type')['Irrigation_Needed_Liters'].mean().sort_values(ascending=False)
            
            fig1 = go.Figure(data=[
                go.Bar(
                    y=crop_data.index,
                    x=crop_data.values,
                    orientation='h',
                    marker=dict(
                        color=crop_data.values,
                        colorscale='Blues',
                        showscale=False
                    ),
                    text=[f'{v:.1f}L' for v in crop_data.values],
                    textposition='outside'
                )
            ])
            
            fig1.update_layout(
                xaxis_title="Average Irrigation (Liters)",
                yaxis_title="",
                height=400,
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0.02)',
                font=dict(size=12),
                showlegend=False
            )
            
            st.plotly_chart(fig1, use_container_width=True, key='crop_chart')
        
        with col2:
            st.markdown("#### 🏜️ Water Requirements by Soil Type")
            soil_data = df.groupby('Soil_Type')['Irrigation_Needed_Liters'].mean().sort_values(ascending=False)
            
            fig2 = go.Figure(data=[
                go.Bar(
                    y=soil_data.index,
                    x=soil_data.values,
                    orientation='h',
                    marker=dict(
                        color=soil_data.values,
                        colorscale='Greens',
                        showscale=False
                    ),
                    text=[f'{v:.1f}L' for v in soil_data.values],
                    textposition='outside'
                )
            ])
            
            fig2.update_layout(
                xaxis_title="Average Irrigation (Liters)",
                yaxis_title="",
                height=400,
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0.02)',
                font=dict(size=12),
                showlegend=False
            )
            
            st.plotly_chart(fig2, use_container_width=True, key='soil_chart')
        
        # Temperature vs Irrigation scatterplot
        st.markdown("#### 🌡️ Temperature Impact on Irrigation Needs")
        
        fig3 = go.Figure()
        
        for crop in df['Crop_Type'].unique():
            crop_df = df[df['Crop_Type'] == crop]
            fig3.add_trace(go.Scatter(
                x=crop_df['Temperature_C'],
                y=crop_df['Irrigation_Needed_Liters'],
                mode='markers',
                name=crop,
                marker=dict(size=8, opacity=0.7),
                hovertemplate='<b>%{fullData.name}</b><br>Temp: %{x}°C<br>Irrigation: %{y}L<extra></extra>'
            ))
        
        fig3.update_layout(
            xaxis_title="Temperature (°C)",
            yaxis_title="Irrigation Needed (Liters)",
            height=500,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0.02)',
            hovermode='closest',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        st.plotly_chart(fig3, use_container_width=True, key='temp_chart')
        
        # Humidity vs Soil Moisture heatmap
        st.markdown("#### 💦 Humidity & Soil Moisture Correlation")
        
        # Create bins for better visualization
        df['Humidity_Bin'] = pd.cut(df['Humidity_%'], bins=5)
        df['Moisture_Bin'] = pd.cut(df['Soil_Moisture_%'], bins=5)
        
        pivot_data = df.groupby(['Humidity_Bin', 'Moisture_Bin'])['Irrigation_Needed_Liters'].mean().reset_index()
        pivot_table = pivot_data.pivot(index='Moisture_Bin', columns='Humidity_Bin', values='Irrigation_Needed_Liters')
        
        fig4 = go.Figure(data=go.Heatmap(
            z=pivot_table.values,
            x=[str(col) for col in pivot_table.columns],
            y=[str(idx) for idx in pivot_table.index],
            colorscale='RdYlBu_r',
            text=pivot_table.values.round(1),
            texttemplate='%{text}L',
            textfont={"size": 10},
            colorbar=dict(title="Irrigation (L)")
        ))
        
        fig4.update_layout(
            xaxis_title="Humidity Range (%)",
            yaxis_title="Soil Moisture Range (%)",
            height=400,
            margin=dict(l=10, r=10, t=10, b=10)
        )
        
        st.plotly_chart(fig4, use_container_width=True, key='heatmap')
        
        # Summary statistics
        st.markdown("---")
        st.markdown("### 📊 Data Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Records", f"{len(df):,}")
        col2.metric("Avg Irrigation", f"{df['Irrigation_Needed_Liters'].mean():.1f}L")
        col3.metric("Max Required", f"{df['Irrigation_Needed_Liters'].max():.1f}L")
        col4.metric("Min Required", f"{df['Irrigation_Needed_Liters'].min():.1f}L")
        
    else:
        st.info("💡 Data file not found. Please run `python src/data_generation.py` first.")

if __name__ == "__main__":
    show_enhanced_analytics()
