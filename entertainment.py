import media

import fresh_tomatoes

baahubali2=media.Tollywoodmovies("Bahubali1",
                          "region drama",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Baahubali_the_Conclusion.jpg/220px-Baahubali_the_Conclusion.jpg",
                          "https://www.youtube.com/watch?v=qD-6d8Wo3do")
robo_2=media.Tollywoodmovies("Robo 2.o",
                              "action drama",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/2.0_film_poster.jpg/220px-2.0_film_poster.jpg",
                              "https://www.youtube.com/watch?v=QDKY8CRe1-0")
transfomers=media.Tollywoodmovies("Transformers",
                                  "war between humans and robots",
                                  "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                                  "https://www.youtube.com/watch?v=2OxkkY1RjmQ")
titanic=media.Tollywoodmovies("Titanic",
                              "Love and tragidy movie",
                              "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                              "https://www.youtube.com/watch?reload=9&v=2e-eXJ6HgkQ")
bahubali1=media.Tollywoodmovies("Bahubali/nThe begining",
                                "Historical action drama",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Baahubali_The_Beginning_Movie_Poster.jpg/220px-Baahubali_The_Beginning_Movie_Poster.jpg",
                                "https://www.youtube.com/watch?v=sOEg_YZQsTI")
aravindhasametha=media.Tollywoodmovies("Aravindha Sametha",
                                       "Faction Drama",
                                       "http://www.cinejosh.com/newsimg/newsmainimg/aravinda-sametha-audio-release-poster_b_1209180609.jpg",
                                       "https://www.youtube.com/watch?v=dNMe5oRfsCE")
movies=[baahubali2,robo_2,transfomers,titanic,bahubali1,aravindhasametha]
fresh_tomatoes.open_movies_page(movies)
