# import mymodule
# print('오늘의 날씨 : {}'.format(mymodule.get_weather()))
# print('오늘은 {}요일 입니다.'.format(mymodule.get_date()))


# import mymodule as mm
# print('오늘의 날씨 : {}'.format(mm.get_weather()))
# print('오늘은 {}요일 입니다.'.format(mm.get_date()))


from c_module_class.mypackage.mymodule import get_weather, get_date
print('오늘의 날씨 : {}'.format(get_weather()))
print('오늘은 {}요일 입니다.'.format(get_date()))
