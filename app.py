import streamlit as st
import pickle
import pandas as pd
import gdown
import os

# Download the similarity.pkl file from Google Drive if not already downloaded
file_id = '1Y2CZg_OXZOVaR0YpBCjQvVMvlytwEi9K'
output_file = 'similarity.pkl'

if not os.path.exists(output_file):
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open(output_file, 'rb'))
movies = pd.DataFrame(movie_dict)

# Recommendation logic
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