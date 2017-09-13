# This file imports the media class and creates multiple instances of movies.
# It then calls a function to generate a webpage displaying movie posters.

import media
import fresh_tomatoes

# Below are some instances for movie class
# each instance represents a movie and stores the corresponsing info

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

despicable_me = media.Movie(
    "Despicable Me",
    "A conman with minions wants to set his mark",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
    "https://www.youtube.com/watch?v=sUkZFetWYY0")

shutter_island = media.Movie(
    "Shutter Island",
    "A thriller like no other",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

twelve_angry_men = media.Movie(
    "12 Angry Men",
    "Life is in their hands, death is on their minds",
    "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
    "https://www.youtube.com/watch?v=A7CBKT0PWFA")

the_prestige = media.Movie(
    "The Prestige",
    "Welcome to the magical world of magic!",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI")

the_big_short = media.Movie(
    "The Big Short",
    "Explains the 2008 housing market collapse",
    "https://upload.wikimedia.org/wikipedia/en/2/2f/Big-short-inside-the-doomsday-machine.jpg",	# NOQA
    "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

# add all the movies to a list
movies = [
    toy_story, despicable_me, shutter_island, twelve_angry_men,
    the_prestige, the_big_short
    ]

fresh_tomatoes.open_movies_page(movies)
