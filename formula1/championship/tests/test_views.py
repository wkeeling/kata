from django.test import TestCase


class HomePageTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.get('/')

        self.assertContains(response, "Formula 1 Championship")

    def test_displays_drivers_championship(self):
        response = self.client.get('/championship/')

        self.assertContains(response, "Formula 1 Championship")
