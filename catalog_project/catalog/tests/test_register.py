from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from core.models.company_models import Company

class RegisterViewTestCase(TestCase):
    def setUp(self):
        company_name = 'Test Company'
        self.company, _ = Company.objects.get_or_create(name=company_name, defaults={'status': 'active'})
        
        self.register_url = reverse('register')

    def test_register_page_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_with_valid_data(self):
        valid_data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'phone': '1234567890',
            'password': 'newpassword123',
            'password_confirm': 'newpassword123', 
            'status': 'active',
            'company': self.company.pk,  
            'profile': 'manager'
        }
        response = self.client.post(self.register_url, data=valid_data)
        self.assertEqual(response.status_code, 302)
        
        user = get_user_model().objects.filter(email='newuser@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.company, self.company)  
        self.assertTrue(user.check_password('newpassword123'))

    def test_register_with_invalid_data(self):
        invalid_data = {
            'name': '',  
            'email': 'invalidemail',
            'phone': '1234567890',
            'password': 'short',
            'password_confirm': 'differentpassword',  
            'status': 'active',
            'company': '', 
            'profile': '' 
        }
        response = self.client.post(self.register_url, data=invalid_data)
        self.assertEqual(response.status_code, 200) 
        
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(msg.message == 'Por favor, corrija os erros abaixo.' for msg in messages))
        self.assertFalse(get_user_model().objects.filter(email='invalidemail').exists())


