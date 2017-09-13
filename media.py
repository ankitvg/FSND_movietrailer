# Google Style Guide for Python suggests capital first letter for class name
# The triple quotes are the values of a predefined class attribute __doc__
# which can be used to describe a class

import webbrowser


class Movie():
    """ This class provides a way to store information related to movies """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        """Initialize movie title, storyline, poster URL and trailer URL"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
	"""Show the trailer of the movie instance"""
    webbrowser.open(self.trailer_youtube_url)
