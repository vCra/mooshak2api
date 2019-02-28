class GenericObject():
    property_names = []

    def save(self, connection):
        raise NotImplemented

    def delete(self, connection):
        raise NotImplemented

    def load_from_dict(self, json: dict) -> object:
        """
        Reads data from a JSON Object/Dict, and sets the attributes of this object with each corresponding key
        """

        for key in json.keys():
            self.property_names.append(key)
            setattr(self, key, json[key])

        return self




