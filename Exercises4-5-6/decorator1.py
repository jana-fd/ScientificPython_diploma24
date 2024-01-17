def check_array(f):
    def wrapper(arr):
        if (len(arr) == 0):
            return 'Array is empty'
        else:
            return f(arr)
    return wrapper

@check_array
def f(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6]
    print(f(arr1))
    arr2 = []
    print(f(arr2))
