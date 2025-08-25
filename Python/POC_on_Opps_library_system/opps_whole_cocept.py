from abc import ABC, abstractmethod
from datetime import datetime

# ------------------ Decorator for logging ------------------

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Finished: {func.__name__}")
        return result
    return wrapper

# ------------------ Abstract Base Class ------------------

class TicketBookingSystem(ABC):
    @abstractmethod
    def show_movies(self):
        pass

    @abstractmethod
    def book_ticket(self, movie_name, seats):
        pass

# ------------------ Movie Class (Data Layer) ------------------

class Movie:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

# ------------------ Booking System Implementation ------------------

class OnlineBookingSystem(TicketBookingSystem):

    # class-level movie list shared across all instances
    movies = {}

    def __init__(self, user_name):
        self.__user_name = user_name  # encapsulated

    @classmethod
    def add_movie(cls, name, seats):
        cls.movies[name] = Movie(name, seats)

    @staticmethod
    def validate_seat_count(seats):
        return seats > 0

    @log_action
    def show_movies(self):
        print(f"\nAvailable Movies for {self.__user_name}:")
        for name, movie in self.movies.items():
            print(f"🎬 {name} - Available Seats: {movie.available_seats()}")

    @log_action
    def book_ticket(self, movie_name, seats):
        if movie_name not in self.movies:
            print("❌ Movie not found!")
            return

        movie = self.movies[movie_name]

        if not self.validate_seat_count(seats):
            print("❌ Invalid number of seats!")
            return

        if movie.available_seats() >= seats:
            movie.booked_seats += seats
            print(f"✅ {self.__user_name} booked {seats} seat(s) for {movie_name}")
        else:
            print("❌ Not enough seats available!")

# ------------------ Polymorphism Example ------------------

class AdminBooking(OnlineBookingSystem):
    @log_action
    def book_ticket(self, movie_name, seats):
        # Admins can overbook
        movie = self.movies.get(movie_name)
        if movie:
            movie.booked_seats += seats
            print(f"👑 Admin {self._OnlineBookingSystem__user_name} overbooked {seats} seat(s) for {movie_name}")
        else:
            print("❌ Movie not found!")

# ------------------ Main Flow ------------------

if __name__ == "__main__":

    # Add movies using class method
    OnlineBookingSystem.add_movie("Inception", 10)
    OnlineBookingSystem.add_movie("Interstellar", 5)

    # Create user and admin
    user1 = OnlineBookingSystem("Sai")
    admin1 = AdminBooking("Teja(Admin)")

    user1.show_movies()
    user1.book_ticket("Inception", 3)
    user1.book_ticket("Inception", 8)  # Not enough seats

    admin1.book_ticket("Interstellar", 6)  # Overbooking by admin

    user1.show_movies()  # Final status
