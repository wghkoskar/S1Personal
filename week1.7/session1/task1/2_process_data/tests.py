from process_data import process_data
empty_list = []
single_integer_list = [1]
multi_integer_list = [1,2,3]
assert process_data(empty_list) == None
assert process_data(single_integer_list) == 1
assert process_data(multi_integer_list) == sum(multi_integer_list)