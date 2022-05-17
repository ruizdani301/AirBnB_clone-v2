#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test for review """

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.review.Review'>"
        pl = Review()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_review(self):
        pass

    def test_pep8_conformance_test_review(self):
        pass

    def test_review_module_docstring(self):
        pass

    def test_review_class_docstring(self):
        pass

    def test_review_func_docstrings(self):
        pass


    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
