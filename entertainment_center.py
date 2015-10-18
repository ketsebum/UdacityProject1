import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "Boy with toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar", "Marine Love Story", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=-9ceBgWV8io")

#print(toy_story.storyline)
#print(avatar.storyline)
#toy_story.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
