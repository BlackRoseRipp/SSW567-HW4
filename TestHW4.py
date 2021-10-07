import unittest
from unittest.mock import MagicMock as Mock
from unittest.mock import patch
import json

from HW4 import getGithubInfo

# We replaced the Github API with a mock in order to effectively test our code

class TestHW4(unittest.TestCase):
    @patch('HW4.requests.get')
    def testOutput(self, mockRes):
        repo_list = [
            {'name': "some_repo1"},
            {'name': "some_repo2"},
            {'name': "some_repo3"}
        ]
        commit_list1 = [
            {'node_id': "HSERFIRBVRBIUIJEFB"},
            {'node_id': "ejrvcbieabicbnbwck"}
        ]
        commit_list2 = [
            {'node_id': "HSERFIRBVRBIUIJEFB"},
            {'node_id': "ejrvcbieabicbnbwck"},
            {'node_id': "VERBUHverniuhVENIU"}
        ]
        commit_list3 = [
            {'node_id': "HSERFIRBVRBIUIJEFB"},
            {'node_id': "ejrvcbieabicbnbwck"},
            {'node_id': "VERBUHverniuhVENIU"},
            {'node_id': "WUYGFCYEURVUIEIUBV"},
            {'node_id': "iecnrbubNEIUverhij"}
        ]
        mockRes.return_value.ok = True
        mockRes.return_value.json.side_effect = [repo_list, commit_list1, commit_list2, commit_list3]
        resp = getGithubInfo("some_user")
        self.assertEqual(resp, [['some_repo1', 2],['some_repo2', 3],['some_repo3', 5]])

    @patch('HW4.requests.get')
    def testObject(self, mockRes):
        mockRes.return_value.ok = True
        mockRes.return_value.json.return_value = {'message': "Not found"}
        resp = getGithubInfo("some_user") 
        self.assertEqual(resp,"User not found")

    @patch('HW4.requests.get')
    def testObject1(self, mockRes):
        mockRes.return_value.ok = False
        resp = getGithubInfo("some_user") 
        self.assertEqual(resp,"Invalid response")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

