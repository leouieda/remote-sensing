"Functions for calculating on lists"

def mean(values):
    "Returns the average of the given values"
    sum_of_values = running_sum(values)
    number_of_elements = length(values)
    result = sum_of_values / number_of_elements 
    return result

def standard_deviation(values):
    "Returns the standard deviation of a list of values"
    mean_value = mean(values)
    running_sum = 0
    for value in values:
        running_sum += (value - mean_value)**2
    number_of_elements = length(values)
    result = (running_sum / (number_of_elements - 1))**0.5
    return result
    
def running_sum(values):
    "Return the sum of all values"
    result = 0
    for value in values:
        result += value
    return result

def length(values):
    "Gives the number of elements in the given list"
    number_of_elements = 0
    for value in values:
        number_of_elements += 1
    return number_of_elements

def test():
    assert length([1, 2, 3]) == 3
    assert mean([2, 2]) == 2
    assert mean([3, 3]) == 3
    assert running_sum([1, 2, 3]) == 6
    assert standard_deviation([2, 2, 2]) == 0