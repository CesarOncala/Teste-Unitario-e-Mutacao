import unittest

from FTSmetodos import numeroPerfeito,mediaIntersecao


class TestMethod(unittest.TestCase):
        
        def test_case1(self):
                self.assertEqual(numeroPerfeito(28),True,"Precisa ser True")
        def test_case2(self):
                self.assertEqual(numeroPerfeito(27),False,"Precisa ser False")
        def test_case3(self):
                self.assertEqual(mediaIntersecao(3,4,[1,2,3,4],[1,2,3]),2.0, "Precisa ser 2.0")
        
        def test_case4(self):
                self.assertEqual(mediaIntersecao(2,6,[7,0,9,4,3,1],[1,3,2,6]),2.0,"Precisa ser 2.0")
        def test_case5(self):
                self.assertEqual(mediaIntersecao(2,2,[0,1],[1,0]),0.5,"Precisa ser 0,5")
        def test_case6(self):
                self.assertEqual(mediaIntersecao(2,2,[0,1],[2,3]),0, "Precisa ser 0")


		 


 
         
                

if __name__=='__main__':
         unittest.main()
