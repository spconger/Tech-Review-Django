from django.test import TestCase
from .models import TechProduct, TechType, TechReview

# Create your tests here.
# model tests

class TechProductTest(TestCase):
    def test_stringOutput(self):
        techproduct=TechProduct(productname='Lenovo Laptop')
        self.assertEqual(str(techproduct), techproduct.productname)

    def test_tablename(self):
        self.assertEqual(str(TechProduct._meta.db_table), 'techproduct')

class TechTypeTest(TestCase):
    def test_stringOutput(self):
        techtype=TechType(typename='Laptop')
        self.assertEqual(str(techtype), techtype.typename)

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')

class TechReviewTest(TestCase):
    def test_stringOutput(self):
        techreview=TechReview(reviewtitle='Lenovo Laptop')
        self.assertEqual(str(techreview), techreview.reviewtitle)

    def test_tablename(self):
        self.assertEqual(str(TechReview._meta.db_table), 'techreview')




