import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

rating_data = pd.read_csv("./data/ratings.csv")
movie_data = pd.read_csv("./data/movies.csv")

rating_data.drop("timestamp", axis=1, inplace=True)
user_movie_rating = pd.merge(rating_data, movie_data, on="movieId")
movie_user_rating = user_movie_rating.pivot_table(
    "rating", index="title", columns="userId"
)
movie_user_rating.fillna(0, inplace=True)

item_based_collaborate = cosine_similarity(movie_user_rating)
item_based_collaborate = pd.DataFrame(
    data=item_based_collaborate,
    index=movie_user_rating.index,
    columns=movie_user_rating.index,
)


def recommend_movie(title):
    return item_based_collaborate[title].sort_values(ascending=False)[1:11]


title = input()

# movie_list = list(item_based_collaborate[title][:6].index)
# print(movie_list)
print(recommend_movie(title))
