

a=["a", "b", "c", "d"]

#string isnt iterable
b="abcdef"
#a number is not iterable
c=15

#a=[["Ann Ables", 1, 1], ["Bob", 2, 2], "c", "d"]

for letter in a:
    print(letter)

print("Done")

for letter in a:
    print(letter)
    if letter =="c":
        break
    print("after if")
print("done")

for letter in a:
    print(letter)
    if letter =="c":
        #to stop that particular iteration
        continue
    print("after if")
print("done")