import streamlit as st
import json
from datetime import datetime
from io import BytesIO
from fpdf import FPDF

#Calculate emissions calculations
class CarbonCalculator
    def calc_energy(electricity, gas, fuel)
        """calculate energy emission through equation"""
        return((electricity * 12 * 0.0005) + (gas * 12 * 0.0053) + (fuel * 12 * 2.32))
    
    def calc_waste()