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

# Below are all the 20 problem statements

print("LETS BEGIN WITH OUR PROBLEMS:\n\tFOLLOWING ARE THE 20 PROBLEM STATEMENTS\n")

# Problem Statement 1: What is the total number of movies/TV shows listed in the dataset?

""" 
    Explanation: Get the number of rows in the DataFrame.
    Pandas/NumPy Method: len(df) or df.shape[0]
"""

if not df.empty:
    total_entries = len(df)
    print(f"1. Total number of entries in the dataset: {total_entries}")
else:
    print("1. Cannot execute: DataFrame is empty.")

# Problem Statement 2: Display the first 5 rows of the dataset to get a preview of the data.

""" 
    Explanation: View the beginning of the DataFrame.
    Pandas/NumPy Method: df.head()
"""
if not df.empty:
    print("\n2. First 5 rows of the dataset:")
    print(df.head())
else:
    print("\n2. Cannot execute: DataFrame is empty.")

# Problem Statement 3: Calculate the average IMDB rating of all entries.

""" 
    Explanation: Find the mean of the 'IMDB_Rating' column.
    Pandas/NumPy Method: df['column'].mean()
"""
if not df.empty and 'IMDB_Rating' in df.columns:
    average_rating = df['IMDB_Rating'].mean()
    print(f"\n3. Average IMDB rating: {average_rating:.2f}")
elif not df.empty:
    print("\n3. 'IMDB_Rating' column not found.")
else:
    print("\n3. Cannot execute: DataFrame is empty.")

# Problem Statement 4: Find the movie or TV show with the highest IMDB rating.

"""
    Explanation: Locate the row with the maximum value in the 'IMDB_Rating' column.
    Pandas/NumPy Method: df['column'].idxmax(), df.loc[]
"""
if not df.empty and 'IMDB_Rating' in df.columns:
    highest_rated_entry = df.loc[df['IMDB_Rating'].idxmax()]
    print(f"\n4. Entry with the highest IMDB rating:")
    print(f"   Title: {highest_rated_entry['Series_Title']}")
    print(f"   Rating: {highest_rated_entry['IMDB_Rating']}")
elif not df.empty:
    print("\n4. 'IMDB_Rating' column not found.")
else:
    print("\n4. Cannot execute: DataFrame is empty.")

# Problem Statement 5: Determine the movie or TV show with the most number of votes.

"""
   Explanation: Locate the row with the maximum value in the 'No_of_Votes' column.
    Pandas/NumPy Method: df['column'].idxmax(), df.loc[] 
"""

if not df.empty and 'No_of_Votes' in df.columns:
    most_voted_entry = df.loc[df['No_of_Votes'].idxmax()]
    print(f"\n5. Entry with the most votes:")
    print(f"   Title: {most_voted_entry['Series_Title']}")
    print(f"   Votes: {most_voted_entry['No_of_Votes']:,}")
elif not df.empty:
    print("\n5. 'No_of_Votes' column not found.")
else:
    print("\n5. Cannot execute: DataFrame is empty.")

# Problem Statement 6: Find the movie or TV show with the longest runtime.

"""
    Explanation: Locate the row with the maximum value in the cleaned 'Runtime_minutes' column.
    Pandas/NumPy Method: df['column'].idxmax(), df.loc[]  
"""

if not df.empty and 'Runtime_minutes' in df.columns:
    longest_runtime_entry = df.loc[df['Runtime_minutes'].idxmax()]
    print(f"\n6. Entry with the longest runtime:")
    print(f"   Title: {longest_runtime_entry['Series_Title']}")
    print(f"   Runtime: {longest_runtime_entry['Runtime']}") # Display original string
elif not df.empty:
    print("\n6. 'Runtime_minutes' column not available. Ensure data cleaning was successful.")
else:
    print("\n6. Cannot execute: DataFrame is empty.")

# Problem Statement 7: List all movies and TV shows released in the year 2000.

"""
    Explanation: Filter the DataFrame to select rows where 'Released_Year' is 2000.
    Pandas/NumPy Method: Boolean indexing df[condition]
"""

if not df.empty and 'Released_Year' in df.columns:
    year_to_filter = 2000
    entries_2000 = df[df['Released_Year'] == year_to_filter]
    print(f"\n7. Movies/TV Shows released in {year_to_filter}:")
    if not entries_2000.empty:
        movie_titles = entries_2000['Series_Title'].tolist()
        for title in movie_titles:
            print(f"\t{movie_titles.index(title) + 1} : {title}")
    else:
        print(f"   No entries found for the year {year_to_filter}.")
elif not df.empty:
    print("\n7. 'Released_Year' column not found.")
else:
    print("\n7. Cannot execute: DataFrame is empty.")

# Problem Statement 8: Filter and display the titles of all entries with an IMDB rating strictly greater than 8.5.

"""
    Explanation: Filter the DataFrame based on the 'IMDB_Rating' column.
    Pandas/NumPy Method: Boolean indexing df[condition]
"""

if not df.empty and 'IMDB_Rating' in df.columns:
    high_rated_entries = df[df['IMDB_Rating'] > 8.5]
    print(f"\n8. Movies/TV Shows with IMDB rating > 8.5:")
    if not high_rated_entries.empty:
        movie_titles = high_rated_entries['Series_Title'].tolist()
        for title in movie_titles:
            print(f"\t{movie_titles.index(title) + 1} : {title}")
    else:
        print("   No entries found with IMDB rating > 8.5.")
elif not df.empty:
     print("\n8. 'IMDB_Rating' column not found.")
else:
     print("\n8. Cannot execute: DataFrame is empty.")

# Problem Statement 9: Find the top 10 movies/TV shows by the number of votes.

"""
    Explanation: Sort the DataFrame by 'No_of_Votes' in descending order and select the top 10 rows.
    Pandas/NumPy Method: .sort_values(), .head()
"""

if not df.empty and 'No_of_Votes' in df.columns:
    top_10_voted = df.sort_values(by='No_of_Votes', ascending=False).head(10)
    print(f"\n9. Top 10 Movies/TV Shows by number of votes:")
    print(top_10_voted[['Series_Title', 'No_of_Votes']])
elif not df.empty:
    print("\n9. 'No_of_Votes' column not found.")
else:
    print("\n9. Cannot execute: DataFrame is empty.")

# Problem Statement 10: Calculate the median IMDB rating of all entries.

"""
    Explanation: Find the median of the 'IMDB_Rating' column.
    Pandas/NumPy Method: df['column'].median()
"""

if not df.empty and 'IMDB_Rating' in df.columns:
    median_rating = df['IMDB_Rating'].median()
    print(f"\n10. Median IMDB rating: {median_rating:.2f}")
elif not df.empty:
    print("\n10. 'IMDB_Rating' column not found.")
else:
    print("\n10. Cannot execute: DataFrame is empty.")

# Problem Statement 11: Count the number of movies/TV shows released in each year and display the counts.

"""
    Explanation: Group by 'Released_Year' and count the occurrences of each year.
    Pandas/NumPy Method: .value_counts()
"""

if not df.empty and 'Released_Year' in df.columns:
    entries_per_year = df['Released_Year'].value_counts().sort_index()
    print(f"\n11. Number of Movies/TV Shows released per year:")
    print(entries_per_year.head()) # Displaying head as the list can be long
    print("   ...")
elif not df.empty:
    print("\n11. 'Released_Year' column not found.")
else:
    print("\n11. Cannot execute: DataFrame is empty.")

# Problem Statement 12: Find the average runtime of movies/TV shows for entries released after the year 2000.

"""
    Explanation: Filter entries released after 2000, then calculate the mean of the 'Runtime_minutes' column for the filtered data.
    Pandas/NumPy Method: Boolean indexing df[condition], .mean()
"""

if not df.empty and 'Released_Year' in df.columns and 'Runtime_minutes' in df.columns:
    entries_after_2000 = df[df['Released_Year'] > 2000]
    if not entries_after_2000.empty:
        average_runtime_after_2000 = entries_after_2000['Runtime_minutes'].mean()
        print(f"\n12. Average runtime of entries released after 2000: {average_runtime_after_2000:.2f} minutes")
    else:
        print("\n12. No entries found released after 2000.")
elif not df.empty:
    missing_cols = [col for col in ['Released_Year', 'Runtime_minutes'] if col not in df.columns]
    print(f"\n12. Required column(s) not found: {missing_cols}. Ensure data cleaning was successful.")
else:
    print("\n12. Cannot execute: DataFrame is empty.")

# Problem Statement 13: Identify the director who has the highest average IMDB rating for their movies/TV shows (considering only directors with at least 5 entries).

"""
    Explanation: Group by 'Director', calculate the mean 'IMDB_Rating' for each group, filter for groups with at least 5 entries, and find the maximum mean rating.
    Pandas/NumPy Method: .groupby(), .mean(), .filter(), .idxmax()
"""

if not df.empty and 'Director' in df.columns and 'IMDB_Rating' in df.columns:
    # Group by director, calculate mean rating, and filter for directors with >= 5 entries
    director_avg_rating = df.groupby('Director')['IMDB_Rating'].agg(['mean', 'count'])
    prolific_directors_avg_rating = director_avg_rating[director_avg_rating['count'] >= 5]

    if not prolific_directors_avg_rating.empty:
        best_director = prolific_directors_avg_rating['mean'].idxmax()
        best_director_avg_rating = prolific_directors_avg_rating['mean'].max()
        print(f"\n13. Director with the highest average IMDB rating (min 5 entries): {best_director} (Average Rating: {best_director_avg_rating:.2f})")
    else:
        print("\n13. No directors found with at least 5 entries.")
elif not df.empty:
    missing_cols = [col for col in ['Director', 'IMDB_Rating'] if col not in df.columns]
    print(f"\n13. Required column(s) not found: {missing_cols}.")
else:
    print("\n13. Cannot execute: DataFrame is empty.")

# Problem Statement 14: Find the movie or TV show with the lowest gross earnings.

"""
    Explanation: Locate the row with the minimum value in the cleaned 'Gross_numeric' column, excluding missing values.
    Pandas/NumPy Method: df['column'].idxmin(), .loc[], .dropna()
"""

if not df.empty and 'Gross_numeric' in df.columns:
    # Drop NaN values in Gross_numeric before finding the minimum
    df_cleaned_gross = df.dropna(subset=['Gross_numeric'])
    if not df_cleaned_gross.empty:
        lowest_gross_entry = df_cleaned_gross.loc[df_cleaned_gross['Gross_numeric'].idxmin()]
        print(f"\n14. Entry with the lowest gross earnings:")
        print(f"   Title: {lowest_gross_entry['Series_Title']}")
        print(f"   Gross: ${lowest_gross_entry['Gross_numeric']:.2f}")
    else:
        print("\n14. No entries with valid gross data found.")
elif not df.empty:
    print("\n14. 'Gross_numeric' column not available. Ensure data cleaning was successful.")
else:
    print("\n14. Cannot execute: DataFrame is empty.")

# Problem Statement 15: Calculate the percentage of entries that are 'Drama' genre (considering entries where 'Drama' is one of the listed genres).

"""
    Explanation: Filter rows where the 'Genre' string contains 'Drama' and calculate the proportion of such rows. 
    Note: This is a simple string check, not an advanced genre analysis.
    Pandas/NumPy Method: .str.contains(), boolean indexing, calculating proportion.
"""

if not df.empty and 'Genre' in df.columns:
    drama_entries_count = df['Genre'].str.contains('Drama', na=False).sum()
    total_entries = len(df)
    percentage_drama = (drama_entries_count / total_entries) * 100 if total_entries > 0 else 0
    print(f"\n15. Percentage of entries listing 'Drama' as a genre: {percentage_drama:.2f}%")
elif not df.empty:
    print("\n15. 'Genre' column not found.")
else:
    print("\n15. Cannot execute: DataFrame is empty.")

# Problem Statement 16: Find the distinct certificates present in the dataset.

"""
    Explanation: Get the unique values from the 'Certificate' column.
    Pandas/NumPy Method: .unique()
"""

if not df.empty and 'Certificate' in df.columns:
    distinct_certificates = df['Certificate'].unique().tolist()
    print("\n16. Distinct Certificates.:")
    for certificates in distinct_certificates:
        print(f"\t{distinct_certificates.index(certificates) + 1} : {certificates}")
elif not df.empty:
    print("\n16. 'Certificate' column not found.")
else:
    print("\n16. Cannot execute: DataFrame is empty.")

# Problem Statement 17: Count how many entries have a runtime between 120 and 180 minutes (inclusive).

"""
    Explanation: Filter rows where 'Runtime_minutes' is within the specified range and count them.
    Pandas/NumPy Method: Boolean indexing with multiple conditions (&)
"""

if not df.empty and 'Runtime_minutes' in df.columns:
    medium_runtime_count = df[
        (df['Runtime_minutes'] >= 120) & (df['Runtime_minutes'] <= 180)
    ].shape[0]
    print(f"\n17. Number of entries with runtime between 120 and 180 minutes: {medium_runtime_count}")
elif not df.empty:
    print("\n17. 'Runtime_minutes' column not available. Ensure data cleaning was successful.")
else:
    print("\n17. Cannot execute: DataFrame is empty.")

# Problem Statement 18: Find the movie or TV show released most recently in the dataset.

"""
    Explanation: Find the maximum value in the 'Released_Year' column and locate the corresponding row(s).
    Pandas/NumPy Method: df['column'].max(), boolean indexing df[condition]
"""

if not df.empty and 'Released_Year' in df.columns:
    most_recent_year = df['Released_Year'].max()
    most_recent_entries = df[df['Released_Year'] == most_recent_year]
    print(f"\n18. Most recently released entry/entries (Year: {int(most_recent_year)}):")
    print(most_recent_entries[['Series_Title', 'Released_Year']])
elif not df.empty:
    print("\n18. 'Released_Year' column not found.")
else:
    print("\n18. Cannot execute: DataFrame is empty.")

# Problem Statement 19: Calculate the correlation coefficient between IMDB Rating and the number of Votes.

"""
    Explanation: Compute the correlation between two numeric columns.
    Pandas/NumPy Method: .corr()
"""

if not df.empty and 'IMDB_Rating' in df.columns and 'No_of_Votes' in df.columns:
    correlation = df['IMDB_Rating'].corr(df['No_of_Votes'])
    print(f"\n19. Correlation coefficient between IMDB Rating and Number of Votes: {correlation:.2f}")
elif not df.empty:
    missing_cols = [col for col in ['IMDB_Rating', 'No_of_Votes'] if col not in df.columns]
    print(f"\n19. Required column(s) not found: {missing_cols}.")
else:
    print("\n19. Cannot execute: DataFrame is empty.")

# Problem Statement 20: List the titles of all entries that have 'Action' as one of their genres and an IMDB rating above 8.0.

"""
    Explanation: Filter entries based on two conditions: 'Genre' contains 'Action' and 'IMDB_Rating' is greater than 8.0.
    Pandas/NumPy Method: .str.contains(), boolean indexing with multiple conditions (&)
"""

if not df.empty and 'Genre' in df.columns and 'IMDB_Rating' in df.columns:
    action_high_rated_entries = df[
        df['Genre'].str.contains('Action', na=False) & (df['IMDB_Rating'] > 8.0)
    ]
    print(f"\n20. Movies/TV Shows with 'Action' genre and IMDB rating > 8.0:")
    if not action_high_rated_entries.empty:
        entries = action_high_rated_entries['Series_Title'].tolist()
        for movies in entries:
            print(f"\t{entries.index(movies)} : {movies}")
    else:
        print("   No entries found meeting these criteria.")
elif not df.empty:
    missing_cols = [col for col in ['Genre', 'IMDB_Rating'] if col not in df.columns]
    print(f"\n20. Required column(s) not found: {missing_cols}.")
else:
    print("\n20. Cannot execute: DataFrame is empty.")

# end of the activity

print("\n\n\t\tEND OF THE ACTIVITY \n\t\t\tTHANKYOU\n")