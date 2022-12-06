import unittest
from entities.user import User
from repositories.user_repository import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.mock_user1 = User('huutium', 'salasana')
        self.mock_user2 = User('Kekkonen', 'mockkakkonen')
        user_repository.delete_all()
        

    def test_find_all_users(self):
        user_repository.create(self.mock_user1)
        user_repository.create(self.mock_user2)
        mock_users = user_repository.find_all()
        self.assertEqual(len(mock_users),2)
        self.assertEqual(mock_users[0].username, self.mock_user1.username)
        self.assertEqual(mock_users[1].username, self.mock_user2.username)

