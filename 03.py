# int ke float
data_int = 5
print(f"tipe data data_int adalah = {type(data_int)}dengan nilai = {data_int}\n")
# data_int akan dibuah ke tipe float
data_float = float(data_int)
print(f"tipe data data_float sekarang = {type(data_float)}dengan nilai = {data_float}\n")

# float ke int
data_float = 10.6 #akan dibulatkan ke bawah
print(f"tipe data data_float adalah = {type(data_float)}dengan nilai = {data_float}\n")
# data_int akan dibuah ke tipe integer
data_int = int(data_float)
print(f"tipe data data_int sekarang = {type(data_int)}dengan nilai = {data_int}\n")

# string ke numerik
dataString = "25" # akan berjalan jika berupa angka (khusus integer harus bilangan bulat)
dataInt = int(dataString)
dataFloat = int(dataString)
total = dataInt + dataFloat
print(f"total dari {dataInt}+ {dataFloat}= {total}")

# int ke bool
dataInt = 1
dataBool = bool(dataInt) # bernilai true
print(f"tipe data dataBool adalah = {type(dataBool)}dengan nilai = {dataBool}\n")
dataInt = 0
dataBool = bool(dataInt) # bernilai false
print(f"tipe data dataBool adalah = {type(dataBool)}dengan nilai = {dataBool}\n")

