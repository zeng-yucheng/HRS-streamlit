import streamlit as st
import subprocess
from constrcutor import constructor
from executor import executor

TAB_INPUT, TAB_RUNNING, TAB_RESULTS = st.tabs(["Construct Scene", "Logs", "Dataset"])


def run_isaac_sim(cmd):
    log = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while True:
        line = log.stdout.readline()
        with TAB_RUNNING:
            st.write(line.decode('gbk').strip("b'"))
        if line == b'' or subprocess.Popen.poll(log) == 0:
            log.stdout.close()
            break


with TAB_INPUT:
    constructor()

with TAB_RUNNING:
    executor(run_isaac_sim)

with TAB_RESULTS:
    with open('data/test.yaml', 'rb') as f:
        st.download_button("Download Dataset", data=f, file_name='test.yaml')
