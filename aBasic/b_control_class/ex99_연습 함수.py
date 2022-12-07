list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
	a = set(list_data)
	return list(a)[1:5]

print(quiz_2(list_1))


def  delete_a_list_element(list_data, element_value):
	if element_value in list_data:
		list_data.remove(element_value)
		return list_data
	else:
		return "False"

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):
		result.append(i)
	return result

print(quiz_1(tuple_1, tuple_2))
