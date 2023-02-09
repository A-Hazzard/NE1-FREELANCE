from django.test import TestCase
from .models import Service


class ServiceModelTestCase(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title='Software Engineer',
            tagline='Work on an exciting new project',
            image='some/image/file.png',
        )

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(self.service.title, 'Software Engineer')
        self.assertEqual(self.service.tagline, 'Work on an exciting new project')
        self.assertEqual(self.service.image, 'some/image/file.png')
