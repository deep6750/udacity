import media
import fresh_tomatoes



toy_story = media.Movie("Toy Story","A story of a boy and his toys that comes to life","Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on a alien planet","Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock","Using rock music to learn","School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratataouille","A rat is a chef in Paris","RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris","Going back in time to meet authors","Midnight_in_Paris_Poster.jpg","://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games","A really real reality show","HungerGamesPoster.jpg","https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
