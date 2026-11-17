from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    def test_index_renders_catalog_template(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'Welcome to the Catalog')
        self.assertTemplateUsed(response, 'catalogo/index.html')
