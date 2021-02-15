from collections import deque

my_sorting_deque=deque


def merge_by_deg(unsorted_array: list):
    sorting_deq=deque()
    for elem_in_array in unsorted_array:
        single_item_list=[]
        single_item_list.append(elem_in_array)
        sorting_deq.append(single_item_list)
    print("Data v Deque:")
    print(sorting_deq)

    while len(sorting_deq)>1:
        sorted_partition=[]
        left_partition=sorting_deq.popleft()
        right_partition=sorting_deq.popleft()

        unsorted_partition = left_partition+right_partition

        while len(unsorted_partition):
            local_min=min(unsorted_partition)
            sorted_partition.append(local_min)
            unsorted_partition.remove(local_min)
        sorting_deq.append(sorted_partition)

    sorted_array=[]
    sorted_array.append(sorting_deq.popleft())
    sorted_array=sorted_array[0]
    return sorted_array

if __name__ == '__main__':
    reversed_array=[]
    for a in range(7,-8,-1):
        reversed_array.append(a)

    print("Data k setrideni: ",reversed_array)
    print(70*"-")
    sorted_array=merge_by_deg(reversed_array)
    print(70 * "-")
    print("Merged by Deque: ", sorted_array)

