from django.test import TestCase

from django.contrib.auth.models import User
from searchResults.models import Job, JobCategory 


class JobModelTestCase(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            title='Software Engineer', 
            description='Work on an exciting new project', 
            price=150.00, 
            category= JobCategory.objects.create(name='Software Engineering'), 
            thumbnail='some/image/file.png', 
            user=User.objects.create(username='test_user')
        )

    def test_job_creation(self):
        self.assertTrue(isinstance(self.job, Job))
        self.assertEqual(self.job.title, 'Software Engineer')
        self.assertEqual(self.job.description, 'Work on an exciting new project')
        self.assertEqual(self.job.price, 150.00)
        self.assertEqual(self.job.category.name, 'Software Engineering')
        self.assertEqual(self.job.thumbnail, 'some/image/file.png')
        self.assertEqual(self.job.user.username, 'test_user')
