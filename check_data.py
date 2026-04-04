import pandas as pd

df = pd.read_csv("data/processed/train.csv")

print(df.head())
print(df.columns)
print(df["interaction_type"].value_counts())
import pandas as pd

df = pd.read_csv("data/processed/train.csv")

total = len(df)
no_inter = (df["interaction_type"] == "no_interaction").sum()
interaction = total - no_inter

print("Total:", total)
print("No Interaction:", no_inter)
print("Interaction:", interaction)
print(f"Total: {total}")
print(f"No Interaction: {no_inter}")
print(f"Interaction: {interaction}")