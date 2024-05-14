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

  def filter_collectibles_by_set(self, set_name):
    set_list = []
    for card in self._collectibles_list[set_name]:
      set_list.append(card)
    
    return set_list
  
  def filter_collectibles_by_title(self, set_list, card_title):
    filtered_list = []
    for card in set_list:
      if card["title"] == card_title:
        filtered_list.append(card)

      return filtered_list
  
  def filter_collectibles_by_category(self, set_list, category_name):
    filtered_list = []
    for card in set_list:
      if card["category"] == category_name:
        filtered_list.append(card)

    return filtered_list

  def filter_collectibles_by_trait(self, set_list, trait_name):
    filtered_list = []
    for card in set_list:
      if card["trait"] == trait_name:
        filtered_list.append(card)

      return filtered_list
    
  def filter_collectibles_by_rarity(self, set_list, rarity_name):
    filtered_list = []
    for card in set_list:
      if card["rarity"] == rarity_name:
        filtered_list.append(card)

      return filtered_list

  def add_book(self, name, author, completion_hours, rating):
    if f"{name}: {author}" not in self._book_list:
      self._book_list[f"{name}: {author}"] = goal_objects.Books(name, author, completion_hours, completion_hours, 1, rating)
      return f"The Book {name} by {author} has been added"
    
    else:
      self._book_list[f"{name}: {author}"].add_total_hours(completion_hours)
      self._book_list[f"{name}: {author}"].incr_times_finished()
      self._book_list[f"{name}: {author}"].update_rating(rating)
      return f"The Book {name} by {author} has been updated"

  
Korachof = User("Korachof", {}, {}, {}, {}, {}, {})

Korachof.add_book("Lost Gods", "Brom", 21, 8)

print(Korachof.get_book_list()["Lost Gods: Brom"].get_total_hours())

Korachof.add_book("Lost Gods", "Brom", 23, 8)

Korachof.add_book

print(Korachof.get_book_list()["Lost Gods: Brom"].get_total_hours())

print(Korachof.get_book_list()["Lost Gods: Brom"].get_name())