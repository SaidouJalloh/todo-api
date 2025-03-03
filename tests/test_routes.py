import json
import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_health_check(self):
        response = self.client.get('/health')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')
        
    def test_create_task(self):
        response = self.client.post(
            '/tasks',
            data=json.dumps({'title': 'Test Task', 'description': 'Test Description'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['title'], 'Test Task')
        self.assertEqual(data['description'], 'Test Description')
        self.assertFalse(data['completed'])
        
    def test_get_tasks(self):
        # Create a task first
        self.client.post(
            '/tasks',
            data=json.dumps({'title': 'Task 1'}),
            content_type='application/json'
        )
        
        response = self.client.get('/tasks')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)