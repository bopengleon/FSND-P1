import fresh_tomatoes
import media

as_tears_go_by = media.Movie("As Tears Go By","A story of boy and his toys that ",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=r3z0Mrng60I")
chungking_express = media.Movie("Chungking Express", "referring to the metaphoric concrete jungle of the city",
	"https://upload.wikimedia.org/wikipedia/en/c/c0/Chungking_Express.jpg",
	"https://www.youtube.com/watch?v=Bjd7PFf_TFw")
ashes_of_time = media.Movie("Ashes of Time", "it imagines the older characters from the book as young men and women",
	"https://upload.wikimedia.org/wikipedia/en/3/37/Ashes2.jpg",
	"https://www.youtube.com/watch?v=4RubLH09hFI")
happy_together = media.Movie("Happy Together","the exposure of something intimate",
	"https://upload.wikimedia.org/wikipedia/en/d/d1/Happy_Together_poster.jpg",
	"https://www.youtube.com/watch?v=f0Dh6Jdc18c")
in_the_mood_for_love= media.Movie("In the Mood for Love","The story takes place in Hong Kong in 1962",
	"https://upload.wikimedia.org/wikipedia/en/4/45/In_the_Mood_for_Love_movie.jpg",
	"https://www.youtube.com/watch?v=BnFjSHQFVkA")
the_longest_nite= media.Movie("The Longest Nite","is a 1998 Hong Kong crime thriller film directed by Patrick Yau and Johnnie To",
	"https://upload.wikimedia.org/wikipedia/en/1/17/LongestNitePoster.jpg",
	"https://www.youtube.com/watch?v=BnFjSHQFVkA")

# as_tears_go_by.show_trailer()

movies = [as_tears_go_by, chungking_express, ashes_of_time, happy_together, in_the_mood_for_love, the_longest_nite]
fresh_tomatoes.open_movies_page(movies)

