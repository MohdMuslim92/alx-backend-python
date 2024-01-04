#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence, key_error_key: str) -> None:
        """Test access_nested_map function for exceptions"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception).strip("'"), key_error_key)


class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Tests get_json's output """
        # Create a mock response with specified payload
        attrs = {'json.return_value': test_payload}

        # Patch 'requests.get' to return the mock response
        with patch("utils.requests.get",
                   return_value=Mock(**attrs)) as req_get:
            # Call get_json with the test URL
            result = get_json(test_url)

            # Assert that get_json output matches the test payload
            self.assertEqual(result, test_payload)

            # Assert that requests.get was called once with the test URL
            req_get.assert_called_once_with(test_url)
