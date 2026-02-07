import pandas as pd
import numpy as np

def clean_flights_df(df):
    df = df.copy()

    # 1) FL_DATE: str -> datetime64[us]
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors="coerce")
    df["FL_DATE"] = df["FL_DATE"].astype("datetime64[us]")

    # 2) CANCELLED y DIVERTED: float -> 0/1 (int)
    for c in ["CANCELLED", "DIVERTED"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype("int64")

    # 3) Horas: int/float -> "HH:MM" (string), manteniendo nulos
    def hhmm_to_str(x):
        if pd.isna(x):
            return pd.NA
        x = int(x)
        s = f"{x:04d}"
        return s[:2] + ":" + s[2:]

    time_cols = ["CRS_DEP_TIME", "DEP_TIME", "WHEELS_OFF", "WHEELS_ON", "CRS_ARR_TIME", "ARR_TIME"]
    for c in time_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").apply(hhmm_to_str).astype("string")

    # 4) Columnas en minutos: float -> Int64 (nullable)
    int_cols = ["CRS_ELAPSED_TIME", "ELAPSED_TIME", "AIR_TIME", "TAXI_OUT", "TAXI_IN"]
    for c in int_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").round(0).astype("Int64")

    return df
