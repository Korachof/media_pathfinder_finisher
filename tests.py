import unittest
import goal_objects

goalobject = goal_objects.GoalObjects("Talked to the Elf Guy", 2024, "6/9/2024", 3, 6)

class TestGoalObject(unittest.TestCase):

    def test_object_title(self):
        self.assertEqual(goalobject.get_title(), "Talked to the Elf Guy")

    def test_object_year_created(self):
        self.assertEqual(goalobject.get_year_created(), 2024)
    
    def test_object_year_finished(self):
        self.assertEqual(goalobject.get_date_finished(), "6/9/2024")

    def test_object_total_hours(self):
        self.assertEqual(goalobject.get_total_hours(), 3)

    def test_object_rating(self):
        self.assertEqual(goalobject.get_rating(), 6)


class TestUsers(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()

