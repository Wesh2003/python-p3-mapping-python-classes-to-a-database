#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

def reset_database():
    Song.drop_table()
    Song.create_table()
    Song.create("hello", "25")
    Song.create("99 Problems", "The Black Album")   


if __name__ == '__main__':
    reset_database()
    import ipdb; ipdb.set_trace()
