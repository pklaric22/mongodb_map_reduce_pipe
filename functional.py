def my_map(data, transform_function):
    result = []
    for item in data:
        result.append(transform_function(item))
    return result


def my_reduce(data, reduce_function, initial_value):
    accumulator = initial_value
    for item in data:
        accumulator = reduce_function(accumulator, item)
    return accumulator


def pipe(*functions):
    def pipeline(input_data):
        result = input_data
        for function in functions:
            result = function(result)
        return result
    return pipeline
