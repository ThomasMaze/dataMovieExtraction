#!/usr/bin/python

import dateListGenerator as gen
import requests as req
import progressbar as pb

def extractMovieList():

    strPattern = '<a class="no_underline" href="/film/fichefilm_gen_cfilm='
    reqPattern = 'http://www.allocine.fr/film/agenda/sem-'
    isMovieName = False
    movieList = []

    dateList = gen.dateGenerator()

    #intializing a progress bar
    bar = pb.ProgressBar(maxval=len(dateList),widgets=[pb.Bar('=','[',']'),'',pb.Percentage()])
    bar.start()

    for date in dateList :

        reqAns = req.get(reqPattern + date +'/')
        htmlCode = reqAns.content.splitlines()

        for line in htmlCode :
            if isMovieName :
                movieList = movieList + [line]
                isMovieName = False

            if line[0:len(strPattern)] == strPattern:
                isMovieName = True

        #updating progress bar
        bar.update(dateList.index(date))

    bar.finish()
    return movieList
