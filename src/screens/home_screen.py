import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout , style_background_home, set_background, logo_home
import base64


def home_screen():


    
    set_background("./images/background_1.jpeg")
    header_home()
    style_background_home()
    style_base_layout()
    

    
    


    

    col1, col2 = st.columns(2, gap="large", vertical_alignment='center')

    with col1:  
            logo_home("images/st_logo.jpg", " I'm Student")
            if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
                st.session_state['login_type']='student'
                st.rerun()

    with col2:  
            logo_home("images/tr_logo.jpg", " I'm Teacher")
            if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
                st.session_state['login_type']='teacher'
                st.rerun()
     

    footer_home()   