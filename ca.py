import streamlit as st

st.title("Carbon Footprint Calculator")

st.write("This calculator estimates your organization's carbon footprint based on energy usage, waste generation, and business travel.")

# Energy Usage
st.subheader("Energy Usage")
electricity_bill = st.number_input("Average monthly electricity bill (euros)", min_value=0.0)
natural_gas_bill = st.number_input("Average monthly natural gas bill (euros)", min_value=0.0)
fuel_bill = st.number_input("Average monthly fuel bill for transportation (euros)", min_value=0.0)

# Waste
st.subheader("Waste")
waste_generated = st.number_input("Total waste generated per month (kilograms)", min_value=0.0)
recycling_percentage = st.number_input("Recycling/composting percentage (0-100)", min_value=0, max_value=100)

# Business Travel
st.subheader("Business Travel")
total_km_traveled = st.number_input("Total kilometers traveled by employees per year for business purposes", min_value=0.0)
fuel_efficiency = st.number_input("Average fuel efficiency of vehicles used for business travel (liters per 100 kilometers)", min_value=0.0)

# Calculations
energy_co2 = (electricity_bill * 12 * 0.0005) + (natural_gas_bill * 12 * 0.0053) + (fuel_bill * 12 * 2.32)
waste_co2 = (waste_generated * 12) * (0.57 - (recycling_percentage / 100))
travel_co2 = (total_km_traveled * (1 / fuel_efficiency)) * 2.31
total_co2 = energy_co2 + waste_co2 + travel_co2

# Display Results
st.subheader("Results")
st.write("**Estimated Carbon Footprint:**", total_co2, "kg CO2")
st.write("**Breakdown:**")
st.write("- Energy usage:", energy_co2, "kg CO2")
st.write("- Waste generation:", waste_co2,