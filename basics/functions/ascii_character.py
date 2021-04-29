#Start of Program
print("Program has started")
print("Please enter and ASCII code: ")

ascii_code = int(input())

if ascii_code in range(32,127):
  print(chr(ascii_code))
else:
  print("Error! Please enter a value between 32 and 126.")

print("Program has ended!")