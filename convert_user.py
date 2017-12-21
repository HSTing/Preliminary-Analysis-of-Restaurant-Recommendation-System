import json
import sqlite3
import time

__author__ = 'Shih-Ting Huang'
"""
CSCI-620: Introduction to Big Data
Author: Shih-Ting Huang (sh3964)

Convert user.json to User table in yelp.db
"""


class Friend:
    __slot__ = 'jsonDict', 'friend_count'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        self.friend_count = len(self.jsonDict)
        # print(self.friend_count)


class User:
    __slot__ = 'jsonDict', 'user_id', 'name', 'review_count', 'yelping_since', 'friend', 'useful', 'funny', 'cool', \
               'fans', 'elite', 'average_stars'
    # 'compliment_hot', 'compliment_more', 'compliment_profile', \
    # 'compliment_cute', 'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', \
    # 'compliment_funny', 'compliment_writer', 'compliment_photos'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        self.user_id = self.jsonDict['user_id']
        self.name = self.jsonDict['name']
        self.review_count = self.jsonDict['review_count']
        self.yelping_since = self.jsonDict['yelping_since']
        self.friend = Friend(self.jsonDict['friends'])
        self.useful = self.jsonDict['useful']
        self.funny = self.jsonDict['funny']
        self.cool = self.jsonDict['cool']
        self.fans = self.jsonDict['fans']
        # self.elite = self.jsonDict['elite']
        self.average_stars = self.jsonDict['average_stars']

    def save_to_database(self):
        con = sqlite3.connect("yelp.db")
        with con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row

            # update diesel
            cur.execute(
                "INSERT INTO User"
                "("
                "user_id,"
                "name,"
                "review_count,"
                "yelping_since,"
                "friend_count,"
                "useful,"
                "funny,"
                "cool,"
                "fans,"
                # "elite,"
                "average_stars"
                ") VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    self.user_id,
                    self.name,
                    self.review_count,
                    self.yelping_since,
                    self.friend.friend_count,
                    self.useful,
                    self.funny,
                    self.cool,
                    self.fans,
                    # self.elite,
                    self.average_stars

                )
            )


def main():
    data = []
    start = time.time()
    with open('user.json') as f:
        for line in f:
            data.append(json.loads(line))
    end = time.time()
    print('Time:', end - start)
    start = time.time()
    for case in data:
        this_case = User(case)
        this_case.save_to_database()
    end = time.time()
    print('Time:', end - start)

if __name__ == '__main__':
    main()
