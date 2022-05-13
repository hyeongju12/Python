class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print('Doing in the water')

    def swim(self):
        print("Moving in water")


nemo = Fish()

nemo.breathe()
nemo.swim()