from itertools import combinations

class Listy:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def podlisty(self):
        final_list = []
        class_list = []
        for x in range (self.n1, self.n2):
            class_list.append(x)
        list_combo = sum([list(map(list, combinations(class_list, i))) for i in range(3, 4)], [])
        for y in range (len(list_combo)):
            if sum(list_combo[y]) == 0:
                final_list.append(list_combo[y]) 
        return final_list

changed_list = Listy(-5, 7)

print (changed_list.podlisty())