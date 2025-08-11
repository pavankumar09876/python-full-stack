# Indexing
# text="pavan"
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[4])

# slicing

s=" Pavan kumar "
# print(s[0:11])
# print(s[0:6])
# print(s[6:11])
# print(s[2:9])
# print(s[-5:-2])
# print(s[6:10])
# print(s[::1])

# String methods

# print(s.upper())
# print(s.lower())
# print(s.replace("kumar","hero"))
# print(s.capitalize()) # only first letter
# print(s.casefold()) #is same as lower
# print(s.center(20,"-"))   #--- pAvan kumar ----
# print(s.count("a")) # it have start and stop values
# print(s.find("kumar"))  # it have start and stop values
# print(s.endswith("kumar "))

# Removing Whitespace

# name=" this new course "
# print(name)
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# name=" this^new^course "
# print(name.split(","))
# print(name.split("^"))

# join
# words = ['pavan', 'aakihl', 'frinds']
# sentence = " ".join(words)
# print(sentence)


# fruits = ['apple', 'banana', 'cherry']
# result = ",".join(fruits)
# print(result)

# l= ['A', 'B', 'C']
# i = "-".join(l)
# print(i)

# Checking String Properties
# c="pavan is a good boy"
# c1="pavan"
# print(c.isalpha()) #false
# print(c1.isalpha()) #true

# b="1234"
# b1="pavan123"
# print(b.isdigit()) #true
# print(b1.isdigit()) #false

# a="pavan123"
# a1="pavan"
# print(a.isalnum()) 
# print(a1.isalnum()) 

# text="  "
# text1="   p   "
# print(text.isspace())
# print(text1.isspace())

# pi =3.14159265
# print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# text ="Python"
# print(f"{text:>10}") 
# print(f"{text:<10}") 
# print(f"{text:^10}")

