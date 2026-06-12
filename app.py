import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_name):
    url = f"https://www.omdbapi.com/?t={movie_name}&apikey=634b47ff"
    data = requests.get(url).json()

    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]

    return "https://via.placeholder.com/300x450?text=No+Poster"

   # response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'. format(movie_id),timeout=20)
   # print(response.status_code)
   # print(response.text)
   # data = response.json()
   # print(data)
   # return "https://via.placeholder.com/300x450?text=no+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        #movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
       # recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].title))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
