import pandas as pd
import operator
from scipy import spatial


import os

class predict:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pkl_path = os.path.join(base_dir, 'algorithms', 'movie_model.pkl')
        self.movies = pd.read_pickle(pkl_path)

    def Similarity(self, movieId1, movieId2):
        a = self.movies.iloc[movieId1]
        b = self.movies.iloc[movieId2]

        genresA = a['genres_bin']
        genresB = b['genres_bin']

        genreDistance = spatial.distance.cosine(genresA, genresB)

        scoreA = a['cast_bin']
        scoreB = b['cast_bin']
        scoreDistance = spatial.distance.cosine(scoreA, scoreB)

        directA = a['director_bin']
        directB = b['director_bin']
        directDistance = spatial.distance.cosine(directA, directB)

        wordsA = a['words_bin']
        wordsB = b['words_bin']
        wordsDistance = spatial.distance.cosine(directA, directB)
        return genreDistance + directDistance + scoreDistance + wordsDistance

    def predict_score(self, name):
        # name = input('Enter a movie title: ')
        new_movie = self.movies[self.movies['original_title'].str.contains(name)].iloc[0].to_frame().T

        def getNeighbors(baseMovie, K):
            distances = []

            for index, movie in self.movies.iterrows():
                if movie['new_id'] != baseMovie['new_id'].values[0]:
                    dist = self.Similarity(baseMovie['new_id'].values[0], movie['new_id'])
                    distances.append((movie['new_id'], dist))

            distances.sort(key=operator.itemgetter(1))
            neighbors = []

            for x in range(K):
                neighbors.append(distances[x])
            return neighbors

        K = 2
        neighbors = getNeighbors(new_movie, K)

        recommend_list = []

        for neighbor in neighbors:
            recommend_list.append(self.movies.iloc[neighbor[0]].iloc[0])

        return recommend_list

    def moviePreds(self, user_preferences):
        movie_id_one = self.movies[self.movies['original_title'] == user_preferences[0]].index[0]
        movie_id_two = self.movies[self.movies['original_title'] == user_preferences[1]].index[0]
        movie_id_three = self.movies[self.movies['original_title'] == user_preferences[2]].index[0]

        diff_one = self.Similarity(movie_id_one, movie_id_two)
        diff_two = self.Similarity(movie_id_three, movie_id_two)
        diff_three = self.Similarity(movie_id_one, movie_id_three)

        min_diff = min(diff_one, diff_two, diff_three)
        movies_recommended = []
        if min_diff == diff_one:
            movies_recommended.extend(self.predict_score(user_preferences[0]))
            movies_recommended.extend(self.predict_score(user_preferences[1]))
        elif min_diff == diff_two:
            movies_recommended.extend(self.predict_score(user_preferences[2]))
            movies_recommended.extend(self.predict_score(user_preferences[1]))
        else:
            movies_recommended.extend(self.predict_score(user_preferences[0]))
            movies_recommended.extend(self.predict_score(user_preferences[2]))
        return movies_recommended





