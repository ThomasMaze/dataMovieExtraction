import pytest
import imp

yearGen = imp.load_source('yearGen', '../yearListGenerator.py')

class TestHtmlExistancy(object):

    def test_HtmlExistancy2014(self):

        year2014 = yearGen.generator(2014)

        for fileName in year2014 :
            try:
                with open('../data/' + fileName, 'r') as htmlFile :
                    assert True
            except IOError :
                assert False

    def test_HtmlExistancy2013(self):

        year2013 = yearGen.generator(2013)

        for fileName in year2013 :
            try:
                with open('../data/' + fileName, 'r') as htmlFile :
                    assert True
            except IOError :
                print fileName
                assert False

    def test_HtmlExistancy2012(self):

        year2012 = yearGen.generator(2012)

        for fileName in year2012 :
            try:
                with open('../data/' + fileName, 'r') as htmlFile :
                    assert True
            except IOError :
                assert False
