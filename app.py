
import streamlit as st
import pandas as pd
import numpy as np
import re
from pathlib import Path
from rank_bm25 import BM25Okapi

# ----------------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------------

st.set_page_config(
    page_title="OTC Medicine Explorer",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}
.stMetric {
    border: 1px solid #DCE5E5;
    padding: 15px;
    border-radius: 12px;
}
h1 {
    color: #16877B;
}
[data-testid="stSidebar"] {
    border-right: 1px solid #DCE5E5;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# 2. LOAD DATA
# ----------------------------------------

@st.cache_data
def load_data():
    path = Path(__file__).parent / "OTC_Final_Classified_300.csv"
    data = pd.read_csv(path)
    return data.fillna("")

df = load_data()

# ----------------------------------------
# 3. RISK CATEGORY DEFINITIONS
# ----------------------------------------

risk_map = {
    "R01_Organ_Toxicity":
        "Organ toxicity",
    "R02_Bleeding":
        "Bleeding",
    "R03_Cardiovascular":
        "Cardiovascular",
    "R04_Allergic_Reactions":
        "Allergic reactions",
    "R05_Neurological_Behavioral":
        "Neurological and behavioral",
    "R06_Skin_Local_Tissue":
        "Skin and local tissue",
    "R07_Gastrointestinal":
        "Gastrointestinal",
    "R08_Other_Documented_Risk":
        "Other documented risk",
    "R09_Risk_Not_Specified":
        "Risk not specified"
}

def get_risks(row):
    return [
        name for col, name in risk_map.items()
        if row[col] == 1
    ]

def split_tags(value):
    return [
        tag.strip() for tag in str(value).split(";")
        if tag.strip()
    ]

df["Risk_List"] = df.apply(get_risks, axis=1)

df["Use_List"] = df["Intended Use Tags"].apply(
    split_tags
)

# ----------------------------------------
# 4. BM25 RETRIEVAL
# ----------------------------------------

def tokenize(text):
    return re.findall(
        r"\b\w+\b",
        str(text).lower()
    )

@st.cache_resource
def build_bm25(documents):
    tokenized = [
        tokenize(doc) for doc in documents
    ]

    return BM25Okapi(
        tokenized,
        k1=1.2,
        b=0.75
    )

documents = (
    df["Product"].astype(str) + " " +
    df["Selected texts (Uses + Warnings)"].astype(str)
).tolist()

bm25 = build_bm25(documents)

# ----------------------------------------
# 5. APPLICATION HEADER
# ----------------------------------------

st.title("💊 OTC Medicine Explorer")

st.markdown(
    "Explore medication information through "
    "faceted navigation and intelligent text retrieval."
)

st.caption(
    "INFO 202 Final Project | "
    "UC Berkeley School of Information"
)

st.info(
    "Educational information system. "
    "Not medical advice. Selected warnings are "
    "not complete medication labels."
)

# ----------------------------------------
# 6. RESET FILTERS
# ----------------------------------------

filter_keys = [
    "group_filter",
    "use_filter",
    "user_filter",
    "form_filter",
    "brand_filter",
    "risk_filter",
    "source_filter"
]

def reset_page():
    st.session_state["results_page"] = 1


def change_page(delta):
    st.session_state["results_page"] += delta


def reset_filters():
    for key in filter_keys:
        st.session_state[key] = []

    st.session_state["search_query"] = ""
    reset_page()

# ----------------------------------------
# 7. SIDEBAR FACETS
# ----------------------------------------

st.sidebar.title("Explore by facets")

st.sidebar.caption(
    "Select one or more values to narrow results."
)

st.sidebar.button(
    "Reset all filters",
    on_click=reset_filters,
    use_container_width=True
)

selected_groups = st.sidebar.multiselect(
    "Therapeutic group",
    sorted(df["Groups"].unique()),
    key="group_filter",
    on_change=reset_page
)

st.sidebar.divider()

all_uses = sorted({
    tag
    for tags in df["Use_List"]
    for tag in tags
})

selected_uses = st.sidebar.multiselect(
    "Intended use",
    all_uses,
    key="use_filter",
    on_change=reset_page
)

selected_users = st.sidebar.multiselect(
    "Intended user",
    sorted(df["Intended User Standardized"].unique()),
    key="user_filter",
    on_change=reset_page
)

selected_forms = st.sidebar.multiselect(
    "Dosage form",
    sorted(df["Dosage Form Family"].unique()),
    key="form_filter",
    on_change=reset_page
)

selected_brands = st.sidebar.multiselect(
    "Brand type",
    sorted(df["Brand Type"].unique()),
    key="brand_filter",
    on_change=reset_page
)

risk_options = [
    name for col, name in risk_map.items()
    if df[col].sum() > 0
]

selected_risks = st.sidebar.multiselect(
    "Documented safety risk",
    risk_options,
    key="risk_filter",
    on_change=reset_page,
    help="Classified from selected warning excerpts."
)

st.sidebar.divider()

selected_sources = st.sidebar.multiselect(
    "Classification source",
    sorted(df["Classification_Source"].unique()),
    key="source_filter",
    on_change=reset_page
)

st.sidebar.caption(
    "OR within each facet. AND across facets."
)

# ----------------------------------------
# 8. SEARCH INTERFACE
# ----------------------------------------

query = st.text_input(
    "Search the medicine collection",
    placeholder="e.g. headache, fever, stomach bleeding",
    key="search_query",
    on_change=reset_page
)

st.caption(
    "BM25 searches product names, uses and warnings. "
    "A matching term may describe a warning "
    "rather than an intended use."
)

# ----------------------------------------
# 9. APPLY FACET FILTERS
# ----------------------------------------

filtered = df.copy()

if selected_groups:
    filtered = filtered[
        filtered["Groups"].isin(selected_groups)
    ]

if selected_uses:
    filtered = filtered[
        filtered["Use_List"].apply(
            lambda tags: bool(
                set(tags) & set(selected_uses)
            )
        )
    ]

if selected_users:
    filtered = filtered[
        filtered["Intended User Standardized"].isin(
            selected_users
        )
    ]

if selected_forms:
    filtered = filtered[
        filtered["Dosage Form Family"].isin(
            selected_forms
        )
    ]

if selected_brands:
    filtered = filtered[
        filtered["Brand Type"].isin(selected_brands)
    ]

if selected_risks:
    filtered = filtered[
        filtered["Risk_List"].apply(
            lambda risks: bool(
                set(risks) & set(selected_risks)
            )
        )
    ]

if selected_sources:
    filtered = filtered[
        filtered["Classification_Source"].isin(
            selected_sources
        )
    ]

# ----------------------------------------
# 10. APPLY BM25 RANKING
# ----------------------------------------

if query.strip():

    scores = bm25.get_scores(tokenize(query))

    filtered = filtered.copy()

    filtered["BM25_Score"] = scores[
        filtered.index.to_numpy()
    ]

    filtered = filtered[
        filtered["BM25_Score"] > 0
    ]

    filtered = filtered.sort_values(
        "BM25_Score",
        ascending=False
    )

else:
    filtered = filtered.sort_values("Item")

# ----------------------------------------
# 11. DYNAMIC COLLECTION METRICS
# ----------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Medicines found",
    len(filtered)
)

c2.metric(
    "Collection size",
    len(df)
)

c3.metric(
    "Human-verified",
    int(
        filtered["Classification_Source"]
        .str.contains("Human-Verified")
        .sum()
    )
)

c4.metric(
    "Machine predicted",
    int(
        (filtered["Classification_Source"]
         == "Machine Predicted").sum()
    )
)

st.divider()

# ----------------------------------------
# 12. ACTIVE FILTER SUMMARY
# ----------------------------------------

active_filters = (
    selected_groups +
    selected_uses +
    selected_users +
    selected_forms +
    selected_brands +
    selected_risks +
    selected_sources
)

if active_filters:
    st.markdown("**Active filters:**")
    st.write(" • ".join(active_filters))

# ----------------------------------------
# 13. COLLECTION OVERVIEW
# ----------------------------------------

with st.expander("View result distribution"):

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("**Therapeutic groups**")

        group_counts = (
            filtered["Groups"].value_counts()
        )

        st.bar_chart(group_counts)

    with chart_col2:
        st.markdown("**Documented safety risks**")

        risk_counts = pd.Series({
            name: filtered[col].sum()
            for col, name in risk_map.items()
        })

        st.bar_chart(risk_counts)

    st.caption(
        "Risk categories are multi-label. "
        "Counts may exceed the number of medicines."
    )

# ----------------------------------------
# 14. DISPLAY MEDICINE CARDS
# ----------------------------------------

st.subheader(
    f"Explore results ({len(filtered)})"
)

if filtered.empty:

    st.warning(
        "No medicines match your current selections. "
        "Try removing a filter or changing your query."
    )

else:

    page_size = st.selectbox(
        "Results per page",
        [10, 20, 50],
        index=0,
        key="results_page_size",
        on_change=reset_page
    )

    total_pages = int(
        np.ceil(len(filtered) / page_size)
    )

    if not 1 <= st.session_state.get("results_page", 1) <= total_pages:
        reset_page()

    page = st.selectbox(
        "Page",
        list(range(1, total_pages + 1)),
        key="results_page"
    )

    start = (page - 1) * page_size
    end = start + page_size

    visible = filtered.iloc[start:end]

    st.caption(
        f"Showing {start + 1}–"
        f"{min(end, len(filtered))} "
        f"of {len(filtered)} medicines"
    )

    for _, row in visible.iterrows():

        with st.container(border=True):

            st.subheader(row["Product"])

            st.caption(
                f'{row["Active Ingredient"]} | '
                f'{row["Groups"]}'
            )

            left, right = st.columns(2)

            with left:

                st.markdown("**Intended use**")
                st.write(row["Intended Use"])

                st.markdown("**Intended user**")
                st.write(
                    row["Intended User Standardized"]
                )

            with right:

                st.markdown("**Dosage form**")
                st.write(row["Dosage Form Family"])

                st.markdown("**Brand type**")
                st.write(row["Brand Type"])

            st.markdown("**Documented safety risk**")

            st.write(" • ".join(row["Risk_List"]))

            st.caption(
                "Classification: " +
                row["Classification_Source"]
            )

            if query.strip():
                st.caption(
                    f'BM25 score: '
                    f'{row["BM25_Score"]:.3f}'
                )

            with st.expander("View uses and warnings"):

                st.markdown("**Documented uses**")
                st.write(row["Uses"])

                st.markdown("**Selected warnings**")
                st.write(row["Selected Warnings"])

                st.markdown("**Original dosage form**")
                st.write(row["Dosage Form"])

                st.caption(
                    f'Medicine ID: {row["Item"]}'
                )

                if row["R09_Risk_Not_Specified"] == 1:
                    st.warning(
                        "Risk not specified does not "
                        "mean risk-free. No specific "
                        "risk was coded or predicted "
                        "from the selected excerpt."
                    )

                if row["Classification_Source"] == "Machine Predicted":
                    st.caption(
                        "Automatically generated risk "
                        "labels have not been "
                        "independently validated."
                    )

    # Bottom pagination controls
    st.divider()
    previous_col, status_col, next_col = st.columns([1, 2, 1])

    previous_col.button(
        "← Previous Page",
        key="previous_page",
        disabled=page == 1,
        on_click=change_page,
        args=(-1,),
        use_container_width=True
    )

    with status_col:
        st.markdown(
            f'<div style="text-align:center">Page {page} of {total_pages}'
            f'<br><small>{start + 1}–{min(end, len(filtered))} '
            f'of {len(filtered)} medicines</small></div>',
            unsafe_allow_html=True
        )

    next_col.button(
        "Next Page →",
        key="next_page",
        disabled=page == total_pages,
        on_click=change_page,
        args=(1,),
        use_container_width=True
    )

# ----------------------------------------
# 15. METHODOLOGY AND LIMITATIONS
# ----------------------------------------

st.divider()

with st.expander("About this system"):

    st.markdown("""
    ### Collection

    300 OTC medicines across five therapeutic groups.

    ### Information organization

    Five facets support structured exploration:
    intended use, intended user, dosage form,
    brand type, and documented safety risk.

    ### Automatic classification

    TF-IDF and multi-label logistic regression
    were used to classify 100 additional medicines
    after training on 200 AI-assisted,
    human-verified reference classifications.

    ### Held-out evaluation

    - Micro F1-score: 89.89%
    - Exact match accuracy: 83.33%
    - Testing sample: 36 medicines

    ### Retrieval

    BM25 with k1 = 1.2 and b = 0.75 ranks
    product names and selected uses and warnings.

    ### Limitations

    - Selected warnings are not complete drug labels.
    - Machine-predicted labels may contain errors.
    - R09 does not indicate absence of risk.
    - R07 had no positive training examples and
      could not be learned by the classifier.
    - Intended-user categories are descriptive,
      not medical eligibility recommendations.
    - The collection is not representative of
      the entire OTC medicine market.
    """)

st.caption(
    "OTC Medicine Explorer | "
    "INFO 202 Academic Project"
)
