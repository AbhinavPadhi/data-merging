import csv
import pandas as pd

df = pd.read_csv('dwarf_stars.csv')

df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

#df["Mass"].dropna(axis=0, how='any',  inplace=False)
#df["Radius"].dropna(axis=0, how='any',  inplace=False)

print(df["Mass"])

df["Mass"] = pd.to_numeric(df["Mass"], downcast="float")
df["Radius"] = pd.to_numeric(df["Radius"], downcast="float")

df["Radius"] = df["Radius"]*0.102763
df["Mass"] = df["Mass"]*0.000954588

df = df.rename({
    "Radius":"solar_radius",
    "Mass":"solar_mass"
    },
    axis='columns')

del df['Unnamed: 0']
df.to_csv('dwarf_stars_processed.csv', index = False)