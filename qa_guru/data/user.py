from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth_day: str
    date_of_birth_month: str
    date_of_birth_year: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str