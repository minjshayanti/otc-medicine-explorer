# Information Retrieval Evaluation

## Overview

This section documents the evaluation of keyword-based BM25 retrieval and structured faceted browsing using a collection of 300 OTC medicines.

## Evaluation Methodology

- Ten information needs and corresponding search queries.
- Binary relevance judgments (0 = not relevant, 1 = relevant).
- Precision@10 for BM25 retrieval.
- Four selected information needs for comparison with faceted browsing.
- Investigation of AND versus OR logic within the Intended Use facet.

## BM25 Retrieval Results

| Metric | Result |
|---|---:|
| Information needs | 10 |
| Original BM25 mean Precision@10 | 0.51 |
| Browser BM25 mean Precision@10 | 0.48 |
| Overlapping query-document pairs | 88 of 100 |
| Combined BM25 relevance judgments | 112 |

The BM25 implementation used in the deployed browser was evaluated separately to account for differences in tokenization and scoring.

## Faceted Browsing Comparison

| Information Need | BM25 P@10 | Faceted Precision |
|---|---:|---:|
| Q2: Cough relief | 1.00 | 1.00 |
| Q4: Pain relief in capsules | 0.20 | 1.00 |
| Q6: Pain and fever | 0.90 | 1.00 |
| Q9: Pain and stomach irritation | 0.00 | 0.00 |
| Mean | 0.525 | 0.750 |

A total of 36 faceted query-document pairs were manually evaluated, of which 26 were judged relevant.

## Boolean Logic Investigation

| Information Need | OR Results | AND Results | Partial Matches |
|---|---:|---:|---:|
| Pain and fever | 68 | 63 | 5 |
| Pain and upset stomach | 71 | 0 | 71 |

The deployed browser uses OR logic within a facet and AND logic across facets. The alternative AND conditions were evaluated programmatically.

## Files

| File | Description |
|---|---|
| OTC_Test_Queries.csv | Original information needs and search queries |
| OTC_Original_Relevance_Judgments.csv | Original 100 BM25 judgments |
| OTC_Additional_Relevance_Judgments.csv | 12 additional judgments |
| OTC_Combined_Relevance_Judgments.csv | Combined BM25 relevance judgments |
| OTC_Browser_BM25_Results.csv | Evaluated browser BM25 results |
| OTC_BM25_Performance_Comparison.csv | Original and browser BM25 comparison |
| OTC_Faceted_Browser_Results.csv | Reproduced browser result counts |
| OTC_Boolean_Logic_Comparison.csv | AND versus OR experiments |
| OTC_Faceted_Relevance_Judgments.csv | 36 faceted relevance judgments |
| OTC_BM25_vs_Faceted_Performance.csv | Comparative retrieval performance |
| OTC_BM25_Performance_Comparison.png | BM25 comparison visualization |
| OTC_BM25_vs_Faceted_Comparison.png | BM25 versus faceted browsing visualization |

## Reproducibility

The retrieval evaluation notebook contains the implementation, relevance judgments, performance calculations, Boolean logic experiments, and visualization code.

The deployed application uses BM25Okapi from the rank-bm25 library with k1 = 1.2 and b = 0.75.

## Limitations

- The comparison uses four selected information needs and is exploratory.
- Q4 evaluates six faceted results rather than ten.
- Faceted browsing exposes structured metadata that is not independently indexed by BM25.
- Faceted results are ordered by item ID rather than relevance score.
- Upset stomach is an approximate representation of stomach irritation.
- Additional BM25 relevance judgments underwent AI-assisted consistency review and human approval.
- The original capsule relevance judgments contain a potential inconsistency involving caplets.
- Recall cannot be reliably estimated without exhaustive relevance judgments.
- Retrieval relevance does not establish clinical suitability or medication safety.

The system is intended for educational information organization and retrieval, not medical recommendations.
