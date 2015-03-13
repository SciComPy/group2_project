import random_walk, unittest, pylab
from unittest import TestCase


class TestRandomWalk(TestCase):

	def test_success(self):
		self.assertTrue(random_walk.runTest(3, 200.0, 200, 500, 100))
		self.assertTrue(random_walk.runTest(3, 200.0, 200, 500, 100, 0.5))

class TestNumTrials(TestCase):

	def test_check_negative_trial(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(-3, 200.0, 200, 500, 100)

	def test_check_zero_trial(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(0, 200.0, 200, 500, 100)


class TestStock(TestCase):

	def test_check_negative_stock(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, 200, -100, 100)

	def test_check_zero_stock(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, 200, 0, 100)


class TestPrice(TestCase):

	def test_check_negative_price(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, 200, 500, -100)

	def test_check_zero_price(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, 200, 500, 0)


class TestBias(TestCase):

	def test_bias_range(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 400.0, 200, 500, 100, -1.0)
			random_walk.runTest(3, 400.0, 200, 500, 100, 1.2)
			random_walk.runTest(3, 400.0, 200, 500, 100, 0.0)

class TestDays(TestCase):

	def test_days_per_year_range(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 400.0, 200, 500, 100) 	# days > 365
			random_walk.runTest(3, 0.0, 200, 500, 100)		# days = 0
			random_walk.runTest(3, -1.0, 200, 500, 100)		# days < 0

	def test_negative_days(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, -200, 500, 100)
		
	def test_zero_days(self):
		with self.assertRaises(ValueError):
			random_walk.runTest(3, 200.0, 0, 500, 100)


class TestDataType(TestCase):
	
	def test_if_string(self):
		with self.assertRaises(TypeError):
			random_walk.runTest("3", 200.0, 200, 500, 100)
			random_walk.runTest(3, "200.0", 200, 500, 100)
			random_walk.runTest(3, 200.0, "200", 500, 100)
			random_walk.runTest(3, 200.0, 200, "500", 100)
			random_walk.runTest(3, 200.0, 200, 500, "100")
			random_walk.runTest(3, 200.0, 200, 500, 100, "0.1")


	# For numTrials, numDays, numStocks
	def test_if_float(self): 
		with self.assertRaises(TypeError):
			random_walk.runTest(3.0, 200.0, 200, 500, 100)
			random_walk.runTest(3, 200.0, 200.0, 500, 100)
			random_walk.runTest(3, 200.0, 200, 500.0, 100)


	def test_if_dict(self):
		with self.assertRaises(TypeError):
			random_walk.runTest({}, 200.0, 200, 500, 100)
			random_walk.runTest(3.0, {}, 200, 500, 100)
			random_walk.runTest(3.0, 200.0, {}, 500, 100)
			random_walk.runTest(3.0, 200.0, 200, {}, 100)
			random_walk.runTest(3.0, 200.0, 200, 500, {})
			random_walk.runTest(3, 200.0, 200, 500, 100, {})



	def test_if_list(self):
		with self.assertRaises(TypeError):
			random_walk.runTest([], 200.0, 200, 500, 100)
			random_walk.runTest(3.0, [], 200, 500, 100)
			random_walk.runTest(3.0, 200.0, [], 500, 100)
			random_walk.runTest(3.0, 200.0, 200, [], 100)
			random_walk.runTest(3.0, 200.0, 200, 500, [])
			random_walk.runTest(3, 200.0, 200, 500, 100, [])


	def test_if_tuple(self):
		with self.assertRaises(TypeError):
			random_walk.runTest((), 200.0, 200, 500, 100)
			random_walk.runTest(3.0, (), 200, 500, 100)
			random_walk.runTest(3.0, 200.0, (), 500, 100)
			random_walk.runTest(3.0, 200.0, 200, (), 100)
			random_walk.runTest(3.0, 200.0, 200, 500, ())
			random_walk.runTest(3, 200.0, 200, 500, 100, ())

if __name__ == '__main__':
    unittest.main()