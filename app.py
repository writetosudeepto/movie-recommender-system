import streamlit as st
import pickle

movies_list_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies_list_df[movies_list_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_rec = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for mv in movies_list_rec:
        movie_id = mv[0]
        recommended_movies.append(movies_list_df.iloc[mv[0]].title)

    return recommended_movies


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
