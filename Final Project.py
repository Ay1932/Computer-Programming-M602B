import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF



# Perform emissions calculations
class EmissionsCalculator:
    MULTIPLIERS = {
        "Personal": 1.0,
        "Business": 1.5,
        "Industrial": 2.0,
    }

    @staticmethod
    def energy_emissions(electricity, gas, fuel, multiplier):
        """Calculate emissions from energy use."""
        return ((electricity * 12 * 0.0005) + (gas * 12 * 0.0053) + (fuel * 12 * 2.32)) * multiplier

    @staticmethod
    def waste_emissions(waste, recycling_rate, multiplier):
        """Calculate emissions from waste management."""
        return (waste * 12 * (0.57 - recycling_rate / 100)) * multiplier

    @staticmethod
    def travel_emissions(distance, efficiency, multiplier):
        """Calculate emissions from travel."""
        return (distance * (1 / efficiency) * 2.31) * multiplier

    @staticmethod
    def total_emissions(energy, waste, travel):
        """Sum up total emissions."""
        return energy + waste + travel


# Main application
class CarbonFootprintApp:
    def __init__(self):
        self.history = HistoryManager.load()

    def run(self):
        st.title("🌿 Carbon Footprint Calculator")
        st.write("Easily calculate your carbon emissions and learn how to reduce your footprint.")

        # User Input
        st.header("📋 Your Information")
        calculator_type = st.selectbox("Select Calculator Type:", ["Personal", "Business", "Industrial"])
        user_name = st.text_input("Your Name:", "Your Name")
        year = st.number_input("Year:", min_value=2000, max_value=2100, value=datetime.now().year)

        # Energy Input
        st.header("💡 Energy Usage")
        electricity = st.number_input("Monthly Electricity Bill (€):", min_value=0.0, value=0.0)
        gas = st.number_input("Monthly Gas Bill (€):", min_value=0.0, value=0.0)
        fuel = st.number_input("Monthly Fuel Bill (€):", min_value=0.0, value=0.0)

        # Waste Input
        st.header("🗑 Waste Management")
        waste = st.number_input("Monthly Waste (kg):", min_value=0.0, value=0.0)
        recycling_rate = st.slider("Recycling Rate (%):", min_value=0, max_value=100, value=0)

        # Travel Input
        st.header("🚗 Travel")
        travel_distance = st.number_input("Annual Travel Distance (km):", min_value=0.0, value=0.0)
        fuel_efficiency = st.number_input("Fuel Efficiency (L/100km):", min_value=0.1, value=10.0)

        if st.button("Calculate Emissions"):
            multiplier = EmissionsCalculator.MULTIPLIERS[calculator_type]

            energy = EmissionsCalculator.energy_emissions(electricity, gas, fuel, multiplier)
            waste = EmissionsCalculator.waste_emissions(waste, recycling_rate, multiplier)
            travel = EmissionsCalculator.travel_emissions(travel_distance, fuel_efficiency, multiplier)
            total = EmissionsCalculator.total_emissions(energy, waste, travel)

            # Show Results
            st.subheader("Your Results")
            st.write(f"**Name:** {user_name}")
            st.write(f"**Year:** {year}")
            st.write(f"**Calculator Type:** {calculator_type}")
            st.write(f"**Energy Emissions:** {energy:.2f} kgCO2")
            st.write(f"**Waste Emissions:** {waste:.2f} kgCO2")
            st.write(f"**Travel Emissions:** {travel:.2f} kgCO2")
            st.write(f"**Total Emissions:** {total:.2f} kgCO2")

            # Generate PDF
            pdf = PDFGenerator.generate(user_name, year, calculator_type, energy, waste, travel, total)
            st.download_button(
                label="Download PDF Report",
                data=pdf,
                file_name=f"{user_name}_carbon_footprint_report.pdf",
                mime="application/pdf",
            )

            

        

# Run the app
if __name__ == "__main__":
    app = CarbonFootprintApp()
    app.run()
