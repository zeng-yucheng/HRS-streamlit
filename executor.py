import streamlit as st


def executor(func):
    # modify this block to build the cmd
    cmd = st.text_input("Please input your parameters")
    st.button("Run Isaac Sim Composer Replicator", on_click=func, kwargs={'cmd': cmd})
