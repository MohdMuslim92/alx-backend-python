#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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


@parameterized_class([
    {
        'org_payload_custom': TEST_PAYLOAD[0][0],
        'repos_payload_custom': TEST_PAYLOAD[0][1],
        'expected_repos_custom': TEST_PAYLOAD[0][2],
        'apache2_repos_custom': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload_custom,
            'https://api.github.com/orgs/google/repos': cls.
            repos_payload_custom,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Integration test for the public_repos method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos_custom,
        )

    def test_public_repos_with_license(self) -> None:
        """Integration test for the public_repos method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos_custom,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
