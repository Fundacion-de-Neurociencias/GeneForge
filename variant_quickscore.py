# variant_quickscore.py
import streamlit as st
from gene_forge_sdk.score_variant import score_variant

st.set_page_config(page_title="Variant QuickScore", layout="centered")

st.title("🧬 Variant QuickScore")

variant_id = st.text_input("Variant ID (rsID o HGVS)", "rs1042522")
gene = st.text_input("Gene symbol", "TP53")

if st.button("Score it!") and variant_id:
    with st.spinner("Running GeneForge inference…"):
        result = score_variant(variant_id, gene)

    st.subheader("⚡ Result")
    st.write(f"**Confidence:** {result['confidence']:.2f}")
    st.code("\n".join(result["gfl_block"].splitlines()), language="gfl")

    with st.expander("🔍 Full JSON"):
        st.json(result)

    st.success("Done! Entry stored in gfDB 👍")
