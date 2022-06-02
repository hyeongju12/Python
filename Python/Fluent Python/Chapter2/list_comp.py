# symbols = '#$%^&'

# symbol_to_ord = [ord(symbol) for symbol in symbols]
# print(symbol_to_ord)

# print('---------------------------------')
# colors = ['red', 'green', 'blue']
# shirts = ['medium', 'small', 'large']

# result= [(color, shirt) for color in colors for shirt in shirts]
# print(result)

# print('---------------------------------')
# symbols2 = '#$%^&'

# symbol_to_ord2 = tuple(ord(symbol2) for symbol2 in symbols2)

# for symbol3 in symbol_to_ord2:
#     print(symbol3)

# colors = ['red', 'green', 'blue']
# sizes = ['medium', 'small', 'large']

# for shirt in ((color, size) for color in colors for size in sizes):
#     print(shirt)
# lax_coordinates = (33.9425, -118.408056)
# latitude, longitude = lax_coordinates
# print(latitude, longitude)

# latitude, longitude = longitude, latitude
# print(latitude, longitude)

# divmod(20, 8)
# t = (20, 8)
# print(divmod(*t))

# import os
# _, filepath = os.path.split('../Chapter1/special_method.py')
# print(filepath)

a, b, *rest = range(5)
print(a, b, *rest)