import goal_objects

class User:
  def __init__(self, name, book_list, movie_list, game_list, tv_list, event_list, collectibles_list):
    self._name = name
    self._book_list = book_list
    self._movie_list = movie_list
    self._game_list = game_list
    self._tv_list = tv_list
    self._event_list = event_list
    self._collectibles_list = collectibles_list

  def get_name(self):
    return self._name

  def get_book_list(self):
    return self._book_list

  def get_movie_list(self):
    return self._movie_list

  def get_game_list(self):
    return self._game_list

  def get_tv_list(self):
    return self._tv_list

  def get_event_list(self):
    return self._event_list

  def get_collectibles_list(self):
    return self._collectibles_list

  def add_book(self, name, author, completion_hours, rating):

    if name not in self._book_list:
      self._book_list[name] = goal_objects.Books(name, author, completion_hours, completion_hours, 1, rating)
      return f"The Book {name} has been added"
    
    else:
      self._book_list[name].add_total_hours(completion_hours)
      self._book_list[name].incr_times_finished()
      self._book_list[name].update_rating(rating)
      return f"The Book {name} has been updated"

  
Korachof = User("Korachof", {}, {}, {}, {}, {}, {})

Korachof.add_book("Lost Gods", "Brom", 21, 8)

print(Korachof.get_book_list()["Lost Gods"].get_name())