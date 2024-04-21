import datetime
import sqlite3
from typing import List
from dataclasses import dataclass

__places = []


@dataclass
class Place:
    name:str | None = ""
    description:str | None = ""
    value: str | None = ""
    price: int | str | None = ""
    start: str | None = ""
    end: str | None = ""
    address: str | None = ""
    phone: str | None = ""
    transport: str | None = ""
    url: str | None = ""
        
    @classmethod
    def from_query(cls, query):
        query = [i if i!='None' else "Нет данных" for i in query]
        return cls(*query, 
                   f'https://maps.google.com/maps?q={query[0].replace(" ", "+").replace("»", "").replace("«", "").replace("<<", "").replace(">>", "")}')

def places() -> List[Place]:
    global __places
    if __places == [] or (__places[1]-datetime.datetime.now()).total_seconds() >= 3600:
        with  sqlite3.connect('db.sqlite') as connection :
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM places")
            __places = [[], None]
            for i in cursor.fetchall():
                __places[0].append(Place.from_query(i))
            __places[1] = datetime.datetime.now()
            cursor.close()
    return __places[0]