import streamlit as st
import yaml

OUTPUT_DATA_OPTIONS = ['RGB', 'Depth', 'Instance Segmentation', 'Semantic Segmentation', 'Bounding Box 2D (Tight)',
                           'Bounding Box 2D (Loose)', 'Bounding Box 3D', 'Groundtruth Stereo', 'Groundtruth Visuals']


def construct_composer_file(options, fn):
    with open(fn, 'w') as f:
        yaml.dump(dict(zip(["output data types"], [options])), f)


def constructor():
    st.title("Please fill in your parameters")

    options = st.multiselect("Output Data Types", OUTPUT_DATA_OPTIONS)
    st.button(
        "Construct Composer File",
        on_click=construct_composer_file,
        kwargs={'options': options, 'fn': 'data/test2.yaml'}
    )
