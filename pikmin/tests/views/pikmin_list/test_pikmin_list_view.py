from django.test import TestCase
from django.shortcuts import reverse

from pikmin.views.pikmin_list.pikmin_list_view import index


class PikminListTest(TestCase):

    def test_pikmin_list_index(self):
        url = reverse('pikmin:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)