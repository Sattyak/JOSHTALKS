from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Task

class APITests(APITestCase):
    def setUp(self):
        """Create test users and tasks."""
        self.user1 = User.objects.create(name='User One', email='user1@example.com', mobile='1234567890')
        self.user2 = User.objects.create(name='User Two', email='user2@example.com', mobile='0987654321')
        self.task = Task.objects.create(name='Test Task', description='This is a test task.', task_type='general')

    def test_create_user(self):
        """Test user creation."""
        response = self.client.post('/api/users/create/', {
            'name': 'New User',
            'email': 'newuser@example.com',
            'mobile': '1112223333'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)  # Ensure the new user is created
        self.assertEqual(response.data['email'], 'newuser@example.com')  # Ensure response contains correct email

    def test_create_task(self):
        """Test task creation."""
        response = self.client.post('/api/tasks/create/', {
            'name': 'New Task',
            'description': 'This is a new task.',
            'task_type': 'general'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # Ensure the new task is created
        self.assertEqual(response.data['name'], 'New Task')  # Ensure response contains correct task name

    def test_assign_task_to_users(self):
        """Test assigning a task to multiple users."""
        response = self.client.patch(f'/api/tasks/{self.task.id}/assign/', {
            'user_ids': [self.user1.id, self.user2.id]
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertIn(self.user1, self.task.assigned_users.all())
        self.assertIn(self.user2, self.task.assigned_users.all())
        self.assertEqual(response.data['message'], 'Task assigned successfully')

    def test_assign_task_invalid_user(self):
        """Test assigning a task to an invalid user."""
        response = self.client.patch(f'/api/tasks/{self.task.id}/assign/', {
            'user_ids': [self.user1.id, 999]  # 999 is an invalid user ID
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "One or more user IDs are invalid.")

    def test_get_user_tasks(self):
        """Test retrieving tasks assigned to a user."""
        self.task.assigned_users.add(self.user1)  # Assign the task to user1
        response = self.client.get(f'/api/users/{self.user1.id}/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # user1 should have 1 task assigned
        self.assertEqual(response.data[0]['name'], self.task.name)

    def test_get_all_users(self):
        """Test retrieving all users."""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 users created in setUp

    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return 1 task created in setUp
        self.assertEqual(response.data[0]['name'], self.task.name)  # Ensure correct task is returned
