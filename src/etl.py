import pandas as pd

def extract():
    return pd.read_csv("loads.csv")

def transform(df):
    df["revenue_per_mile"] = (df["revenue"] / df["miles"]).round(2)
    df["high_value_load"] = df["revenue"] >= 500
    return df

def load(df):
    df.to_csv("processed_loads.csv", index=False)

if __name__ == "__main__":
    data = extract()
    cleaned = transform(data)
    load(cleaned)

    print(f"Processed {len(cleaned)} loads.")