
# Data Dictionary

## 1. Dataset Overview

| Property | Description |
|---|---|
| Filename | OTC_Final_Classified_300.csv |
| File format | CSV |
| Number of resources | 300 |
| Number of columns | 26 |
| Unit of observation | Individual OTC medicine product |
| Primary key | Item |
| Therapeutic groups | 5 |
| Primary facets | 5 |
| Reference classifications | 200 |
| Machine-generated classifications | 100 |

## 2. Dataset Structure

The final dataset consists of four components:

- 12 original descriptive metadata columns
- 3 standardized facet columns
- 9 binary safety risk classification columns
- 2 classification summary and provenance columns

## 3. Original Descriptive Metadata

| Column | Logical Data Type | Description |
|---|---|---|
| Groups | Categorical | Primary therapeutic group assigned to the product. |
| Item | Integer | Unique medicine identifier and primary key. |
| Product | Text | Recorded medicine product name. |
| Intended Use | Text | Original therapeutic purpose descriptions. May contain multiple values. |
| Intended User | Categorical | Original documented target population. |
| Dosage Form | Categorical | Original formulation or delivery description. |
| Brand Type | Categorical | Recorded commercial brand classification. |
| Active Ingredient | Text | Recorded active ingredients and strengths where available. |
| Uses | Text | Selected descriptions of therapeutic uses. |
| Selected Warnings | Text | Selected medication warning excerpts used for risk classification. |
| Selected texts (Uses + Warnings) | Text | Combined therapeutic-use and warning text used for information retrieval. |
| Initial Codes | Text | Preliminary coding information retained from the original dataset. Not used as reference labels for the final classifier. |

## 4. Standardized Facet Columns

| Column | Logical Data Type | Description | Transformation |
|---|---|---|---|
| Intended Use Tags | Multi-value categorical text | Standardized therapeutic-purpose tags. | Split compound values, normalize capitalization, consolidate selected synonyms, and remove duplicate tags. |
| Intended User Standardized | Categorical | Standardized target population description. | Normalize inconsistent formatting while retaining population and age qualifiers. |
| Dosage Form Family | Categorical | Standardized formulation or delivery family. | Consolidate 52 original descriptions into 11 families. |

### Standardized Vocabulary Sizes

| Facet | Number of Categories | Assignment |
|---|---:|---|
| Intended Use Tags | 50 | Multi-label |
| Intended User Standardized | 11 | Single-label |
| Dosage Form Family | 11 | Single-label |
| Brand Type | 4 | Single-label |
| Documented Safety Risk | 9 | Multi-label with an exclusive residual category |

Intended Use Tags are stored as semicolon-separated values in the CSV file.

Brand Type is used directly from the original metadata.

## 5. Invented Safety Risk Facet

The nine safety risk columns represent binary category membership.

A value of 1 indicates that the category was assigned.

A value of 0 indicates that the category was not assigned.

A value of 0 must not be interpreted as evidence that the corresponding medical risk is absent.

| Column | Type | Definition | Assigned Products |
|---|---|---|---:|
| R01_Organ_Toxicity | Binary integer | Explicit internal organ damage or toxicity. | 31 |
| R02_Bleeding | Binary integer | Explicit bleeding-related adverse outcomes. | 36 |
| R03_Cardiovascular | Binary integer | Explicit cardiovascular adverse outcomes. | 20 |
| R04_Allergic_Reactions | Binary integer | Explicit allergic adverse reactions. | 4 |
| R05_Neurological_Behavioral | Binary integer | Explicit neurological, alertness, or behavioral adverse outcomes. | 53 |
| R06_Skin_Local_Tissue | Binary integer | Explicit skin or local tissue adverse outcomes. | 34 |
| R07_Gastrointestinal | Binary integer | Explicit non-bleeding gastrointestinal adverse outcomes. | 0 |
| R08_Other_Documented_Risk | Binary integer | Explicit adverse outcomes not covered by R01–R07. | 24 |
| R09_Risk_Not_Specified | Binary integer | No specific adverse outcome coded or predicted. | 158 |

The assigned product counts combine reference classifications and machine predictions.

Multiple specific risk categories may be assigned to a single medicine.

R09 is mutually exclusive with R01–R08.

R07 had no positive reference examples and could not be learned by the automatic classifier.

Detailed category definitions and inclusion and exclusion rules are available in [Safety Risk Codebook](Safety_Risk_Codebook.md).

## 6. Classification Summary and Provenance

| Column | Logical Data Type | Description |
|---|---|---|
| Risk_Codes | Multi-value categorical text | Semicolon-separated risk codes derived from the nine binary classification columns. |
| Classification_Source | Categorical | Identifies how the risk classification was generated. |

### Classification_Source Values

| Value | Count | Meaning |
|---|---:|---|
| AI-Assisted, Human-Verified | 200 | Reference classifications generated with AI assistance and human verification. |
| Machine Predicted | 100 | Classifications generated by the trained multi-label logistic regression model. |

The 100 machine-generated classifications have not been independently validated.

## 7. Example Resource

The following example illustrates how descriptive metadata and the invented facet are combined.

| Field | Example Value |
|---|---|
| Item | 2 |
| Product | Advil |
| Groups | Pain and Fever |
| Active Ingredient | Ibuprofen 200 mg |
| Intended Use | Pain; Fever |
| Intended User | Adult |
| Dosage Form | Tablet/Caplet |
| Dosage Form Family | Tablets and Caplets |
| Brand Type | National brand |
| R02_Bleeding | 1 |
| R03_Cardiovascular | 1 |
| Risk_Codes | R02; R03 |
| Classification_Source | AI-Assisted, Human-Verified |

## 8. Data Quality and Integrity Rules

| Validation Rule | Result |
|---|---|
| Exactly 300 medicine records | Passed |
| Exactly 26 columns | Passed |
| Unique medicine identifiers | Passed |
| 60 medicines per therapeutic group | Passed |
| No missing risk labels | Passed |
| Risk columns contain only 0 or 1 | Passed |
| Every medicine has at least one risk-category assignment | Passed |
| R09 does not coexist with specific risk categories | Passed |
| Classification provenance retained | Passed |

These validation checks establish structural integrity rather than clinical accuracy.

## 9. Dataset Lineage

The final dataset was constructed through the following stages:

| Stage | Dataset | Purpose |
|---|---|---|
| 1 | Original OTC medicine dataset | Source collection |
| 2 | OTC_Medicines_Standardized.csv | Cleaned metadata and standardized facets |
| 3 | OTC_Labeled_200.csv | AI-assisted, human-verified reference classifications |
| 4 | OTC_Unlabeled_100.csv | Remaining medicines selected for automatic classification |
| 5 | OTC_Machine_Predicted_100.csv | Automatically generated risk classifications |
| 6 | OTC_Final_Classified_300.csv | Integrated dataset used by the browser |

The final integration uses Item as the unique join key.

## 10. Field Usage Within the Application

| Application Function | Dataset Fields |
|---|---|
| Therapeutic group navigation | Groups |
| Intended-use filtering | Intended Use Tags |
| Intended-user filtering | Intended User Standardized |
| Dosage-form filtering | Dosage Form Family |
| Brand-type filtering | Brand Type |
| Safety-risk filtering | R01–R09 binary columns |
| Classification provenance filtering | Classification_Source |
| BM25 retrieval | Product; Selected texts (Uses + Warnings) |
| Medicine result cards | Product; Active Ingredient; descriptive facets; risk labels |
| Expanded medicine information | Uses; Selected Warnings; Dosage Form; Item |
| Dynamic distribution charts | Groups; R01–R09 binary columns |

## 11. Interpretation and Limitations

- The dataset represents a selected collection rather than the entire OTC medicine market.
- Therapeutic groups were deliberately balanced at 60 products per group.
- Selected warnings are excerpts rather than complete medication labels.
- Standardization may obscure distinctions in the original metadata.
- Reference labels were AI-assisted and human-verified.
- Machine-generated labels may contain classification errors.
- Binary risk assignments do not represent risk severity or probability.
- R09 does not indicate absence of medical risk.
- R07 contains no positive assignments.
- Intended-user values do not establish clinical eligibility.

The dataset is intended for academic information organization and retrieval research, not medical decision-making.
