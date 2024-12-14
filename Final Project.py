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
    
    def calc_waste(waste , recycling)
        """Calculate waste emission through equation"""
        return(waste * 12 * (0.57 - recycling / 100))
    
    def calc_travel(traveled_distance , fuel_efficiency)
        """Calculate Business Travel emission through equation"""
        return(traveled_distance * (1 / fuel_efficiency) * 2.31)