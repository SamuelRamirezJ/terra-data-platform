import pandas as pd
from src.etl import transform


def test_transform():
    df = pd.DataFrame([
        {
            "load_id": 1,
            "miles": 100,
            "revenue": 500
        }
    ])

    result = transform(df)

    assert result.loc[0, "revenue_per_mile"] == 5.00
    assert bool(result.loc[0, "high_value_load"]) is True