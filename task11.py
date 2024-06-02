class Dessert:
    name: str
    calories: int

    def __init__(self, name: str = '', calories: int = 0) -> None:
        self.name = name
        self.calories = calories

    def __str__(self) -> str:
        return f"It's a {self.name} dessert with {self.calories} calories"

    def get_name(self) -> str:
        return self.name

    def get_calories(self) -> int:
        return self.calories

    def set_name(self,name: str) -> None:
        self.name = name

    def set_calories(self,calories: int) -> None:
        self.calories = calories

    def is_healthy(self) -> bool:
        return self.calories < 200

    def is_delicious(self) -> bool:
        return True
