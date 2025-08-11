# Fixed vowel extraction code
l = "hello wOrld"

# Method 1: Using string membership
print("Vowels found (Method 1):")
for i in l:
    if i.lower() in "aeiou":
        print(i)

print("\n" + "="*30 + "\n")

# Method 2: Using case-insensitive check
print("Vowels found (Method 2):")
vowels = "aeiouAEIOU"
for char in l:
    if char in vowels:
        print(char)

print("\n" + "="*30 + "\n")

# Method 3: Using list comprehension (more Pythonic)
print("All vowels as list:", [char for char in l if char.lower() in "aeiou"])
