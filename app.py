import pickle
import streamlit as st
import requests
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1:6])
    recommended_movie_names = []
    #recommended_movie_posters = []
    for i in movies_list[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].movie_id
        #recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names#,recommended_movie_posters


st.header('Movie Recommender System')
movies_dic = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dic)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)