import webbrowser

class Tollywoodmovies():
     def __init__(self,movie_title,movie_storyline,movie_poster,movie_youtube_url):
          self.title=movie_title
          self.story=movie_storyline
          self.poster=movie_poster
          self.youtube_url=movie_youtube_url
     def show_movie_trilers(self):
          webbrowser.open(self.youtube_url)
