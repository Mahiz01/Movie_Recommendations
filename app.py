import streamlit as st
import pickle
import pandas as pd
import requests


#incomplete code , have to develope the path os movie and put it in the responsee and return the link which bring out the image
#-----------------------------------
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=aadf877270c9182ffddde8007cfaae63&language=en-U'.format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']
#-------------------------------------

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    # i=0
    # if(i<5):
    #     movie_id=movies.iloc[i[0]].movie_id
    #     recommended_movies.append(movies.iloc[i[0]].title)
    #     recommended_movies_poster.append(fetch_poster(movie_id))
    #     i+=1
    # else:
    #     return recommended_movies,recommended_movies_poster

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))


    return recommended_movies,recommended_movies_poster

movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
   movies['title'].values )

if st.button('Recommend'):
    name,poster = recommend(selected_movie_name)


    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    #----------------------------------------------
       