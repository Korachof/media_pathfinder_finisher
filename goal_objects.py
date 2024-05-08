class Books:
  def __init__(self, name, author, completion_hours, total_hours, times_finished, rating):
    self._name = name
    self._author = author
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  def get_name(self):
    return self._name
  
  def get_author(self):
    return self._author

  def get_completion_hours(self):
    return self._completion_hours

  def get_total_hours(self):
    return self._total_hours

  def get_times_finished(self):
    return self._times_finished

  def get_rating(self):
    return self._rating
  
  def add_total_hours(self, additional_hours):
    self._total_hours += additional_hours

  def incr_times_finished(self):
    self._times_finished += 1

  def update_rating(self, new_rating):
    self._rating = new_rating

  
