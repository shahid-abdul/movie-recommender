import gdown
import pickle
import pandas as pd
import streamlit as st
import os

# Function to download file from Google Drive
def download_file_from_google_drive(file_id, output_path):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False)

# File paths for the .pkl files
movie_dict_file = 'movie_dict.pkl'
similarity_file = 'similarity.pkl'

# Replace these with the actual Google Drive file IDs
movie_dict_file_id = '1Y2CZg_OXZOVaR0YpBCjQvVMvlytwEi9K'  # movie_dict.pkl
similarity_file_id = '1vY-_IeqQpdKuZz5HECowh3-LPhHiX6Cf'  # similarity.pkl (from earlier)

# Download files from Google Drive if they don't exist locally
if not os.path.exists(movie_dict_file):
    download_file_from_google_drive(movie_dict_file_id, movie_dict_file)

if not os.path.exists(similarity_file):
    download_file_from_google_drive(similarity_file_id, similarity_file)

# Load the .pkl files
movie_dict = pickle.load(open(movie_dict_file, 'rb'))
similarity = pickle.load(open(similarity_file, 'rb'))
movies = pd.DataFrame(movie_dict)

# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] 
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title("Movies Recommended System")
selected_movie_name = st.selectbox(
    'Select a movie from the below list of movies',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
