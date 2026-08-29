CREATE TABLE loads (
    load_id INTEGER PRIMARY KEY,
    date DATE,
    miles INTEGER,
    tons DECIMAL(10,2),
    rate_per_ton DECIMAL(10,2),
    revenue DECIMAL(10,2),
    revenue_per_mile DECIMAL(10,2),
    high_value_load BOOLEAN
);