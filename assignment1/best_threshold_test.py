import unittest
from assignment1.best_threshold import best_threshold

class TestBestThreshold(unittest.TestCase):
    def test_valid_thresholds(self):
        data = [
            {'threshold': 0.1, 'TP': 90, 'FP': 30, 'FN': 10},
            {'threshold': 0.2, 'TP': 85, 'FP': 25, 'FN': 15},
            {'threshold': 0.3, 'TP': 92, 'FP': 20, 'FN': 8},
            {'threshold': 0.4, 'TP': 95, 'FP': 15, 'FN': 5},
            {'threshold': 0.5, 'TP': 88, 'FP': 10, 'FN': 12},
        ]
        self.assertEqual(best_threshold(data), 0.4)

    def test_no_valid_threshold(self):
        data = [
            {'threshold': 0.1, 'TP': 10, 'FP': 30, 'FN': 90},
            {'threshold': 0.2, 'TP': 5, 'FP': 25, 'FN': 95},
        ]
        self.assertIsNone(best_threshold(data))

    def test_tie_in_precision(self):
        data = [
            {'threshold': 0.3, 'TP': 9, 'FP': 1, 'FN': 0},  # precision = 0.9
            {'threshold': 0.5, 'TP': 18, 'FP': 2, 'FN': 0}, # precision = 0.9, same
        ]
        self.assertEqual(best_threshold(data), 0.3)  # max returns first of tie

if __name__ == "__main__":
    unittest.main()