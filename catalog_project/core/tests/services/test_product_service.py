from core.services.product_services import ProductService
from core.models.product_models import Product
from core.tests.base_test_case import BaseTestCase

class ProductServiceTest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.service = ProductService()

    def test_create_product(self):
        product = self.service.create_product(self.product_data)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.catalog, self.catalog)

    def test_get_product(self):
        product = self.service.create_product(self.product_data)
        fetched_product = self.service.get_product(product.id)
        self.assertEqual(fetched_product.id, product.id)
        self.assertEqual(fetched_product.name, product.name)

    def test_update_product(self):
        product = self.service.create_product(self.product_data)
        updated_data = {'name': 'Updated Product'}
        updated_product = self.service.update_product(product.id, updated_data)
        self.assertEqual(updated_product.name, updated_data['name'])

    def test_delete_product(self):
        product = self.service.create_product(self.product_data)
        self.service.delete_product(product.id)
        deleted_product = self.service.get_product(product.id)
        self.assertIsNone(deleted_product)

    def test_list_products(self):
        self.service.create_product(self.product_data)
        products = self.service.list_products()
        self.assertGreater(len(products), 0)
