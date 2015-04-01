from django.contrib.sites.models import Site
from django.core.urlresolvers import set_urlconf
from django.test import TestCase


class SearchFormTestCase(TestCase):
    fixtures = ['doc_test_fixtures']

    def setUp(self):
        # We need to create an extra Site because docs have SITE_ID=2
        Site.objects.create(name='Django test', domain="example.com")

    @classmethod
    def tearDownClass(cls):
        # cleanup URLconfs changed by django-hosts
        set_urlconf(None)
        super(SearchFormTestCase, cls).tearDownClass()

    def test_empty_get(self):
        response = self.client.get('/en/dev/search/',
                                   HTTP_HOST='docs.djangoproject.dev:8000')
        self.assertEqual(response.status_code, 200)
