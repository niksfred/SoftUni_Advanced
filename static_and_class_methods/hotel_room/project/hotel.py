from project.room import Room


class Hotel:
    def __init__(self, name) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count:int):
        instance_name = f"{stars_count} stars Hotel"
        return cls(instance_name)
    
    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests = sum([room.guests for room in self.rooms])
                
    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()
                self.guests = sum([room.guests for room in self.rooms])

    def status(self):
        res = ""
        res += f"Hotel {self.name} has {self.guests} total guests\n"
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        res += f"Free rooms: " + ", ".join(free_rooms) + "\n"
        res += f"Taken rooms: " + ", ".join(taken_rooms)
        return res


    
