import extractMovieList as ml

def main() :
    liste = ml.extractMovieList()

    for movieName in liste:
        print movieName

if __name__ == '__main__':
    main()
