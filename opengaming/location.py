import uuid

class Location(object):
    def __init__(self, name, id=None, available=True):
        self.name = name
        if id == None:
            id = str(uuid.uuid4())
        self.id = id
        self.available = available

    def to_dict(self) -> dict:
        return vars(self)

    def __repr__(self) -> str:
        return f'Location(id: "{self.id}", name: "{self.name}")'

    def __eq__(self, o: object) -> bool:
        assert type(o) == Location
        return self.id == o.id

    def __lt__(self, o: object):
        assert type(o) == Location
        return self.name < o.name

    @classmethod
    def from_dict(cls, dictionary: dict):
        location = Location(dictionary['name'])
        for k, v in dictionary.items():
            setattr(location, k, v)
        return location
