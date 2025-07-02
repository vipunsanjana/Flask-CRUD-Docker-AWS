# In-memory data storage (mock database)
class Item:
    data = {}
    counter = 1

    @classmethod
    def create(cls, name):
        item_id = cls.counter
        cls.data[item_id] = {'id': item_id, 'name': name}
        cls.counter += 1
        return cls.data[item_id]

    @classmethod
    def read(cls, item_id):
        return cls.data.get(item_id)

    @classmethod
    def update(cls, item_id, name):
        if item_id in cls.data:
            cls.data[item_id]['name'] = name
            return cls.data[item_id]
        return None

    @classmethod
    def delete(cls, item_id):
        return cls.data.pop(item_id, None)

    @classmethod
    def list_all(cls):
        return list(cls.data.values())
