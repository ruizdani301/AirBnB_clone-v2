#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ test for Amenity """

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.amenity.Amenity'>"
        pl = Amenity()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_amenity(self):
        pass

    def test_pep8_conformance_test_amenity(self):
        pass

    def test_amenity_module_docstring(self):
        pass

    def test_amenity_class_docstring(self):
        pass

    def test_amenity_func_docstrings(self):
        pass

    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
