import goal_objects
import cards
import json

class User:
  def __init__(self, name: str, book_list: dict, movie_list: dict, game_list: dict, tv_list: dict, event_list: dict, booster_pack_list: dict, collectibles_list: dict):
    self._name = name
    self._book_list = book_list
    self._movie_list = movie_list
    self._game_list = game_list
    self._tv_list = tv_list
    self._event_list = event_list
    self._booster_pack_list = booster_pack_list
    self._booster_pack_quantity = {}
    self._collectibles_list = collectibles_list
    self._card_sets = {}
    self._card_file = self.open_card_list_db()
    self.update_card_sets(self._card_file)

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
  
  def get_pack_quantity(self, set_name):
    qty = 0
    if set_name in self._packs_quantity:
      qty = self._packs_quantity[set_name]

    return qty

  def select_booster_to_open(self, set_name):
    booster_pack = None
    if len(self._booster_pack_list[set_name]) > 0:
      booster_pack = self._booster_pack_list[set_name][0]
      self._booster_pack_list[set_name].pop(0)

    return self.open_booster_pack(booster_pack)
  
  def open_booster_pack(self, booster_pack):
    if booster_pack is None:
      print(f"You do not have any booster packs of this type")
      return

    for card in booster_pack.get_contents():
      if booster_pack.get_set_name() in self._collectibles_list:
        if card.get_name() in self._collectibles_list[booster_pack.get_set_name()]:
          self._collectibles_list[booster_pack.get_set_name()][card.get_name()].increment_quantity()

        else:
          self._collectibles_list[booster_pack.get_set_name()][card.get_name()] = card
        
      else:
        self._collectibles_list[booster_pack.get_set_name()] = {card.get_name(): card}
      
      print(f"Opened {card.get_name()} from {booster_pack.get_set_name()}")
      print(card._quantity)
    
    self._booster_pack_quantity[booster_pack.get_set_name()] -= 1

    del booster_pack

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
    
  def add_tv_show(self, title: str, creator: str, seasons_list):
    if f"{title}: {creator}" not in self._tv_list:
      self._tv_list[f"{title}: {creator}"] = goal_objects.TvShow(title, creator, seasons_list)
      return f"The TV Show {title} by {creator} has been added"
    
    else:
      return f"The TV Show {title} by {creator} already exists"

  def add_tv_season(self, tv_show: str, creator: str, season_num: int, completion_hours: int, rating: int):
    self.add_tv_show(tv_show, creator, {})

    if self._tv_list[f"{tv_show}: {creator}"].get_seasons_list()[season_num]:
      self._tv_list[f"{tv_show}: {creator}"].add_total_hours(completion_hours)
      self._tv_list[f"{tv_show}: {creator}"].incr_times_finished()
      self._tv_list[f"{tv_show}: {creator}"].update_rating(rating)
      return f"Season {season_num} of {tv_show} by {creator} has been updated"
    
    else:
      self._tv_list[f"{tv_show}: {creator}"].add_season(goal_objects.TvShowSeason(tv_show, season_num, completion_hours, completion_hours, 1, rating))
      return f"Season {season_num} of {tv_show} by {creator} has been created"
    
  def add_booster_pack(self, set_name: str):
    booster = cards.CardPacks(self._card_sets[set_name])
    if set_name not in self._booster_pack_list:
      self._booster_pack_list[set_name] = [booster]

    else:
      self._booster_pack_list[set_name].append(booster)

    print(f"The booster pack from {set_name} has been added.")

    self.increment_booster_pack(set_name)

  def increment_booster_pack(self, set_name: str):
    if set_name in self._booster_pack_quantity:
      self._booster_pack_quantity[set_name] += 1

    else:
      self._booster_pack_quantity[set_name] = 1

  def open_card_list_db(self):
    with open("card_set_db.json") as card_set_file:
      card_list_data = json.load(card_set_file)

    card_set_file.close()
    
    return card_list_data

  def update_card_sets(self, card_list_data):
    for key in card_list_data:
      self._card_sets[key] = cards.CardSet(key, card_list_data)
    

  
Korachof = User("Korachof", {}, {}, {}, {}, {}, {}, {})

print(Korachof._card_sets)

Korachof.add_book("Lost Gods", "Brom", 21, 8)

print(Korachof.get_book_list()["Lost Gods: Brom"].get_name())

Korachof.add_booster_pack("Wildlife Mayhem")
Korachof.add_booster_pack("Wildlife Mayhem")
Korachof.add_booster_pack("Wildlife Mayhem")
Korachof.add_booster_pack("Monstrous Ground")
Korachof.add_booster_pack("Wildlife Mayhem")

print(f"Number of Wildlife Mayhem Boosters is: {Korachof._booster_pack_quantity['Wildlife Mayhem']}")
print(f"Number of Monstrous Ground Boosters is: {Korachof._booster_pack_quantity['Monstrous Ground']}")

Korachof.select_booster_to_open("Wildlife Mayhem")
Korachof.select_booster_to_open("Wildlife Mayhem")
Korachof.select_booster_to_open("Wildlife Mayhem")
Korachof.select_booster_to_open("Wildlife Mayhem")
Korachof.select_booster_to_open("Wildlife Mayhem")
Korachof.select_booster_to_open("Monstrous Ground")

print(f"Number of Wildlife Mayhem Boosters is: {Korachof._booster_pack_quantity['Wildlife Mayhem']}")

print(Korachof.get_collectibles_list())


def odds_opening_rare(num_of_packs):
  odds = 0.917
  print(range(num_of_packs + 1))
  for num in range(num_of_packs + 1):
    odds = odds * 0.917

  return odds

print(odds_opening_rare(3))