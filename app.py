import streamlit as st
import pickle
import pandas as pd


def recommend(movie):     
    movies_index=movies[movies["title"]==movie].index[0]
    distance=similarity[movies_index]
    movies_list=sorted(list(enumerate(distance)), reverse=True , key=lambda x : x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]["title"])
    return recommended_movies   

movies_dict= pickle.load(open("movies.pkl","rb"))
similarity= pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(movies_dict)

    

st.title("MOVIE RECOMMENDER SYSTEM")
selected_movie_name = st.selectbox(
    'Select a movie ',
    movies["title"].values)

if st.button('RECOMMEND'):
    recommendations=recommend(selected_movie_name)
    for r in recommendations:
        st.write(r)

