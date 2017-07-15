import media  # import media file containing movie data structure
import fresh_tomatoes
# movie objects for 6 movies are created
avatar = media.Movie('Avatar', 'An alien adventure by a human.',
                     'img/avatar.jpg', 'https://www.youtube.com/watch?v=cRdxXPV9GNQ')  # NOQA
silence_lambs = media.Movie('Silence of the lambs', 'A thriller',
                          'img/silence.jpg', 'https://www.youtube.com/watch?v=RuX2MQeb8UM')  # NOQA
momento = media.Movie('Memento', 'A confusing suspense thriller',
                      'img/memento.jpg', 'https://www.youtube.com/watch?v=E77LfnMI-34')  # NOQA
raw = media.Movie('Raw', 'Seems like a good movie not watched yet',
                  'img/raw.jpg', 'https://www.youtube.com/watch?v=fHLJ7TH4ybw')
spiderman = media.Movie('Spiderman Homecoming', 'spiderman is coming  home',
                        'img/spiderman-homecoming.jpg', 'https://www.youtube.com/watch?v=39udgGPyYMg')  # NOQA
la = media.Movie('L.A Confidential', ' a murder suspense thriller',
                 'img/la.jpg', 'https://www.youtube.com/watch?v=C4XbnrmbEME')
# append list of movie objects
movie = [avatar, silence_lambs, momento, raw, spiderman, la]
# movie list is passed on to open_movies_page function
fresh_tomatoes.open_movies_page(movie)
