from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user('hn', 'hn@rs.com', 'P@ssword12432')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'hn@rs.com')

    def test_raise_error_when_no_username_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='abc@a.com', password='Pass#0f34fdf')

    def test_raise_error_when_no_email_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='qa', email='', password='Pass#0f34fdf')

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='username', email='abc@a.com', password='password123!@', is_superuser=False)

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='username', email='abc@a.com', password='password123!@', is_staff=False)

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username='username', email='', password='password123!@')

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'dba', 'as@b.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'as@b.com')