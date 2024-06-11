import goal_objects
import cards
import json
from random import choice

# Global Constants
# Card Set Lists
CURRENT_BASE_SET = "Base Set 1"
BOOK_CARD_SET_LIST = [["Underrealm Gateway"], ["Hazardous Waters"], ["Hidden Jungle"], ["Formidable Beasts"], ["Characters of Legend"]]
MOVIE_CARD_SET_LIST = [["Wildlife Mayhem"], ["Hazardous Waters 2"], ["Sands of Death"], ["Legendary Monsters"], ["Characters of Legend 2"]]
VIDEO_GAME_CARD_SET_LIST = [["Extraplanar Activity"], ["Hazardous Waters 3"], ["Swiftblade Fields"], ["Formidable Beasts 2"], ["Celestial Power"]]
SHOW_CARD_SET_LIST = [["Monstrous Ground"], ["Hazardous Waters 4"], ["Sands of Death 2"], ["Demonic Pact"], ["Strange Animals"]]
EVENT_CARD_SET_LIST= [["Arctic Passage"], ["Hazardous Waters 4"], ["Mountain Clash"], ["Formidable Beasts 3"], ["Characters of Legend 3"]]
# Lists containing attributes to connect to the right Card Set List
BOOK_SET_REQ_LIST = [151, 301, 451, 601, 600]
MOVIE_SET_REQ_LIST = [71, 101, 151, 191, 190]
VIDEO_GAME_SET_REQ_LIST = [16, 41, 81, 121, 120]
SHOW_SET_REQ_LIST = [281, 481, 681, 881, 880]
SOCIAL_EVENT_SET_REQ_LIST = [60, 120, 180, 240]


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
        self._base_card_file = self.open_base_card_list_db()
        self.update_card_sets("standard", self._card_file)
        self.update_card_sets("base", self._base_card_file)
        

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

def find_card_set(self, attribute, set_list, req_list):
  set_list_index = 0
  for req in req_list:
    if req == attribute:
      set = [choice(set_list[set_list_index]), 1]
  
    self.get_booster_pack_type((set))
