import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

#Calculate emissions calculations
class CarbonCal
    def calc_energy(electricity, gas, fuel)
        """calculate energy emission through equation"""
        return((electricity * 12 * 0.0005) + (gas * 12 * 0.0053) + (fuel * 12 * 2.32))
    
    def calc_waste(waste , recycling)
        """Calculate waste emission through equation"""
        return(waste * 12 * (0.57 - recycling / 100))
    
    def calc_travel(traveled_distance , fuel_efficiency)
        """Calculate Business Travel emission through equation"""
        return(traveled_distance * (1 / fuel_efficiency) * 2.31)
    
    def calc_total_emission(energy , waste , travel)
        return (energy + waste + travel)
    
#Main app

class Emissionapp
    def run(self):
        st.title("🌿 Carbon Footprint Calculator")
        st.write("Calculate your carbon emissions from energy, waste, and travel.")

     # User Input Section
        st.header("📜 Enter Your Details")
        calculator_type = st.selectbox("Calculator Type:", ["Personal", "Business", "Industrial"])
        user_name = st.text_input("Your Name:", "Person/Company Name")
        year = st.number_input("Year:", min_value=2000, max_value=2100, value=datetime.now().year)

        # Input fields for Energy, Waste, and Travel
        st.header("💡 Energy Usage")
        electricity = st.number_input("Monthly Electricity Bill (€):", min_value=0.0, value=0.0)
        gas = st.number_input("Monthly Gas Bill (€):", min_value=0.0, value=0.0)
        fuel = st.number_input("Monthly Fuel Bill (€):", min_value=0.0, value=0.0)

        st.header("🗑 Waste Management")
        waste = st.number_input("Monthly Waste (kg):", min_value=0.0, value=0.0)
        recycling = st.slider("Recycling Percentage (%):", min_value=0, max_value=100, value=0)

        st.header("🚗 Travel Impact")
        travel_distance = st.number_input("Annual Travel Distance (km):", min_value=0.0, value=0.0)
        fuel_efficiency = st.number_input("Fuel Efficiency (L/100km):", min_value=0.1, value=10.0)

        if st.button("Calculate Emissions"):

            energy_emissions = CarbonCal.calc_energy(electricity, gas, fuel)
            waste_emissions = CarbonCal.calc_waste(waste, recycling)
            travel_emissions = CarbonCal.calc_travel(travel_distance, fuel_efficiency)
            total_emissions = CarbonCal.calc_total_emission(energy_emissions, waste_emissions, travel_emissions)

            # Display results
            st.subheader("Results")
            st.write(f"**Name:** {user_name}")
            st.write(f"**Year:** {year}")
            st.write(f"**Calculator Type:** {calculator_type}")
            st.write(f"**Energy Emissions:** {energy_emissions:.2f} kgCO2")
            st.write(f"**Waste Emissions:** {waste_emissions:.2f} kgCO2")
            st.write(f"**Travel Emissions:** {travel_emissions:.2f} kgCO2")
            st.write(f"**Total Carbon Emissions:** {total_emissions:.2f} kgCO2")