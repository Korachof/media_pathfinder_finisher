class Books:
  def __init__(self, name, completion_hours, total_hours, times_finished, rating, unique_packs):
    self._name = name
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating
    self._unique_packs = unique_packs

  def get_name(self):
    return self._name

  def get_completion_hours(self):
    return self._completion_hours

  def get_total_hours(self):
    return self._total_hours

  def get_times_finished(self):
    return self._times_finished

  def get_rating(self):
    return self._rating

  def get_unique_packs(self):
    return self._unique_packs
