'''
Created on 23/01/2015

@author: dave
'''
import unittest
import GLSapp


class Test(unittest.TestCase):


    def setUp(self):
        print("running setUp")
        pass


    def tearDown(self):
        print("running tearDown")
        pass


    def testBasic(self):
        print("I ran")
        pass


if __name__ == "__main__":
    unittest.main()