# actividad 24/5

import unittest

m3i = 'x es el medio'
m2i = 'z es el medio'
m3d = 'y es el medio'
mnt = 'Los 3 son iguales'


def medio (x,y,z):
    if x >= z and z <= y: #z es el del medio
        return(m2i)
    elif x >= y and  x <= z: # x es el medio
       return (m3i)
    elif x <= y and y <= z : #y es el medio
        return (m3d)
    else:
        return('Los 3 son iguales')

class TestMedio(unittest.TestCase):


#casos de prueba

   def test1(self):
      self.assertTrue(medio(30,10,20),20)

   def test2(self):
      self.assertEqual(medio(8,8,8),mnt)
   def test3(self):
      self.assertEqual(medio(8,5,18),m3i)
   def test4(self):
      self.assertEqual(medio(10,20,30),m3d)
   def test5(self):
      self.assertEqual(medio(10,20,30),m3d)
   def test6(self):
      self.assertTrue(medio(10,10,30),10)

      

      

if __name__ == '__main__':
    unittest.main()
