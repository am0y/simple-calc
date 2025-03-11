import unittest
import math
from calculator import add, subtract, multiply, divide, power, square_root, memory_store, memory_recall, memory_clear, memory_add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-4, 2), -2)
        
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 5), 0)
        
    def test_square_root(self):
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(2), math.sqrt(2))
        
        with self.assertRaises(ValueError):
            square_root(-1)
    
    def test_memory_operations(self):
        # Test memory store
        self.assertEqual(memory_store(5), 5)
        self.assertEqual(memory_recall(), 5)
        
        # Test memory clear
        self.assertEqual(memory_clear(), 0)
        self.assertEqual(memory_recall(), 0)
        
        # Test memory add
        memory_store(10)
        self.assertEqual(memory_add(5), 15)
        self.assertEqual(memory_recall(), 15)
        
        # Reset memory for other tests
        memory_clear()

if __name__ == "__main__":
    unittest.main()