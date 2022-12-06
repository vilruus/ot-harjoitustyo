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

    def test_find_user_by_username(self):
        user_repository.create(self.mock_user1)
        mock_user = user_repository.find_by_username('huutium')
        self.assertEqual(mock_user.username, self.mock_user1.username)

    def test_delete_all_users(self):
        user_repository.create(self.mock_user1)
        user_repository.create(self.mock_user2)
        mock_users = user_repository.find_all()
        self.assertEqual(len(mock_users),2)
        user_repository.delete_all()
        mock_users = user_repository.find_all()
        self.assertEqual(len(mock_users),0)

    def test_create_user(self):
        user_repository.create(self.mock_user1)
        mock_user = user_repository.find_by_username('huutium')
        self.assertEqual(mock_user.username, self.mock_user1.username)