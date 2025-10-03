import numpy as np
import pandas as pd
import os

os.chdir("Project_PAMANA_dataset")

df = pd.read_csv("PAMANA_dataset.csv")

# Checking
df.head()
df[df["filename"].str.contains("Agung")]
df[df["filename"].str.contains("Dabakan")]
df[df["filename"].str.contains("Gandingan")]
df[df["filename"].str.contains("Kulintang")]
df[df["filename"].str.contains("Tongatong")]


# Create `instrument` Column
conditions = [
    df["filename"].str.contains("Agung"),
    df["filename"].str.contains("Dabakan"),
    df["filename"].str.contains("Gandingan"),
    df["filename"].str.contains("Kulintang"),
    df["filename"].str.contains("Tongatong")
]
choices = ["Agung", "Dabakan", "Gandingan", "Kulintang", "Tongatong"]
df["instrument"] = np.select(conditions, choices, default="NA")

# Create `type` Column
conditions = [
    df["filename"].str.contains("Gong"),
    df["filename"].str.contains("Drum_Head"),
    df["filename"].str.contains("Shell"),
    df["filename"].str.contains("Closed"),
    df["filename"].str.contains("Hits"),
    df["filename"].str.contains("Open")
]
choices = ['Gong', 'Drum_Head', 'Shell', 'Closed', 'Open', 'Hits']
df["type"] = np.select(conditions, choices, default="NA")

# Create 'tune' Column
conditions = [
    df["filename"].str.contains("01"),
    df["filename"].str.contains("02"),
    df["filename"].str.contains("03"),
    df["filename"].str.contains("04"),
    df["filename"].str.contains("05"),
    df["filename"].str.contains("06"),
    df["filename"].str.contains("07"),
    df["filename"].str.contains("08"),
]
choices = ['01', '02', '03', '04', '05', '06', '07', '08']
df['tune'] = np.select(conditions, choices, default="")
df['tune'] = pd.to_numeric(df['tune'], errors="coerce").astype("Int32")

df['instrument'].unique()
df['type'].unique()
df['tune'].unique()
df.nunique()
df.head(10)

instrument_counts = df["instrument"].value_counts(normalize=True) * 100
print(instrument_counts)

# Plotting
df_type_tune = df.copy()
df_type_tune["type_tune"] = df['type'].astype(str) + "_T" + df['tune'].astype(str)
df_type_tune.head()

from plotnine import ggplot, aes, geom_bar  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ggplot(df_type_tune, aes(x="instrument", fill="type_tune")) +\
    geom_bar()

ggplot(df_type_tune, aes(x="instrument", fill="type_tune")) +\
    geom_bar(position="dodge")

ggplot(df_type_tune, aes(x="instrument", fill="type")) +\
    geom_bar(position="dodge")

ggplot(df_type_tune, aes(x="instrument")) +\
    geom_bar(fill="skyblue")

plt.close("all")
