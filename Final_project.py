# Import necessary libraries
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from datetime import datetime

# Step 1: Define the function to calculate carbon footprint
def calculate_footprint(electricity, gas, fuel, waste, recycling_rate, distance, efficiency):
    # Emission factors for each source
    electricity_factor = 0.85  # kg CO2 per kWh
    gas_factor = 2.1           # kg CO2 per cubic meter
    fuel_factor = 2.31         # kg CO2 per liter
    waste_factor = 0.45        # kg CO2 per kg

    # Calculate emissions for each category
    energy_emissions = (electricity * electricity_factor) + (gas * gas_factor) + (fuel * fuel_factor)
    waste_emissions = waste * waste_factor * ((100 - recycling_rate) / 100)
    travel_emissions = (distance / 100) * efficiency * fuel_factor
    total_emissions = energy_emissions + waste_emissions + travel_emissions

    return energy_emissions, waste_emissions, travel_emissions, total_emissions

# Step 2: Define the function to generate PDF report
def generate_pdf(name, year, calculator_type, energy, waste, travel, total):
    pdf_filename = f"CarbonFootprintReport_{name.replace(' ', '_')}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Adding the title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(4.25 * inch, 10.5 * inch, "Carbon Emission Report")

    # Adding the details
    c.setFont("Helvetica", 12)
    y = 10 * inch

    details = [
        f"Name: {name}",
        f"Year: {year}",
        f"Calculator Type: {calculator_type}",
        f"Energy Emissions: {energy:.2f} kgCO2",
        f"Waste Emissions: {waste:.2f} kgCO2",
        f"Travel Emissions: {travel:.2f} kgCO2",
        f"Total Carbon Emissions: {total:.2f} kgCO2"
    ]

    for line in details:
        c.drawString(1 * inch, y, line)
        y -= 0.4 * inch

    c.save()
    return pdf_filename

# Step 3: Initialize history in session_state if it doesn't exist
if "history" not in st.session_state:
    st.session_state.history = []

# Step 4: Set up the page layout
st.set_page_config(page_title="Carbon Footprint Calculator", layout="wide")

# Step 5: Display title and description
st.markdown("<h1 style='text-align: center;'>\U0001F331 Carbon Footprint Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Quickly measure your carbon emissions and find simple steps to reduce them</h4>", unsafe_allow_html=True)
st.write("---")

# Step 6: Input section for calculator type
st.markdown("### Select Calculator Type:")
calculator_type = st.radio(label="Calculator Type", options=["Personal", "Business"], label_visibility="visible")

# Step 7: Input section for user details
st.markdown("### Your Details:")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name")
    year = st.number_input("Year", min_value=2000, max_value=2100, value=datetime.now().year)

st.write("---")

# Step 8: Input for energy usage
st.markdown("### \U0001F4A1 Energy Usage")
electricity = st.number_input("Monthly Electricity Bill (€)", min_value=0.0, format="%.2f")
gas = st.number_input("Monthly Gas Bill (€)", min_value=0.0, format="%.2f")
fuel = st.number_input("Monthly Fuel Bill (€)", min_value=0.0, format="%.2f")

st.write("---")

# Step 9: Input for waste management
st.markdown("### \U0001F5D1 Waste Management")
waste = st.number_input("Monthly Waste (kg)", min_value=0.0, format="%.2f")
recycling_rate = st.slider("Recycling Rate (%)", min_value=0, max_value=100, value=0)

st.write("---")

# Step 10: Input for travel emissions
st.markdown("### \U0001F697 Travel")
distance = st.number_input("Annual Travel Distance (km)", min_value=0.0, format="%.2f")
efficiency = st.number_input("Fuel Efficiency (L/100km)", min_value=0.0, format="%.2f", value=10.0)

# Step 11: Calculate emissions and generate report
if st.button("⚡ Calculate Carbon Emissions", use_container_width=True):
    energy, waste_emissions, travel, total = calculate_footprint(electricity, gas, fuel, waste, recycling_rate, distance, efficiency)

    st.success("✅ Estimated Carbon Footprint")
    st.write(f"\U0001F4A1 Energy Emissions: **{energy:.2f} kg CO2**")
    st.write(f"🗑 Waste Emissions: **{waste_emissions:.2f} kg CO2**")
    st.write(f"\U0001F697 Travel Emissions: **{travel:.2f} kg CO2**")
    st.write(f"🌍 Total: **{total:.2f} kg CO2**")

    filename = generate_pdf(name, year, calculator_type, energy, waste_emissions, travel, total)
    with open(filename, "rb") as f:
        st.download_button("⬇ Download PDF Report", f, file_name=filename, mime="application/pdf", use_container_width=True)

    st.session_state.history.append({
        "Name": name,
        "Year": year,
        "Calculator Type": calculator_type,
        "Energy (kg CO2)": f"{energy:.2f}",
        "Waste (kg CO2)": f"{waste_emissions:.2f}",
        "Travel (kg CO2)": f"{travel:.2f}",
        "Total (kg CO2)": f"{total:.2f}"
    })

# Step 12: Display history of calculations
if st.session_state.history:
    st.write("---")
    st.markdown("### 📜 Updated Calculation History")
    st.table(st.session_state.history)

st.write("---")

# Step 13: Clear history button
if st.button("🗑 Clear History", use_container_width=True):
    st.session_state.history = []
    st.success("History cleared.")