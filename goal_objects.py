class Books:
  """Creates a Book object to represent a finished book by the user."""
  def __init__(self, name: str, author: str, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._name = name
    self._author = author
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
  def __init__(self, title: str, director: str, completion_hours: int, total_hours: int, times_finished: int, rating: int):
    self._title = title
    self._director = director
    self._completion_hours = completion_hours
    self._total_hours = total_hours
    self._times_finished = times_finished
    self._rating = rating

  def get_title(self):
    """Returns the Movie title as STR"""
    return self._title
  
  def get_director(self):
    """Returns the Movie Director as STR"""
    return self._director

  def get_completion_hours(self):
    """Returns the Movie first completion hours as INT"""
    return self._completion_hours

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
  def __init__(self, title: str, creator: str, seasons_list: list, avg_rating: int):
    self._title = title
    self._creator = creator
    self._seasons_list = seasons_list
    self._avg_rating = avg_rating

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
    seasons_list = self.get_seasons_list()
    num_of_seasons = len(seasons_list)
    rating = 0

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

  
