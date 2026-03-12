from fastapi import FastAPI
import pandas as pd
import os
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GeoPulse AI API running"}


@app.get("/events")
def get_events():

    if not os.path.exists("events.csv"):
        return {"error": "No event data found"}

    df = pd.read_csv("events.csv")

    # Replace NaN values
    df = df.replace({np.nan: "Unknown"})

    # Convert Risk column to numeric safely
    if "Risk" in df.columns:
        df["Risk"] = pd.to_numeric(df["Risk"], errors="coerce").fillna(0)

    return df.to_dict(orient="records")