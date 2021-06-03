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
uploaded_file = st.file_uploader("Formato \"dd-mm-aaaa_hh_mm_ss.csv\"",
                                  type='csv',
                                  accept_multiple_files=False)


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader('Elapsed time (m)')
    elapsed_time = max(df['time']) - min(df['time'])
    st.write(elapsed_time / 60)

    fig_pressure = go.Figure()
    fig_pressure.add_trace(go.Scatter(y=df['up_pressure'], name="High"))
    fig_pressure.add_trace(go.Scatter(y=df['down_pressure'], name="Low"))
    fig_pressure.update_xaxes(title_text='Time (s)')
    fig_pressure.update_yaxes(title_text="Pressure (bar)")
    st.plotly_chart(fig_pressure)

    fig_acc = go.Figure()
    fig_acc.add_trace(go.Scatter(y=df['acc_x'], name="X"))
    fig_acc.add_trace(go.Scatter(y=df['acc_y'], name="Y"))
    fig_acc.add_trace(go.Scatter(y=df['acc_z'], name="Z"))
    fig_acc.update_xaxes(title_text='Time (s)')
    fig_acc.update_yaxes(title_text="Acceleration (g)")
    st.plotly_chart(fig_acc)

    if st.button('Plot in new window'):
        fig_pressure.show()
        fig_acc.show()
