# 5.1
# perintah Tambah
a = 5
b = 3.5
hasil = a + b
print(f"{a}+ {b}= {hasil}")
# perintah Kurang
hasil = a - b
print(f"{a}- {b}= {hasil}")
# perintah Kali
hasil = a * b
print(f"{a}* {b}= {hasil}")
# perintah Bagi
a = 3
b = 4
hasil = a / b
print(f"{a}* {b}= {hasil}")

# 5.2
# a pangkat b
a = 2
b = 3
hasil = a**b
print(f"{a}pangkat {b}= {hasil}\n")
# modulus
hasil = b % a
print(f"sisa hasil bagi dari {b}dibagi {a}= {hasil}")

# 5.3
a = 10
b = 3
hasil = a / b
print(f"{a}/ {b}= {hasil}\n") # menghasilkan angka dibelakang koma (desimal)
# floor division, menghilangkan angka dibelakang koma
hasil = a // b
print(f"{a}// {b}= {hasil}\n") # menghasilkan angka dibelakang koma (desimal), dan melakukan pembulatan ke bawah

# 5.4
x = 3 - 4 + 5 * 6 / (3 + (11 - 4))
print(f"nilai dari x adalah {x} \n")
print('''diperoleh dari:
1. x = 3 - 4 + 5 * 6 / (3 + 7)
2. x = 3 - 4 + 5 * 6 / 10
3. x = 3 - 4 + 30 / 10
3. x = 3 - 4 + 3
4. x = 3 - 1
5. x = 2
''')

x = 4 + 5 * 2 # kali akan dihitung terlebih dahulu
y = (4 + 5) * 2 # dalam kurung akan dihitung terlebih dahulu
print(f"hasil x = {x} \n")
print(f"hasil y = {y}")