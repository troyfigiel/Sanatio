import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class ValidatorTest(unittest.TestCase):
    """ """

    def test_equals_true(self):
        self.assertTrue(validator.isEquals('foo', 'foo'))
        self.assertTrue(validator.isEquals('foo', 'Foo', ignoreCase=True))
        
    def test_equals_false(self):
        self.assertFalse(validator.isEquals('foo', 'bar'))
        self.assertFalse(validator.isEquals('foo', 'Foo'))
        self.assertFalse(validator.isEquals('foo', 'Foo', ignoreCase=False))
        
    def test_length_true(self):
        self.assertTrue(validator.isLength('foo', 1, 3))
        self.assertTrue(validator.isLength('foobar', 2, 6))
        
    def test_length_false(self):
        self.assertFalse(validator.isLength('foo', 4, 6))
        self.assertFalse(validator.isLength('foobar', 2, 3))
        
    def test_alphanumeric_true(self):
        self.assertTrue(validator.isAlphanumeric('foo123'))
        self.assertTrue(validator.isAlphanumeric('FOO123'))
        
    def test_alphanumeric_false(self):
        self.assertFalse(validator.isAlphanumeric('foo123!'))
        self.assertFalse(validator.isAlphanumeric('FOO123!'))
        
    def test_alpha_true(self):
        self.assertTrue(validator.isAlpha('foo'))
        self.assertTrue(validator.isAlpha('FOO'))
        
    def test_alpha_false(self):
        self.assertFalse(validator.isAlpha('foo123'))
        self.assertFalse(validator.isAlpha('FOO123'))
    
    def test_contains_true(self):
        self.assertTrue(validator.contains('foo', 'oo'))
        self.assertTrue(validator.contains('foo', 'FOO', ignoreCase=True))
        
    def test_contains_false(self):
        self.assertFalse(validator.contains('foo', 'bar'))
        self.assertFalse(validator.contains('foo', 'FOO', ignoreCase=False))
    
    def test_isEmpty_true(self):
        self.assertTrue(validator.isEmpty(''))
        self.assertTrue(validator.isEmpty(' '))
    
    def test_isEmpty_false(self):
        self.assertFalse(validator.isEmpty('foo'))
        self.assertFalse(validator.isEmpty(' foo '))

    def test_isSlug_true(self):
        self.assertTrue(validator.isSlug('foo-bar'))
        self.assertTrue(validator.isSlug('foo-bar-123'))
        self.assertTrue(validator.isSlug('foo-bar-123-456'))

    def test_isSlug_false(self):
        self.assertFalse(validator.isSlug('foo bar'))



if __name__ == '__main__':
    unittest.main()
