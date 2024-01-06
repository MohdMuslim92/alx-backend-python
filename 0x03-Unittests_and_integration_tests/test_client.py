#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import MagicMock, Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
        ])
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict, mocked: MagicMock) -> None:
        """Tests the org method."""
        mocked.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), response)
        mocked.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org)
                )
