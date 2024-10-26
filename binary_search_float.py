
def main():
    test_array = [1.1, 1.3, 2.5, 3.8, 4.6, 5.3, 6.1, 7.9, 8.7, 9.0, 10.2]

    test_search(test_array, 3.5)
    test_search(test_array, 4)
    test_search(test_array, 6.0)
    test_search(test_array, 2.5)
    test_search(test_array, 0)
    test_search(test_array, 100.2)
    test_search(test_array, 9.0)
    test_search(test_array, 9.1)
    test_search(test_array, 8.700003)
    test_search(test_array, 8.699999)
    test_search(test_array, .9)
    test_search(test_array, 10.2)
    test_search(test_array, 5.3)
    

def test_search(array, target):
    iterations, result = binary_search_with_upper_bound(array, target)
    print(f"What we was looking for: {target}, what we found: {result}, how many iterations it took: {iterations}")


def binary_search_with_upper_bound(array, target) -> tuple:
    low, high = 0, len(array) - 1
    
    iterations = 0
    upper_bound = array[-1] # start with max value of array

    if target >= upper_bound:
        # fast check if target is more or equal to upper_bound, 
        # in this case we can skip loop altogether (means iterations = 0),
        # and return result immediately.
        return (iterations, upper_bound)

    while low <= high:
        iterations += 1

        mid = (low + high) // 2
        mid_value = array[mid]

        if mid_value < target:
            # definitely not what we're looking for
            low = mid + 1
        elif mid_value > target:
            # might be what we're looking for, but try find even closer value to target
            upper_bound = mid_value
            high = mid - 1
        else:
            # target directly equals this value
            return (iterations, mid_value)

    return (iterations, upper_bound)


if __name__ == '__main__':
    main()