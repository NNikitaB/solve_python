from functools import total_ordering


@total_ordering
class Technic:
    __slots__ = ('name', 'cost', 'availability')

    def __init__(self, name="untitled", cost=500, availability=False):
        self.name: str = name
        self.cost: int = cost
        self.availability: bool = availability

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __eq__(self, other):
        return len(self.name) == len(other.name)


#def get_category(t: Technic):
#    split_cost = 1000
#    return "Бюджетный" if t.cost < split_cost else "Дорогой"


#ls = [Technic("Phone1", 55, True),
#      Technic("Phone2", 1000, True),
#      Technic("Phone3", 999, True),
#      Technic("Phone4", 5000, True)]

#for it in ls:
#    print(it.name, '=', it.cost, "is", get_category(it))

print(Technic("Phone1", 55, True) > Technic("Phone2", 1000, True))
print(Technic("Phone3", 999, True) == Technic("Phone4", 5000, True))
print(Technic("Phone3", 999, True) != Technic("Phone4", 5000, True))
print(Technic("Phone3", 999, True) <= Technic("Phone4444444", 5000, True))
