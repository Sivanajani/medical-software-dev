"""Streamlit web app for computing GC-content from a DNA sequence or FASTA file.

Reuses compute_gc_content and parse_fasta from exercise_02/gccompute.py.
Run with: streamlit run app.py
"""
import sys
import os
import tempfile
import streamlit as st

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'exercise_02'))
from gccompute import compute_gc_content, parse_fasta


st.title("GC-Content")

st.header("Enter sequence")
raw_seq = st.text_area("Enter sequence", placeholder="ATCGATCG...", label_visibility="collapsed")
if st.button("Calculate"):
    if raw_seq.strip():
        gc = compute_gc_content(raw_seq.strip())
        st.success(f"GC-Content: {gc:.6f} %")
    else:
        st.error("Please enter a DNA sequence.")

st.divider()

st.header("Upload FASTA file")
uploaded_file = st.file_uploader("Choose a file", type=["fasta", "fna", "fa", "txt"])
if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".fasta") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            sequences = parse_fasta(tmp_path)
        except SystemExit:
            st.error("The uploaded file contains no valid FASTA sequences.")
            sequences = []
        finally:
            os.unlink(tmp_path)

        for header, seq in sequences:
            gc = compute_gc_content(seq)
            st.write(f"**{header}**")
            st.success(f"GC-Content: {gc:.6f} %")

    except UnicodeDecodeError:
        st.error("The uploaded file contains invalid characters and could not be read.")
    except OSError as e:
        st.error(f"Could not read the uploaded file: {e}")
