import requests

class Blog:
    def posts(self):
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()

    def post_by_user_id(self, userId: str):
        endereco = f"https://jsonplaceholder.typicode.com/posts?userId={userId}"
        response = requests.get(endereco)
        return response.json()


import unittest
from unittest.mock import patch

class TestBlog(unittest.TestCase):
    @staticmethod
    def mock_posts():
        return [
            {'userId': 1, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'},
            {'userId': 2, 'id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}
        ]

   
    @patch('blog.requests.get')
    def test_posts(self, mock_get):
        expected_data = self.mock_posts()
        mock_get.return_value.json.return_value = expected_data
        blog = Blog()
        actual_data = blog.posts()
        self.assertEqual(actual_data, expected_data)

    
    @patch('blog.requests.get')
    def test_post_by_user_id_exists(self, mock_get):
        user_id = '1'
        expected_data = [post for post in self.mock_posts() if post['userId'] == int(user_id)]
        mock_get.return_value.json.return_value = expected_data
        blog = Blog()
        actual_data = blog.post_by_user_id(user_id)
        self.assertEqual(actual_data, expected_data)

if __name__ == '__main__':
    unittest.main()