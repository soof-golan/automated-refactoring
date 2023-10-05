

class LegacyClass:
    def __init__(self, value):
        self.value = value

    async def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value