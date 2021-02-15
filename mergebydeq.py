from collections import deque

my_sorting_deque=deque


def merge_by_deg(unsorted_array: list):
    sorting_deq=deque(unsorted_array)

    while len(sorting_deq)>1:
        print(sorting_deq)
        unsorted_partition=[]
        sorted_partition=[]
        unsorted_partition.append(sorting_deq.popleft())
        unsorted_partition.append(sorting_deq.popleft())
        while len(unsorted_partition):
            local_min=min(unsorted_partition)
            sorted_partition.append(local_min)
            unsorted_partition.remove(local_min)
        sorting_deq.append(sorted_partition)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reversed_array=[]
    for a in range(10,0,-1):
        reversed_array.append(a)
    print (a)
    merge_by_deg(reversed_array)

