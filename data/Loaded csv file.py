import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load CSV
data = pd.read_csv("top10s.csv", encoding="ISO-8859-1")

#Quick check


#Check missing values
print(data.isnull().sum()) #this will check all the missing values then sum it up

#check duplicates
print(f"Number of duplicates: {data.duplicated().sum()}") #this will check all duplicates then sum it up

#drop duplicates
data = data.drop_duplicates()

data = data.rename(columns={
    'Nrgy': 'Energy',
    'Dnce': 'Danceability',
    'DB': 'Loudness',
    'Live': 'Liveness',
    'Val': 'Valence',
    'Dur': 'Duration_sec',
    'Acous': 'Acousticness',
    'Spch': 'Speechiness',
    'Pop': 'Popularity'
})

print(data.head())

 #visualization
 #1. Song run time
 #set the style
sns.set_style("whitegrid")
 #plot distribution of song duration
plt.figure(figsize=(10,6))
sns.histplot(data["Duration_sec"], bins=30, kde=True, color="skyblue")
plt.title("Distribution of song runtime")
plt.xlabel("Duration (seconds)", fontsize=14)
plt.ylabel("Number of songs", fontsize=14)
plt.show()

#2. Common Genres
#count the songs per genre
genre_count = data["Top Genre"].value_counts().head(10)

#plot the top 10 genres
plt.figure(figsize=(10,6))
sns.barplot(x=genre_count.values, y=genre_count.index, palette="viridis")
plt.title("Top 10 Genres in Spotify Top 10s (2010-2019)", fontsize=16)
plt.xlabel("Number of Songs", fontsize=14)
plt.ylabel("Genre", fontsize=14)
plt.show()

#3. Energy vs Popularity
plt.figure(figsize=(10,6))
sns.scatterplot(data=data, x="Energy", y="Popularity", hue="Top Genre", alpha=0.7, palette="tab10")
plt.title("Energy vs Popularity", fontsize=16)
plt.xlabel("Energy", fontsize=14)
plt.ylabel("Popularity", fontsize=14)
plt.legend(title="Top .Genre", bbox_to_anchor=(1.05,1), loc='upper left')
plt.show()

#4 Danceability vs Popularity
plt.figure(figsize=(10,6))
sns.scatterplot(data=data, x="Danceability", y="Popularity", hue="Danceability", alpha=0.7, palette="tab10")
plt.title("Danceability vs Popularity", fontsize=16)
plt.xlabel("Danceability", fontsize=14)
plt.ylabel("Popularity", fontsize=14)
plt.legend(title="Danceability", bbox_to_anchor=(1.05,1), loc='upper left')
plt.show()

corr= data["Danceability"].corr(data["Popularity"])
print(f"Correlation between Danceability and Popularity: {corr:.2f}")

#5. Popular songs by year
#sort year and popularity
top10 = data.sort_values(['Year', 'Popularity'], ascending=[True, False])

#group by year and get top 10
top10 = top10.groupby('Year').head(10)

#plot barchart
plt.figure(figsize=(12,8))
sns.barplot(data=top10, x='Year', y='Popularity', ci=None, estimator='mean')
plt.title("Top 10 songs Average Popularity by year", fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Popularity', fontsize=14)
plt.xticks(rotation=45)
plt.show()