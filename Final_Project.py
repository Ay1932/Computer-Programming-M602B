import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

# Performing calculations
class CalcEmission:
    MULTIPLIERS = {
        "Personal": 1.0,
        "Business": 1.5,
        "Industrial": 2.0,
    }

    @staticmethod
    def energy_emi(electricity, gas, fuel, multiplier):
        """Calculate emissions from energy use."""
        return ((electricity * 12 * 0.0005) + (gas * 12 * 0.0053) + (fuel * 12 * 2.32)) * multiplier

    @staticmethod
    def waste_emi(waste, recycling_rate, multiplier):
        """Calculate emissions from waste management."""
        return (waste * 12 * (0.57 - recycling_rate / 100)) * multiplier

    @staticmethod
    def travel_emi(distance, efficiency, multiplier):
        """Calculate emissions from travel."""
        return (distance * (1 / efficiency) * 2.31) * multiplier

    @staticmethod
    def total_emi(energy, waste, travel):
        """Sum up total emissions."""
        return energy + waste + travel
 
# Main application
class CarbonCalculator:
    def __init__(self):
        self.history = HistoryManager.load()

    def run(self):
        st.title("🌿 Carbon Footprint Calculator")
        st.write("Easily calculate your carbon emissions and learn how to reduce your footprint.")

        # User Input
        st.header("📋 Your Information")
        type = st.selectbox("Select Calculator Type:", ["Personal", "Business", "Industrial"])
        name = st.text_input("Your Name:", "Your Name")
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
            multiplier = CalcEmission.MULTIPLIERS[type]

            energy = CalcEmission.energy_emi(electricity, gas, fuel, multiplier)
            waste = CalcEmission.waste_emi(waste, recycling_rate, multiplier)
            travel = CalcEmission.travel_emi(travel_distance, fuel_efficiency, multiplier)
            total = CalcEmission.total_emi(energy, waste, travel)

            # Show Results
            st.subheader("Your Results")
            st.write(f"**Name:** {name}")
            st.write(f"**Year:** {year}")
            st.write(f"**Calculator Type:** {type}")
            st.write(f"**Energy Emissions:** {energy:.2f} kgCO2")
            st.write(f"**Waste Emissions:** {waste:.2f} kgCO2")
            st.write(f"**Travel Emissions:** {travel:.2f} kgCO2")
            st.write(f"**Total Emissions:** {total:.2f} kgCO2")

            # Generate PDF
            pdf = PDFGenerator.generate(name, year, type, energy, waste, travel, total)
            st.download_button(
                label="Download PDF Report",
                data=pdf,
                file_name=f"{name}_carbon_report.pdf",
                mime="application/pdf",
            )

            # Save to history
            entry = {
                "date": datetime.now().isoformat(),
                "name": name,
                "year": year,
                "calculati": type,
                "energy_emi": energy,
                "waste_emi": waste,
                "travel_emi": travel,
                "total_emi": total,
            }
            self.history.insert(0, entry)
            self.history = self.history[:10]  
            HistoryManager.save(self.history)

        # Sidebar: History
        st.sidebar.header("📜 Calculation History")
        if self.history:
            for record in self.history[:5]:
                st.sidebar.write(f"**{record['name']}** ({record['date']}): {record['total_emi']:.2f} kgCO₂")
        else:
            st.sidebar.write("No history yet.")

        if st.sidebar.button("Clear History"):
            self.history = []
            HistoryManager.save(self.history)
            st.sidebar.write("History cleared.")

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
# Create a PDF report
class PDFGenerator:
    @staticmethod
    def generate(name, year, type, energy, waste, travel, total):
        """Generate a PDF report of the emissions calculation."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Carbon Emission Report", ln=True, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Year: {year}", ln=True)
        pdf.cell(200, 10, txt=f"Calculator Type: {type}", ln=True)
        pdf.cell(200, 10, txt=f"Energy Emissions: {energy:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Waste Emissions: {waste:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Travel Emissions: {travel:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Total Carbon Emissions: {total:.2f} kgCO2", ln=True)

        buffer = BytesIO()
        pdf_output = pdf.output(dest='S').encode('latin1')
        buffer.write(pdf_output)
        buffer.seek(0)

        return buffer

# Run the app
if __name__ == "__main__":
    app = CarbonCalculator()
    app.run()