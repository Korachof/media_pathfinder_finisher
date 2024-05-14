class Books:
  """Creates a Book object to represent a finished book by the user."""
  def __init__(self, name: str, author: str, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._name = name
    self._author = author
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  def get_name(self):
    """Returns the Book name as STR"""
    return self._name
  
  def get_author(self):
    """Returns the Book author as STR"""
    return self._author

  def get_completion_hours(self):
    """Returns the Book first completion hours as INT"""
    return self._completion_hours

  def get_total_hours(self):
    """Returns the Book total hours as INT"""
    return self._total_hours

  def get_times_finished(self):
    """Returns the book times finished as INT"""
    return self._times_finished

  def get_rating(self):
    """Returns the book rating as INT"""
    return self._rating
  
  def add_total_hours(self, additional_hours: int):
    """Add additional_hours to total_hours and return new total hours as INT"""
    self._total_hours += additional_hours
    return self._total_hours

  def incr_times_finished(self):
    """Increment the times finished and return the new times_finished as INT"""
    self._times_finished += 1
    return self._times_finished

  def update_rating(self, new_rating: int):
    """Update the rating to new_rating and return rating as INT"""
    self._rating = new_rating
    return self._rating


class Movies:
  """Creates a Movie object to represent a finished movie by the user."""
  def __init__(self, title: str, director: str, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._title = title
    self._director = director
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  
