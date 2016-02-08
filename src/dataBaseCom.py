import extractMovieList as ml
import MySQLdb
import getpass as gp
from datetime import date

def dbConnect():

    user = raw_input('user: ')
    pwd = gp.getpass()

    try :
        db = MySQLdb.connect(host='localhost', user=user , passwd=pwd , db='testMovie')
        print 'connection succeeded'
    except :
        print 'connection failed'

    return db

def addMovie(name,releaseDate,db):

    if not(isinstance(releaseDate,date)):
        print 'Bad argument - addMovie wait a datetime.date as 2nd argument'

    sql = "insert into movie values('%s','%s')" % (name, releaseDate.isoformat())
    executeQuery(sql,db)


def removeMovie(name,db):

    sql = "delete from movie where title='" + name + "';"
    executeQuery(sql,db)

def getList(db):
    sql = "select * from movie;"
    listing = executeQuery(sql,db)
    return listing



def executeQuery(sql,db):
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
