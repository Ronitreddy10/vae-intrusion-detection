import pandas as pd
import os

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "UNSW-NB15")
train_file = os.path.join(data_dir, "UNSW_NB15_training-set.parquet")

try:
    df = pd.read_parquet(train_file)
    print("Columns:")
    for col in df.columns:
        print(col)
except Exception as e:
    print(f"Error reading parquet: {e}")
