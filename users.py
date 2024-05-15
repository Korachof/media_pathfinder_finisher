import goal_objects

class User:
  def __init__(self, name: str, book_list: dict, movie_list: dict, game_list: dict, tv_list: dict, event_list: dict, booster_pack_list: dict, collectibles_list: dict):
    self._name = name
    self._book_list = book_list
    self._movie_list = movie_list
    self._game_list = game_list
    self._tv_list = tv_list
    self._event_list = event_list
    self._booster_pack_list = booster_pack_list
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
  
  def get_booster_pack_list(self):
    return self._booster_pack_list

  def get_collectibles_list(self):
    return self._collectibles_list
  
  def filter_booster_packs_by_set(self, set_name: str):
    set_list = []
    for pack in self._booster_pack_list[set_name]:
      set_list.append(pack)

      return set_list

  def filter_collectibles_by_set(self, set_name: str):
    set_list = []
    for card in self._collectibles_list[set_name]:
      set_list.append(card)
    
    return set_list
  
  def filter_collectibles_by_title(self, set_list, card_title: str):
    filtered_list = []
    for card in set_list:
      if card["title"] == card_title:
        filtered_list.append(card)

      return filtered_list
  
  def filter_collectibles_by_category(self, set_list, category_name: str):
    filtered_list = []
    for card in set_list:
      if card["category"] == category_name:
        filtered_list.append(card)

    return filtered_list

  def filter_collectibles_by_trait(self, set_list, trait_name: str):
    filtered_list = []
    for card in set_list:
      if card["trait"] == trait_name:
        filtered_list.append(card)

      return filtered_list
    
  def filter_collectibles_by_rarity(self, set_list, rarity_name: str):
    filtered_list = []
    for card in set_list:
      if card["rarity"] == rarity_name:
        filtered_list.append(card)

      return filtered_list

  def add_book(self, name: str, author: str, completion_hours: int, rating: int):
    if f"{name}: {author}" not in self._book_list:
      self._book_list[f"{name}: {author}"] = goal_objects.Books(name, author, completion_hours, completion_hours, 1, rating)
      return f"The Book {name} by {author} has been added"
    
    else:
      self._book_list[f"{name}: {author}"].add_total_hours(completion_hours)
      self._book_list[f"{name}: {author}"].incr_times_finished()
      self._book_list[f"{name}: {author}"].update_rating(rating)
      return f"The Book {name} by {author} has been updated"
    
  def add_movie(self, title: str, director: str, year: int, completion_hours: int, rating: int):
    if f"{title}: {director}: {year}" not in self._movie_list:
      self._movie_list[f"{title}: {director}: {year}"] = goal_objects.Movies(title, director, year, completion_hours, completion_hours, 1, rating)
      return f"The Movie {title} by {director} from {year} has been added"
    
    else:
      self._movie_list[f"{title}: {director}: {year}"].add_total_hours(completion_hours)
      self._movie_list[f"{title}: {director}: {year}"].incr_times_finished()
      self._movie_list[f"{title}: {director}: {year}"].update_rating(rating)
      return f"The Movie {title} by {director} from {year} has been updated"
    
  def add_video_game(self, title: str, publisher: str, year: int, game_system: str, completion_hours: int, rating: int):
    if f"{title}: {publisher}: {year}" not in self._game_list:
      self._game_list[f"{title}: {publisher}: {year}"] = goal_objects.VideoGames(title, publisher, year, game_system, completion_hours, completion_hours, 1, rating)
      return f"The Video Game {title} by {publisher} from {year} has been added"
    
    else:
      self._game_list[f"{title}: {publisher}: {year}"].add_total_hours(completion_hours)
      self._game_list[f"{title}: {publisher}: {year}"].incr_times_finished()
      self._game_list[f"{title}: {publisher}: {year}"].update_rating(rating)
      return f"The Video Game {title} by {publisher} from {year} has been updated"


  
Korachof = User("Korachof", {}, {}, {}, {}, {}, {})

Korachof.add_book("Lost Gods", "Brom", 21, 8)

print(Korachof.get_book_list()["Lost Gods: Brom"].get_total_hours())

Korachof.add_book("Lost Gods", "Brom", 23, 8)

Korachof.add_book

print(Korachof.get_book_list()["Lost Gods: Brom"].get_total_hours())

print(Korachof.get_book_list()["Lost Gods: Brom"].get_name())