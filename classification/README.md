
# Safety Risk Classification Datasets

This directory contains the reference and automatically generated classifications for the invented Documented Safety Risk facet.

## Files

- OTC_Labeled_200.csv: Stratified sample of 200 medicines with AI-assisted, human-verified risk classifications, supporting evidence, and coding notes.
- OTC_Unlabeled_100.csv: Remaining 100 medicines before automatic classification.
- OTC_Risk_Category_Distribution.csv: Distribution of risk categories in the reference sample.
- OTC_Machine_Predicted_100.csv: Automatically generated classifications for the remaining 100 medicines.

## Sampling Method

The reference sample contains 40 medicines from each of the five therapeutic groups.

Stratified random sampling was performed using random_state=42.

The remaining 100 medicines contain 20 products from each therapeutic group.

## Classification Method

The automatic classification pipeline uses TF-IDF text representation and One-vs-Rest logistic regression.

The model was evaluated using a grouped held-out split of the 200 reference examples before being retrained on all 200 examples.

The remaining 100 medicines were subsequently classified using the retrained model.

## Related Documentation

- [Safety Risk Codebook](../docs/Safety_Risk_Codebook.md)
- [Faceted Taxonomy](../docs/Faceted_Taxonomy.md)
- [Data Dictionary](../docs/Data_Dictionary.md)

## Limitations

Reference labels were AI-assisted and human-verified rather than independently hand-coded.

The 100 machine-generated classifications have not been independently validated.

The classifications represent selected warning excerpts and should not be interpreted as comprehensive medication safety assessments.
