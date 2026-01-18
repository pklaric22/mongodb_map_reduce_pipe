from flask import Flask, jsonify, render_template
from db import get_movies, get_genres
from functional import my_map, my_reduce, pipe
from analysis import (
    analyze_movie,
    best_movie_reducer,
    build_genre_lookup,
    map_movies_with_genres,
    reduce_group_by_genre,
    sort_each_genre,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyzed-movies")
def analyzed_movies():
    movies = get_movies()
    analyzed = my_map(movies, analyze_movie)
    return jsonify(analyzed)


@app.route("/best-movie")
def best_movie():
    movies = get_movies()
    analyzed = my_map(movies, analyze_movie)

    best = my_reduce(analyzed, best_movie_reducer, analyzed[0])
    return jsonify(best)


@app.route("/pipeline/ranked-by-genre")
def ranked_by_genre():
    movies = get_movies()
    genres = get_genres()

    genre_lookup = build_genre_lookup(genres)

    pipeline = pipe(
        map_movies_with_genres(genre_lookup),
        reduce_group_by_genre,
        sort_each_genre,
    )

    result = pipeline(movies)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
