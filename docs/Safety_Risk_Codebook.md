
# Documented Safety Risk: Classification Codebook

## 1. Purpose

The Documented Safety Risk facet organizes explicit adverse outcomes described in selected OTC medication warning excerpts.

This facet was developed specifically for the OTC Medicine Explorer project because the original dataset contained unstructured warning texts but no standardized safety risk classification.

The objective is to support information organization and retrieval, not to establish clinical safety profiles or recommend medications.

## 2. Classification Framework

| Property | Definition |
|---|---|
| Facet name | Documented Safety Risk |
| Source field | Selected Warnings |
| Unit of classification | Individual medicine product |
| Classification approach | Multi-label |
| Number of categories | 9 |
| Membership representation | Binary: 0 or 1 |
| Reference sample | 200 medicines |
| Automatically classified sample | 100 medicines |

A medicine may receive multiple specific risk labels when multiple distinct adverse outcomes are explicitly documented.

## 3. General Coding Rules

1. Classify only adverse outcomes explicitly documented in the Selected Warnings field.

2. Do not infer adverse outcomes from active ingredients, therapeutic groups, product names, or general pharmacological knowledge.

3. Do not classify a pre-existing medical condition as an adverse outcome unless the warning explicitly identifies it as a potential consequence of medication use.

4. Precautions, dosage restrictions, age restrictions, and interaction warnings do not independently qualify as adverse outcomes.

5. Assign multiple labels when the warning documents multiple distinct adverse outcomes.

6. Assign each individual adverse outcome to the most appropriate category according to the inclusion and exclusion rules.

7. Use R08 when an explicit adverse outcome does not fit R01–R07.

8. Use R09 when an available warning excerpt does not explicitly document a specific adverse outcome.

9. R09 cannot coexist with R01–R08.

10. Missing warning text should be treated as missing information rather than automatically classified as R09.

11. The Initial Codes field is not used as classification ground truth because exploratory inspection identified inconsistencies.

## 4. Category Definitions

### R01 — Organ Toxicity

**Definition:** Explicit damage or toxicity affecting internal organs, particularly the liver or kidneys.

**Include:**
- Liver damage
- Liver toxicity
- Kidney damage
- Kidney toxicity

**Exclude:**
- Pre-existing liver or kidney disease
- Instructions to consult a doctor because of organ disease
- Cardiovascular outcomes classified under R03

**Example:** Excessive acetaminophen may cause severe liver damage.

### R02 — Bleeding

**Definition:** Explicit bleeding-related adverse outcomes.

**Include:**
- Stomach bleeding
- Gastrointestinal bleeding
- Other explicitly documented bleeding outcomes

**Exclude:**
- Pre-existing bleeding symptoms
- Bloody stool mentioned only as a contraindication
- Gastrointestinal discomfort without bleeding

**Boundary rule:** Gastrointestinal bleeding is assigned to R02 rather than R07.

**Example:** NSAIDs may cause severe stomach bleeding.

### R03 — Cardiovascular

**Definition:** Explicit adverse outcomes affecting the cardiovascular system.

**Include:**
- Heart attack
- Heart failure
- Stroke
- Increased blood pressure
- Serious heart problems
- Explicit cardiovascular events

**Exclude:**
- Pre-existing heart disease
- Pre-existing hypertension
- Instructions to consult a doctor without an explicit adverse outcome

**Example:** Excess loperamide can cause serious heart problems.

### R04 — Allergic Reactions

**Definition:** Explicit adverse outcomes identified as allergic reactions.

**Include:**
- Allergic reactions
- Severe allergic reactions
- Explicitly documented hypersensitivity reactions

**Exclude:**
- Pre-existing allergies
- Instructions to avoid a product because of an existing allergy
- Skin irritation without explicit identification as an allergic reaction

**Example:** Naproxen may cause severe allergic reactions.

### R05 — Neurological and Behavioral

**Definition:** Explicit adverse outcomes affecting alertness, neurological functioning, or behavior.

**Include:**
- Drowsiness
- Dizziness
- Nervousness
- Sleeplessness

**Exclude:**
- Instructions to avoid driving without an explicit adverse outcome
- Instructions to avoid sleeping while using a product
- Alcohol or sedative restrictions without a documented adverse outcome

**Example:** Caffeine may cause nervousness.

### R06 — Skin and Local Tissue

**Definition:** Explicit adverse outcomes affecting skin or local tissues.

**Include:**
- Skin irritation
- Severe skin reactions
- Burns
- Local tissue irritation or damage

**Exclude:**
- External-use instructions
- Instructions to avoid contact with eyes
- Existing skin conditions
- Reactions explicitly identified as allergic, classified under R04

**Example:** Heat wraps may cause burns.

### R07 — Gastrointestinal

**Definition:** Explicit non-bleeding adverse outcomes affecting gastrointestinal functioning.

**Include:**
- Nausea
- Vomiting
- Other explicitly documented gastrointestinal adverse effects

**Exclude:**
- Gastrointestinal symptoms that the medicine is intended to treat
- Existing digestive conditions
- Gastrointestinal bleeding, classified under R02

**Classification limitation:** No positive R07 examples were identified in the 200 reference classifications. Consequently, the automatic classifier could not learn this category.

The category is retained to preserve the conceptual coverage of the taxonomy.

### R08 — Other Documented Risk

**Definition:** An explicit adverse outcome that does not satisfy the definitions of R01–R07.

**Include:**
- Choking
- Bitter taste
- Worsening congestion
- Reye syndrome
- Other explicitly documented outcomes outside the primary categories

**Exclude:**
- General precautions without an explicit adverse outcome
- Dosage restrictions alone
- Age restrictions alone
- Pre-existing conditions
- Outcomes already covered by R01–R07

**Example:** Prolonged use may worsen congestion.

**Design limitation:** This category contains heterogeneous outcomes that may not share a consistent vocabulary or underlying mechanism.

### R09 — Risk Not Specified

**Definition:** No specific adverse outcome is identified in the available selected warning excerpt under the coding rules.

**Include:**
- General dosage instructions
- Precautions without an explicit adverse outcome
- Age restrictions
- Interaction restrictions without a documented adverse outcome
- Instructions to consult a healthcare professional without an explicit adverse outcome

**Exclude:**
- Any excerpt containing an explicit adverse outcome classified under R01–R08
- Missing warning text

**Example:** Do not exceed the recommended dose; consult a doctor if symptoms persist.

**Exclusivity rule:** R09 cannot coexist with R01–R08.

**Important:** R09 does not indicate that a medicine is safe or risk-free.

For machine-generated classifications, R09 is derived when the model predicts no specific risk category. This may reflect either the warning content or a model classification error.

## 5. Classification Decision Process

1. Read the complete selected warning excerpt.

2. Determine whether an explicit adverse outcome is documented.

3. If no explicit adverse outcome is documented, assign R09.

4. If an explicit adverse outcome is documented, compare it against R01–R07.

5. If it does not satisfy any primary category definition, assign R08.

6. Repeat for each distinct adverse outcome.

7. Verify that R09 does not coexist with any specific risk label.

8. Record supporting textual evidence and relevant coding notes.

## 6. Worked Classification Examples

| Product | Documented Warning | Reference Codes |
|---|---|---|
| Advil Dual Action | Severe stomach bleeding, cardiovascular events, and liver damage | R01; R02; R03 |
| Excedrin Tension Headache | Liver damage and nervousness | R01; R05 |
| ThermaCare HeatWraps | May cause burns | R06 |
| Vicks Sinex Severe Nasal Spray | Prolonged use may worsen congestion | R08 |
| Astepro Children's Allergy Nasal Spray | Drowsiness or bitter taste | R05; R08 |
| Imodium Multi-Symptom Relief | Serious heart problems; avoid use with bloody stool | R03 |

Warning descriptions in this table are abbreviated for illustration. Classification is based on the complete selected warning excerpts in the dataset.

## 7. Reference Classification Procedure

A stratified sample of 200 medicines was selected from the 300-medicine collection.

Each of the five therapeutic groups contributed 40 medicines.

An initial pilot of 20 medicines was used to apply and examine the coding framework.

The remaining 180 sampled medicines were subsequently classified.

Reference labels were generated with AI assistance and human verification.

The resulting reference dataset contains:

- Unique medicine identifiers
- Selected warning excerpts
- Nine binary risk-category columns
- Supporting evidence
- Coding notes

Validation checks confirmed:

- No duplicate medicine identifiers
- No missing risk labels
- No invalid category codes
- No conflicts between R09 and specific risk categories

These checks establish structural consistency, not independent clinical or inter-annotator validity.

## 8. Classification Distribution

| Category | Reference Sample (200) | Machine Predicted (100) | Combined (300) |
|---|---:|---:|---:|
| R01 Organ toxicity | 20 | 11 | 31 |
| R02 Bleeding | 28 | 8 | 36 |
| R03 Cardiovascular | 16 | 4 | 20 |
| R04 Allergic reactions | 3 | 1 | 4 |
| R05 Neurological and behavioral | 39 | 14 | 53 |
| R06 Skin and local tissue | 19 | 15 | 34 |
| R07 Gastrointestinal | 0 | 0 | 0 |
| R08 Other documented risk | 20 | 4 | 24 |
| R09 Risk not specified | 101 | 57 | 158 |

Counts are not mutually exclusive across specific risk categories because the facet supports multi-label classification.

## 9. Quality Control and Limitations

The reference classifications were AI-assisted and human-verified rather than independently hand-coded.

Independent inter-annotator agreement was not measured.

The 100 automatically generated classifications have not been independently validated.

Rare categories have limited training and evaluation support.

R07 could not be learned because no positive reference examples were available.

The classification scheme does not systematically represent risk severity, probability, dosage dependence, contraindications, or individual medical circumstances.

The codebook should therefore be interpreted as an operational framework for organizing selected warning texts rather than a comprehensive clinical safety taxonomy.

## 10. Future Revisions

Future development could include:

- Independent human annotation and agreement analysis.
- Additional examples for underrepresented categories.
- Refinement of heterogeneous residual categories.
- More explicit separation of adverse outcomes and precautions.
- Separate representation of risk severity and contextual conditions.
- Distinguishing insufficient source information from model uncertainty.
- Evaluation using complete medication labels.
