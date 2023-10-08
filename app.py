import streamlit as st 
import pickle
import pandas as pd 

def recommend(movie):
  movie_index =movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

  recommended_movie_names = []
# loop 
  for i in movies_list:
    recommended_movie_names.append(movies_list.iloc[i[0]].title)

  return recommended_movie_names

# READ PICKLE
similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)

# TITLE
st.title('Movie Recommendation System')

#  selectbox n Button
option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
  recommendations= recommend(option)
  for i in recommendations:
    st.write(i)
