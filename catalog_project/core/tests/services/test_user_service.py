from django.test import TestCase
from core.services.user_service import UserService
from core.models.user_models import User
from core.models.company_models import Company

class UserServiceTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', status='active')
        self.user = User.objects.create(name='Test User', email='test@example.com', phone='1234567890', password='password', status='active', company=self.company)

    def test_get_all_users(self):
        users = UserService.get_all_users()
        self.assertIn(self.user, users)

    def test_get_user_by_id(self):
        user = UserService.get_user_by_id(self.user.id)
        self.assertEqual(self.user, user)

    def test_create_user(self):
        data = {'name': 'New User', 'email': 'new@example.com', 'phone': '0987654321', 'password': 'newpassword', 'status': 'active', 'company': self.company.id}
        user = UserService.create_user(data)
        self.assertEqual(user.name, 'New User')
        self.assertEqual(user.company, self.company)

    def test_update_user(self):
        data = {'name': 'Updated User'}
        user = UserService.update_user(self.user.id, data)
        self.assertEqual(user.name, 'Updated User')

    def test_delete_user(self):
        UserService.delete_user(self.user.id)
        user = UserService.get_user_by_id(self.user.id)
        self.assertIsNone(user)
