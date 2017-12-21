import json
import sqlite3
import time

__author__ = 'Shih-Ting Huang'
"""
CSCI-620: Introduction to Big Data
Author: Shih-Ting Huang (sh3964)

Convert checkin.json to CheckIn table in yelp.db
"""


class TimeSlot:
    __slot__ = 'jsonDict', \
               '0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', \
               '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', \
               '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'

    def __init__(self, json_dict):
        default = 0
        self.jsonDict = json_dict

        try:
            self.t0 = self.jsonDict['0:00']
        except KeyError:
            self.t0 = default

        try:
            self.t1 = self.jsonDict['1:00']
        except KeyError:
            self.t1 = default

        try:
            self.t2 = self.jsonDict['2:00']
        except KeyError:
            self.t2 = default

        try:
            self.t3 = self.jsonDict['3:00']
        except KeyError:
            self.t3 = default

        try:
            self.t4 = self.jsonDict['4:00']
        except KeyError:
            self.t4 = default

        try:
            self.t5 = self.jsonDict['5:00']
        except KeyError:
            self.t5 = default

        try:
            self.t6 = self.jsonDict['6:00']
        except KeyError:
            self.t6 = default

        try:
            self.t7 = self.jsonDict['7:00']
        except KeyError:
            self.t7 = default

        try:
            self.t8 = self.jsonDict['8:00']
        except KeyError:
            self.t8 = default

        try:
            self.t9 = self.jsonDict['9:00']
        except KeyError:
            self.t9 = default

        try:
            self.t10 = self.jsonDict['10:00']
        except KeyError:
            self.t10 = default

        try:
            self.t11 = self.jsonDict['11:00']
        except KeyError:
            self.t11 = default

        try:
            self.t12 = self.jsonDict['12:00']
        except KeyError:
            self.t12 = default

        try:
            self.t13 = self.jsonDict['13:00']
        except KeyError:
            self.t13 = default

        try:
            self.t14 = self.jsonDict['14:00']
        except KeyError:
            self.t14 = default

        try:
            self.t15 = self.jsonDict['15:00']
        except KeyError:
            self.t15 = default

        try:
            self.t16 = self.jsonDict['16:00']
        except KeyError:
            self.t16 = default

        try:
            self.t17 = self.jsonDict['17:00']
        except KeyError:
            self.t17 = default

        try:
            self.t18 = self.jsonDict['18:00']
        except KeyError:
            self.t18 = default

        try:
            self.t19 = self.jsonDict['19:00']
        except KeyError:
            self.t19 = default

        try:
            self.t20 = self.jsonDict['20:00']
        except KeyError:
            self.t20 = default

        try:
            self.t21 = self.jsonDict['21:00']
        except KeyError:
            self.t21 = default

        try:
            self.t22 = self.jsonDict['22:00']
        except KeyError:
            self.t22 = default

        try:
            self.t23 = self.jsonDict['23:00']
        except KeyError:
            self.t23 = default




class Time:
    __slot__ = 'jsonDict', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'

    def __init__(self, json_dict):
        default = None
        self.jsonDict = json_dict
        try:
            self.mon = TimeSlot(self.jsonDict['Monday'])
        except KeyError:
            self.jsonDict['Monday'] = {}
            self.mon = TimeSlot(self.jsonDict['Monday'])

        try:
            self.tue = TimeSlot(self.jsonDict['Tuesday'])
        except KeyError:
            self.jsonDict['Tuesday'] = {}
            self.tue = TimeSlot(self.jsonDict['Tuesday'])

        try:
            self.wed = TimeSlot(self.jsonDict['Wednesday'])
        except KeyError:
            self.jsonDict['Wednesday'] = {}
            self.wed = TimeSlot(self.jsonDict['Wednesday'])

        try:
            self.thu = TimeSlot(self.jsonDict['Thursday'])
        except KeyError:
            self.jsonDict['Thursday'] ={}
            self.thu = TimeSlot(self.jsonDict['Thursday'])

        try:
            self.fri = TimeSlot(self.jsonDict['Friday'])
        except KeyError:
            self.jsonDict['Friday'] = {}
            self.fri = TimeSlot(self.jsonDict['Friday'])

        try:
            self.sat = TimeSlot(self.jsonDict['Saturday'])
        except KeyError:
            self.jsonDict['Saturday'] = {}
            self.sat = TimeSlot(self.jsonDict['Saturday'])

        try:
            self.sun = TimeSlot(self.jsonDict['Sunday'])
        except KeyError:
            self.jsonDict['Sunday'] = {}
            self.sun = TimeSlot(self.jsonDict['Sunday'])


class CheckIn:
    __slot__ = 'jsonDict', 'time', 'business_id'

    def __init__(self, json_dict):
        self.jsonDict = json_dict
        self.time = Time(self.jsonDict['time'])
        self.business_id = self.jsonDict["business_id"]

    def save_to_database(self):
        con = sqlite3.connect("yelp.db")
        with con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row
            cur.execute(
                "INSERT INTO CheckIn"
                "("
                "business_id,"
                "Mon0,"
                "Mon1,"
                "Mon2,"
                "Mon3,"
                "Mon4,"
                "Mon5,"
                "Mon6,"
                "Mon7,"
                "Mon8,"
                "Mon9,"
                "Mon10,"
                "Mon11,"
                "Mon12,"
                "Mon13,"
                "Mon14,"
                "Mon15,"
                "Mon16,"
                "Mon17,"
                "Mon18,"
                "Mon19,"
                "Mon20,"
                "Mon21,"
                "Mon22,"
                "Mon23,"
                "Tue0,"
                "Tue1,"
                "Tue2,"
                "Tue3,"
                "Tue4,"
                "Tue5,"
                "Tue6,"
                "Tue7,"
                "Tue8,"
                "Tue9,"
                "Tue10,"
                "Tue11,"
                "Tue12,"
                "Tue13,"
                "Tue14,"
                "Tue15,"
                "Tue16,"
                "Tue17,"
                "Tue18,"
                "Tue19,"
                "Tue20,"
                "Tue21,"
                "Tue22,"
                "Tue23,"
                "Wed0,"
                "Wed1,"
                "Wed2,"
                "Wed3,"
                "Wed4,"
                "Wed5,"
                "Wed6,"
                "Wed7,"
                "Wed8,"
                "Wed9,"
                "Wed10,"
                "Wed11,"
                "Wed12,"
                "Wed13,"
                "Wed14,"
                "Wed15,"
                "Wed16,"
                "Wed17,"
                "Wed18,"
                "Wed19,"
                "Wed20,"
                "Wed21,"
                "Wed22,"
                "Wed23,"
                "Thu0,"
                "Thu1,"
                "Thu2,"
                "Thu3,"
                "Thu4,"
                "Thu5,"
                "Thu6,"
                "Thu7,"
                "Thu8,"
                "Thu9,"
                "Thu10,"
                "Thu11,"
                "Thu12,"
                "Thu13,"
                "Thu14,"
                "Thu15,"
                "Thu16,"
                "Thu17,"
                "Thu18,"
                "Thu19,"
                "Thu20,"
                "Thu21,"
                "Thu22,"
                "Thu23,"
                "Fri0,"
                "Fri1,"
                "Fri2,"
                "Fri3,"
                "Fri4,"
                "Fri5,"
                "Fri6,"
                "Fri7,"
                "Fri8,"
                "Fri9,"
                "Fri10,"
                "Fri11,"
                "Fri12,"
                "Fri13,"
                "Fri14,"
                "Fri15,"
                "Fri16,"
                "Fri17,"
                "Fri18,"
                "Fri19,"
                "Fri20,"
                "Fri21,"
                "Fri22,"
                "Fri23,"
                "Sat0,"
                "Sat1,"
                "Sat2,"
                "Sat3,"
                "Sat4,"
                "Sat5,"
                "Sat6,"
                "Sat7,"
                "Sat8,"
                "Sat9,"
                "Sat10,"
                "Sat11,"
                "Sat12,"
                "Sat13,"
                "Sat14,"
                "Sat15,"
                "Sat16,"
                "Sat17,"
                "Sat18,"
                "Sat19,"
                "Sat20,"
                "Sat21,"
                "Sat22,"
                "Sat23,"
                "Sun0,"
                "Sun1,"
                "Sun2,"
                "Sun3,"
                "Sun4,"
                "Sun5,"
                "Sun6,"
                "Sun7,"
                "Sun8,"
                "Sun9,"
                "Sun10,"
                "Sun11,"
                "Sun12,"
                "Sun13,"
                "Sun14,"
                "Sun15,"
                "Sun16,"
                "Sun17,"
                "Sun18,"
                "Sun19,"
                "Sun20,"
                "Sun21,"
                "Sun22,"
                "Sun23"
                ") VALUES ("
                "?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"

                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?,"
                "?,?,?,?,?,?)",

                (
                    self.business_id,

                    # self.hours,
                    self.time.mon.t0,
                    self.time.mon.t1,
                    self.time.mon.t2,
                    self.time.mon.t3,
                    self.time.mon.t4,
                    self.time.mon.t5,
                    self.time.mon.t6,
                    self.time.mon.t7,
                    self.time.mon.t8,
                    self.time.mon.t9,
                    self.time.mon.t10,
                    self.time.mon.t11,
                    self.time.mon.t12,
                    self.time.mon.t13,
                    self.time.mon.t14,
                    self.time.mon.t15,
                    self.time.mon.t16,
                    self.time.mon.t17,
                    self.time.mon.t18,
                    self.time.mon.t19,
                    self.time.mon.t20,
                    self.time.mon.t21,
                    self.time.mon.t22,
                    self.time.mon.t23,

                    self.time.tue.t0,
                    self.time.tue.t1,
                    self.time.tue.t2,
                    self.time.tue.t3,
                    self.time.tue.t4,
                    self.time.tue.t5,
                    self.time.tue.t6,
                    self.time.tue.t7,
                    self.time.tue.t8,
                    self.time.tue.t9,
                    self.time.tue.t10,
                    self.time.tue.t11,
                    self.time.tue.t12,
                    self.time.tue.t13,
                    self.time.tue.t14,
                    self.time.tue.t15,
                    self.time.tue.t16,
                    self.time.tue.t17,
                    self.time.tue.t18,
                    self.time.tue.t19,
                    self.time.tue.t20,
                    self.time.tue.t21,
                    self.time.tue.t22,
                    self.time.tue.t23,

                    self.time.wed.t0,
                    self.time.wed.t1,
                    self.time.wed.t2,
                    self.time.wed.t3,
                    self.time.wed.t4,
                    self.time.wed.t5,
                    self.time.wed.t6,
                    self.time.wed.t7,
                    self.time.wed.t8,
                    self.time.wed.t9,
                    self.time.wed.t10,
                    self.time.wed.t11,
                    self.time.wed.t12,
                    self.time.wed.t13,
                    self.time.wed.t14,
                    self.time.wed.t15,
                    self.time.wed.t16,
                    self.time.wed.t17,
                    self.time.wed.t18,
                    self.time.wed.t19,
                    self.time.wed.t20,
                    self.time.wed.t21,
                    self.time.wed.t22,
                    self.time.wed.t23,

                    self.time.thu.t0,
                    self.time.thu.t1,
                    self.time.thu.t2,
                    self.time.thu.t3,
                    self.time.thu.t4,
                    self.time.thu.t5,
                    self.time.thu.t6,
                    self.time.thu.t7,
                    self.time.thu.t8,
                    self.time.thu.t9,
                    self.time.thu.t10,
                    self.time.thu.t11,
                    self.time.thu.t12,
                    self.time.thu.t13,
                    self.time.thu.t14,
                    self.time.thu.t15,
                    self.time.thu.t16,
                    self.time.thu.t17,
                    self.time.thu.t18,
                    self.time.thu.t19,
                    self.time.thu.t20,
                    self.time.thu.t21,
                    self.time.thu.t22,
                    self.time.thu.t23,

                    self.time.fri.t0,
                    self.time.fri.t1,
                    self.time.fri.t2,
                    self.time.fri.t3,
                    self.time.fri.t4,
                    self.time.fri.t5,
                    self.time.fri.t6,
                    self.time.fri.t7,
                    self.time.fri.t8,
                    self.time.fri.t9,
                    self.time.fri.t10,
                    self.time.fri.t11,
                    self.time.fri.t12,
                    self.time.fri.t13,
                    self.time.fri.t14,
                    self.time.fri.t15,
                    self.time.fri.t16,
                    self.time.fri.t17,
                    self.time.fri.t18,
                    self.time.fri.t19,
                    self.time.fri.t20,
                    self.time.fri.t21,
                    self.time.fri.t22,
                    self.time.fri.t23,

                    self.time.sat.t0,
                    self.time.sat.t1,
                    self.time.sat.t2,
                    self.time.sat.t3,
                    self.time.sat.t4,
                    self.time.sat.t5,
                    self.time.sat.t6,
                    self.time.sat.t7,
                    self.time.sat.t8,
                    self.time.sat.t9,
                    self.time.sat.t10,
                    self.time.sat.t11,
                    self.time.sat.t12,
                    self.time.sat.t13,
                    self.time.sat.t14,
                    self.time.sat.t15,
                    self.time.sat.t16,
                    self.time.sat.t17,
                    self.time.sat.t18,
                    self.time.sat.t19,
                    self.time.sat.t20,
                    self.time.sat.t21,
                    self.time.sat.t22,
                    self.time.sat.t23,

                    self.time.sun.t0,
                    self.time.sun.t1,
                    self.time.sun.t2,
                    self.time.sun.t3,
                    self.time.sun.t4,
                    self.time.sun.t5,
                    self.time.sun.t6,
                    self.time.sun.t7,
                    self.time.sun.t8,
                    self.time.sun.t9,
                    self.time.sun.t10,
                    self.time.sun.t11,
                    self.time.sun.t12,
                    self.time.sun.t13,
                    self.time.sun.t14,
                    self.time.sun.t15,
                    self.time.sun.t16,
                    self.time.sun.t17,
                    self.time.sun.t18,
                    self.time.sun.t19,
                    self.time.sun.t20,
                    self.time.sun.t21,
                    self.time.sun.t22,
                    self.time.sun.t23
                )

            )


def main():
    data = []
    with open('checkin.json') as f:
        for line in f:
            data.append(json.loads(line))

    start = time.time()
    for case in data:
        this_case = CheckIn(case)
        this_case.save_to_database()
    end = time.time()
    print("Time:", end - start)


if __name__ == '__main__':
    main()