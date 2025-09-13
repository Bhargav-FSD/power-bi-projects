import pandas as pd
import os

# Load sample dataset
data_path = os.path.join('data', 'sample_data.csv')
df = pd.read_csv(data_path)

# Example preprocessing
summary = df.describe()
print(summary)

# Save processed dataset
df.to_csv(os.path.join('data', 'processed_data.csv'), index=False)
