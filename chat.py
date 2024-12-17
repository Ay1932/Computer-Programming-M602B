import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

# Manage calculation history
class HistoryManager:
    @staticmethod
    def load():
        """Load calculation history from a file."""
        try:
            with open("calculation_history.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save(history):
        """Save calculation history to a file."""
        with open("calculation_history.json", "w") as file:
            json.dump(history, file, indent=4)

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

# Create a PDF report
class PDFGenerator:
    @staticmethod
    def generate(user_name, year, calculator_type, energy, waste, travel, total):
        """Generate a PDF report of the emissions calculation."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times New Roman", size=12)

        pdf.cell(200, 10, txt="Carbon Emission Report", ln=True, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Name: {user_name}", ln=True)
        pdf.cell(200, 10, txt=f"Year: {year}", ln=True)
        pdf.cell(200, 10, txt=f"Calculator Type: {calculator_type}", ln=True)
        pdf.cell(200, 10, txt=f"Energy Emissions: {energy:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Waste Emissions: {waste:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Travel Emissions: {travel:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Total Carbon Emissions: {total:.2f} kgCO2", ln=True)

        buffer = BytesIO()
        pdf_output = pdf.output(dest='S').encode('latin1')
        buffer.write(pdf_output)
        buffer.seek(0)

        return buffer

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

            # Save to history
            entry = {
                "date": datetime.now().isoformat(),
                "user_name": user_name,
                "year": year,
                "calculator_type": calculator_type,
                "energy_emissions": energy,
                "waste_emissions": waste,
                "travel_emissions": travel,
                "total_emissions": total,
            }
            self.history.insert(0, entry)
            self.history = self.history[:10]  # Keep last 10 entries
            HistoryManager.save(self.history)

        # Sidebar: History
        st.sidebar.header("📜 Calculation History")
        if self.history:
            for record in self.history[:5]:
                st.sidebar.write(f"**{record['user_name']}** ({record['date']}): {record['total_emissions']:.2f} kgCO₂")
        else:
            st.sidebar.write("No history yet.")

        if st.sidebar.button("Clear History"):
            self.history = []
            HistoryManager.save(self.history)
            st.sidebar.write("History cleared.")

# Run the app
if __name__ == "__main__":
    app = CarbonFootprintApp()
    app.run()
