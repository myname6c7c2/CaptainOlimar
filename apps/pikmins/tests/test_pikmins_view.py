from datetime import datetime

from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.test import TestCase
from django.shortcuts import reverse

from pikmin.lib.choices import SEX
from pikmin.models.pikmins.pikmin import Pikmin
from pikmin.views.pikmins.pikmins_view import PikminSearchForm


class PikminListTest(TestCase):
    fixtures = ['pikmin']

    def login(self):
        self.client.force_login(User.objects.create_user('test'))

    def setUp(self):
        session = self.client.session
        form_data = {
            'first_name': '',
            'last_name': '',
            'first_name_kana': '',
            'last_name_kana': '',
            'sex': '0',
        }
        session['form_data'] = form_data
        session.save()

    def test_init_pikmins_index(self):
        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['pikmins'].count(), 5)

    def test_create_button_vilibility(self):
        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertNotContains(response, '新規登録')

        self.login()
        response = self.client.get(url)
        self.assertContains(response, '新規登録')

    def test_not_exist_first_name_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name'] = 'not exist'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 0)

    def test_exist_last_name_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name'] = 'ピクミン'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 2)

    def test_not_exist_first_name_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name'] = 'not exist'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 0)

    def test_exist_first_name_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name'] = 'ピクミン'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 2)

    def test_not_exist_first_name_kana_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name_kana'] = 'not exist'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 0)

    def test_exist_first_name_kana_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['first_name_kana'] = 'タロウ'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 1)

    def test_not_exist_last_name_kana_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['last_name_kana'] = 'not exist'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 0)

    def test_exist_last_name_kana_pikmins(self):
        session = self.client.session
        form_data = session['form_data'] 
        form_data['last_name_kana'] = 'ピクミン'
        session.save()

        url = reverse('pikmins:index')
        response = self.client.get(url)
        self.assertEquals(response.context['pikmins'].count(), 2)

    def test_init_pikmins_create_logged_in(self):
        self.login()
        url = reverse('pikmins:create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_init_pikmins_update_logged_in(self):
        self.login()
        url = reverse('pikmins:update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_init_pikmins_create_not_login(self):
        url = reverse('pikmins:create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_init_pikmins_update_not_login(self):
        url = reverse('pikmins:update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)