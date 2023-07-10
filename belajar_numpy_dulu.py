import numpy as np

#ini add 2 list sesuai urutan
a = np.add([1,2,3,4,5,6], [1,2,3,4,5,6])
print(a)

#all = cek ada 0, gak ada = true, ada = false
b = np.array([1,2,3,4])
print(np.all(b))
c = np.array([0,1,2,3])
print(np.all(c))

#any sama aja kayak all
d = np.array([1,1,1])
print(any(d))

#ndim = number dimension, ada berapa dimensi list didalam array
e = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(e.ndim) #2 karena dimensi ke 2

#dtype = liat data type, important to know karena numpy itu based on C, jadi data type matters utk setoran memori
f = np.array([1,2,3]) #default number list type is int32
print(f.dtype)

g = np.array([1,2,3], dtype = 'int8') #bisa atur sendiri typenya apa tapi ya diliat juga masuk gak typenya
print(g.dtype)

#size = ukuran ada brp banyak element di dalam array numpy
h = np.array([1]) #elementnya cuma angka 1
print(h.size)

i = np.array([[1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16]])
print(i.size)

#shape = dia kasih tau ukuran sesuai dimensi
j = np.array([[1,2,3], [4,5,6]]) #ini (2,3) karena ada 2 baris dan 3 kolom / 2 list dan 3 element
print(j.shape) 

#filling arrays --> cara kita isi np.array tapi bukan kita yang isi valuenya , tapi program yg isikan

#misal mau isi angka yg spesifik, pakai np.full 
k = np.full((2,3), 7) #((dimensinya mau berapa), isinya mau apa)
print(k)

#misal mau isinya cuma angka 0
l = np.zeros((2,3)) #cuma provide dimensi, isinya fix 0 semua
print(l)

#atau isi angka 1
m = np.ones((2,3))
print(m)

#ada cara lain, misal mau angka mulai dari berapa, berhenti pas berapa, longkap angka berapa dengan arange yang g nya 1 (karena range)
n = np.arange(0,100,5) # 0 start, 100 ends gk termasuk 100, 5 itu longkap 5 angka
print(n)

#kalau mau mulai dari berapa, berhenti pas berapa, tapi batasin panjang list, pakai linspace
o = np.linspace(0, 100, 2) #dia bakal ambil angka dari range 0 sampe 100 tapi bukan kayak 0 dan 1, dia bakal membagi angka limit dengan angka berhenti
# dan kalau ada 0, maka 0 akan selalu ada, lalu baru angka stop dibagi limit list
print(o) #example pertama ini printnya 0 dan 100, karena cuma batasnya 2, 0 kan sudah ambil 1 slot, 100 / 1 = 100.

#percobaan lain
p = np.linspace(0, 100, 5) #disini max 5 angka, 0 ambil tempatnya jadi sisa 4, maka 100 / 4 = 25,50,75,100
print(p)

q =  np.linspace(0,100,11) #11 ambil slot utk 0 sisa 10, lalu 100 / 10 = 10,20,30,etc
print(q)

#use numpy for mathematic stuff
s = np.array([1,2,3])
t = np.array([4,5,6])
print(s + t)
print(s * t)
print(s ** t)

u = np.array([1,2,3,4,5,6,7,8,])
print(np.isinf(u))

#manipulate elements in array
v = np.array([[1,2,3], [4,5,6]])

v = np.append(v, [7,8,9])

v = np.insert(v, 4, [10,11,12])

v = np.delete(v, 5)
print(v)

#merge and split array
x1 = np.array([[1,2,3], [4,5,6]])
x2 = np.array([[7,8,9], [10,11,12]])

x = np.concatenate((x1, x2))
print(x)

#concatenate bisa pakai axis juga buat membedakan cara gabung. axis sesuai dimensionnya ada berapa, kalo dimension = 1, axis cuma bisa 0. dst.
x = np.concatenate((x1,x2), axis=1)
print(x)

#other way to merge is stack, axis not wrriten = default = nambah dimensionnya jadi lebih masuk 1 array
x = np.stack((x1, x2))
print(x)

#with axis
x = np.stack((x1,x2), axis=1)
print(x)

#split array
y1 = np.array([1,2,3,4,5,6,7,8,9,10])

y = np.split(y1, 2)
print(y)

#cobain import export file lewat numpy
z = np.save("split_from_y.npy", y)

z1 = np.load("split_from_y.npy")
print(z1)