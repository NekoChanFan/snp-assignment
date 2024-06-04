import task11


class JellyBean(task11.Dessert):
    flavour: str

    def __init__(self, name: str = "", calories: int = 0, flavour: str = "") -> None:
        super().__init__(name, calories)
        self.flavour = flavour

    def __str__(self) -> str:
        return f"It's a JellyBean called {self.name} with {self.flavour} flavour and {self.calories} calories"

    def get_flavour(self):
        return self.flavour

    def set_flavour(self, flavour=""):
        self.flavour = flavour

    def is_delicious(self) -> bool:
        return True if self.flavour != "black licorice" else False
