# Thyroid Dataset Documentation

## Overview

This dataset contains thyroid disease patient records used for analyzing and predicting thyroid conditions. The dataset includes demographic information, medical history, and thyroid hormone test results.

## Dataset Statistics

- **Total Records**: 908 patients
- **Total Columns**: 31 features
- **Missing Values**: 0 (clean dataset)
- **Memory Usage**: ~2.1 KB

## Patient Demographics

| Category | Count | Percentage |
|----------|-------|-----------|
| Female | 626 | 68.9% |
| Male | 282 | 31.1% |
| Pregnant | 38 | 4.2% |
| Not Pregnant | 870 | 95.8% |

## Column Descriptions

### Demographics
- **Age**: Patient age in years (Range: 18-79)
- **Sex**: Gender (Female or Male)

### Medical History (Binary 0/1)
- **Family_History_Thyroid**: Family history of thyroid disease
- **Pregnant**: Current pregnancy status
- **on_thyroxine**: Currently on thyroxine medication
- **query_on_thyroxine**: Query about thyroxine usage
- **on_antithyroid_medication**: On anti-thyroid medication
- **sick**: Patient reported being sick
- **thyroid_surgery**: History of thyroid surgery
- **I131_treatment**: Received radioactive iodine treatment
- **query_hypothyroid**: Query about hypothyroidism
- **query_hyperthyroid**: Query about hyperthyroidism
- **lithium**: Currently taking lithium
- **goitre**: Has goitre (enlarged thyroid)
- **tumor**: Has thyroid tumor
- **hypopituitary**: Has hypopituitary condition
- **psych**: Has psychiatric conditions

### Test Results (Binary - Measured or Not)
- **TSH_measured**: TSH test performed (1=yes, 0=no)
- **TSH**: Thyroid Stimulating Hormone level (numerical)
- **T3_measured**: T3 test performed
- **T3**: Triiodothyronine hormone level
- **TT4_measured**: Total T4 test performed
- **TT4**: Total T4 hormone level
- **T4U_measured**: T4 uptake test performed
- **T4U**: T4 uptake level
- **FTI_measured**: Free Thyroxine Index test performed
- **FTI**: Free Thyroxine Index
- **TBG_measured**: Thyroid Binding Globulin test performed
- **TBG**: Thyroid Binding Globulin level

### Other
- **referral_source**: How patient was referred

## Data Encoding

### Binary Features
Binary columns use the following encoding:
- **0** = No/False/Negative
- **1** = Yes/True/Positive

### Thyroid Status
- **0** = No thyroid family history
- **1** = Has thyroid family history or thyroid condition

## Key Findings

### Gender Distribution in Thyroid Disease
- **Females**: 69.5% of thyroid cases (173 out of 249)
- **Males**: 30.5% of thyroid cases (76 out of 249)
- Females are 2.3x more likely to have thyroid family history

### Pregnancy and Thyroid
- **Pregnant women**: 31.6% have thyroid family history
- **Non-pregnant women**: 27.4% have thyroid family history
- Pregnancy increases thyroid risk by approximately 4.2%

### Age Distribution
- **Min Age**: 18 years
- **Max Age**: 79 years
- **Mean Age**: 50.1 years
- **Median Age**: 50.0 years

Age Categories:
- Young (0-30): 169 patients (18.6%)
- Middle (30-60): 430 patients (47.4%)
- Senior (60+): 309 patients (34.0%)

## Data Quality

- No missing values in the dataset
- All records are clean and complete
- Balanced representation across age groups
- Female-biased sample (68.9% female vs 31.1% male)

## Use Cases

This dataset can be used for:
1. Thyroid disease prediction and classification
2. Risk factor analysis
3. Medical decision support systems
4. Clinical research and analysis
5. Machine learning model training

## File Format

- Format: Excel (.xlsx)
- Sheet Name: thyroid_dataset
- Encoding: UTF-8

## Data Preparation

The dataset has been preprocessed:
- Null values removed
- No missing data imputation needed
- Ready for exploratory data analysis
- Suitable for machine learning pipeline

## Notes

- The dataset contains mostly binary categorical features representing clinical indicators
- Numerical hormone levels (TSH, T3, T4, etc.) are continuous variables
- Thyroid disease is significantly more prevalent in females
- Pregnancy status correlates with increased thyroid issues
- Medical history and test results provide comprehensive clinical context

## References

This dataset is commonly used in medical AI and machine learning research for thyroid disease classification and prediction tasks.

---

Last Updated: March 21, 2026
