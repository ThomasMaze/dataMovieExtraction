"""
This module create the dialog between the MySQL database 'testMovie' and our app.
it contains all the fonction to add movie into the database, remove a movie from the
database and get the movie list """

import extractMovieList as ml
import MySQLdb
import getpass as gp
from datetime import date

def dbConnect():
    """
    Used to connect to the MySQL database 'testMovie' with
    user: root
    passwd: ********
    It is assumed that de DB testMovie already exists. It returns the database"""

    user = raw_input('user: ')
    pwd = gp.getpass()

    try :
        db = MySQLdb.connect(host='localhost', user=user , passwd=pwd , db='testMovie')
        print 'connection succeeded'
    except :
        print 'connection failed'

    return db

def addMovie(name,releaseDate,db):
    """
    Add a movie to the database (see 'dbConnect()') given:
    name -> str
    releaseDate -> datetime.date
    db -> _mysql.connection"""

    if not(isinstance(releaseDate,date)):
        print 'Bad argument - addMovie wait a datetime.date as 2nd argument'

    ind = name.find('"')
    if ind != -1 :
        name = name[0:ind]
        
    sql = 'insert into movie values("%s","%s")' % (name, releaseDate.isoformat())
    executeQuery(sql,db)


def removeMovie(name,db):
    """
    Remove a movie from the database (see 'dbConnect()') given:
    name -> str
    db -> _mysql.connection"""

    sql = "delete from movie where title='" + name + "';"
    executeQuery(sql,db)

def getList(db):
    """
    Get the movie list from the database (see 'dbConnect()') given:
    db -> _mysql.connection"""

    sql = "select * from movie;"
    listing = executeQuery(sql,db)
    return listing

def executeQuery(sql,db):
    """
    Execute a query to the database (see 'dbConnect()') given:
    sql -> str request
    db -> _mysql.connection
    It returns the results if there is any"""

    c = db.cursor()
    c.execute(sql)
    db.commit()
    rows = c.fetchall()

    if rows != () :
        return rows

if __name__ == '__main__':
    db = dbConnect()
    movieList = getList(db)
    for movie in movieList :
        print movie
    db.close()
