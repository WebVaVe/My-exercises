class Flight():
    def __init__(self,x):
        self.capacity = x
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        f = self.capacity - len(self.passengers)
        return f

flight1 = Flight(3)
people = ["Ariyan","mohamad","ali","hossein"]

for person in people:
    if flight1.add_passengers(person):
        print(f"add {person} to flight1 successfully")
    else:
        print(f"no available seat for {person}")
