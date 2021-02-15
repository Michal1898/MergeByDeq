from collections import deque

my_sorting_deque=deque


def merge_by_deg(unsorted_array: list):
    sorting_deq=deque(unsorted_array)
    print(sorting_deq)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reversed_array=[]
    for a in range(10,0,-1):
        reversed_array.append(a)
    print (a)
    merge_by_deg(reversed_array)
