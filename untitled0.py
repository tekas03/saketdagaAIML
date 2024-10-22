# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ad3rt7nSEc3ZiSo2NSJ_yvvQG1_hSulU
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Load the data
data = pd.read_csv('mrdd.csv')

# Preprocess the data
# Encode categorical features
label_encoders = {}
for column in ['Gender', 'Preferred_Genre', 'Genre']:
  le = LabelEncoder()
  data[column] = le.fit_transform(data[column])
  label_encoders[column] = le

# Define features and target
X = data[['Age', 'Gender', 'Preferred_Genre', 'Genre']]
y = data['Song_Name'] # You might want to use Song_ID for better identification

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create KNN model
knn = NearestNeighbors(n_neighbors=5) # You can adjust the number of neighbors
knn.fit(X_train)

def recommend_music(age, gender, preferred_genre):




  # Encode the input
  input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [label_encoders['Gender'].transform([gender])[0]],
    'Preferred_Genre': [label_encoders['Preferred_Genre'].transform([preferred_genre])[0]],
    'Genre': [0] # Dummy value, as we will find neighbors
   })

   # Find the nearest neighbors
  distances, indices = knn.kneighbors(input_data)

   # Get recommended songs
  recommended_songs = y_train.iloc[indices[0]].values
  return recommended_songs

if __name__ == "__main__":
  print("Welcome to the Music Recommendation System!")
  age = int(input("Enter your age: "))
  gender = input("Enter your gender (Male/Female/Other): ")
  preferred_genre = input("Enter your preferred genre:['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical']")






  recommendations = recommend_music(age, gender, preferred_genre)
  print("We recommend the following songs:")
  for song in recommendations:
    print(song)