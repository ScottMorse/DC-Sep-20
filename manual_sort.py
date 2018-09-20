
class _List:

    def __init__(self,*items):
        self.items = items
    
    def sort(self):
        new_list = []

        for i in range(len(self.items)):
            new_list.append(None)

        for item in self.items:
            index = 0
            for other_item in self.items:
                if other_item < item:
                    index += 1
                if other_item == item and item in new_list:
                    index = new_list.index(item) + 1
            new_list[index] = item
        
        self.items = tuple(new_list)
        return self.items
    
    def __get__(self):
        return self.items

int_list = _List(8,10,18,3,5,7,3)

int_list.sort()

print(int_list.items)
