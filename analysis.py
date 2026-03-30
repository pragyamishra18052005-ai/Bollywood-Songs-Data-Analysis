import pandas as pd
import re

df = pd.read_csv("BollywoodSongsAtoZ.csv")

def extract_year(album):
    match = re.search(r'\((\d{4})\)', str(album))
    return int(match.group(1)) if match else None

df['Year'] = df['Album Name'].apply(extract_year)
df['Decade'] = df['Year'].apply(lambda y: f"{(y//10)*10}s" if y else 'Unknown')
df['Movie'] = df['Album Name'].apply(lambda x: re.sub(r'\(\d{4}\)', '', str(x)).strip())

df.to_csv("bollywood_clean.csv", index=False)
print(f"✅ {len(df)} songs clean ho gaye!")
print(df[['Movie', 'Song Name', 'Singer Name', 'Year', 'Decade']].head())