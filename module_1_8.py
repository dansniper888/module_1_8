my_dict = {'Alex': 1995, 'Pety': 1992, 'Kirill': 1994}
print(my_dict)
print(my_dict['Pety'])
my_dict['Anton'] = 1998
print(my_dict['Anton'])
my_dict .update({'Lesha' : 1993, 'Vadim' : 1990})
print(my_dict)
my_dict.pop("Lesha")
print(my_dict.get('Lesha'))
print(my_dict)

my_set = {1,1,"tape",6,8,6,6,345,1,}
print(my_set)
my_set.add(65)
my_set.add(69464)
my_set.discard('tape')
print(my_set)