#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ test for the class city"""

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.city.City'>"
        pl = City()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_city(self):
        pass

    def test_pep8_conformance_test_city(self):
        pass

    def test_city_module_docstring(self):
        pass

    def test_city_class_docstring(self):
        pass

    def test_city_func_docstrings(self):
        pass

    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
