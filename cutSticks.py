def cutTheSticks(arr):
    # Write your code here
    if arr == []:
        return []

    min = min(arr)

    new_list = [num-min for num in arr if num>min]

    return [len(arr)] + cutTheSticks(new_list)