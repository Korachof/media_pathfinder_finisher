import json

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
    self._set_list[title] = Cards(title, category, trait, rarity, card_num)


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
