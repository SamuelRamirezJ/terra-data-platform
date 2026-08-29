import pandas as pd
import random
from datetime import datetime, timedelta

loads = []

for i in range(100):
    miles = random.randint(10, 150)
    tons = round(random.uniform(20, 25), 2)
    rate_per_ton = round(random.uniform(8, 30), 2)

    loads.append({
        "load_id": i + 1,
        "date": datetime.today() - timedelta(days=random.randint(0, 90)),
        "miles": miles,
        "tons": tons,
        "rate_per_ton": rate_per_ton,
        "revenue": round(tons * rate_per_ton, 2)
    })

df = pd.DataFrame(loads)

df.to_csv("loads.csv", index=False)

print(f"Generated {len(df)} trucking loads.")
print(df.head())