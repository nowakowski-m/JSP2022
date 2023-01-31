def insert_type(test_list):

# Sortowanie metodą wstawiania

    checking_list = test_list
    sorted_list = []

    for y in range (len(checking_list)):
        sorted_list.append(min(checking_list))
        checking_list.remove(min(checking_list))

    return sorted_list

def bubble_type(test_list):

# Sortowanie metodą bąbelkową

    checking_list = test_list

    for i in range(len(checking_list)):
        for j in range(0, len(checking_list)-i-1):
            if checking_list[j] > checking_list[j+1]:
                checking_list[j], checking_list[j+1] = checking_list[j+1], checking_list[j]
    
    sorted_list = checking_list

    return sorted_list