#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ test for base model"""

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.base_model.BaseModel'>"
        pl = BaseModel()
        self.assertTrue(str(type(pl)), clp)

    def __init__(self, *args, **kwargs):
        """ yesy __init__"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ test for setUp """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ test for default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test for kwards"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ test for kwards init """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ test for str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test for to_dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test for kwards_none """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ test for kwards_one"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ test for _id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test_created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test_updated_at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def setUpClass(cls):
        pass

    def test_pep8_conformance_base(self):
        pass

    def test_pep8_conformance_test_base(self):
        pass

    def test_base_module_docstring(self):
        pass

    def test_base_class_docstring(self):
        pass

    def test_base_func_docstrings(self):
        pass

    def test_is_subclass(self):
        pass

    def test_name_attr(self):
        pass

    def test_to_dict_creates_dict(self):
        pass

    def test_str(self):
        pass
