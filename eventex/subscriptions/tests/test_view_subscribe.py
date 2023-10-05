from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')


    def test_get(self):
        """
        Get /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        """
        Must use subscriptions/subscription_form.html
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """
        Html must contain input tags
        """

        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


    def test_csrf(self):
        """
        HTML must contain csrf
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Context must have subscription form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='João Pedro', cpf='12345678901',
                    email='example@gmail.com', phone='0101010101')
        self.resp = self.client.post('/inscricao', data)

    #def test_save_subscription(self):
    #    self.assertTrue(Subscription.objects.exists())

class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})


    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())
