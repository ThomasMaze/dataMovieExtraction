import extractMovieList as ml
import dataBaseCom as dbCom
from datetime import date


def main() :
    liste = ml.extractMovieList()
    db = dbCom.dbConnect()

    for movieName in liste:
        dbCom.addMovie(movieName, date(2000,1,1), db)

    db.close()

if __name__ == '__main__':
    main()
