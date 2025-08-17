import pandas as pd
from pathlib import Path

# === CONFIG ===
RAW_DATA_DIR = Path("data/raw")

# === FIND ALL CSV FILES ===
csv_files = list(RAW_DATA_DIR.glob("*.csv"))

if not csv_files:
    print("❌ No CSV files found in data/raw/")
else:
    print(f"📂 Found {len(csv_files)} CSV files in data/raw/:")
    for file in csv_files:
        print(f" - {file.name}")

    # === PROFILE EACH DATASET ===
    for file in csv_files:
        print("\n" + "="*60)
        print(f"📊 Profiling: {file.name}")
        print("="*60)

        try:
            df = pd.read_csv(file)

            # Basic info
            print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]:,} columns")
            print("\nColumns:")
            print(df.columns.tolist())

            # Missing values
            missing = df.isna().sum()
            missing_pct = (missing / len(df) * 100).round(2)
            missing_df = pd.DataFrame({
                "Missing Count": missing,
                "Missing %": missing_pct
            }).sort_values(by="Missing %", ascending=False)
            print("\nMissing Values:")
            print(missing_df[missing_df["Missing Count"] > 0])

            # Sample rows
            print("\nSample data:")
            print(df.head(3))

        except Exception as e:
            print(f"⚠️ Could not read {file.name}: {e}")
