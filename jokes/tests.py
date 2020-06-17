from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Content
# Create your tests here.

class JokesTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'tester',
            email = 'tester@email.com',
            password = 'pass'
        )

        self.content = Content.objects.create(
            title = 'this is a joke',
            author = self.user,
            body = 'this is the joke body',
        )


    def test_string_representation(self):
        content = Content(title='joke')
        self.assertEqual(str(content), content.title)


    def test_jokes_content(self):
        self.assertEqual(f'{self.content.title}', 'this is a joke')
        self.assertEqual(f'{self.content.author}', "tester")
        self.assertEqual(f'{self.content.body}', 'this is the joke body')


    def test_jokes_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this is a joke')
        self.assertTemplateUsed(response, 'list.html')


    def test_jokes_detail_view(self):
        response = self.client.get('/content/1/')
        no_response = self.client.get('/content/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'this is the joke body')
        self.assertTemplateUsed(response, 'details.html')


    def test_jokes_create_view(self):
        response = self.client.post(reverse('new'), {
            'title': 'another joke',
            'author': self.user,
            'body': "this is another joke",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'another joke')
        self.assertContains(response, 'this is another joke')


    def test_jokes_update_view(self):
        response = self.client.post(reverse('update',args='1'), {
            'title': 'Updated joke',
            'body': 'Updated joke body',
        })
        self.assertEqual(response.status_code, 302)


    def test_snack_delete_view(self):
        response = self.client.get(reverse('delete',args='1'))
        self.assertEqual(response.status_code, 200)


