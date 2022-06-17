#!/usr/bin/env python3
""" Unit Test
"""
import unittest
import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    ''' test that the method returns what it is supposed to. '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' testing the map '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' exceptions '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' test that utils.get_json returns the expected result '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' testing json get'''
        class Mocked(Mock):
            ''' mock patches '''

            def json(self):
                ''' json patch mock'''
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    ''' memoizing to mock classes '''

    def test_memoize(self):
        ''' mocking methods '''

        class TestClass:
            ''' test class for memoizing '''

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
