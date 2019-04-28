from django.test import TestCase
from django.shortcuts import reverse

from pikmin.models.pikmins.pikmin import Pikmin
from pikmin.views.pikmins.pikmins_view import index


class PikminListTest(TestCase):

    def test_pikmins_index(self):
        url = reverse('pikmin:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)