from django.test import TestCase
from .models import AboutUsContent

class AboutUsContentTestCase(TestCase):
    def setUp(self):
        AboutUsContent.objects.create(
            information="This is some information about the company"
        )

    def test_about_us_content(self):
        about_us_content = AboutUsContent.objects.first()
        self.assertEqual(about_us_content.information, "This is some information about the company")
