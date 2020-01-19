from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """ Test creating a new user with an email is sucessful"""
        email = 'test@test.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that a new email is normalized"""
        email = 'test@LONDONAPP.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='testpass123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'pass123foo'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
