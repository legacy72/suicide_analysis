# TODO: реализовать
import json

from predictions.constants import *


class Predictor:
    _BANNED_DICT = {}
    _NORMAL_DICT = {}

    _BANNED_FREQUENCIES = 0
    _NORMAL_FREQUENCIES = 0

    def __init__(self):
        with open(TRAINING_DATA) as file:
            self._data = json.loads(file.read())

    def result(self):
        return self._data
