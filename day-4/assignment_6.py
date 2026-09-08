"""
Assignment 6: Metaclasses in Python (The Blueprint of a Class)
"""

MODEL_REGISTRY = {}

class ModelMeta(type):
    def __new__(mcs, name, bases, attrs):
        if name != "BaseModel":
            if "table_name" not in attrs or not attrs["table_name"]:
                raise TypeError(f"Class '{name}' must define a non-empty 'table_name' attribute.")

            attrs["table_name"] = attrs["table_name"].lower()

        cls = super().__new__(mcs, name, bases, attrs)

        if name != "BaseModel":
            MODEL_REGISTRY[attrs["table_name"]] = cls

        return cls


class BaseModel(metaclass=ModelMeta):
    pass


class UserModel(BaseModel):
    table_name = "USERS"


class ProductModel(BaseModel):
    table_name = "PRODUCTS"


if __name__ == "__main__":
    print("Metaclass Auto-Registration ")
    print(f"Registered ORM Models: {MODEL_REGISTRY}")

    u = UserModel()
    print(f"User Model Table Name: {u.table_name}")

    print("\nMetaclass Validation Test")
    try:
        class InvalidModel(BaseModel):
            pass
    except TypeError as e:
        print(f"Expected Error Caught at Class Definition Time -> {e}")
