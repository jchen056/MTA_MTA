import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.header('Dynamic Pricing and Simulation')
st.markdown('''
            
- We want to **dynamically price fare** based on our model prediction, real-time traffic, occurrence of events, etc.
- Through dynamic pricing, we can encourage people to travel off peak hours, which is a win-win for MTA and riders.
''')

# image = Image.open('visualizations/simulation/dp.png')
# st.image(image, caption='Dynamic Pricing to Encourage People to Travel off Peak hours')
dynamic_pricing_html=open("visualizations/simulation/dynamic_pricing.html")
src_code=dynamic_pricing_html.read()
components.html(src_code, width=1000, height=1000)
