#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test for User """

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.user.User'>"
        pl = User()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_user(self):
        pass

    def test_pep8_conformance_test_user(self):
        pass

    def test_user_module_docstring(self):
        pass

    def test_user_class_docstring(self):
        pass

    def test_user_func_docstrings(self):
        pass


    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
