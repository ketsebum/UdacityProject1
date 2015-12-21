import webbrowser

#Object Movie created with basic information
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image,
				 trailer_youtube, imdb):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_url = imdb

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def show_imdb_page(self):
		webbrowser.open(self.imdb_url)