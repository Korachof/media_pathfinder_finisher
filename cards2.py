import json
from random import randrange

# Globals for standard booster packs 
STRD_PACK_COMMON_MAX = 31
STRD_PACK_UNCOMMON_MAX = 47
STRD_PACK_RARE_MAX = 59
STRD_PACK_UNIQUE_MAX = 7
# Globals for expansion booster packs
EXP_PACK_COMMON_MAX = 11
EXP_PACK_UNCOMMON_MAX = 17
EXP_PACK_RARE_MAX = 21
EXP_PACK_UNIQUE_MAX = 6
# Globals for addvanced booster packs
ADV_PACK_ULTRA_RARE_MAX = 6
#Globals for Base set booster packs
BASE_PACK_COMMON_MAX = 201
BASE_PACK_UNCOMMON_MAX = 311
BASE_PACK_RARE_MAX = 391
BASE_PACK_UNIQUE_MAX = 401


class CardSet:
    def __init__(self, name, card_db, set_contents):
        self._name = name
        self._card_db = card_db
        self._set_dict = {}
        self._set_contents = set_contents
        self.add_cards_from_db()
    
    def get_name(self):
        """Get Card Set name
        returns: self._name (STR)"""
        return self._name

    def get_set_dict(self):
        """get Card Set card list
        returns: self._set_list_hash"""
        return self._set_dict

    def open_card_list_db(self):
        """open the card list database
        returns: card_list_data (DICT)"""
        if self._set_type == "standard":
            with open(f"{self._card_db}") as card_set_file:
                card_list_data = json.load(card_set_file)

            card_set_file.close()
    
        return card_list_data
    
    def add_cards_from_db(self):
        """add cards from json database to hashmap
        returns: None"""
        for card in self._set_contents[self._name]:
            self.add_card(
                card["title"],
                card["category"],
                card["trait"],
                card["rarity"],
                card["cardNumber"])

    def add_card(self, title, category, trait, rarity, card_num):
        """add card using attributes to hashmap
        returns: None"""
        self._set_dict[title] = Cards(title, category, trait, rarity, card_num, 1)


class CardPacks:
    """parent CardPack class"""
    def __init__(self, card_set: CardSet):
        self._card_set = card_set
        self._contents = []

    def get_set_name(self):
        """returns the CardPack set name (STR)"""
        return self._card_set.get_name()
    
    def get_card_set(self):
        """returns: CardPack card_set (OBJ)"""
        return self._card_set
  
    def get_contents(self):
        """returns CardPack contents (LIST)"""
        return self._contents
  
    def fill_packs(self, pack_registry):
        """Fills the CardPack with cards
        returns: True if contents set correctly"""
        set_list = self._card_set.get_set_list()
        booster_pack = []

        while len(pack_registry) > 0:
            for key in set_list:
                if set_list[key].get_card_num() in pack_registry:
                    booster_pack.append(set_list[key])
                    pack_registry.remove(set_list[key].get_card_num())

        return self.set_contents(booster_pack)
        
    def set_contents(self, booster_pack):
        """set the contents of the CardPack
        returns: True"""
        for card in booster_pack:
            self._contents.append(card)

        return True


class StandardCardPacks(CardPacks):
    """child class of CardPacks"""
    def __init__(self, card_set:CardSet):
        self.set_pack_registry()
        super().__init__(self, card_set)

    def set_pack_registry(self):
        """Sets the card numbers for the cards in the pack
        2 Common, 1 Uncommon, 1 Common/Uncommon, 1 Rare/Unique
        returns: True if pack successfully created"""
        card1 = randrange(1, STRD_PACK_COMMON_MAX)
        card2 = randrange(1, STRD_PACK_COMMON_MAX)
        while card2 == card1:
            card2 = randrange(1, STRD_PACK_COMMON_MAX)
        card3 = randrange(1, STRD_PACK_UNCOMMON_MAX)
        while card3 == card1 or card3 == card2:
            card3 = randrange(1, STRD_PACK_UNCOMMON_MAX)
        card4 = randrange(STRD_PACK_COMMON_MAX, STRD_PACK_UNCOMMON_MAX)
        while card4 == card1 or card4 == card2 or card4 == card3:
            card4 = randrange(STRD_PACK_COMMON_MAX, STRD_PACK_UNCOMMON_MAX)

        card5= self.check_for_unique()
        return self.fill_packs([card1, card2, card3, card4, card5])

    def check_for_unique(self):
        """Checks to see if the 5th card in the pack is a rare or
        unique. Creates the card number.
        returns: card5 (INT)"""
        card5 = randrange(STRD_PACK_UNCOMMON_MAX, STRD_PACK_RARE_MAX)

        if card5 == 47 or card5 == 51 or card5 == 58:
            unique_chance = randrange(1, STRD_PACK_UNIQUE_MAX)
        if unique_chance == 1:
            card5 = 59
        elif unique_chance == 6:
            card5 = 60

        return card5
    

class Cards:
    def __init__(self, title, category, trait, rarity, card_num, quantity):
        self._title = title
        self._category = category
        self._trait = trait
        self._rarity = rarity
        self._card_num = card_num
        self._quantity = quantity
        
    def get_name(self):
        """returns: Card name (STR)"""
        return self._title

    def get_category(self):
        """returns: Card category (STR)"""
        return self._category

    def get_trait(self):
        """returns: Card trait (STR)"""
        return self._trait

    def get_rarity(self):
        """returns: Card rarity (STR)"""
        return self._rarity

    def get_card_num(self):
        """returns: card number (INT)"""
        return self._card_num
  
    def increment_quantity(self):
        """increments quantity the user possesses of this card"""
        self._quantity += 1
  