import unittest

#def my_func(a,'ttest_ex.pyb'):
def my_func(a,b):
        return a * b

class TestME(unittest.TestCase):   #unittest.TestCase---super class TestME is sub class
        def setup(self):
                pass
        def testnum(self):
                self.assertEqual(my_func(3,4),12)

        def teststr(self):
                self.assertEqual(my_func('a',3),'a')

if __name__ == '__main__':
        unittest.main()





#run as

#>> python
