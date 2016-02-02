from setuptools import setup,find_packages

def readme() :
    with open('README.rst') as f:
        return f.read()

setup(

    name = 'Movie Data Base',
    version = '__version__',
    description = 'Extract movie realses each week from 2012 to now',
    long_description = readme(),
    url = 'https://github.com/ThomasMaze/dataMovieExtraction',
    author = 'Thomas Maze',
    author_email = 't.mazaleyrat@gmail.com',
    license = 'UNLICENSE',
    packages = find_packages(exclude=['docs' , 'test*']),
    entry_points = {
        'console_scripts': [
            'moviedb=src.extractMovieList:main',
        ],
    },

)
