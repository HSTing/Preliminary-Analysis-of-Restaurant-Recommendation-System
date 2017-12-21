import json
import sqlite3
import time

__author__ = 'Shih-Ting Huang'
"""
CSCI-620: Introduction to Big Data
Author: Shih-Ting Huang (sh3964)

Convert review.json to Review table in yelp.db
"""


class Review:
    __slot__ = 'jsonDict', 'review_id', 'user_id', 'stars', 'text','business_id', 'date', 'useful', 'funny', 'cool'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        self.date = self.jsonDict['date']
        self.stars = self.jsonDict['stars']
        self.business_id = self.jsonDict['business_id']
        self.user_id = self.jsonDict['user_id']
	self.review = self.jsonDict['text']
        self.review_id = self.jsonDict['review_id']
        self.useful = self.jsonDict['useful']
        self.funny = self.jsonDict['funny']
        self.cool = self.jsonDict['cool']

    def save_to_database(self):
        con = sqlite3.connect("yelp.db")
        with con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row

            # update diesel
            cur.execute(
                "INSERT INTO Review"
                "("
                "review_id,"
                "user_id,"
                "business_id,"
                "date,"
		"review,"
                "stars,"
                "useful,"
                "funny,"
                "cool"
                ") VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    self.review_id,
                    self.user_id,
                    self.business_id,
                    self.date,
		    self.review,
                    self.stars,
                    self.useful,
                    self.funny,
                    self.cool
                )
            )


def main():
    data = []
    start = time.time()
    with open('review.json') as f:
        i = 0
        for line in f:
            if i % 10 == 0:
                data.append(json.loads(line))
            i += 1
    end = time.time()
    print('Time:', end - start)
    start = time.time()
    for case in data:
        this_case = Review(case)
        this_case.save_to_database()
    end = time.time()
    print('Time:', end - start)

if __name__ == '__main__':
    main()
