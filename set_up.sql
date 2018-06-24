CREATE TABLE IF NOT EXISTS historical_data (
    date                TEXT,
    ticker              TEXT,
    open                REAL,
    high                REAL,
    low                 REAL,
    close               REAL,
    adjusted_close      REAL,
    volume              INTEGER,
    dividend_amount     REAL,
    split_coefficient   REAL,
);
