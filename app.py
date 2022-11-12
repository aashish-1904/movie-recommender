import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
        page_title="Movie-Recommender",
        page_icon="🎬",
        layout="wide",
    )
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarities.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US%7C'.format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append((fetch_poster(movie_id)))

    return recommended_movies,recommended_movies_poster

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.beta_columns (5)
    with col1:
        st.image(posters[0])
        st.caption(names[0])  
    with col2:
        st.image(posters[1])
        st.caption(names[1])    
    with col3:
        st.image(posters[2])
        st.caption(names[2])
    with col4:
        st.image(posters[3])
        st.caption(names[3])
    with col5:
        st.image(posters[4])
        st.caption(names[4])
   