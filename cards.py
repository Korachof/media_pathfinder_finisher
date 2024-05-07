class CardSet:
  def __init__(self, name, set_list):
    self._name = name
    self._set_list = set_list

  def get_name(self):
    return self._name

  def get_set_list(self):
    return self._set_list
    
class Cards:
  def __init__(self, name, attack, ac, rarity, description):
    self._name = name
    self._attack = attack
    self._ac = ac
    self._rarity = rarity
    self._description = description

  def get_name(self):
    return self._name

  def get_attack(self):
    return self._attack

  def get_ac(self):
    return self._ac

  def get_rarity(self):
    return self._rarity

  def get_description(self):
    return self._description
