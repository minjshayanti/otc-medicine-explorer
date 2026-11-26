
# Faceted Taxonomy and Classificatory Principles

## 1. Organizing System

### What is being organized?

The organizing system contains 300 over-the-counter (OTC) medicine products distributed equally across five therapeutic groups:

- Pain and Fever
- Cough Cold & Flu
- Allergy & Respiratory
- Digestive & Heartburn
- Skin & Topical

### Why organize these resources?

Medication information contains multiple dimensions, including therapeutic purposes, intended populations, formulations, ingredients, and safety warnings.

A single hierarchical classification or keyword search may not adequately support information needs involving multiple dimensions simultaneously.

The system therefore combines faceted classification and ranked text retrieval to support both structured exploration and free-text discovery.

### Intended users

The system is designed for educational exploration by individuals interested in comparing documented medication characteristics.

It is not designed to recommend medicines or determine clinical suitability.

## 2. Resource Granularity

The unit of organization is an individual medicine product rather than an active ingredient, brand, or therapeutic condition.

Products containing the same active ingredient may differ in:

- Dosage form
- Strength
- Intended population
- Therapeutic purpose
- Selected warnings

Each product is assigned a unique item identifier.

Products with similar names are retained as distinct resources when their formulations or documented characteristics differ.

This granularity preserves meaningful product-level distinctions but may introduce redundancy among closely related formulations.

## 3. Faceted Taxonomy Design

The organizing system contains five primary facets.

| Facet | Classificatory Principle | Cardinality | Origin |
|---|---|---|---|
| Intended Use | Documented therapeutic purpose | Multi-label | Standardized metadata |
| Intended User | Documented target population | Single-label | Standardized metadata |
| Dosage Form | Physical formulation or delivery family | Single-label | Standardized metadata |
| Brand Type | Brand classification | Single-label | Existing metadata |
| Documented Safety Risk | Explicit adverse outcomes in selected warnings | Multi-label | Invented facet |

Therapeutic groups provide an additional navigation structure.

Classification provenance is retained as administrative metadata rather than an intrinsic characteristic of the medicine.

## 4. Individual Facet Definitions

### 4.1 Intended Use

**Classificatory principle:** The therapeutic purposes documented in the product metadata.

The original intended-use descriptions were standardized into individual tags.

The standardization process included:

- Splitting compound descriptions into individual tags.
- Normalizing capitalization.
- Consolidating selected synonymous expressions.
- Removing duplicate tags within individual products.

The resulting vocabulary contains 50 distinct intended-use tags.

**Examples:** Pain, fever, allergy, cough, heartburn, and cold.

This facet supports multiple values because a single product may address multiple symptoms.

**Design limitation:** The vocabulary contains both broad therapeutic concepts and specific symptoms. Some values, such as topical, describe administration rather than therapeutic purpose. This reduces conceptual consistency.

A future revision could separate therapeutic purpose, symptom, and administration route into distinct dimensions.

### 4.2 Intended User

**Classificatory principle:** The population documented in the product metadata.

The original population descriptions were standardized into 11 categories.

**Examples:**

- Adult
- Child
- Adult / 12+
- Adult / Child
- Adult / Child 6+

Combined population descriptions are preserved to avoid removing age-related information during standardization.

Each medicine receives one standardized population description.

**Design limitation:** Although each product has one assigned value, the underlying population categories overlap conceptually.

For example, Adult and Adult / 12+ are not mutually exclusive populations.

A future system could represent minimum age and intended population as separate structured attributes.

The current categories must not be interpreted as clinical eligibility recommendations.

### 4.3 Dosage Form

**Classificatory principle:** The standardized formulation or delivery family associated with each product.

The original 52 dosage-form descriptions were consolidated into 11 families.

| Dosage Form Family | Product Count |
|---|---:|
| Tablets and Caplets | 102 |
| Creams and Semisolids | 53 |
| Liquids | 44 |
| Capsules | 23 |
| Sprays and Rinses | 22 |
| Powders and Granules | 17 |
| Drops | 13 |
| Washes and Cleansers | 9 |
| Lozenges and Chews | 8 |
| External Applications | 7 |
| Rectal Preparations | 2 |
| Total | 300 |

The original dosage-form descriptions are retained alongside the standardized families.

This supports simplified navigation without permanently discarding the original metadata.

**Design limitation:** Some families describe physical form, while others describe administration or delivery methods.

Consequently, the categories are operationally exclusive in the dataset but not perfectly exclusive at the conceptual level.

A more rigorous taxonomy could separate physical form, administration route, and delivery mechanism.

### 4.4 Brand Type

**Classificatory principle:** The brand classification recorded in the original metadata.

| Brand Type | Product Count |
|---|---:|
| National brand | 270 |
| Store brand | 27 |
| Generic | 2 |
| Unknown | 1 |
| Total | 300 |

Each product receives one brand-type value.

The Unknown category preserves uncertainty instead of forcing an unsupported classification.

**Design limitation:** The distinction between generic and store-brand products may depend on how brand ownership and commercial identity are defined.

The distribution also reflects the composition of the selected collection rather than the overall OTC medicine market.

### 4.5 Documented Safety Risk

**Classificatory principle:** Explicit adverse outcomes documented in selected medication warning excerpts.

This invented facet was developed because the original metadata contained warning texts but did not provide a standardized classification of adverse outcomes.

| Code | Category |
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

A product may receive multiple specific risk labels when its selected warning excerpt documents multiple adverse outcomes.

Classification is based on explicit textual evidence rather than inferred pharmacological properties.

Precautions, pre-existing conditions, usage restrictions, and interaction warnings are not automatically classified as adverse outcomes.

R09 is mutually exclusive with R01–R08.

Detailed inclusion and exclusion criteria are documented in the separate safety risk codebook.

## 5. Mutual Exclusivity and Category Overlap

Mutual exclusivity must be considered at two levels:

1. Whether each resource receives only one category assignment.
2. Whether the categories themselves represent conceptually distinct sets.

These two properties are not equivalent.

| Facet | Assignment Exclusivity | Conceptual Exclusivity |
|---|---|---|
| Intended Use | No | Partial |
| Intended User | Yes | Partial |
| Dosage Form | Yes | Partial |
| Brand Type | Yes | Intended, but potentially ambiguous |
| Documented Safety Risk | No | Intended at the adverse-outcome level |

Multi-label classification is necessary for Intended Use and Documented Safety Risk because individual medicines can have multiple therapeutic purposes and adverse outcomes.

For the safety risk facet, the goal is to classify each explicit adverse outcome into the most appropriate category while allowing multiple distinct outcomes per product.

For example, gastrointestinal bleeding is classified as Bleeding rather than simultaneously as Bleeding and Gastrointestinal.

This decision reduces redundant labeling but prioritizes one interpretation of the adverse outcome over another.

## 6. Orthogonality Between Facets

The five facets are designed to represent different descriptive dimensions:

- Intended Use: What is the product used for?
- Intended User: For whom is it documented?
- Dosage Form: In what form is it delivered?
- Brand Type: How is it commercially classified?
- Documented Safety Risk: What adverse outcomes are documented?

Conceptual independence does not necessarily imply statistical independence.

For example, particular dosage forms may be associated with specific therapeutic purposes, while particular active ingredients may be associated with specific warning categories.

These relationships do not automatically invalidate the faceted design.

However, some existing metadata values introduce conceptual overlap. The presence of topical within intended-use tags is one example.

The system therefore approximates orthogonality rather than claiming complete independence between facets.

## 7. Classical and Graded Category Membership

The implemented taxonomy primarily uses discrete category assignments.

For example, a product receives the Bleeding label when its selected warning explicitly documents bleeding as an adverse outcome.

The intended necessary condition is explicit textual evidence. The sufficient condition is an adverse outcome that satisfies the category definition and its exclusion rules.

However, not all classification decisions are equally straightforward.

Some adverse outcomes have strong category membership, while others are ambiguous or potentially belong to multiple conceptual categories.

For example:

- Liver damage is a clear example of organ toxicity.
- Stomach bleeding could conceptually belong to both bleeding and gastrointestinal categories.
- Bitter taste does not fit neatly into the primary risk categories.

These examples illustrate the tension between classical rule-based classification and more flexible prototype-based or graded interpretations.

The implemented system resolves these ambiguities through explicit coding rules rather than graded membership scores.

Machine learning introduces statistical uncertainty, but the final browser presents discrete predicted labels rather than probabilities.

## 8. Residual Categories

The taxonomy includes three important forms of residual classification.

### Unknown Brand Type

This category preserves uncertainty in the original metadata.

It prevents unsupported assumptions about commercial identity.

### R08: Other Documented Risk

This category accommodates explicit adverse outcomes that do not fit the primary safety risk categories.

Examples include choking, bitter taste, worsening congestion, and Reye syndrome.

Its heterogeneous membership reveals limitations in the coverage of the taxonomy.

The classification experiment also suggests that this category is comparatively difficult for the model to learn.

### R09: Risk Not Specified

This category represents the absence of a specific coded or predicted adverse outcome in the selected warning excerpt.

It does not represent the absence of medication risk.

The complete collection contains 158 products assigned to R09.

Of these:

- 101 are AI-assisted, human-verified classifications.
- 57 are machine-predicted classifications.

For reference classifications, R09 reflects the coding interpretation of the available warning text.

For machine predictions, R09 is assigned when the model predicts no specific risk category.

These two mechanisms must be distinguished because the latter may also reflect classification errors.

## 9. Faceted Navigation and Retrieval

The interactive browser implements:

- OR logic within a facet.
- AND logic across different facets.
- Multi-select category filtering.
- Dynamic result counts.
- BM25-ranked text retrieval.
- Classification provenance filtering.

For example, selecting pain and fever within Intended Use retrieves products associated with either therapeutic purpose.

Adding Tablets and Caplets as a dosage-form filter restricts those results to the selected formulation family.

This approach supports progressive refinement without requiring users to navigate a single predetermined hierarchy.

Keyword retrieval complements faceted navigation when users have specific terms that are not represented directly in the taxonomy.

## 10. Classification Trade-offs and Limitations

The taxonomy simplifies medication information to support consistent organization and navigation.

However, this simplification also excludes important dimensions.

The safety risk facet does not systematically represent:

- Risk severity
- Probability of adverse outcomes
- Dose-dependent risk
- Duration-dependent risk
- Drug interactions
- Contraindications
- Individual medical history

Consequently, medicines assigned the same risk category may have substantially different clinical characteristics.

The taxonomy also depends on selected warning excerpts rather than complete medication labels.

The classification experiment introduces additional limitations:

- Reference classifications were AI-assisted and human-verified.
- The 100 machine-generated classifications remain independently unvalidated.
- R07 had no positive training examples.
- Rare categories have limited evaluation support.
- Statistical associations may be mistaken for explicit adverse outcomes.

These limitations demonstrate that classification is not a neutral representation of reality.

The categories reflect decisions about which distinctions are useful, which information is retained, and which complexities are excluded.

## 11. Future Improvements

Potential improvements include:

1. Separate therapeutic purpose from symptom and administration route.
2. Represent intended population and minimum age independently.
3. Separate physical formulation from delivery mechanism.
4. Refine heterogeneous residual risk categories.
5. Distinguish warning-text limitations from model uncertainty.
6. Expand reference classifications for rare risk categories.
7. Conduct independent human coding and agreement analysis.
8. Evaluate the browser with representative users.
9. Introduce contextual retrieval that distinguishes therapeutic uses from warnings.

## 12. Theoretical Framework

The taxonomy is informed by three information organization perspectives.

### Glushko: The Discipline of Organizing

The project considers resource granularity, organizing principles, descriptive properties, category design, and the interactions supported by an organizing system.

### Hearst: Faceted Navigation

The browser applies multiple descriptive dimensions to support flexible exploration and progressive refinement of information needs.

### Bowker and Star: Sorting Things Out

The project examines how classification decisions make certain distinctions visible while obscuring others.

Residual categories, ambiguous category boundaries, and incomplete warning information illustrate the consequences of imposing a standardized classification scheme on complex resources.

Specific connections to the assigned readings and verified citations will be developed in the final report.
