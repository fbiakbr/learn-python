print("TEMPERATURE CONVERTER \n")
C = input("Masukkan suhu dalam Celcius: ")
R = float(C) * 4/5
F = float(C) * 9/5 + 32
K = float(C) + 273.15
print("Suhu dalam Reamur: ", R)
print("Suhu dalam Fahrenheit: ", F)
print("Suhu dalam Kelvin: ", K)
print("\n")

K = input("Masukkan suhu dalam Kelvin: ")
C = float(K) - 273.15
R = float(K) * 4/5 - 273
F = float(K) * 9/5 - 459.67
print("Suhu dalam Celcius: ", C)
print("Suhu dalam Reamur: ", R)
print("Suhu dalam Fahrenheit: ", F)
print("\n")

F = input("Masukkan suhu dalam Fahrenheit: ")
C = (float(F) - 32) * 5/9
R = (float(F) - 32) * 4/9
K = (float(F) + 459.67) * 5/9
print("Suhu dalam Celcius: ", C)
print("Suhu dalam Reamur: ", R)
print("Suhu dalam Kelvin: ", K)
print("\n")

R = input("Masukkan suhu dalam Reamur: ")
C = float(R) * 5/4
F = float(R) * 9/4 + 32
K = float(R) * 5/4 + 273.15
print("Suhu dalam Celcius: ", C)
print("Suhu dalam Fahrenheit: ", F)
print("Suhu dalam Kelvin: ", K)
print("\n")
print("20.240.0104 - Febiadi Wisnu Akbar")