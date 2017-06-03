# Sistem Pakar

## Latar Belakang Masalah
Menjelaskan bagaimana membuat computer seolah-olah menjadi pakar di dalam kecerdasan buatan

## Permasalahan dan Solusi Masalah
   Sistem pakar adalah system informasi yang berisi pengetahuan dari pakar sehingga dapat digunakan untuk kolsuntasi. Bentuk umum system pakar merupakan suatu program yang dibuat 
berdasarka suatu set aturan yang menganalisis informasi (diberikan oleh pengguna system) mengenai suatu kelas masalah spesifik serta analisis matematis dari masalah tersebut. Menerapkan 
aturan-aturan serta pengetahuan-pengetahuan melalui Struktur Sistem Pakar :
 
   Karakterisitik yang membedakan sistem pakar dengan perangkat lunak biasa, diantaranya :
1.	Kemungkinan Banyak Jawaban
Memakan waktu lama untuk menguji dan mempelajari jawaban, Karena ruang persoalan berukuran besar dan tak pasti
2.	Data Kabur
System pakar mencapai konklusi yang tidak pasti Karena inforasi dipakai terlalu sering berupa data yang kabur
3.	Heuristik (ilmu pengetahuan yang berhubungan dengan suatu penemuan)
Menggunakan pengetahuan untuk memperoleh suatu solusi
4.	Informatif (memberi informasi)
Memberikan kemudahan jawaban kepada user, sehingga user merasa puas dengan jawaban yang diberikan system pakar 
 

   Mekanisme inferensi dalam system pakar menerapkan pengetahuan untuk solusi problema yang sebenarnya.ada beberapa pendeketan dalam menyusun struktur mekanisme inferensi :
1.	Inferensi 
Aturan diekspresikan dalam bentuk kondisi IF-THEN. IF adalah kondisi yang telah ada dan THEN adalah aksi atau tanggapan lain yang akan timbul. Terdapat dua pendekatan dalam menyusun mekanisme inferens berbasis aturan :
a.	Forward Chaining
Permasalahan telah diketahuikeadaan awalnya (bentuk IF) dan ingin diketahui akibatnya (bentuk THEN)
Contoh :
Awal fakta		: A,B,C,D,E
Aturan		: 1. Jika A dan B maka F
			  2. Jika C dan D maka G
			  3. Jika F dan G maka H
			  4. Jika E dan H maka I
Keterangan :
Pertama fakta A dan B diketahui, aturan 	1 mengetahui F. fakta C dan D diketahui, aturan 2 mengetahui G. fakta F dan G diketahui, aturan 3 mengetahui H. aturan 4 I Karena H dan E diketahui.

b.	Backward Chaining
Interpreter memeriksa aturan dari fakta dalam basis data yaitu hipotesa. Menguji bagian THEN mencari yang sesuai. Proses berantai terus berlangsung sampai hipotesa terbukti kebenaranya
Keterangan :
Mengetahui I, dibuktikan E dan H (aturan 4). Membuktikan H, dibuktikan F dan G (aturan 3). Membuktikan F, dibuktikan A dan B (aturan 1). Membutktikan G, dibuktikan C dan D (aturan 2). 

2.	Pelacakan
Teknik ini dipakai pada situasi dimana hasil yang dieksak tidak mungkin dilakukan, sehingga pemecahan yang diperoleh lebih bersifat cukup. Terdapat dua pendekatan dalam menyusun mekanisme inferens berbasis aturan :
a.	Depth First Search
Bermula dari node akar dan bergerak ke bawah untuk memeriksa semua anak turunan dari suatu cabang sebelum ke cabang lain.
Pelacakan dimuali dari 1, diteruskan ke 2,3,4 gagal. pelacakan d=kembali keatas ke node 3, tidak ada jalan alternative sehingga terpaksa dilakukan runut balik ke node 2 diteruskaan ke 5,6, gagal rnut balik ke 5,7 gagal. runut balik terus-menerus sampai tujuan tercapai
b.	Breadth First Search
Pelacakan dilakukan terhadap semua cabang, baru dietruskan ke level yang lebih dalam. 
Pelacakan menurut 1,2,3,4,5,6,7 pelacakan akan berhenti pada node 7, Karena node 7 merupakan tujuan

3.	Probabilitas
Suatu kejadian yang menunjukankemungkinan terjadinya suatu kejadian. Nilainya dianta 0 dan 1. Kejadian yang mempunyai nilai probablitias 1 adalah kejadian yang pasti terjadi atau sesuatu telah terjadi. Terdapat tiga pendekatan dalam menyusun mekanisme inferens berbasis aturan : <br>
a.	Bayes 
Menyatakan seberapa jauh derajat kepercayaan subjektif harus berubah secara rasional ketika ada petunjuk baru
Contoh :
Jika selalu berbunyi = ya
Maka status disk drive = tidak sempurna (cf = 0.8)
Jadi suatu aturan mempunyai dua impilkasi penting. Pertama menyatakan user mampu membedakan antara "normal" da "suara aneh". Kedua bila confidence factor dinyatakan suatu probablitias status disk drive tidak sempurna didapat harga = 1 - 0.8 = 0.2 = 20 %.  
b.	Fuzzy
Suatu cara yang tepat untuk memetakan suatu ruang input ke dalam suatu ruang output 
Contoh :
IF disk drive berisi = yes (fv = 0.8)
AND format disket menimbulkan kerusakan = yes (fv = 0.3)
THEN status disk drive rusak (cf = 0.9)
Dengan memakai kalkulus fuzzy dipilih nilai minimum 0.8 dan 0.3
Jadi, confidende factor untuk aturan adalah 0.3 * 0.9 = 27
c.	Confident Factor Union Methods
Suatu alternative pendekatan untuk menentukan confidence factor dari beberapa aturan
C (cf) = cf1 + cf2 - cf1 * cf2
Dimana :
C (cf) = hasil akhir dari factor kepastian (cf)
cf1    = nilai factor kepastian (cf) dari aturan 1
cf2    = nilai factor kepastian (cf) dari aturan 2
Contoh :
cf1 = 0.2		cf2 = 0.5
C(cf) = 0.2 + 0.5 - 0.2 * 0.5 = 0.6
Bila aturan ke 3 dengan cf3 = 0.5, maka :
C(cf) = 0.6 + 0.5 - 0.6 * 0.5 = 0.8

Mod merupakan operasi pembagian yang memberikan hasil sisa hasil bagi. Hasil dari mod harus harus lebih dari sama dengan NOL dan kurang dari pembagi dan memberikan hasil bilangan bulat. 
1144067 MOD 1

## Kesimpulan  
Sistem pakar merupakan perangkat lunak yang digunakan untuk memecahkan masalah yang biasanya deiselesaikan oleh seorang 

## Saran 
Sebaiknya selalu diadakan praktik tiap minggu agar mahasiswa lebih memahami tentang materi kecerdasan buatan

## Daftar Pustaka
[1] https://id.wikipedia.org/wiki/Sistem_pakar <br>
[2[ http://entin.lecturer.pens.ac.id/Kecerdasan%20Buatan/Buku/Bab%206%20Sistem%20Pakar.pdf

## Scan Plagiarisme :
[1] https://drive.google.com/open?id=0B3mytGJbyhIhN1pPVFUtYmtYcEk <br>
[2] https://drive.google.com/open?id=0B3mytGJbyhIhUjZqb0pPTWNwbzg 
