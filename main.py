#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:44:59 2021

@author: victor
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title('PIG Data Viewer (v0)')
st.write("""
          ## Informações sobre corridas de PIGs no duto de testes do LAMP/UFRN
          """)
          
st.write("""### Escolha um arquivo para análise:""")
uploaded_file = st.file_uploader("Formato \"local_dd-mm-aaaa.csv\" (ex.: \"10-12-2020.csv\")",
                                  type='csv', accept_multiple_files=False)


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
st.subheader('Duração do teste (m): ')
elapsed_time = max(df['time']) - min(df['time'])
st.write(elapsed_time / 60)



# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(y=df['up_pressure'], name="Upstream press."),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(y=df['down_pressure'], name="Downstream press."),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(y=df['acc_x'], name="X-acc."),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(y=df['acc_y'], name="Y-acc."),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(y=df['acc_z'], name="Z-acc."),
    secondary_y=False,
)

fig.update_xaxes(title_text='Time (s)')
fig.update_yaxes(title_text="Acceleration (g)", secondary_y=False)
fig.update_yaxes(title_text="Pressure (bar)", secondary_y=True)
#fig.show() # plot in new page
st.plotly_chart(fig) # plot in the same page
