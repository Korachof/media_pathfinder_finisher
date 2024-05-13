class CardSet:
  def __init__(self, name, set_list_hash):
    self._name = name
    self._set_list_hash = set_list_hash

  def get_name(self):
    return self._name

  def get_set_list(self):
    return self._set_list_hash

  def get_card_from_db(self):

  
  # def add_card(self, title, category, trait, rarity, card_num):
  #  self._set_list[title] = Cards(title, category, trait, rarity, card_num)


    
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
