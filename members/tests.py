from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass!123')
        self.profile = Profile.objects.create(user=self.user)

    def tearDown(self):
        del self.profile
        del self.user

    def test_profile_creation(self):
        """Test the profile model"""
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.user.username, 'user1')
        self.assertEqual(self.profile.profile_picture.name, 'profile_photos/default.png')


