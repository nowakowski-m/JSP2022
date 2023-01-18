from itertools import combinations

class Listy:
    def __init__(self, class_list):
        self.class_list = class_list
    
    def przeksztalcenia(self):
        list_combo = sum([list(map(list, combinations(self.class_list, i))) for i in range(len(self.class_list) + 1)], [])
        return list_combo
        
test_list = [1, 2, 3]
changed_list = Listy(test_list)

print (changed_list.przeksztalcenia())