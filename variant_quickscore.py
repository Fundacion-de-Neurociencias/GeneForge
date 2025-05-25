# variant_quickscore.py
import streamlit as st
import pandas as pd
from io import StringIO
from gene_forge_sdk.score_variant import score_variant

st.set_page_config(page_title="Variant QuickScore", layout="centered")
st.title("🧬 Variant QuickScore")

tab1, tab2 = st.tabs(["Single variant", "VCF batch"])

# ───────────── SINGLE VARIANT ─────────────
with tab1:
    vid  = st.text_input("Variant ID (rsID or HGVS)", "rs1042522")
    gene = st.text_input("Gene symbol", "TP53")
    if st.button("Score it!"):
        with st.spinner("Scoring…"):
            result = score_variant(vid, gene)
        st.subheader("⚡ Result")
        st.write(f"**Confidence:** {result['confidence']:.2f}")
        st.code("\n".join(result["gfl_block"].splitlines()), language="gfl")
        with st.expander("🔍 Full JSON"):
            st.json(result)
        st.success("Stored in gfDB ✅")

# ───────────── BATCH VCF ─────────────
with tab2:
    vcf_file = st.file_uploader("Upload VCF", type=["vcf"])
    if vcf_file:
        content = vcf_file.getvalue().decode("utf-8")
        rows = []
        for ln in content.splitlines():
            if ln.startswith("#"):
                continue
            chrom, pos, _id, ref, alt, *_rest = ln.split("\t")
            variant_hgvs = f"{chrom}:{pos}{ref}>{alt}"
            gene = "UNKNOWN"
            res  = score_variant(variant_hgvs, gene)
            rows.append({
                "Variant": variant_hgvs,
                "Confidence": res["confidence"],
                "Label": res["gfdb_entry"]["explanation"][:40] + "…"
            })
        df = pd.DataFrame(rows)
        st.subheader("📊 Batch results")
        st.dataframe(df)
        st.success(f"Processed {len(rows)} variants and stored in gfDB ✅")
