import unittest
import requests

class TestFibonacciAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/api"

    def test_valid_input(self):
        response = requests.get(f"{self.BASE_URL}/fibonacci?n=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sequence": [0, 1, 1, 2, 3]})

    def test_invalid_input(self):
        response = requests.get(f"{self.BASE_URL}/fibonacci?n=-5")
        self.assertEqual(response.status_code, 400)

class TestPalindromeAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/api"

    def test_palindrome_true(self):
        response = requests.get(f"{self.BASE_URL}/palindrome?number=121")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_palindrome": True, "number": 121})

    def test_palindrome_false(self):
        response = requests.get(f"{self.BASE_URL}/palindrome?number=123")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_palindrome": False, "number": 123})

class TestReverseLinkedListAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/api"

    def test_reverse_linked_list(self):
        data = {"list": [1, 2, 3, 4, 5]}
        response = requests.post(f"{self.BASE_URL}/reverse-linked-list", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"reversed_list": [5, 4, 3, 2, 1]})

    def test_empty_list(self):
        data = {"list": []}
        response = requests.post(f"{self.BASE_URL}/reverse-linked-list", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"reversed_list": []})

if __name__ == '__main__':
    unittest.main()
