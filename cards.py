import json
import random


class CardSet:
  def __init__(self, name, set_list_hash):
    self._name = name
    self._set_list_hash = set_list_hash

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
    self._set_list_hash[title] = Cards(title, category, trait, rarity, card_num)


class CardPacks:
  def __init__(self, set_name, card_set, contents):
    self._set_name = set_name
    self._card_set = card_set
    self._contents = contents
    self._COMMON_MAX = 20
    self._UNCOMMON_MAX = 20
    self._RARE_MAX = 18
    self._UNIQUE_MAX = 6

  def get_set_name(self):
    return self._set_name

  def get_card_set(self):
    return self._card_set
  
  def get_contents(self):
    return self._contents
  
  def set_contents(self):
    """3 Common, 1 Uncommon, 1 Rare/Unique"""
    card1 = random(1, self._COMMON_MAX)
    card2 = random(1, self._COMMON_MAX)
    card3 = random(1, self._COMMON_MAX)
    card4 = random(1, self._UNCOMMON_MAX)
    card5 = random(1, self._RARE_MAX)
    
    if card5 == 1 or card5 == 3 or card5 == 7 or card5 == 11 or card5 == 18:
      unique_chance = random(1, self._UNIQUE_MAX)
      if unique_chance == 1:
        card5 = 19

      elif unique_chance == 6:
        card5 = 20

    return self.fill_packs([card1, card2, card3, card4, card5])

  def fill_packs(self, pack_registry):
    set_list = self._card_set.get_set_list()
    booster_pack = []

    while len(pack_registry) > 0:
      for key in set_list:
        if set_list[key].get_card_num() in pack_registry:
          booster_pack.append(set_list[key])
          pack_registry.remove(set_list[key].get_card_num())



class Cards:
  def __init__(self, title, category, trait, rarity, card_num):
    self._title = title
    self._category = category
    self._trait = trait
    self._rarity = rarity
    self._card_num = card_num

  def get_name(self):
    return self._name

  def get_category(self):
    return self._category

  def get_trait(self):
    return self._trait

  def get_rarity(self):
    return self._rarity

  def get_card_num(self):
    return self._card_num


wildlife_mayhem = CardSet("Wildlife Mayhem", {})

card_dict = wildlife_mayhem.open_card_list_db()

wildlife_mayhem.add_cards_from_db(card_dict)

print(wildlife_mayhem.get_set_list())
