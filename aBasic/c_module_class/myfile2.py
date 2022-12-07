# import mypackage.mymodule
# print('오늘의 날씨 : {}'.format(mypackage.mymodule.get_weather()))
# print('오늘은 {}요일 입니다.'.format(mypackage.mymodule.get_date()))


# from mypackage import mymodule
# print('오늘의 날씨 : {}'.format(mymodule.get_weather()))
# print('오늘은 {}요일 입니다.'.format(mymodule.get_date()))


from mypackage import mymodule as mm
print('오늘의 날씨 : {}'.format(mm.get_weather()))
print('오늘은 {}요일 입니다.'.format(mm.get_date()))
