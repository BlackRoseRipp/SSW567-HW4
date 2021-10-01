import unittest

from HW4 import getGithubInfo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestHW4(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testComplexity(self): 
        self.assertEqual(getGithubInfo("BlackRoseRipp")[0],'Complexity: 43 commits','This is correct.')

    def testSudokuSolver(self): 
        self.assertEqual(getGithubInfo("BlackRoseRipp")[13],'SudokuSolver: 12 commits','This is correct.')

    def testDesignPattern(self): 
        self.assertEqual(getGithubInfo("BlackRoseRipp")[1],'DesignPatternLab: 3 commits','This is correct.')

    



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

