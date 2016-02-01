import yearListGenerator as gen
import requests as req

strPattern = '<a class="no_underline" href="/film/fichefilm_gen_cfilm='
reqPattern = 'http://www.allocine.fr/film/agenda/sem-'
isMovieName = False
movieList = []

dateList = gen.generateList()

for date in dateList :

    reqAns = req.get(reqPattern + date +'/')
    htmlCode = reqAns.content.splitlines()

    for line in htmlCode :
        if isMovieName :
            movieList = movieList + [line]
            isMovieName = False

        if line[0:len(strPattern)] == strPattern:
            isMovieName = True

print len(movieList)
