def energy_usage():
    electricity_bill = float(input("Enter your average monthly electricity bill in euros: "))
    natural_gas_bill = float(input("Enter your average monthly natural gas bill in euros: "))
    fuel_bill = float(input("Enter your average monthly fuel bill for transportation in euros: "))

    # Calculating CO2 emissions for energy usage
    electricity_emission = electricity_bill * 12 * 0.0005
    natural_gas_emission = natural_gas_bill * 12 * 0.0053
    fuel_emission = fuel_bill * 12 * 2.32

    total_energy_emission = electricity_emission + natural_gas_emission + fuel_emission
    return total_energy_emission

def waste():
    waste_generated = float(input("Enter the amount of waste you generate per month in kilograms: "))
    recycling_percentage = float(input("Enter the percentage of waste recycled or composted: "))

    # Calculating CO2 emissions for waste
    waste_emission = waste_generated * 12 * (0.57 - (recycling_percentage / 100))
    return waste_emission

def business_travel():
    kilometers_per_year = float(input("Enter the total kilometers your employees travel per year for business purposes: "))
    fuel_efficiency = float(input("Enter the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers: "))

    # Calculating CO2 emissions for business travel
    travel_emission = kilometers_per_year * (1 / (fuel_efficiency / 100)) * 2.31
    return travel_emission

def main():
    # Calculate each component of CO2 emissions
    energy_emission = energy_usage()
    waste_emission = waste()
    travel_emission = business_travel()

    # Calculate total CO2 emissions
    total_emission = energy_emission + waste_emission + travel_emission

    # Display results
    print("\n--- CO₂ Emissions ---")
    print(f"Energy Usage CO₂ Emission: {energy_emission:.2f} kgCO₂")
    print(f"Waste CO₂ Emission: {waste_emission:.2f} kgCO₂")
    print(f"Business Travel CO₂ Emission: {travel_emission:.2f} kgCO₂")
    print(f"Total CO₂ Emission: {total_emission:.2f} kgCO₂")

# Run the program
if __name__ == "__main__":
    main()
