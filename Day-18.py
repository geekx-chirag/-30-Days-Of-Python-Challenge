class AvengerMeta(type):
    def __new__(cls, name, bases, class_dict):
        if any(attr.isupper() for attr in class_dict if not attr.startswith("__")):
            raise ValueError("All avenger names must be lowercase")
        return super().__new__(cls, name, bases, class_dict)
    
class Hero(metaclass=AvengerMeta):
    ironman = "Tony Stark"