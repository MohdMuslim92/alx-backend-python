#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module"""

import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence, expected_result: Any) -> None:
        """Test access_nested_map function with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
