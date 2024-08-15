from django.test import TestCase
from core.models.userPermission import UserPermission
from core.services.user_service import UserService
from core.models.user_models import User
from core.models.company_models import Company
from core.models.permission_models import Permission

class UserServiceTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', status='active')
        self.permission1 = Permission.objects.create(name='Permission 1', status='active')
        self.permission2 = Permission.objects.create(name='Permission 2', status='active')
        
        self.user = User.objects.create_user(
            email='test@example.com',
            password='password',
            name='Test User',
            phone='1234567890',
            status='active',
            company=self.company,
            profile='manager'
        )

    def test_get_all_users(self):
        users = UserService.get_all_users()
        self.assertIn(self.user, users)

    def test_get_user_by_id(self):
        user = UserService.get_user_by_id(self.user.id)
        self.assertEqual(self.user, user)

    def test_create_user(self):
        data = {
            'name': 'New User',
            'email': 'new@example.com',
            'phone': '0987654321',
            'password': 'newpassword',
            'status': 'active',
            'company': self.company.id,
            'profile': 'admin'
        }
        user = UserService.create_user(data)
        self.assertEqual(user.name, 'New User')
        self.assertEqual(user.company, self.company)
        self.assertEqual(user.profile, 'admin')
        self.assertTrue(user.check_password('newpassword'))

        user_permissions = UserPermission.objects.filter(user=user)
        # Verifica que as permissões corretas foram atribuídas
        self.assertIn(self.permission1, [up.permission for up in user_permissions])
        self.assertIn(self.permission2, [up.permission for up in user_permissions])

    def test_update_user(self):
        data = {
            'name': 'Updated User',
            'email': 'updated@example.com',
            'profile': 'admin'
        }
        user = UserService.update_user(self.user.id, data)
        self.assertEqual(user.name, 'Updated User')
        self.assertEqual(user.email, 'updated@example.com')
        self.assertEqual(user.profile, 'admin')
        self.assertEqual(user.company, self.company)

    def test_delete_user(self):
        UserService.delete_user(self.user.id)
        user = UserService.get_user_by_id(self.user.id)
        self.assertIsNone(user)
