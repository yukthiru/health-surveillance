import pandas as pd
import numpy as np

np.random.seed(42)

districts = ["Mumbai", "Delhi", "Bengaluru", "Chennai",
             "Kolkata", "Pune", "Hyderabad", "Jaipur",
             "Lucknow", "Bhopal"]

diseases = ["Dengue", "Malaria", "Cholera"]

weeks = pd.date_range(start="2024-01-01", periods=52, freq="W")

multipliers = {"Mumbai": 8, "Delhi": 6, "Bengaluru": 3,
               "Chennai": 2, "Kolkata": 1.5, "Pune": 1.3,
               "Hyderabad": 1.1, "Jaipur": 1.0,
               "Lucknow": 0.9, "Bhopal": 0.8}

rows = []
for district in districts:
    for disease in diseases:
        base = np.random.randint(15, 30)
        for i, week in enumerate(weeks):
            if i < 48:
                cases = int(base + np.random.randint(-3, 5))
            else:
                cases = int(base * multipliers[district])
            rows.append({
                "district": district,
                "disease": disease,
                "week": week.strftime("%Y-%m-%d"),
                "cases": cases
            })

df = pd.DataFrame(rows)
df.to_csv("data/disease_data.csv", index=False)
print("Done!", len(df), "rows")
print(df.tail(15))


