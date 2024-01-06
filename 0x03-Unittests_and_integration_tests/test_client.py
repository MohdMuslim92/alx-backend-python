#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import MagicMock, Mock, patch, PropertyMock


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

    def test_public_repos_url(self):
        """Tests the _public_repos_url method."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_orgs:
            mock_orgs.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    @patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
            )
    def test_public_repos(self, mocked_url, mocked_get_json):
        """Test GithubOrgClient.public_repos"""

        # Set the mocked property to a known URL
        mocked_url.return_value = 'https://api.github.com/users/google/repos'

        self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
                )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test GithubOrgClient.has_license"""
        github_client = GithubOrgClient("google")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
