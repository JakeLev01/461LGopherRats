from flask import Flask, request, jsonify


class hardwareSet:

    app = Flask(__name__)

    def __init__(self):
        self.__capacity = 0
        self.__availability = 0
        self.__checkedOut = 0

    def initialize_capacity(self, qty):
        self.__capacity = qty
        self.__availability = self.__capacity

    def set_capacity(self, qty):
        if qty > self.__capacity:
            change = qty - self.__capacity
            self.__availability += change
            self.__capacity = qty
        elif qty < self.__capacity:
            change = self.__capacity - qty
            self.__availability -= change
            self.__capacity = qty
            if self.__availability < 0:
                self.__availability = 0

    def get_availability(self):
        return self.__availability

    def get_capacity(self):
        return self.__capacity

    def check_out(self, qty):
        if qty < 0:
            return -1
        elif qty > self.__availability:
            self.__checkedOut += self.__availability
            self.__availability = 0
            return -1
        else:
            self.__availability -= qty
            self.__checkedOut += qty
            return 0

    def check_in(self, qty):
        if qty < 0:
            return
        elif (qty > self.__capacity) or (qty + self.__availability) > self.__capacity:
            updateCheckOut = self.__capacity - self.__availability
            self.__checkedOut -= updateCheckOut
            self.__availability = self.__capacity
        else:
            self.__availability += qty
            self.__checkedOut -= qty

    def get_checkedout_qty(self):
        return self.__checkedOut