import json
import sqlite3
import time

__author__ = 'Shih-Ting Huang'
"""
CSCI-620: Introduction to Big Data
Author: Shih-Ting Huang (sh3964)

Convert tip.json to Tip table in yelp.db
"""


class Tip:
    __slot__ = 'jsonDict', 'text', 'date', 'likes', 'business_id', 'user_id'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        # self.text = self.jsonDict['text']
        self.date = self.jsonDict['date']
        self.likes = self.jsonDict['likes']
        self.business_id = self.jsonDict['business_id']
        self.user_id = self.jsonDict['user_id']

    def save_to_database(self):
        con = sqlite3.connect("yelp.db")
        with con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row

            # update diesel
            cur.execute(
                "INSERT INTO Tip"
                "("
                "user_id,"
                "business_id,"
                "date,"
                "likes"
                # "text"
                ") VALUES (?,?,?,?)",
                (
                    self.user_id,
                    self.business_id,
                    self.date,
                    self.likes,
                    # self.text
                )
            )


def main():
    data = []
    with open('tip.json') as f:
        for line in f:
            data.append(json.loads(line))
    start = time.time()
    for case in data:
        this_case = Tip(case)
        this_case.save_to_database()
    end = time.time()
    print('Time:', end - start)

if __name__ == '__main__':
    main()