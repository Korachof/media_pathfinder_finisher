import unittest
import cards
import users
import goal_objects


class TestBookGoalObject(unittest.TestCase):

    def test_create_book1(self):
        book1 = goal_objects.Books("Cat in the Hat", "Dr. Seuss", 61, 1, 1, 1, 5)

    def test_create_book2(self):
        book2 = goal_objects.Books("Romeo & Juliet", "William Shakespeare", 138, 1, 1, 1, 4)
    
    def test_create_book3(self):
        book3 = goal_objects.Books("Perdido Street Station", "China Mieville", 640, 1, 1, 1, 7)


    def test_book_name1(self):
        self.assertEqual(book1.get_name(), "Cat in the Hat")

    def test_book_name2(self):
        self.assertEqual(self._book2.get_name(), "Romeo & Juliet")

    def test_book_name3(self):
        self.assertEqual(self._book3.get_name(), "Perdido Street Station")


class TestUsers(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()

