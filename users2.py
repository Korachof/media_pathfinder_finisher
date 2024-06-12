import goal_objects
import cards
import json
import itertools
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
# Pack Type List
PACK_TYPE_LIST = [cards.StandardCardPacks, cards.ExpansionCardPacks, cards.AdvancedCardPacks, cards.BaseSetCardPacks]


class User:
    def __init__(self, name: str, book_dict: dict, movie_dict: dict, game_dict: dict, tv_dict: dict, event_dict: dict, booster_pack_dict: dict, collectibles_dict: dict):
        self._name = name
        self._book_dict = book_dict
        self._movie_dict = movie_dict
        self._game_dict = game_dict
        self._tv_dict = tv_dict
        self._event_dict = event_dict
        self._booster_pack_dict = booster_pack_dict
        self._booster_pack_quantity = {}
        self._collectibles_dict = collectibles_dict
        self._card_sets = {}
        self._card_file = self.open_card_list_db()
        self._base_card_file = self.open_base_card_list_db()
        self.update_card_sets("standard", self._card_file)
        self.update_card_sets("base", self._base_card_file)

# User getter methods

    def get_name(self):
        """returns: User object name (STR)"""
        return self._name

    def get_book_dict(self):
        """returns: User object book_dict (DICT)"""
        return self._book_dict

    def get_movie_dict(self):
        """returns: User object movie_dict (DICT)"""
        return self._movie_dict

    def get_game_dict(self):
        """returns: User object game_dict (DICT)"""
        return self._game_dict

    def get_tv_dict(self):
        """returns: User object tv_dict (DICT)"""
        return self._tv_dict

    def get_event_dict(self):
        """returns: User object event_dict (DICT)"""
        return self._event_dict
  
    def get_booster_pack_dict(self):
        """returns: User object booster_pack_dict (DICT)"""
        return self._booster_pack_dict

    def get_collectibles_dict(self):
        """returns: User object collectibles_dict (DICT)"""
        return self._collectibles_dict
  
    def get_pack_quantity(self, set_name):
        """returns the number of a specific booster pack the user has
        parameter: set_name (STR)
        returns: qty (INT)"""
        qty = 0
        if set_name in self._packs_quantity:
            qty = self._packs_quantity[set_name]

        return qty
    
# User booster pack methods
    
    def get_booster_pack_type(self, set_info):
        if set_info[1] == 0 or set_info[1] == 1:
            self.add_booster_pack(set_info[0], set_info[1])
            self.add_base_set_booster_pack(CURRENT_BASE_SET)
        elif set_info[1] == 2 or set_info[1] == 3:
            self.add_booster_pack(set_info[0], set_info[1])
            self.add_base_set_booster_pack(CURRENT_BASE_SET)
            self.add_base_set_booster_pack(CURRENT_BASE_SET)
        elif set_info[1] == 4:
            self.add_booster_pack(set_info[0], set_info[1])
            self.add_base_set_booster_pack(CURRENT_BASE_SET)
            self.add_base_set_booster_pack(CURRENT_BASE_SET)
            self.add_base_set_booster_pack(CURRENT_BASE_SET)  

    def add_booster_pack(self, set_name: str, set_type_index):
        booster = PACK_TYPE_LIST[set_type_index](self._card_sets[set_name])
        if set_name not in self._booster_pack_dict:
            self._booster_pack_dict[set_name] = [booster]
        else:
            self._booster_pack_dict[set_name].append(booster)

        print(f"The booster pack from {set_name} has been added.")
        self.increment_booster_pack(set_name)

    def add_base_set_booster_pack(self, set_name:str):
        booster = cards.BaseSetCardPacks(self._card_sets[set_name])

        if set_name not in self._booster_pack_dict:
            self._booster_pack_dict[set_name] = [booster]
        else:
            self._booster_pack_dict[set_name].append(booster)

        print(f"The booster pack from {set_name} has been added.")
        self.increment_booster_pack(set_name)

    def increment_booster_pack(self, set_name: str):
        if set_name in self._booster_pack_quantity:
            self._booster_pack_quantity[set_name] += 1

        else:
            self._booster_pack_quantity[set_name] = 1

    def select_booster_to_open(self, set_name):
        """Select the booster pack to open corresponding to the set_name
        parameter: set_name (STR
        returns: None)"""
        booster_pack = None
        if len(self._booster_pack_list[set_name]) > 0:
            booster_pack = self._booster_pack_dict[set_name][0]
            self._booster_pack_list[set_name].pop(0)

        return self.open_booster_pack(booster_pack)
  
    def open_booster_pack(self, booster_pack):
        """opens the booster pack
        parameter: booster_pack (OBJ)
        returns: None"""
        if booster_pack is None:
            print(f"You do not have any booster packs of this type")
            return

        # get_contents returns a list
        for card in booster_pack.get_contents():
            if booster_pack.get_set_name() in self._collectibles_dict:
                if card.get_name() in self._collectibles_dict[booster_pack.get_set_name()]:
                    self._collectibles_dict[booster_pack.get_set_name()][card.get_name()].increment_quantity()
                else:
                    self._collectibles_dict[booster_pack.get_set_name()][card.get_name()] = card
        else:
            self._collectibles_dict[booster_pack.get_set_name()] = {card.get_name(): card}
      
        print(f"Opened {card.get_name()} from {booster_pack.get_set_name()}")
        print(card._quantity)
    
        self._booster_pack_quantity[booster_pack.get_set_name()] -= 1

        del booster_pack

        self.get_booster_pack_type((set))

# User card set methods

    def find_card_set(self, attribute, set_list, req_list):
        """find the card set that matches the attribute
        parameter: attribute (INT)
        parameter: set_list (LIST)
        parameter: req_list (LIST)
        returns """
        set_list_index = 0
        for req in itertools.islice(req_list, 4):
            if attribute < req:
                set = [choice(set_list[set_list_index]), set_list_index]
                return self.get_booster_pack_type((set))
            set_list_index += 1

        if attribute > req_list[4]:
                set = [choice(set_list[4]), 4]
                return self.get_booster_pack_type((set))
        
    def open_card_list_db(self):
        with open("card_set_db.json") as card_set_file:
            card_list_data = json.load(card_set_file)

        card_set_file.close()
    
        return card_list_data
  
    def open_base_card_list_db(self):
        with open("base_card_set_db.json") as card_set_file:
            card_list_data = json.load(card_set_file)

        card_set_file.close()
    
        return card_list_data

    def update_card_sets(self, set_type, card_list_data):
        if set_type == "base":
            for key in card_list_data:
                self._card_sets[key] = cards.CardSet(key, "base_card_set_db.json", card_list_data)
        elif set_type == "standard":
            for key in card_list_data:
                self._card_sets[key] = cards.CardSet(key, "card_set_db.json", card_list_data)

# User filter methods

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
    

