# 🎶 Spotify Top 10 Songs (2010–2019) — Data Analysis Project

Welcome to yet another data analysis adventure! This time, I dived into the Spotify Top 10 songs from 2010 to 2019 to explore trends in music popularity, song characteristics, and what makes a chart-topping hit.

This project was super fun, insightful, and helped me sharpen both my Excel and Python (Pandas + Seaborn) skills. Here’s how it went:

📝 Project Goals
I aimed to answer questions like:
✅ What’s the average length of a popular song?
✅ Which genre dominates the charts?
✅ Is there a relationship between energy and popularity?
✅ Do songs with higher danceability get more popular?
✅ Which year produced the most popular hits?

🔍 Workflow
1️⃣ Excel Cleaning & Prep
Used PROPER() to fix column headers (bye-bye lowercase 👋).

Removed duplicates using Data → Remove Duplicates.

Spotted missing values using Conditional Formatting → Highlight Blanks.

Saved cleaned data as a .csv for Python.

2️⃣ Python EDA & Visualization
✅ Loaded data with pd.read_csv()
✅ Checked missing values with .isnull().sum()
✅ Removed duplicates with .drop_duplicates()

📊 Key Insights
🎧 Song Duration![Distribution of song runtime](https://github.com/user-attachments/assets/a8095125-dc7b-4c09-aa85-d68c86c3982d)


80+ songs had a duration of 220–230 seconds → the “radio-friendly” standard!

Very few songs were under 150 seconds or over 350 seconds.

🎧 Most Common Genre
![Top Genre in Spotify(2010-2019(](https://github.com/user-attachments/assets/7b4e43e9-30df-4b61-89dd-6d445fb31e17)

🏆 Dance Pop takes the crown with over 300 songs!

Next up: Pop with 50+ songs; others trail far behind.

🎧 Energy vs Popularity![Energy vs popularity](https://github.com/user-attachments/assets/4592b6d8-0fa2-4f0d-837a-8c345206e960)


Majority of songs cluster between 60–80 energy & 60–80 popularity.

Dance pop (green dots) heavily dominates → no clear positive/negative trend.

🎧 Danceability vs Popularity
![Danceability vs popularity](https://github.com/user-attachments/assets/e86288a9-c06f-40c6-b57a-779c328c5566)

High danceability (60–80) is common in popular songs, but not an absolute rule.

🎧 Popular Songs by Year![Top 10 songs Average Popularity by year](https://github.com/user-attachments/assets/2e98e856-a18e-4115-ad7e-b98f359ace2a)


2019 had the most popular hits, followed by 2018.

🧠 What I Learned
✅ How to clean and explore data in both Excel & Python.
✅ How to use histograms and scatterplots for pattern discovery.
✅ That a hit song is often danceable, energetic, and fits a standard length.
✅ Scatterplots are great for exploring relationships between numerical variables.

🚀 Next Steps
Thinking of adding:
🔹 Artist-level analysis (Who dominated the charts?)
🔹 Sentiment analysis of lyrics (if lyrics data is added)
🔹 Correlation heatmaps between all numeric features
