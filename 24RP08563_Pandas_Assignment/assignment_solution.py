"""Pandas dataset preparation assignment: BARINDA System Sylvere (24RP08563)
Dataset: Breast Cancer Wisconsin (Diagnostic), 569 rows, 30 numerical features + target.
The original file is supplied in this folder. The dataset is a genuine public dataset
packaged by scikit-learn from the Wisconsin Diagnostic Breast Cancer data.
"""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
INPUT = BASE / "original_dataset.csv"

# Q1: Load the supplied original real-world dataset.
df = pd.read_csv(INPUT)
print("Q1 - Dataset loaded from", INPUT.name)

# Q2: Explore the original dataset.
print("\\nQ2(a) First 10 rows\\n", df.head(10))
print("\\nQ2(b) Last 10 rows\\n", df.tail(10))
print("\\nQ2(c) Dimensions:", df.shape)
print("\\nQ2(d) Columns and dtypes:\\n", df.dtypes)
print("\\nQ2(e) info:")
df.info()
print("\\nQ2(e) describe:\\n", df.describe())

# Q3: Selection and filtering.
print("\\nQ3(a) Selected columns:\\n", df[["mean radius", "mean texture", "mean area"]].head())
median_radius = df["mean radius"].median()
print("\\nQ3(b) Radius above median (", median_radius, "):\\n", df[df["mean radius"] > median_radius].head())
print("\\nQ3(c) Target class 0 (malignant):\\n", df[df["target"] == 0].head())
print("\\nQ3(d) Target 0 AND radius above median:\\n", df[(df["target"] == 0) & (df["mean radius"] > median_radius)].head())
print("\\nQ3(e) Sorted by mean area descending:\\n", df.sort_values("mean area", ascending=False).head())

# Q4: Missing values. Use median for numeric and mode for categorical if needed.
missing_count = df.isna().sum()
missing_percent = df.isna().mean() * 100
print("\\nQ4(a) Missing counts:\\n", missing_count)
print("\\nQ4(b) Missing percentage:\\n", missing_percent.round(2))
clean = df.copy()
for col in clean.select_dtypes(include="number").columns:
    if col != "target" and clean[col].isna().any():
        clean[col] = clean[col].fillna(clean[col].median())
# Target is a categorical label even though it is encoded numerically; use mode if missing.
if clean["target"].isna().any():
    clean["target"] = clean["target"].fillna(clean["target"].mode().iloc[0])
for col in clean.select_dtypes(include=["object", "category"]).columns:
    if clean[col].isna().any():
        clean[col] = clean[col].fillna(clean[col].mode().iloc[0])
print("Q4(c) Applied median to numeric missing values and mode to categorical missing values, only where needed.")

# Q5: Duplicates and invalid values.
duplicate_count = clean.duplicated().sum()
clean = clean.drop_duplicates().copy()
# Dataset-specific validity: measurements must be positive; target must be 0 or 1.
measurement_cols = [c for c in clean.columns if c != "target"]
invalid_measurement = (clean[measurement_cols] < 0).any(axis=1)
invalid_target = ~clean["target"].isin([0, 1])
invalid_rows = invalid_measurement | invalid_target
invalid_count = int(invalid_rows.sum())
clean = clean.loc[~invalid_rows].copy()
print("\\nQ5(a) Duplicate records before removal:", duplicate_count)
print("Q5(b) Removed duplicate rows.\\nQ5(c) Invalid measurement/target rows:", invalid_count)
print("Q5(d) Removed rows with negative measurements or target outside 0/1.")

# Q6: Type conversion, text standardization, meaningful names, calculated field.
clean["target"] = clean["target"].astype("int64")
clean = clean.rename(columns={
    "mean radius": "mean_radius", "mean texture": "mean_texture",
    "mean perimeter": "mean_perimeter", "mean area": "mean_area",
    "mean smoothness": "mean_smoothness", "mean compactness": "mean_compactness",
    "mean concavity": "mean_concavity", "mean concave points": "mean_concave_points",
    "mean symmetry": "mean_symmetry", "mean fractal dimension": "mean_fractal_dimension",
    "radius error": "radius_error", "texture error": "texture_error",
    "perimeter error": "perimeter_error", "area error": "area_error",
    "smoothness error": "smoothness_error", "compactness error": "compactness_error",
    "concavity error": "concavity_error", "concave points error": "concave_points_error",
    "symmetry error": "symmetry_error", "fractal dimension error": "fractal_dimension_error",
    "worst radius": "worst_radius", "worst texture": "worst_texture",
    "worst perimeter": "worst_perimeter", "worst area": "worst_area",
    "worst smoothness": "worst_smoothness", "worst compactness": "worst_compactness",
    "worst concavity": "worst_concavity", "worst concave points": "worst_concave_points",
    "worst symmetry": "worst_symmetry", "worst fractal dimension": "worst_fractal_dimension"
})
clean["diagnosis"] = clean["target"].map({0: "Malignant", 1: "Benign"})
clean["mean_area_per_radius"] = clean["mean_area"] / clean["mean_radius"]
clean = clean.drop(columns=["target"])
print("\\nQ6(a-d) Data types, names and derived feature updated.\\n", clean.dtypes.tail())

# Q7: Statistics for numerical column; interpret group with highest/lowest mean.
stat_column = "mean_radius"
statistics = clean[stat_column].agg(["mean", "median", "min", "max", "std"])
group_means = clean.groupby("diagnosis")[stat_column].mean().sort_values(ascending=False)
print("\\nQ7(a-c) Statistics for mean_radius:\\n", statistics)
print("\\nQ7(d) Mean radius by diagnosis (highest first):\\n", group_means)

# Q8: Grouping and aggregate statistics.
group_counts = clean.groupby("diagnosis").size().sort_values(ascending=False).rename("record_count")
group_mean = clean.groupby("diagnosis")["mean_radius"].mean().sort_values(ascending=False).rename("mean_radius_average")
group_summary = clean.groupby("diagnosis").agg(
    records=("mean_radius", "count"),
    mean_radius_mean=("mean_radius", "mean"),
    mean_radius_min=("mean_radius", "min"),
    mean_radius_max=("mean_radius", "max"),
    mean_radius_std=("mean_radius", "std"),
    mean_area_mean=("mean_area", "mean"),
    mean_texture_mean=("mean_texture", "mean")
).sort_values("mean_radius_mean", ascending=False)
print("\\nQ8(a) Counts:\\n", group_counts)
print("\\nQ8(b) Mean radius by diagnosis:\\n", group_mean)
print("\\nQ8(c-d) Grouped aggregate (sorted):\\n", group_summary)

# Q9: Save and verify the outputs.
clean.to_csv(BASE / "cleaned_dataset.csv", index=False)
with pd.ExcelWriter(BASE / "summary_report.xlsx", engine="openpyxl") as writer:
    group_summary.to_excel(writer, sheet_name="Grouped Statistics")
    group_counts.to_frame().to_excel(writer, sheet_name="Group Counts")
    statistics.to_frame(name="mean_radius_statistics").to_excel(writer, sheet_name="Overall Statistics")
    pd.DataFrame({"missing_count": missing_count, "missing_percent": missing_percent}).to_excel(writer, sheet_name="Missing Values")
# Verify outputs reopen and have content.
verified_csv = pd.read_csv(BASE / "cleaned_dataset.csv")
verified_xlsx = pd.read_excel(BASE / "summary_report.xlsx", sheet_name="Grouped Statistics", index_col=0)
assert len(verified_csv) == len(clean) and verified_csv.shape[1] == clean.shape[1]
assert not verified_csv.isna().any().any()
assert len(verified_xlsx) == 2
print("\\nQ9: CSV and Excel exports verified successfully.")
print("Cleaned data dimensions:", verified_csv.shape)
print("\\nQ10 report is provided as Data Preparation Report.docx in this folder.")
