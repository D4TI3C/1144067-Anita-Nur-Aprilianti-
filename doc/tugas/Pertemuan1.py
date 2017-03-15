import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa arab")
a = raw_input("Masukan Nilai 1: ")
p = raw_input("Masukan Nilai 2: ")
r = raw_input("Masukan Nilai 3: ")
i = raw_input("Masukan Nilai 4: ")
l = raw_input("Masukan Nilai 5: ")

if a == 'wahidun':
	a=1

if a == 'itsnaani':
	a=2

if a == 'tsalaatsatun':
	a=3

if a == 'arbaatun':
	a=4

if a == 'khomsatun':
	a=5

if a == 'sittatun':
	a=6

if a == 'sabatun':
	a=7

if a == 'tsamaaniatun':
	a=8

if a == 'tisatun':
	a=9

if a == 'sifr':
	a=0


if p == 'wahidun':
	p=1

if p == 'itsnaani':
	p=2

if p == 'tsalaatsatun':
	p=3

if p == 'arbaatun':
	p=4

if p == 'khomsatun':
	p=5

if p == 'sittatun':
	p=6

if p == 'sabatun':
	p=7

if p == 'tsamaaniatun':
	p=8

if p == 'tisatun':
	p=9

if p == 'sifr':
	p=0
	

if r == 'wahidun':
	r=1

if r == 'itsnaani':
	r=2

if r == 'tsalaatsatun':
	r=3

if r == 'arbaatun':
	r=4

if r == 'khomsatun':
	r=5

if r == 'sittatun':
	r=6

if r == 'sabatun':
	r=7

if r == 'tsamaaniatun':
	r=8

if r == 'tisatun':
	r=9

if r == 'sifr':
	r=0


if i == 'wahidun':
	i=1

if i == 'itsnaani':
	i=2

if i == 'tsalaatsatun':
	i=3

if i == 'arbaatun':
	i=4

if i == 'khomsatun':
	i=5

if i == 'sittatun':
	l=6

if i == 'sabatun':
	i=7

if i == 'tsamaaniatun':
	i=8

if i == 'tisatun':
	i=9

if i == 'sifr':
	i=0


if l == 'wahidun':
	l=1

if l == 'itsnaani':
	l=2

if l == 'tsalaatsatun':
	l=3

if l == 'arbaatun':
	l=4

if l == 'khomsatun':
	l=5

if l == 'sittatun':
	l=6

if l == 'sabatun':
	l=7

if l == 'tsamaaniatun':
	l=8

if l == 'tisatun':
	l=9

if l == 'sifr':
	l=0


jumlah =(a*p)+(r/i-l)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
