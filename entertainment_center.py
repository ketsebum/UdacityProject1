import fresh_tomatoes
import media

#Creation of my 3 favorite movie objects
toy_story = media.Movie("Toy Story", "Boy with toys",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "Marine Love Story",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=uZNHIU3uHT4")

terminator = media.Movie("Terminator 2",
						 "Machine saves boy from machine",
						 "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
						 "https://www.youtube.com/watch?v=eajuMYNYtuY")

#Putting my movies into a list and html page
movies = [toy_story, avatar, terminator]

#Open the beautiful page
fresh_tomatoes.open_movies_page(movies)
