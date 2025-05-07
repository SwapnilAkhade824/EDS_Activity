# importing the required modules

import kagglehub
import pandas as pd
import numpy as np
import os

download_dir = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")

file_name = "imdb_top_1000.csv"
file_path = None

# checking weather the file is downloaded 

for root, dirs, files in os.walk(download_dir):

    if file_name in files:
        file_path = os.path.join(root,file_name)
        break

if file_path:

    print(f"Found dataset at: {file_path}\n")

    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.\n")

        # --- Data Cleaning/Preparation ---
        # Convert 'Runtime' from string (e.g., '142 min') to numeric (minutes)
        if 'Runtime' in df.columns and df['Runtime'].dtype == 'object':
            # Handle potential errors during conversion, turning invalid entries into NaN
            df['Runtime_minutes'] = df['Runtime'].str.replace(' min', '', regex=False).astype(float)

        # Convert 'Gross' from string (e.g., '28,341,469') to numeric (float)
        if 'Gross' in df.columns and df['Gross'].dtype == 'object':
             # Remove commas and convert to float. Handle NaN values gracefully.
             df['Gross_numeric'] = df['Gross'].str.replace(',', '', regex=False).astype(float)

        # Ensure 'Released_Year' is numeric
        if 'Released_Year' in df.columns:
            # Coerce errors turns invalid parsing into NaN 
             df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce') 

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        print("Unable to load the dataset.")


print("--- Finding 10 Grains from the Dataset ---")

# Grain 1: Find the movie with the highest IMDB Rating
print("\nGrain 1: Movie with the highest IMDB Rating")
highest_rated_movie = df.loc[df['IMDB_Rating'].idxmax()]
print(highest_rated_movie[['Series_Title', 'IMDB_Rating']])

# Grain 2: Find the top 5 longest movies (based on Runtime_minutes)
print("\nGrain 2: Top 5 Longest Movies")
longest_movies = df.nlargest(5, 'Runtime_minutes')
print(longest_movies[['Series_Title', 'Runtime_minutes']])

# Grain 3: Find the number of movies released in the year 2000
print("\nGrain 3: Number of movies released in 2000")
movies_in_2000 = df[df['Released_Year'] == 2000]
print(f"Number of movies released in 2000: {len(movies_in_2000)}")

# Grain 4: Find all movies directed by Christopher Nolan
print("\nGrain 4: Movies directed by Christopher Nolan")
nolan_movies = df[df['Director'] == 'Christopher Nolan']
print(nolan_movies[['Series_Title', 'Released_Year']])

# Grain 5: Calculate the average IMDB rating for 'Action' movies
print("\nGrain 5: Average IMDB Rating for 'Action' movies")
# Note: Some movies have multiple genres, this will include movies where 'Action' is part of the genre string
action_movies = df[df['Genre'].str.contains('Action', na=False)]
average_action_rating = action_movies['IMDB_Rating'].mean()
print(f"Average IMDB Rating for Action movies: {average_action_rating:.2f}")

# Grain 6: Find the movie with the highest Gross revenue (numeric)
print("\nGrain 6: Movie with the highest Gross Revenue")
# Ensure 'Gross_numeric' exists and is not all NaN
if 'Gross_numeric' in df.columns and df['Gross_numeric'].notna().any():
    highest_gross_movie = df.loc[df['Gross_numeric'].idxmax()]
    print(highest_gross_movie[['Series_Title', 'Gross_numeric']])
else:
    print("Gross_numeric column is not available or contains no valid data.")


# Grain 7: Find the top 3 most frequent Genres
print("\nGrain 7: Top 3 Most Frequent Genres")
# This counts occurrences of each unique genre string, including combinations
top_genres = df['Genre'].value_counts().head(3)
print(top_genres)

# Grain 8: Find movies released in the 1990s (1990-1999)
print("\nGrain 8: Movies released in the 1990s")
# Ensure 'Released_Year' is numeric and handle potential NaNs
nineties_movies = df[(df['Released_Year'] >= 1990) & (df['Released_Year'] <= 1999)].dropna(subset=['Released_Year'])
print(nineties_movies[['Series_Title', 'Released_Year']].head()) # Print head as there might be many

# Grain 9: Find the movie with the most 'No_of_Votes'
print("\nGrain 9: Movie with the most Votes")
most_voted_movie = df.loc[df['No_of_Votes'].idxmax()]
print(most_voted_movie[['Series_Title', 'No_of_Votes']])

# Grain 10: Find the movie with the lowest Meta Score (ignoring missing values)
print("\nGrain 10: Movie with the lowest Meta Score")
# Ensure 'Meta_score' exists and is not all NaN
if 'Meta_score' in df.columns and df['Meta_score'].notna().any():
    lowest_meta_score_movie = df.loc[df['Meta_score'].idxmin()]
    print(lowest_meta_score_movie[['Series_Title', 'Meta_score']])
else:
     print("Meta_score column is not available or contains no valid data.")


print("\n--- End of Finding 10 Grains ---")
