import streamlit as st
import pandas as pd
import modules.utils as utils


@st.cache_data
def load_data(folder: str = "data/", file: str = "data.csv") -> pd.DataFrame:
    return utils.load_data(folder, file)


@st.cache_resource
def load_model():
    return utils.load_model("sentence-transformers/all-MiniLM-L6-v2")


@st.cache_data
def load_index(folder: str = "data/", file: str = "index.bin"):
    return utils.load_index(folder, file)