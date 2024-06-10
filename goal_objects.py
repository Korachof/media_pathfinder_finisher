class GoalObjects():
    """Parent class for all child goal object classes"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int):
        self._title = title
        self._year_created = year_created
        self._date_finished = date_finished
        self._total_hours = total_hours
        self._rating = rating

    def get_title(self):
        """returns: the goal object title (STR)"""
        return self._title
    
    def get_year_created(self):
        """returns: the goal object's year created (INT)"""
        return self._year_created
    
    def get_date_finished(self):
        """returns: the goal object date finished (STR)"""
        return self._date_finished

    def get_total_hours(self):
        """returns: the goal object total hours (INT)"""
        return self._total_hours

    def get_rating(self):
        """returns: the goal object rating (INT)"""
        return self._rating
    
    def add_total_hours(self, additional_hours: int):
        """Add additional_hours to total_hours and return new total hours as INT"""
        self._total_hours += additional_hours
        return self._total_hours
    
    def update_rating(self, new_rating: int):
        """Update the rating to new_rating and return rating as INT"""
        self._rating = new_rating
        return self._rating


class Books(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, author: str, page_count: int, times_finished: int):
        self._author = author
        self._page_count = page_count
        self._times_finished = times_finished
        super().__init__(title, year_created, date_finished, total_hours, rating)

    def get_author(self):
        """returns: the book object's author (STR)"""
        return self._author
    
    def get_page_count(self):
        """returns: the book object's page count (INT)"""
        return self._page_count
    
    def get_times_finished(self):
        """returns: the book object's times finished (INT)"""
        return self._times_finished
    

class Movies(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, director: str, runtime: int, times_watched: int):
        self._director = director
        self._runtime = runtime
        self._times_watched = times_watched
        super().__init__(title, year_created, date_finished, total_hours, rating)

    def get_director(self):
        """returns: the movie object's director (STR)"""
        return self._director
    
    def get_runtime(self):
        """returns: the movie object's runtime (INT)"""
        return self._runtime
    
    def get_times_watched(self):
        """returns: the movie object's times watched (INT)"""
        return self._times_watched

    def incr_times_watched(self):
        """Increment the times watched and return the new times_finished as INT"""
        self._times_watched += 1
        return self._times_watched
    

class VideoGames(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, completion_hours: int, year_created: int, date_finished: str, total_hours: int, rating: int, publisher: str, all_achievements: bool, times_finished: int):
        self._publisher = publisher
        self._completion_hours = completion_hours
        self._all_achievements = all_achievements
        self._times_finished = times_finished
        super().__init__(title, year_created, date_finished, completion_hours, total_hours, rating)

    def get_publisher(self):
        """returns: video game object's publisher (STR)"""
        return self._publisher

    def get_completion_hours(self):
        """returns: video game object's completion hours (INT)"""
        return self._completion_hours
    
    def get_achievement_status(self):
        """returns: video game all achievements check (BOOL)"""
        return self._all_achievements
    
    def get_times_finished(self):
        """returns: the video game object's times finished (INT)"""
        return self._times_finished
    
    def incr_times_finished(self):
        """Increment the times finished and return the new times_finished as INT"""
        self._times_finished += 1
        return self._times_finished


class Shows(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, creator: str):
        self._creator = creator
        super().__init__(title, year_created, date_finished, total_hours, rating)

    def get_creator(self):
        """returns: show object's creator (STR)"""
        return self._creator
    

class SeasonalShows(Shows):
    """child class to goal objects parent class"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, creator: str, seasons_dict: dict):
        self._seasons_dict = seasons_dict
        self._season_avg = self.find_avg_rating()
        super().__init__(title, year_created, total_hours, date_finished, rating, creator)

    def get_seasons_dict(self):
        """returns: the seasonal show object's seasons dictionary (DICT)"""
        return self._seasons_dict

    def add_new_season(self, finish_date, runtime, season_num, rating):
        """adds a new season object to the seasons_dict"""
        season = Seasons(self._title, self._year_created, finish_date, runtime, rating, self._creator, season_num, 1)
        self._seasons_dict[season_num] = season

    def find_avg_rating(self):
        """finds the average rating of all seasons"""

        if len(self._seasons_dict) > 0:
            rating_avg = sum(self._seasons_dict) / len(self._seasons_dict)

            return round(rating_avg, 2)


class Seasons(Shows):
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, creator: str, season_num: int, times_finished: int):
        self._season_num = season_num
        self._times_finished = times_finished
        super().__init__(title, year_created, total_hours, date_finished, rating, creator)

    def get_season_num(self):
        """returns: show season object's season number (INT)"""
        return self._season_num
    
    def incr_times_finished(self):
        """Increment the times finished and return the new times_finished as INT"""
        self._times_finished += 1
        return self._times_finished
    

class SocialEvents(GoalObjects):
    """child class to goal objects parent class"""
    def __init__(self, title: str, year_created: int, date_finished: str, total_hours: int, rating: int, event_type: str, location: str):
        self._event_type = event_type
        self._location = location
        super().__init__(title, year_created, date_finished, total_hours, rating)

    def get_event_type(self):
        """returns: social event object's event type (STR)"""
        return self._event_type
    
    def get_location(self):
        """returns: social event object's location (STR)"""
        return self._location