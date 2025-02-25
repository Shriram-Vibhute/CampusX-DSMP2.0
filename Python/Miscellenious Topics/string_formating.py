# Using % operator - just like c language
print("Geeks : %d, Portal : %7.9f" % (1000, 0005.333)) 
print("Total students : %3d, Boys : %2d" % (240, 120)) # print integer value
print("%7.3o" % (25)) # print octal value
print("%10.5E" % (356.08977)) # print exponential value

# format method
print("Hello {1:2.3f}, ok {0:3d}".format(134, 6.83274))
# {1:2.3f} -> 1: index in format function and 2.3f is formating pattern

# f-strings
a = 34
b = 5.9384
print(f"Hello {a:2d}, ok {b:.7f}")
 
# string methods -> center(50, '#'), rjust(50, '#'), ljust(50, '#')