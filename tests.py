import unittest
import goal_objects


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

    def test_add_total_hours(self):
        goalobject2 = goal_objects.GoalObjects("Terry the Sheep", 2018, "6/2/2018", 5, 6)
        self.assertEqual(goalobject2.add_total_hours(15), 20)
    
    def test_update_rating(self):
        self.assertEqual(goalobject.update_rating(7), 7)

    def test_rating_updates(self):
        self.assertEqual(goalobject.update_rating(2), goalobject.get_rating())


class TestUsers(unittest.TestCase):
    pass


if __name__ == "__main__":
    goalobject = goal_objects.GoalObjects("Talked to the Elf Guy", 2024, "6/9/2024", 3, 6)
    unittest.main()

