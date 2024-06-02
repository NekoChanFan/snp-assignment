import task11

class JellyBean(task11.Dessert):
    flavour : str | None

    def get_flavour(self):
        return self.flavour

    def set_flavour(self, flavour=None):
        self.flavour = flavour

    def is_delicious(self) -> bool:
        return True if self.flavour != "black licorice" else False

