import unittest
import json
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the app using importlib to handle the hyphen in filename
import importlib.util
spec = importlib.util.spec_from_file_location("aoai_assignment", "aoai-assignment.py")
aoai_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aoai_module)
app = aoai_module.app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello_default(self):
        """Test default greeting"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello, World!')
        self.assertEqual(data['name'], 'World')
    
    def test_hello_with_name(self):
        """Test greeting with valid name"""
        response = self.app.get('/?name=John')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello, John!')
        self.assertEqual(data['name'], 'John')
    
    def test_hello_with_invalid_name(self):
        """Test greeting with invalid characters"""
        response = self.app.get('/?name=<script>alert("xss")</script>')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Invalid name parameter', data['error'])
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_404_error(self):
        """Test 404 error handling"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Not found')

if __name__ == '__main__':
    unittest.main()
