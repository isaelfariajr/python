import unittest


def isAbundant(x):
    """Returns whether the given number x is abundant."""
    if x <= 0:
        return False
    factor_sum = 0
    for i in range(1, x):
        if x % i == 0:
            factor_sum += i
    return factor_sum > x


def isNarcissistic(x):
    """Returns whether a given number is Narcissistic."""
    num_digits = len(str(x))
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(x))
    return sum_of_powers == x


def isTriangular(x):
    """Returns whether a given number x is triangular."""
    n = (8 * x + 1) ** 0.5
    return n.is_integer() and (n - 1) % 2 == 0


def isComposite(x):
  """Returns whether the given number x is composite."""
  if x <= 1:
      return False
  if x <= 3:
      return False
  for i in range(2, int(x**0.5) + 1):
      if x % i == 0:
          return True
  return False


def isComposite_test(x):
  """Returns whether the given number x is composite."""
  if x <= 1:
      return False
  if x <= 3:
      return False
  for i in range(2, int(x**0.5) + 1):
      if x % i == 0:
          return True
  return False


def isPrime(x):
    """Returns whether the given number x is prime."""
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def getFactors(x):
    """Returns a list of factors of the given number x."""
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)

    return factors


class Test(unittest.TestCase):

  def test_factors(self):
    # num: int = 2
    # factors_test = [1, 2]
    # factors = self.getFactors(num)
    # self.assertEqual(factors_test, factors, str(factors) + ' are not the factors of ' + str(num))

    # num = 12
    # factors_test = [1, 2, 3, 4, 6, 12]
    # factors = self.getFactors(num)
    # self.assertEqual(factors_test, factors, str(factors) + ' are not the factors of ' + str(num))

    num = 13
    factors_test = [1, 13]
    factors = getFactors(num)
    self.assertEqual(factors_test, factors, str(factors) + ' are not the factors of ' + str(num))

  def test_isPrime(self):
      prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                       29, 31, 37, 41, 43, 47, 53, 59,
                       61, 67, 71, 73, 79, 83, 89, 97,
                       101, 103, 107, 109, 113, 127,
                       131, 137, 139, 149, 151, 157,
                       163, 167, 173, 179, 181]

      for i in prime_numbers:
          self.assertTrue(isPrime(i), str(i) + ' is prime')

  def test_isComposite(self):
      composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16,
                           18, 20, 21, 22, 24, 25, 26, 27,
                           28, 30, 32, 33, 34, 35, 36,
                           38, 39, 40, 42, 44, 45, 46, 48,
                           49, 50, 51, 52, 54, 55, 56, 57,
                           58, 60, 62, 63, 64, 65, 66, 91, 93]

      for i in composite_numbers:
          self.assertTrue(isComposite(i), str(i) + ' is composite')

      not_composite_numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23,
                               29, 31, 37, 41, 43, 47, 53, 59,
                               61, 67, 71, 73, 79, 83, 89]
      for i in not_composite_numbers:
          self.assertTrue(not (isComposite(i)), str(i) + ' is not composite')

  def test_isComposite_test(self):
      composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16,
                           18, 20, 21, 22, 24, 25, 26, 27,
                           28, 30, 32, 33, 34, 35, 36,
                           38, 39, 40, 42, 44, 45, 46, 48,
                           49, 50, 51, 52, 54, 55, 56, 57,
                           58, 60, 62, 63, 64, 65, 66, 91, 93]

      for i in composite_numbers:
          self.assertTrue(isComposite(i), str(i) + ' is composite')

      not_composite_numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23,
                               29, 31, 37, 41, 43, 47, 53, 59,
                               61, 67, 71, 73, 79, 83, 89]

      for i in not_composite_numbers:
          self.assertTrue(not (isComposite(i)), str(i) + ' is not composite')

  def test_isAbundant(self):
      abundant_numbers = [12, 18, 20, 24, 30, 36, 40, 42, 48,
                          54, 56, 60, 66, 70, 72, 78, 80, 84,
                          88, 90, 96, 100, 102, 104, 108, 112,
                          114, 120]

      for i in abundant_numbers:
          self.assertTrue(isAbundant(i), str(i) + ' is abundant')

      not_abundant_numbers = [1, 2, 3, 4, 5, 6,
                              7, 8, 9, 10, 11, 13,
                              14, 15, 16, 17, 19,
                              21, 22, 23, 25, 26, 27, 28, 29,
                              91, 92, 93, 94, 95, 119]

      for i in not_abundant_numbers:
          self.assertTrue(not (isAbundant(i)), str(i) + ' is not abundant')

  def test_isTriangular(self):

      triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
                            66, 78, 91, 105, 120, 136, 153, 171,
                            190, 210, 231]

      for i in triangular_numbers:
          self.assertTrue(isTriangular(i), str(i) + ' is triangular')

      not_triangular_numbers = [2, 4, 5, 7, 8, 9, 11, 12, 13, 14,
                                16, 17, 18, 19, 20,
                                22, 23, 24, 25, 26, 27,
                                29, 30, 31, 32, 33, 34, 35,
                                37, 40, 41, 42, 43, 44,
                                54, 56, 189, 191, 209, 211, 230, 232]

      for i in not_triangular_numbers:
          self.assertTrue(not (isTriangular(i)), str(i) + ' is not triangular')

      # test existence of docstring
      self.assertTrue(len(isTriangular.__doc__) > 1, "there is no docstring for isTriangular")
      print("Success!")

  def test_isNarcissistic(self):
      narcissistic_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

      for i in narcissistic_numbers:
          self.assertTrue(isNarcissistic(i), str(i) + ' is narcissistic')

      non_narcissistic_numbers = [10, 11, 12, 13, 152, 154, 369, 372, 406]

      for i in non_narcissistic_numbers:
          self.assertTrue(not (isNarcissistic(i)), str(i) + ' is not narcissistic')

      # test existence of docstring
      self.assertTrue(len(isNarcissistic.__doc__) > 1, "there is no docstring for isNarcissistic")
      print("Success!")

if __name__ == '__main__':
  unittest.main()