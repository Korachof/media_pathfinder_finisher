class GoalObjects():
    """Parent class for all child goal object classes"""
    def __init__(self, title: str, date_finished: str, completion_hours: int, total_hours: int, rating: int):
        self._title = title
        self._date_finished = date_finished
        self._completion_hours = completion_hours
        self._total_hours = total_hours
        self._rating = rating

    def get_title(self):
        """returns: the goal object title (STR)"""
        return self._title
    
    def get_date_finished(self):
        """returns: the goal object date finished (STR)"""
        return self._date_finished

    def get_completion_hours(self):
        """returns: the goal object completion hours (INT)"""
        return self._completion_hours

    def get_total_hours(self):
        """returns: the goal object total hours (INT)"""
        return self._total_hours

    def get_rating(self):
        """returns: the goal object rating (INT)"""
        return self._rating
    
    def update_rating(self, new_rating: int):
        """Update the rating to new_rating and return rating as INT"""
        self._rating = new_rating
        return self._rating


class Books(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, date_finished: str, completion_hours: int, total_hours: int, rating: int, author: str, page_count: int, times_finished: int):
        self._author = author
        self._page_count = page_count
        self._times_finished = times_finished
        super().__init__(title, date_finished, completion_hours, total_hours, rating)

    def get_author(self):
        """returns: the book object's author (STR)"""
        return self._author
    
    def get_page_count(self):
        """returns: the book object's page count (INT)"""
        return self._page_count
    
    def get_times_finished(self):
        """returns: the book object's times finished (INT)"""
        return self._times_finished
    

class Movies(GoalObjects)
    """child class to goal objects parent class"""
    def __init__(self, title: str, date_finished: str, completion_hours: int, total_hours: int, rating: int, director: str, runtime: int, times_watched: int):
        self._director = director
        self._runtime = runtime
        self._times_watched = times_watched
        super().__init__(title, date_finished, completion_hours, total_hours, rating)

    def get_director(self):
        """returns: the book object's author (STR)"""
        return self._director
    
    def get_runtime(self):
        """returns: the book object's page count (INT)"""
        return self._runtime
    
    def get_times_watched(self):
        """returns: the book object's times finished (INT)"""
        return self._times_watched

    def incr_times_watched(self):
        """Increment the times finished and return the new times_finished as INT"""
        self._times_watched += 1
        return self._times_watched
    

