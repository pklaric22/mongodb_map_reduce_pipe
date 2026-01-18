import math
from functional import my_reduce


def analyze_movie(movie):
    rating = movie.get("averageRating", 0)
    views = movie.get("views", 0)
    year = movie.get("releaseYear", 2020)
    genres = movie.get("genreIds", [])

    current_year = 2025
    age = max(current_year - year, 1)

    score = rating * math.log(views + 1) * (1 / age)

    return {
        "title": movie.get("title"),
        "genres": genres,
        "rating": rating,
        "views": views,
        "finalScore": round(score, 3),
    }


def best_movie_reducer(best, current):
    return current if current["finalScore"] > best["finalScore"] else best


def build_genre_lookup(genres):
    lookup = {}
    for genre in genres:
        lookup[genre["_id"]] = genre["name"]
    return lookup


def map_movies_with_genres(genre_lookup):
    def mapper(movies):
        analyzed = []
        for movie in movies:
            m = analyze_movie(movie)
            mapped = []
            for gid in m["genres"]:
                mapped.append(genre_lookup.get(gid, gid))
            m["genres"] = mapped
            analyzed.append(m)
        return analyzed
    return mapper


def reduce_group_by_genre(analyzed_movies):
    def reducer(acc, movie):
        for genre in movie["genres"]:
            acc.setdefault(genre, []).append(movie)
        return acc

    return my_reduce(analyzed_movies, reducer, {})


def sort_each_genre(grouped_movies):
    result = {}

    for genre, movies in grouped_movies.itms():
        itms = movies.copy()
        n = len(itms)

        for i in range(1, n):
            current = itms[i]
            j=i-1

            while j >= 0 and itms[j]["finalScore"] < current["finalScore"]:
                itms[j+1] = itms[j]
                j-=1

            itms[j+1]=current

        result[genre] = itms

    return result
