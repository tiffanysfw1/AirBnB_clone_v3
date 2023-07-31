import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    def __init__(self):
        """Instantiate a FileStorage object"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """Return the dictionary __objects"""
        if cls is not None:
            return {key: value for key, value in self.__objects.items()
                    if isinstance(value, cls)}
        return self.__objects

    def new(self, obj):
        """Add the object to __objects with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        json_objects = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key, value in jo.items():
                cls_name = value.get("__class__")
                if cls_name in classes:
                    cls = classes[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects.pop(key, None)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.reload()

    def get(self, cls, id):
        """Retrieve an object based on the class and ID."""
        key = cls.__name__ + '.' + id
        return self.__objects.get(key, None)

    def count(self, cls=None):
        """Count the number of objects in storage matching the given class."""
        if cls:
            return len(self.all(cls))
        return len(self.__objects)
