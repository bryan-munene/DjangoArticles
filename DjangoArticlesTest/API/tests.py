from django.test import TestCase
from .models import Articles

class ModelTestCase(TestCase):
    """This is the base class of the tests for the Articles Model class. It defines the test suite"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.article_name = "Write world class code"
        self.article_text = "To write world class code one needs to practice continuosly to master the craft"
        self.article_author = "Test User"
        self.article = Articles(name=self.article_name, text=self.article_text, author=self.article_author)

    def test_model_can_create_an_article(self):
        """Test the articles model can create an article."""
        old_count = Articles.objects.count()
        self.article.save()
        new_count = Articles.objects.count()
        self.assertNotEqual(old_count, new_count)

    