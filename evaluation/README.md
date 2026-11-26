
# Automatic Classification Evaluation

This directory contains the experimental results from the supervised multi-label classification of the Documented Safety Risk facet.

## Experimental Design

- Reference dataset: 200 medicines
- Training set: 164 medicines
- Held-out test set: 36 medicines
- Split method: GroupShuffleSplit
- Random state: 42
- Text representation: TF-IDF with unigrams and bigrams
- Classifier: One-vs-Rest logistic regression
- Baseline: Assign Risk Not Specified (R09) to every product

Identical normalized warning texts were grouped to prevent exact warning-text overlap between the training and test sets.

## Evaluation Files

| Filename | Description |
|---|---|
| OTC_Model_Evaluation.csv | Overall classification performance metrics |
| OTC_Baseline_Comparison.csv | Comparison between logistic regression and the majority baseline |
| OTC_Category_Performance.csv | Category-level precision, recall, F1-score, and support |
| OTC_Classification_Errors.csv | Incorrect classifications and associated warning texts |
| OTC_Learned_Features.csv | Highest-weighted positive features for individual risk categories |
| OTC_Heldout_Test_Predictions.csv | Actual and predicted labels for the 36 held-out medicines |

## Key Results

| Metric | Majority Baseline | Logistic Regression |
|---|---:|---:|
| Micro F1-score | 40.00% | 89.89% |
| Exact Match Accuracy | 44.44% | 83.33% |
| Hamming Loss | 14.81% | 2.78% |

The logistic regression model correctly reproduced the complete reference label set for 30 of the 36 held-out medicines.

## Error Analysis

Six held-out medicines contained classification discrepancies.

The observed errors suggest challenges involving:

- Distinguishing adverse outcomes from precautions.
- Recognizing less frequently represented expressions.
- Classifying heterogeneous residual risks.
- Separating contextual meaning from statistical word associations.

These explanations are interpretations of observed errors rather than experimentally established causal explanations.

## Learned Feature Analysis

The learned features demonstrate associations between warning vocabulary and predefined risk categories.

Examples include:

- Liver damage and acetaminophen for organ toxicity.
- Stomach bleeding for bleeding.
- Heart and blood pressure for cardiovascular risks.
- Drowsiness and nervousness for neurological and behavioral risks.

Some learned features also reflect ingredient associations and precautionary language rather than direct adverse outcomes.

This illustrates both the usefulness and limitations of supervised text classification.

## Limitations

- The held-out test set contains only 36 medicines.
- Rare risk categories have limited evaluation support.
- R07 Gastrointestinal had no positive reference examples.
- Reference classifications were AI-assisted and human-verified.
- Exact duplicate warning texts were grouped, but near-duplicate texts may remain.
- Performance on the 100 automatically classified medicines has not been independently measured.
- Learned feature weights do not establish causal relationships.

The evaluation measures agreement with the operational reference classification scheme rather than clinical accuracy.
