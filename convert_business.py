import json
import sqlite3
import time

__author__ = 'Shih-Ting Huang'
"""
CSCI-620: Introduction to Big Data
Author: Shih-Ting Huang (sh3964)

Convert business.json to Business table in yelp.db
"""


class Hours:
    __slots__ = 'jsonDict', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

    def __init__(self, json_dict):
        self.jsonDict = json_dict['hours']
        self.Monday = self.jsonDict['Monday'] if 'Monday' in self.jsonDict else None
        self.Tuesday = self.jsonDict['Tuesday'] if 'Tuesday' in self.jsonDict else None
        self.Wednesday = self.jsonDict['Wednesday'] if 'Wednesday' in self.jsonDict else None
        self.Thursday = self.jsonDict['Thursday'] if 'Thursday' in self.jsonDict else None
        self.Friday = self.jsonDict['Friday'] if 'Friday' in self.jsonDict else None
        self.Saturday = self.jsonDict['Saturday'] if 'Saturday' in self.jsonDict else None
        self.Sunday = self.jsonDict['Sunday'] if 'Sunday' in self.jsonDict else None


class BizType:
    __slot__ = 'jsonDict', 'biz_type'

    def __init__(self, json_dict):
        self.jsonDict = json_dict['categories']
        related_type = ['Restaurants', 'Food', 'Diners']
        self.biz_type = 0
        for x in related_type:
            # found! break the search
            if x in self.jsonDict:
                self.biz_type = 1
                break
        # if 'Restaurants' in self.jsonDict or 'Food' in self.jsonDict or 'Diners' in self.jsonDict:
        #     self.biz_type = 1
        # else:
        #     self.biz_type = 0


class Attributes:
    __slots__ = 'jsonDict', 'goodForGroup', 'goodForKids', 'wheelchair', 'noiseLevel', 'alcohol', \
                'takeOut', 'reservation', 'delivery', 'hasTV', 'wifi', 'priceLevel', 'creditCard'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        # print(self.jsonDict)
        attributes = ['RestaurantsGoodForGroups', 'GoodForKids', 'NoiseLevel', 'Alcohol', 'RestaurantsTakeOut',
                      'RestaurantsReservations', 'BusinessAcceptsCreditCards', 'RestaurantsDelivery', 'HasTV',
                      'RestaurantsPriceRange2', 'WiFi', 'WheelchairAccessible']
        default = None
        try:
            self.goodForGroup = self.jsonDict['RestaurantsGoodForGroups']
        except KeyError:
            self.goodForGroup = default

        try:
            self.goodForKids = self.jsonDict['GoodForKids']
        except KeyError:
            self.goodForKids = default

        try:
            self.wheelchair = self.jsonDict['WheelchairAccessible']
        except KeyError:
            self.wheelchair = default

        try:
            self.noiseLevel = self.jsonDict['NoiseLevel']
        except KeyError:
            self.noiseLevel = default

        try:
            self.alcohol = self.jsonDict['Alcohol']
        except KeyError:
            self.alcohol = default

        try:
            self.takeOut = self.jsonDict['RestaurantsTakeOut']
        except KeyError:
            self.takeOut = default

        try:
            self.reservation = self.jsonDict['RestaurantsReservations']
        except KeyError:
            self.reservation = default

        try:
            self.delivery = self.jsonDict['RestaurantsDelivery']
        except KeyError:
            self.delivery = default

        try:
            self.hasTV = self.jsonDict['HasTV']
        except KeyError:
            self.hasTV = default

        try:
            self.wifi = self.jsonDict['WiFi']
        except KeyError:
            self.wifi = default

        try:
            self.priceLevel = self.jsonDict['RestaurantsPriceRange2']
        except KeyError:
            self.priceLevel = default

        try:
            self.creditCard = self.jsonDict['BusinessAcceptsCreditCards']
        except KeyError:
            self.creditCard = default


class Business:
    __slots__ = 'jsonDict', 'name', 'business_id', 'postal_code', 'is_open', 'hours', 'stars', 'state', 'city', \
                'categories', 'neighborhood', 'longitude', 'attributes', 'review_count', 'address', 'latitude'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        self.categories = BizType(json_dict)
        if self.categories.biz_type == 1:
            self.name = json_dict['name']
            self.business_id = json_dict['business_id']
            # p_code = str(json_dict['postal_code']).split(' ')
            # if len(p_code) > 1:
            #     self.postal_code = p_code[0] + '_' + p_code[1]
            # else:
            #
            self.postal_code = json_dict['postal_code']
            self.is_open = json_dict['is_open']
            self.stars = json_dict['stars']
            self.state = json_dict['state']
            self.city = json_dict['city']
            self.neighborhood = json_dict['neighborhood']
            self.longitude = json_dict['longitude']
            # self.attributes = str(json_dict['attributes'])
            self.attributes = Attributes(json_dict['attributes'])
            self.review_count = json_dict['review_count']
            self.address = json_dict['address']
            self.latitude = json_dict['latitude']
            self.hours = Hours(json_dict)

    def save_to_database(self):
        con = sqlite3.connect("business.db")
        with con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row
            cur.execute(
                "INSERT INTO Business("

                "name,"
                "business_id,"
                "neighborhood,"
                "address,"
                "city,"

                "state,"
                "postal_code,"
                "latitude,"
                "longitude,"
                "stars,"

                "review_count,"
                "is_open,"
                # "attributes,"
                "categories,"
                # "hours,"

                "goodForGroup,"
                "goodForKids,"
                "wheelchair,"
                "noiseLevel,"
                "alcohol,"

                "takeOut,"
                "reservation,"
                "delivery,"
                "hasTV,"
                "wifi,"

                "priceLevel,"
                "creditCard,"

                "monday,"
                "tuesday,"
                "wednesday,"
                "thursday,"
                "friday,"
                "saturday,"
                "sunday"

                ") VALUES ("
                "?,?,?,?,?,"
                "?,?,?,?,?,"
                "?,?,?,"
                "?,?,?,?,?,"
                "?,?,?,?,?,"
                "?,?,"
                "?,?,?,?,?,?,?)",

                (
                    self.name,
                    self.business_id,
                    self.neighborhood,
                    self.address,
                    self.city,
                    self.state,
                    self.postal_code,
                    self.latitude,
                    self.longitude,
                    self.stars,
                    self.review_count,
                    self.is_open,
                    # self.attributes,
                    self.categories.biz_type,

                    # attributes
                    self.attributes.goodForGroup,
                    self.attributes.goodForKids,
                    self.attributes.wheelchair,
                    self.attributes.noiseLevel,
                    self.attributes.alcohol,
                    self.attributes.takeOut,
                    self.attributes.reservation,
                    self.attributes.delivery,
                    self.attributes.hasTV,
                    self.attributes.wifi,
                    self.attributes.priceLevel,
                    self.attributes.creditCard,

                    # self.hours,
                    self.hours.Monday,
                    self.hours.Tuesday,
                    self.hours.Wednesday,
                    self.hours.Thursday,
                    self.hours.Friday,
                    self.hours.Saturday,
                    self.hours.Sunday
                )

                )


def main():
    data = []
    with open('business.json') as f:
        for line in f:
            data.append(json.loads(line))
    start = time.time()
    for case in data:
        this_case = Business(case)
        if this_case.categories.biz_type == 1:
            this_case.save_to_database()
    end = time.time()
    print('Time:', end - start)

if __name__ == '__main__':
    main()