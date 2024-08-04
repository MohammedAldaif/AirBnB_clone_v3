#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def populate_db():
    # Create a new session
    session = storage.session()

    # Add States
    states = [
        State(name='California'),
        State(name='New York'),
        State(name='Texas')
    ]
    for state in states:
        session.add(state)

    # Add Cities
    cities = [
        City(name='Los Angeles', state_id=states[0].id),
        City(name='New York City', state_id=states[1].id),
        City(name='Houston', state_id=states[2].id)
    ]
    for city in cities:
        session.add(city)

    # Add Users
    users = [
        User(email='user1@example.com', password='password'),
        User(email='user2@example.com', password='password')
    ]
    for user in users:
        session.add(user)

    # Add Amenities
    amenities = [
        Amenity(name='Pool'),
        Amenity(name='Gym'),
        Amenity(name='WiFi')
    ]
    for amenity in amenities:
        session.add(amenity)

    # Add Places
    places = [
        Place(name='Beach House', city_id=cities[0].id, user_id=users[0].id),
        Place(name='City Apartment', city_id=cities[1].id, user_id=users[1].id)
    ]
    for place in places:
        session.add(place)

    # Add Reviews
    reviews = [
        Review(text='Great place!', place_id=places[0].id, user_id=users[0].id),
        Review(text='Not bad.', place_id=places[1].id, user_id=users[1].id)
    ]
    for review in reviews:
        session.add(review)

    # Commit the changes
    session.commit()

if __name__ == '__main__':
    populate_db()
