import pandas as pd

rawData = pd.read_excel("Himani_AI/ApplicationCatalog (2).xlsx",sheet_name="Application Descriptions")
print(rawData.head())


rawDependencies = pd.read_excel("Himani_AI/ApplicationCatalog (2).xlsx",sheet_name= "Application Dependencies")
print(rawDependencies.head())

print(rawData.columns)

import pandas as pd

# Load the Excel file
file_path = "Himani_AI/ApplicationCatalog (2).xlsx"

# Read all sheets
all_sheets = pd.read_excel(file_path, sheet_name=None)

for sheet_name, df in all_sheets.items():
    print(f"\n=== Sheet: {sheet_name} ===")
    
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(f"Data Type: {df[col].dtype}")
        
        # show up to 10 unique values
        unique_vals = df[col].dropna().unique()[:10]
        print(f"Unique Values (sample): {unique_vals}")

        import pandas as pd

df = pd.read_excel("Himani_AI/ApplicationCatalog (2).xlsx",sheet_name="Application Descriptions")

business_lines = (
    "US Banking, Canadian Banking, Global Banking and Markets, "
    "International Banking, Retail Banking, Global Finance, Global Wealth Management"
)

# Replace "all 7" in the Business Line column
df["Business Line(s)"] = df["Business Line(s)"].replace(
    to_replace=r'(?i)^all\s*7$',     # regex to match "all 7" case-insensitive
    value=business_lines,
    regex=True
)

# Save updated file
df.to_excel("Himani_AI/ApplicationCatalog(vdraft2).xlsx", index=False)




