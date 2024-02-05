#!/usr/bin/env python3
""" Function Generic """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict


class TestAccessNestedMap(unittest.TestCase):
    """ map with key path """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """ memoize a method """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])

    def test_access_nested_map_exception(

        self, nested_map: Dict[str, Any], path: Tuple[str]

    ) -> None:

        """doc doc doc"""

        with self.assertRaises(KeyError):

            access_nested_map(nested_map, path)