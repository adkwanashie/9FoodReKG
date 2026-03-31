# -----------------------------------------------------
# 9FoodReKG App — main.py
# -----------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()

# Load API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import streamlit as st
from pathlib import Path

# -----------------------------------------------------
# App Metadata
# -----------------------------------------------------
st.set_page_config(
    page_title="9FoodReKG",
    page_icon="",
)

st.title("9FoodReKG")


# -----------------------------------------------------
# Knowledge Graph Overview with Expanders
# -----------------------------------------------------
st.markdown("""
## Knowledge Graph Overview

This Knowledge Graph models Nigeria’s food and beverage regulatory framework.  
It integrates multiple entity types including **Regulations, Regulation Versions, Clauses, Schedules, Issuing Authorities, Concepts, and Defined Terms**.  
""")

with st.expander("📜 Regulations"):
    st.markdown("""
    - Food Products Advertisement Regulations (2021‑09‑01)  
    - Fruit Juice and Nectar Regulations (2021‑09‑03)  
    - Milk and Dairy Products Regulations (2021‑09‑13)  
    - Non‑Nutritive Sweeteners in Food Products Regulations (2021‑07‑14)  
    - Soft Drinks Regulations (2021‑09‑15)  
    - Food Irradiation Regulations (2021‑08‑31)  
    - Food Grade (Table or Cooking) Salt Regulations (2021‑08‑18)  
    - Pre‑Packaged Food (Labelling) Regulations (2023‑05‑17)  
    - Fats, Oils and Foods Containing Fats and Oils Regulations (2023‑05‑16)  
    - Food Fortification Regulations (2021‑07‑07)  
    - Spirits Drink Regulations (2021‑07‑07)  
    - Wine Regulations (2021‑07‑07)  
    """)

with st.expander("📑 Clauses"):
    st.markdown("""
    Clauses capture specific legal requirements, prohibitions, and penalties.  
    Examples include:
    - Advertising restrictions (e.g., food products must be registered before advertisement).  
    - Composition standards (e.g., fruit juice must contain ≥85% fruit content).  
    - Labelling rules (e.g., milk products must declare animal source).  
    - Penalties (e.g., fines up to ₦800,000 for individuals, ₦5,000,000 for corporates).  
    """)

with st.expander("📂 Schedules"):
    st.markdown("""
    Schedules provide detailed technical standards such as:
    - Nutrient Reference Values (NRVs) for vitamins and minerals.  
    - Permitted additives and contaminant limits.  
    - Composition standards for milk, oils, and sweeteners.  
    - Classification of food categories (e.g., wine, spirits, soft drinks).  
    """)

with st.expander("🏛️ Issuing Authority"):
    st.markdown("""
    The regulatory framework is issued by:
    - **Federal Ministry of Health**  
    - **NAFDAC (National Agency for Food and Drug Administration and Control)**  

    These authorities oversee compliance, enforcement, and publication of regulations.  
    """)

st.markdown("""
Together, the KG enables **traceability of legal requirements**, supports **compliance queries**, and provides a foundation for **benchmarking performance, accuracy, semantic reasoning, and usability** in regulatory AI applications.
""")

# -----------------------------------------------------
# Knowledge Graph Evaluation Categories in Expanders
# -----------------------------------------------------
st.subheader("Evaluation Categories & References")

with st.expander("Performance Benchmarks"):
    st.markdown("""
    - Throughput (queries/sec)  
    - Scalability (performance vs graph size)  
    - Concurrency (multi‑user load)  
    - Cold vs warm cache latency  
""")

with st.expander("Accuracy & Quality Benchmarks"):
    st.markdown("""
    - Precision, Recall, F1‑score (against gold standard)  
    - Coverage (percentage of expected entities/relations present)  
    - Consistency (no contradictions, duplicates)  
    - Completeness (ratio of expected vs actual KG content)  
""")

with st.expander("Semantic Evaluation"):
    st.markdown("""
    - Link prediction accuracy (Hits@k, MRR)  
    - Entity alignment accuracy (cross‑dataset matching)  
    - Ontology compliance (schema adherence)  
 """)

with st.expander("Usability & Interpretability"):
    st.markdown("""
    - Query expressiveness (complex multi‑hop queries vs simple counts)  
    - Explainability (traceability of answers to source triples/clauses)  
    - Visualization clarity (user studies on interpretability)  
 """)

# -----------------------------------------------------
# Connect to Neo4j via kg_loader
# -----------------------------------------------------
from kg import kg_loader

st.sidebar.title("Database Connection")

try:
    # Quick test query
    results = kg_loader.run_query("MATCH (r:Regulation) RETURN r.title LIMIT 3")
    st.sidebar.success("Connected to Neo4j")
    st.sidebar.write("Sample Regulations:")
    for r in results:
        st.sidebar.write(f"- {r['r.title']}")
except Exception as e:
    st.sidebar.error(f"Neo4j connection failed : {e}")

# -----------------------------------------------------
# Render selected page content
# -----------------------------------------------------
if "target_page" in st.session_state:
    target = st.session_state["target_page"]
    st.write(f"Loading page: {target}")
    # You can import or execute the page script here if needed
    # For example:
    # exec(open(pages[target]).read(), globals())
else:
    st.write("Use the sidebar to navigate.")