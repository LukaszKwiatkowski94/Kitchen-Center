from django.test import TestCase
from customuser.models import CustomUser

class CustomUserModelTest(TestCase):

    def test_create_user(self):
        """Test create new user"""
        user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertIsNone(user.date_of_birth)

    def test_create_superuser(self):
        """Test create new super user - admin"""
        admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            username='adminuser',
            password='adminpassword'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertTrue(admin_user.check_password('adminpassword'))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertIsNone(admin_user.date_of_birth)
