import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

# Utility class for history management
class HistoryManager:

    def load_history():
        """Load calculation history from a JSON file."""
        try:
            with open("calculation_history.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


    def save_history(history):
        """Save the updated calculation history to a JSON file."""
        with open("calculation_history.json", "w") as file:
            json.dump(history, file, indent=4)

# Class to encapsulate emissions calculations
class EmissionsCalculator:
    


    def calculate_energy_emissions(electricity, gas, fuel, multiplier):
        """Calculate emissions from energy usage."""
        return ((electricity * 12 * 0.0005) + (gas * 12 * 0.0053) + (fuel * 12 * 2.32)) * multiplier


    def calculate_waste_emissions(waste, recycling, multiplier):
        """Calculate emissions from waste management."""
        return (waste * 12 * (0.57 - recycling / 100)) * multiplier


    def calculate_travel_emissions(travel_distance, fuel_efficiency, multiplier):
        """Calculate emissions from travel."""
        return (travel_distance * (1 / fuel_efficiency) * 2.31) * multiplier


    def calculate_total_emissions(energy, waste, travel):
        """Calculate total emissions by summing all categories."""
        return energy + waste + travel

# Class to generate a PDF report
class PDFReport:

    def generate_pdf(user_name, year, calculator_type, energy, waste, travel, total):
        """Generate a PDF report for the calculation results."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Carbon Emission Report", ln=True, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Name: {user_name}", ln=True)
        pdf.cell(200, 10, txt=f"Year: {year}", ln=True)
        pdf.cell(200, 10, txt=f"Calculator Type: {calculator_type}", ln=True)
        pdf.cell(200, 10, txt=f"Energy Emissions: {energy:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Waste Emissions: {waste:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Travel Emissions: {travel:.2f} kgCO2", ln=True)
        pdf.cell(200, 10, txt=f"Total Carbon Emissions: {total:.2f} kgCO2", ln=True)

        pdf_buffer = BytesIO()
        pdf_output = pdf.output(dest='S').encode('latin1')  # 'S' returns PDF as string
        pdf_buffer.write(pdf_output)
        pdf_buffer.seek(0)  # Rewind the buffer for reading

        return pdf_buffer

# Main application class
class CarbonFootprintApp:
    def __init__(self):
        self.history = HistoryManager.load_history()

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
            multiplier = EmissionsCalculator.MULTIPLIERS[calculator_type]

            energy_emissions = EmissionsCalculator.calculate_energy_emissions(electricity, gas, fuel, multiplier)
            waste_emissions = EmissionsCalculator.calculate_waste_emissions(waste, recycling, multiplier)
            travel_emissions = EmissionsCalculator.calculate_travel_emissions(travel_distance, fuel_efficiency, multiplier)
            total_emissions = EmissionsCalculator.calculate_total_emissions(energy_emissions, waste_emissions, travel_emissions)

            # Display results
            st.subheader("Results")
            st.write(f"**Name:** {user_name}")
            st.write(f"**Year:** {year}")
            st.write(f"**Calculator Type:** {calculator_type}")
            st.write(f"**Energy Emissions:** {energy_emissions:.2f} kgCO2")
            st.write(f"**Waste Emissions:** {waste_emissions:.2f} kgCO2")
            st.write(f"**Travel Emissions:** {travel_emissions:.2f} kgCO2")
            st.write(f"**Total Carbon Emissions:** {total_emissions:.2f} kgCO2")

            # Generate and provide PDF for download
            pdf_buffer = PDFReport.generate_pdf(user_name, year, calculator_type, energy_emissions, waste_emissions, travel_emissions, total_emissions)
            st.download_button(
                label="Download Report as PDF",
                data=pdf_buffer,
                file_name=f"{user_name}_carbon_emission_report.pdf",
                mime="application/pdf",
            )

            # Save to history
            new_entry = {
                "date": datetime.now().isoformat(),
                "user_name": user_name,
                "year": year,
                "calculator_type": calculator_type,
                "energy_emissions": energy_emissions,
                "waste_emissions": waste_emissions,
                "travel_emissions": travel_emissions,
                "total_emissions": total_emissions
            }
            self.history.insert(0, new_entry)
            if len(self.history) > 10:
                self.history.pop()
            HistoryManager.save_history(self.history)

        # Sidebar: Display History
        st.sidebar.header("Calculation History")
        if self.history:
            for entry in self.history[:5]:
                st.sidebar.write(f"**{entry['user_name']}** ({entry['date']}): {entry['total_emissions']:.2f} kgCO₂")
        else:
            st.sidebar.write("No history available.")

        if st.sidebar.button("Clear History"):
            self.history = []
            HistoryManager.save_history(self.history)
            st.sidebar.write("History cleared!")

# Run the app
if __name__ == "__main__":
    app = CarbonFootprintApp()
    app.run()
