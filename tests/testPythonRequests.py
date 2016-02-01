import requests as req

r = req.get('http://www.allocine.fr/film/agenda/sem-2016-01-06/')
strPattern = '<a class="no_underline" href="/film/fichefilm_gen_cfilm='
isMovieName = False
movieList = []

htmlCode = r.content.splitlines()

for line in htmlCode :
    if isMovieName :
        movieList = movieList + [line]
        isMovieName = False

    if line[0:len(strPattern)] == strPattern:
        isMovieName = True

for movie in movieList :
    print movie
    raw_input()
