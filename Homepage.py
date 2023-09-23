import streamlit as st
import base64
import streamlit_authenticator as stauth
##user authentication

# ... Rest of your application code ...

import yaml
import streamlit as st
from yaml.loader import SafeLoader
st.set_page_config(
            page_title="HomePage",
    )
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status:
    st.write(f'Welcome *{name}*')
    



    st.sidebar.success("Select a page above.")




    

    video = "inv1.mp4"
    def loop_video(video_file, width, height):
        video_url = f"data:video/mp4;base64,{base64.b64encode(video_file.read()).decode()}"
        return f"""
    <div style="width:{width}px; height:{height}px">
        <video autoplay loop style="width:100%; height:100%; object-fit:contain">
            <source src="{video_url}" type="video/mp4">
        </video>
    </div>
    """

    st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }
    </style>
    """,
        unsafe_allow_html=True
    )
    with st.markdown('<div class="center">', unsafe_allow_html=True):
        st.title("Inventory Management")

    # Display the video with the loop_video function
    with open("inv1.mp4", "rb") as video_file:
        st.markdown(loop_video(video_file, width=500, height=300), unsafe_allow_html=True)

    st.caption("Inventory management is the tracking of inventory from manufacturers to warehouses and from these "
            "facilities to point of sale")
    st.subheader("How does inventory management work?")
    st.caption("The goal of inventory "
        "management is to have the right products in the right place at the right time. This requires inventory "
        "visibility — knowing when to order, how much to order and where to store stock. ")
    st.caption("The basic steps of inventory management include:")
    st.caption("1. Purchasing inventory: Ready-to-sell goods are purchased and delivered to the warehouse or directly to "
        "the point of sale.")
    st.caption("2. Storing inventory: Inventory is stored until needed. Goods or materials are transferred across your "
        "fulfillment network until ready for shipment")
    st.caption('Team Members: :blue[_Vishwajeet Jagtap, Vishal Patil, Viraj Sawarkar, Vaibhav Bidkar, Vaishnavi Gurav, Vinay Shinde_]')
    # ###---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    authenticator.logout("Logout", "sidebar")