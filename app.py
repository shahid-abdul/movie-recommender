import gdown
import pickle
import pandas as pd
import streamlit as st
import os

# Function to download file from Google Drive
def download_file_from_google_drive(file_id, output_path):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False)

# File paths
movie_dict_file = 'movie_dict.pkl'
similarity_file = 'similarity.pkl'

# File IDs
movie_dict_file_id = '1Y2CZg_OXZOVaR0YpBCjQvVMvlytwEi9K'
similarity_file_id = '1vY-_IeqQpdKuZz5HECowh3-LPhHiX6Cf'

# Download if not exist
if not os.path.exists(movie_dict_file):
    download_file_from_google_drive(movie_dict_file_id, movie_dict_file)
if not os.path.exists(similarity_file):
    download_file_from_google_drive(similarity_file_id, similarity_file)

# Load and process
movie_dict = pickle.load(open(movie_dict_file, 'rb'))
similarity = pickle.load(open(similarity_file, 'rb'))

# Create DataFrame and normalize columns
movies = pd.DataFrame(movie_dict)
movies.columns = movies.columns.map(str).str.strip().str.lower()

if 'title' not in movies.columns:
    st.error("Column 'title' not found in data.")
    st.stop()

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]]['title'] for i in movie_list]

# Streamlit UI
st.title("🎬 Movie Recommendation System")
selected_movie_name = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    try:
        recommendations = recommend(selected_movie_name)
        st.write("Top 5 Recommendations:")
        for movie in recommendations:
            st.write("👉", movie)
    except:
        st.error("Something went wrong while recommending.")
