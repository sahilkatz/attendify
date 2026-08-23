import streamlit as st

import base64


def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def header_home():

    logo = get_image_base64("images/logo2.png")
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px; ">
            <img src="data:image/png;base64,{logo}" style='height:200px; border-radius:70px;border: 3px solid white; ' />
            <h1 style='text-align:center; font-size:4rem ;color:white'>ATTENDIFY</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo = get_image_base64("images/logo2.png")
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src="data:image/png;base64,{logo}" style='height:85px;border-radius:30px;border: 3px solid white;' />
            <h2   style='text-align:center;margin-top:30px; color: #5865F2 !important; font-size:0.1px'>ATTENDIFY</h2>
        </div>   
                
                """, unsafe_allow_html=True)


  