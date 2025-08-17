import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

def inspect_csv(file_path):
    print(f"\n📄 File: {file_path.name}")
    print(f"   Size: {file_path.stat().st_size / 1024:.2f} KB")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"   ❌ Error reading file: {e}")
        return

    print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print("   Columns:", list(df.columns))
    print("   Missing values per column:")
    print(df.isnull().sum())
    print("\n   Preview:")
    print(df.head(), "\n" + "-"*60)

def main():
    csv_files = list(RAW_DATA_DIR.glob("*.csv"))
    if not csv_files:
        print("⚠️ No CSV files found in data/raw/")
        return

    for file in csv_files:
        inspect_csv(file)

if __name__ == "__main__":
    main()
