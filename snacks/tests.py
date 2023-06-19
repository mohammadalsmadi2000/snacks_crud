from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

class SnacksTests(TestCase):
    """
    Test case for Snack model and views.
    """

    def test_list_page_status_code(self):
        """
        Test the status code of the list page.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        """
        Test the template used for the list page.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        

    def setUp(self):
        """
        Set up the necessary objects for the tests.
        """
        self.user = get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            title='test',
            description="test info",
            purchaser=self.user
        )

    def test_str_method(self):
        """
        Test the __str__ method of the Snack model.
        """
        self.assertEqual(str(self.snack), "test")

    def test_detail_view(self):
        """
        Test the detail view for a Snack object.
        """
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_view(self):
        """
        Test the create view for a Snack object.
        """
        obj = {
            'title': "test2",
            'description': "info...",
            'purchaser': self.user.id
        }

        url = reverse('snack_create')
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse('snack_detail', args=[2]))
