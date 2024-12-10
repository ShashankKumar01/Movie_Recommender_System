import pickle
import streamlit as st
import requests
import pandas as pd

# Fanart.tv API key
fanart_api_key = "034040afe8def3d783142685fd9d8b2b"

# Function to fetch movie posters from Fanart.tv
# Function to fetch movie posters from Fanart.tv


def get_movie_poster(movie_id):
    url = f"https://webservice.fanart.tv/v3/movies/{movie_id}?api_key={fanart_api_key}"
    response = requests.get(url)
    try:
        # Extract the first poster URL from the response
        poster_url = response.json()['movieposter'][0]['url']
        return poster_url
    except (KeyError, IndexError):
        return "https://via.placeholder.com/200x300?text=Poster+Not+Available"  # Placeholder if no poster is available


# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list[1:6]:  # Top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(get_movie_poster(movie_id))  # Fetch poster using Fanart.tv

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.header('Movie Recommender System')

# Load movies and similarity data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Display recommendations and posters
if st.button('Show Recommendation'):
    recommendations, posters = recommend(selected_movie)
    for name, poster in zip(recommendations, posters):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(poster, width=100)  # Display poster image
        with col2:
            st.write(name)  # Display movie title
