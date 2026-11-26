
# 💊 OTC Medicine Explorer

### A Faceted Information Organization and Retrieval System

**UC Berkeley | School of Information | INFO 202 Final Project**

[Launch Live Application](https://otc-medicine-explorer.streamlit.app/)

---

## Project Overview

OTC Medicine Explorer is an interactive information organization and retrieval system designed to help users navigate a collection of 300 over-the-counter (OTC) medicines.

Traditional keyword search can make it difficult to distinguish therapeutic uses, product characteristics, and documented safety warnings. This project explores how faceted classification, machine learning, and ranked text retrieval can complement one another to support structured information discovery.

## Key Features

- Interactive faceted navigation
- Multi-select filtering across five facets
- Dynamic result counts and distribution charts
- BM25-ranked keyword search
- Expandable medicine information cards
- Automatic multi-label risk classification
- Transparent classification provenance
- Publicly accessible web application

## Dataset

The collection contains 300 OTC medicine products organized into five therapeutic groups.

| Therapeutic Group | Products |
|---|---:|
| Pain and Fever | 60 |
| Cough Cold & Flu | 60 |
| Allergy & Respiratory | 60 |
| Digestive & Heartburn | 60 |
| Skin & Topical | 60 |
| **Total** | **300** |

The final dataset contains 26 columns, including original product metadata, standardized facets, risk classifications, and classification provenance.

## Faceted Taxonomy

| Facet | Classificatory Principle |
|---|---|
| Intended Use | Therapeutic purpose |
| Intended User | Documented target population |
| Dosage Form | Standardized formulation family |
| Brand Type | Brand classification |
| Documented Safety Risk | Explicit adverse outcomes in selected warning texts |

The browser uses OR logic within each facet and AND logic across different facets.

Therapeutic groups provide additional navigation, while classification provenance allows users to distinguish reference labels from machine predictions.

### Invented Facet: Documented Safety Risk

This facet was developed to organize adverse outcomes documented in selected medication warning excerpts.

| Code | Risk Category |
|---|---|
| R01 | Organ toxicity |
| R02 | Bleeding |
| R03 | Cardiovascular |
| R04 | Allergic reactions |
| R05 | Neurological and behavioral |
| R06 | Skin and local tissue |
| R07 | Gastrointestinal |
| R08 | Other documented risk |
| R09 | Risk not specified |

The facet supports multi-label classification because a medicine may have multiple documented risks.

R08 accommodates explicit adverse outcomes that do not fit the other defined categories.

R09 is mutually exclusive with all specific risk categories. It indicates that no specific adverse outcome was coded or predicted from the selected warning excerpt, not that the medicine is risk-free.

## Machine Learning

A supervised multi-label classification pipeline was developed to scale the invented safety risk facet across the collection.

### Classification Workflow

1. Stratified sampling of 200 medicines.
2. AI-assisted labeling with human verification.
3. Grouped training and testing split to prevent exact normalized warning-text overlap.
4. TF-IDF feature extraction using unigrams and bigrams.
5. One-vs-Rest logistic regression.
6. Held-out evaluation and baseline comparison.
7. Classification error and learned feature analysis.
8. Retraining on all 200 reference examples.
9. Automatic classification of the remaining 100 medicines.

### Model Performance

The model was evaluated on 36 held-out medicines.

| Evaluation Metric | Result |
|---|---:|
| Micro Precision | 88.89% |
| Micro Recall | 90.91% |
| Micro F1-score | 89.89% |
| Macro F1-score (Supported Categories) | 86.75% |
| Exact Match Accuracy | 83.33% |
| Hamming Loss | 2.78% |

### Baseline Comparison

| Metric | Majority Baseline | Logistic Regression |
|---|---:|---:|
| Micro F1-score | 40.00% | 89.89% |
| Exact Match Accuracy | 44.44% | 83.33% |
| Hamming Loss | 14.81% | 2.78% |

The final model was subsequently trained on all 200 reference classifications and applied to the remaining 100 medicines.

### Classification Provenance

- 200 AI-assisted, human-verified classifications
- 100 automatically predicted classifications

## Information Retrieval

The application integrates BM25-ranked keyword search across product names and selected uses and warnings.

BM25 parameters:

- k1 = 1.2
- b = 0.75

An earlier retrieval experiment using the medicine collection evaluated 10 queries with 100 relevance judgments and achieved a mean Precision@10 of 0.51.

Consistency between the earlier experimental implementation and the deployed browser remains to be verified.

Faceted navigation complements keyword retrieval by allowing users to constrain results using structured product attributes.

## System Architecture

```text
OTC Medicine Collection
          |
          v
Data Cleaning and Standardization
          |
          v
Faceted Taxonomy Development
          |
          v
Reference Classification (200)
          |
          v
TF-IDF + Logistic Regression
          |
          v
Automatic Classification (100)
          |
          v
Integrated Dataset (300)
          |
          v
Faceted Filtering + BM25 Retrieval
          |
          v
Streamlit Web Application
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Text Representation | TF-IDF |
| Information Retrieval | BM25 |
| Application Framework | Streamlit |
| Development Environment | Google Colab |
| Version Control | GitHub |
| Deployment | Streamlit Community Cloud |

## Repository Structure

```text
otc-medicine-explorer/
├── app.py
├── requirements.txt
├── OTC_Final_Classified_300.csv
└── README.md
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/minjshayanti/otc-medicine-explorer.git
cd otc-medicine-explorer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

## Limitations and Responsible Use

- The collection is limited to 300 selected OTC medicine products.
- Selected warning excerpts do not represent complete medication labels.
- Reference classifications were AI-assisted and human-verified rather than independently hand-coded.
- Automatically predicted risk classifications have not been independently validated.
- Gastrointestinal risk (R07) had no positive training examples and could not be learned.
- Risk not specified (R09) does not indicate absence of risk.
- Keyword retrieval may match safety warnings rather than therapeutic uses.
- Intended-user categories are descriptive and do not establish medical eligibility.
- The application is intended for educational and information organization purposes only.

**This application does not provide medical advice or medication recommendations.**

## Academic Context

Developed as part of the INFO 202 course at the UC Berkeley School of Information.

The project explores faceted classification, information organization, supervised machine learning, information retrieval, and the limitations of classification systems.

## Author

Shayanti Minj

Master of Information Management and Systems (MIMS)

University of California, Berkeley
