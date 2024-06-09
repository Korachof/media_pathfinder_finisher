class Books:
  """Creates a Book object to represent a finished book by the user."""
  def __init__(self, name: str, author: str, page_count: int, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._name = name
    self._author = author
    self._page_count = page_count
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  def get_name(self):
    """Returns the Book name as STR"""
    return self._name
  
  def get_author(self):
    """Returns the Book author as STR"""
    return self._author
  
  def get_page_count(self):
    """Returns the Book page count as INT"""
    return self._page_count

  def get_completion_hours(self):
    """Returns the Book first completion hours as INT"""
    return self._completion_hours

  def get_total_hours(self):
    """Returns the Book total hours as INT"""
    return self._total_hours

  def get_times_finished(self):
    """Returns the book times finished as INT"""
    return self._times_finished

  def get_rating(self):
    """Returns the book rating as INT"""
    return self._rating
  
  def get_standard_sets(self):
    """Returns the standard sets list as LIST"""
    return self._standard_sets
  
  def get_expansion_sets(self):
    """Returns the expansion sets list as LIST"""
    return self._expansion_sets

  def get_advanced_sets(self):
    """Returns the advanced sets list as LIST"""
    return self._advanced_sets

  def add_total_hours(self, additional_hours: int):
    """Add additional_hours to total_hours and return new total hours as INT"""
    self._total_hours += additional_hours
    return self._total_hours

  def incr_times_finished(self):
    """Increment the times finished and return the new times_finished as INT"""
    self._times_finished += 1
    return self._times_finished

  def update_rating(self, new_rating: int):
    """Update the rating to new_rating and return rating as INT"""
    self._rating = new_rating
    return self._rating


class Movies:
  """Creates a Movie object to represent a finished movie by the user."""
  def __init__(self, title: str, director: str, year: int, completion_minutes: int, total_minutes: int, times_finished: int, rating: int):
    self._title = title
    self._director = director
    self._year = year
    self._completion_minutes = completion_minutes
    self._total_minutes = total_minutes
    self._times_finished = times_finished
    self._rating = rating
    self._MAX_REWARD1 = 80
    self._MAX_REWARD2 = 130
    self._MAX_REWARD3 = 180
#   self._MAX_REWARD4 = >210
    self._HARDCORE_TO_THE_MEGA_FINISHED_REWARD = 7

  def get_title(self):
    """Returns the Movie title as STR"""
    return self._title
  
  def get_director(self):
    """Returns the Movie Director as STR"""
    return self._director
  
  def get_year(self):
    """Returns the Movie year as INT"""
    return self._year

  def get_completion_minutes(self):
    """Returns the Movie first completion hours as INT"""
    return self._completion_minutes

  def get_total_hours(self):
    """Returns the Movie total hours as INT"""
    return self._total_hours

  def get_times_finished(self):
    """Returns the Movie times finished as INT"""
    return self._times_finished

  def get_rating(self):
    """Returns the Movie rating as INT"""
    return self._rating

  def add_total_hours(self, additional_hours: int):
    """Add additional_hours to total_hours and return new total hours as INT"""
    self._total_hours += additional_hours
    return self._total_hours

  def incr_times_finished(self):
    """Increment the times finished and return the new times_finished as INT"""
    self._times_finished += 1
    return self._times_finished

  def update_rating(self, new_rating: int):
    """Update the rating to new_rating and return rating as INT"""
    self._rating = new_rating
    return self._rating


class VideoGames:
  """Creates a Video Game object to represent a finished video game by the user."""
  def __init__(self, title: str, publisher: str, game_system: str, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._title = title
    self._publisher = publisher
    self._game_system = game_system
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating
    self._MAX_REWARD1 = 15
    self._MAX_REWARD2 = 40
    self._MAX_REWARD3 = 80
    self._MAX_REWARD4 = 120
#   self._MAX_REWARD5 = >120
    self._HARDCORE_TO_THE_MEGA_TOTAL_HOURS = 200

  def get_title(self):
    """Returns the Video Game title as STR"""
    return self._title

  def get_publisher(self):
    """Returns the Video Game Director as STR"""
    return self._publisher

  def get_game_system(self):
    """Returns the Video Game game system as STR"""
    return self._game_system

  def get_completion_hours(self):
    """Returns the Video Game first completion hours as INT"""
    return self._completion_hours

  def get_total_hours(self):
    """Returns the Video Game total hours as INT"""
    return self._total_hours

  def get_times_finished(self):
    """Returns the Video Game times finished as INT"""
    return self._times_finished

  def get_rating(self):
    """Returns the Video Game rating as INT"""
    return self._rating

  def add_total_hours(self, additional_hours: int):
    """Add additional_hours to total_hours and return new total hours as INT"""
    self._total_hours += additional_hours
    return self._total_hours

  def incr_times_finished(self):
    """Increment the times finished and return the new times_finished as INT"""
    self._times_finished += 1
    return self._times_finished

  def update_rating(self, new_rating: int):
    """Update the rating to new_rating and return rating as INT"""
    self._rating = new_rating
    return self._rating


class TvShow:
  """Creates a TV Show object to represent a tv show with at least one finished season by the user."""
  def __init__(self, title: str, creator: str, first_season_rating: int, seasons_list: list):
    self._title = title
    self._creator = creator
    self._first_season_rating = first_season_rating
    self._seasons_list = seasons_list
    self._avg_rating = self.get_avg_rating()

  def get_title(self):
    """Returns the TV Show title as STR"""
    return self._title

  def get_creator(self):
    """Returns the TV show creator as STR"""
    return self._creator

  def get_seasons_list(self):
    """Returns the TV Show seasons list as LIST"""
    return self._seasons_list
  
  def add_season(self, season):
    """Adds a new season to the TV Show seasons list"""
    self._seasons_list.append(season)
  
  def get_total_hours(self):
    """Returns the TV Show total hours as INT"""
    seasons_list = self.get_seasons_list()
    total = 0

    for season in seasons_list:
      total += season.get_total_hours()

    return total
  
  def get_avg_rating(self):
    """Returns the average rating of all the seasons as FLOAT to two decimal points"""
    if len(self.get_seasons_list()) == 0:
      return self._first_season_rating

    seasons_list = self.get_seasons_list()
    num_of_seasons = len(seasons_list)

    for season in seasons_list:
      rating += season.get_rating()

    return round(rating / num_of_seasons, 2)

  
class TvShowSeason:
  def __init__(self, tv_show: str, season_num: int, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._tv_show = tv_show
    self._season_num = season_num
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  def get_tv_show(self):
    """Returns the TV Show Season Tv Show name as STR"""
    return self._tv_show
  
  def get_season_num(self):
    """Returns the TV Show Season Number as INT"""
    return self._season_num

  def get_completion_hours(self):
    """Returns the TV Show Season first completion hours as INT"""
    return self._completion_hours

  def get_total_hours(self):
    """Returns the TV Show Season total hours as INT"""
    return self._total_hours

  def get_times_finished(self):
    """Returns the TV Show Season times finished as INT"""
    return self._times_finished

  def get_rating(self):
    """Returns the TV Show Season rating as INT"""
    return self._rating

  def add_total_hours(self, additional_hours: int):
    """Add additional_hours to total_hours and return new total hours as INT"""
    self._total_hours += additional_hours
    return self._total_hours

  def incr_times_finished(self):
    """Increment the times finished and return the new times_finished as INT"""
    self._times_finished += 1
    return self._times_finished

  def update_rating(self, new_rating: int):
    """Update the rating to new_rating and return rating as INT"""
    self._rating = new_rating
    return self._rating

  
class Events:
  def __init__(self, name: str, location: str, date: str, completion_hours: int, keyword: str, rating):
    self._name = name
    self._location = location
    self._date = date
    self._completion_hours = completion_hours
    self._keyword = keyword
    self._rating = rating
    self._standard_sets = ["Nightmare Wetlands"]
    self._expansion_sets = ["Arctic Passage", "Mountain Clash"]
    self._advanced_sets = ["Formidable Beasts 3", "Characters of Legend 3"]

  def get_name(self):
    """Returns the Event name as STR"""
    return self._name
  
  def get_location(self):
    """Returns the Event location as STR"""
    return self._location
  
  def get_date(self):
    """Returns the Event date as STR"""
    return self._date
  
  def get_completion_hours(self):
    """Returns the Event completion hours as INT"""
    return self._completion_hours
  
  def get_keyword(self):
    """Returns the Event keyword as STR"""
    return self._keyword
  
  def get_rating(self):
    """Returns the Event rating as INT"""
    return self._rating

