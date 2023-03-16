import json

class User:
    def __init__(self, firstname : str, lastname : str, age : int, gender : str, job : str) -> None:
        self._firstname = firstname
        self._lastname  = lastname
        self._age       = age
        self._gender    = gender
        self._job       = job

    # === Firstname === #
    def get_firstname(self) -> str:
        return self._firstname

    def set_firstname(self, new_firstname : str) -> str:
        self._firstname = new_firstname

    # === Lastname === #
    def get_lastname(self) -> str:
        return self._lastname

    def set_lastname(self, new_lastname : str) -> str:
        self._lastname = new_lastname

    # === Age === #
    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age : int) -> int:
        self._age = new_age

    # === Gender === #
    def get_gender(self) -> str:
        return self._gender

    def set_gender(self, new_gender : str) -> str:
        self._gender = new_gender

    # === Job === #
    def get_job(self) -> str:
        return self._job

    def set_job(self, new_job : str) -> str:
        self._job = new_job

    # === Methods === #

    def to_json(self) -> None:
        d = vars(self)
        correct_dict = { k.replace('_', ''): v for k, v in d.items() }
        json_object = json.dumps(correct_dict, default = lambda o: o.__dict__, indent = 4)
        print(json_object)
