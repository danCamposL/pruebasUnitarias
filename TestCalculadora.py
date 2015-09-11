import unittest

class TestCalculadora(unittest.TestCase):
	def test_suma_de_2_mas_2(self):
		calc = Calculadora()
		
		resultado = calc.suma(2,2)
		
		self.assertEqual(4, resultado)


	def test_suma_de_3_mas_3(self):
		calc = Calculadora()
		
		resultado = calc.suma(3,3)
		
		self.assertEqual(6, resultado)
		
class Calculadora():
	def suma(self, num1, num2):
		return num1+num2
		
if __name__ =='__main__':
	unittest.main()