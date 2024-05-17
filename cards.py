import json
from random import randrange


class CardSet:
  def __init__(self, name, set_contents):
    self._name = name
    self._set_list_hash = {}
    self._set_contents = set_contents
    self.add_cards_from_db(self._set_contents)

  def get_name(self):
    return self._name

  def get_set_list(self):
    return self._set_list_hash

  def open_card_list_db(self):
    with open("card_set_db.json") as card_set_file:
      card_list_data = json.load(card_set_file)

    card_set_file.close()
    
    return card_list_data
    
  def add_cards_from_db(self, card_list_data):
    for card in card_list_data[self._name]:
      self.add_card(
        card["title"],
        card["category"],
        card["trait"],
        card["rarity"],
        card["cardNumber"])

  def add_card(self, title, category, trait, rarity, card_num):
    self._set_list_hash[title] = Cards(title, category, trait, rarity, card_num, 1)


class CardPacks:
  def __init__(self, card_set: CardSet):
    self._card_set = card_set
    self._COMMON_MAX = 31
    self._UNCOMMON_MAX = 47
    self._RARE_MAX = 59
    self._UNIQUE_MAX = 7
    self._contents = []
    self.set_pack_registry()

  def get_set_name(self):
    return self._card_set.get_name()

  def get_card_set(self):
    return self._card_set
  
  def get_contents(self):
    return self._contents
  
  def set_pack_registry(self):
    """2 Common, 1 Uncommon, 1 Common/Uncommon, 1 Rare/Unique"""
    card1 = randrange(1, self._COMMON_MAX)
    card2 = randrange(1, self._COMMON_MAX)
    while card2 == card1:
      card2 = randrange(1, self._COMMON_MAX)
    card3 = randrange(1, self._UNCOMMON_MAX)
    while card3 == card1 or card3 == card2:
      card3 = randrange(1, self._COMMON_MAX)
    card4 = randrange(self._COMMON_MAX, self._UNCOMMON_MAX)
    while card4 == card1 or card4 == card2 or card4 == card3:
      card4 = randrange(1, self._COMMON_MAX)

    card5= self.check_for_unique()
    return self.fill_packs([card1, card2, card3, card4, card5])

  def check_for_unique(self):
    card5 = randrange(self._UNCOMMON_MAX, self._RARE_MAX)

    if card5 == 47 or card5 == 51 or card5 == 58:
      unique_chance = randrange(1, self._UNIQUE_MAX)
      if unique_chance == 1:
        card5 = 59

      elif unique_chance == 6:
        card5 = 60

    return card5

  def fill_packs(self, pack_registry):
    set_list = self._card_set.get_set_list()
    booster_pack = []

    while len(pack_registry) > 0:
      for key in set_list:
        if set_list[key].get_card_num() in pack_registry:
          booster_pack.append(set_list[key])
          pack_registry.remove(set_list[key].get_card_num())

    return self.set_contents(booster_pack)
  
  def set_contents(self, booster_pack):
    for card in booster_pack:
      self._contents.append(card)


class Cards:
  def __init__(self, title, category, trait, rarity, card_num, quantity):
    self._title = title
    self._category = category
    self._trait = trait
    self._rarity = rarity
    self._card_num = card_num
    self._quantity = quantity

  def get_name(self):
    return self._title

  def get_category(self):
    return self._category

  def get_trait(self):
    return self._trait

  def get_rarity(self):
    return self._rarity

  def get_card_num(self):
    return self._card_num
  
  def increment_quantity(self):
    self._quantity += 1