# Computer-Programming-M602B
Carbon Footprint Calculator

Overview This Carbon Footprint Calculator helps measure how much carbon dioxide (CO₂) a person produces through Energy use, Waste, and Travel. It gives an idea of the environmental impact of these activities.

Getting Started To use this calculator, enter information in three areas:

Energy: Provide details about your monthly electricity, gas, and fuel bills. Waste: Share how much waste you create monthly and how much you recycle. Travel: Give details about how far you travel each year and your vehicle's fuel efficiency.

Prerequisites Before installing the software, make sure you have these Python modules:

Streamlit: For creating the web interface. ReportLab: For making PDF reports to download.

Installation Run the following commands to set up the software: pip install streamlit pip install reportlab

Usage Example Input Details: Type: Personal Name: Dhruvin Kheni Year: 2024 Monthly Energy Bills: Electricity: €60 Gas: €40 Fuel: €25 Monthly Waste: 35 kg Recycling Rate: 60% Annual Travel Distance: 15,000 km Fuel Efficiency: 7 L/100km Generated Output: Energy Emissions: 620.0 kg CO₂ Waste Emissions: 28.0 kg CO₂ Travel Emissions: 3,750 kg CO₂ Total Emissions: 4,398.0 kg CO₂ Note: These results are estimates. Regular tracking and reducing waste, energy, and travel can help lower your carbon footprint.

Python Imports Used: import streamlit as st from reportlab.lib.pagesizes import letter from reportlab.lib.units import inch from reportlab.pdfgen import canvas from datetime import datetime

Conclusion This calculator is a helpful tool for understanding personal carbon emissions. It supports making better choices to protect the environment.

