import streamlit as st
import base64




def set_background(image_file):

    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{img}") ;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )




def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def logo_home(image_path,x=""):

    logo =get_image_base64(image_path)
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:0px; margin-top:0px; ">
            <h2 style='text-align:center ;color:#14447B'><b>{x}</b></h2>
            <img src="data:image/png;base64,{logo}" style='height:250px; border-radius:60px; margin-bottom :20px; ' />
            
        </div>   
                
                """, unsafe_allow_html=True)







def style_background_home():

    st.markdown("""
        <style>

                # .stApp {
                #     background: #353B55 !important;
                # }

                .stApp div[data-testid="stColumn"]{
                    background-color:white !important;
                    padding:2rem !important;
                    border-radius: 5rem !important;
                    display:flex !important;
                    flex-direction:column !important; 
                    align-items:center !important; 
                    justify-content:center !important;
                    box-shadow: 0 0 15px rgba(179, 225, 240, 0.7) !important;
                    
                    
                   
                    
                    }

                        
        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_background_dashboard():

    st.markdown("""
        <style>

                # .stApp {
                #     background: #67A6CE !important;
                # }

        </style>  

                """
            ,unsafe_allow_html=True)
    



    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Fugaz+One&family=Stack+Sans+Notch:wght@200..700&display=swap');
                
         /* Hide Top Bar of streamlit */
                
            MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: "Stack Sans Notch", sans-serif !important;
                font-size: 4rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                
                
            }
                

            h2 {
                font-family: "Stack Sans Notch", sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                
                
                
            }

                               

            

            
                
            h3, h4, p{
                font-family: 'Outfit', sans-serif !important;
                color:white !important;
                   
            }

           
               

            button{
                border-radius: 1.5rem !important;
                background-color: #14447B  !important;
                background-color:  !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #43C0E2  !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)