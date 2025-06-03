import pandas as pd
import numpy as np
import os
import random

from utils import save_df_as_csv

# Constants
n = 5000
locations = ['NY', 'CA', 'TX', 'FL', 'IL']
genders = ['M', 'F']

# Simulate data
np.random.seed(42)
data = {
    "user_id": range(1, n + 1),
    "group": np.random.choice(['A', 'B'], size=n),
    "age": np.random.randint(18, 60, size=n),
    "gender": np.random.choice(genders, size=n),
    "location": np.random.choice(locations, size=n),
    "previous_purchases": np.random.poisson(2, size=n)
}

df = pd.DataFrame(data)
df["email_version"] = df["group"].map({'A': 'Text-heavy', 'B': 'Image-rich'})

# Simulate click behavior
df["click"] = df.apply(lambda row: 
                       np.random.binomial(1, 0.15 if row["group"] == "A" else 0.20), axis=1)

# Simulate conversions only if clicked
df["conversion"] = df.apply(lambda row:
                            np.random.binomial(1, 0.10) if row["click"] == 1 else 0, axis=1)

# Save to CSV
output_dir = os.path.join(os.path.dirname(__file__), "..",'Data',"input")
output_file = "email_campaign.csv"

save_df_as_csv(df, output_dir, output_file)



