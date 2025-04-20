import pandas as pd

# Load the CSV files
df1 = pd.read_csv("./data/01.csv")
df2 = pd.read_csv("./data/02.csv")
df4 = pd.read_csv("./data/03.csv")

# Concatenate the DataFrames
merged_df = pd.concat([df1, df2, df4], ignore_index=True)

# Save the result to a new CSV file
merged_df.to_csv("./data/nlp_stackoverflow_posts.csv", index=False)

print("Files merged successfully into 03.csv")


