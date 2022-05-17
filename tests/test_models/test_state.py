#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test for state"""

    @classmethod
    def setUpClass(cls):
        pass

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.state.State'>"
        pl = State()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    """
    def test_pep8_conformance_state(self):
        pass

    def test_pep8_conformance_test_state(self):
        pass

    def test_state_module_docstring(self):
        pass

    def test_state_class_docstring(self):
        pass

    def test_state_func_docstrings(self):
        pass


    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
"""