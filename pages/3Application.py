import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

st.header('Dynamic Pricing and Simulation')
st.markdown('''
            
- We want to **dynamically price fare** based on our model prediction, real-time traffic, occurrence of events, etc.
- Through dynamic pricing, we can encourage people to travel off peak hours, which is a win-win for MTA and riders.
''')
# tab1, tab2=st.tabs(['Dynamic Pricing','Simulation'])
# with tab1:
image = Image.open('visualizations/simulation/dp.png')
st.image(image, caption='Dynamic Pricing to Encourage People to Travel off Peak hours')
