# Sistem Pakar

## Latar Belakang Masalah
Menjelaskan bagaimana membuat computer seolah-olah menjadi pakar di dalam kecerdasan buatan

## Permasalahan dan Solusi Masalah
Sistem pakar adalah system informasi yang berisi pengetahuan dari pakar sehingga dapat digunakan untuk kolsuntasi. Bentuk umum system pakar merupakan suatu program yang dibuat berdasarka suatu set aturan yang menganalisis informasi (diberikan oleh pengguna system) mengenai suatu kelas masalah spesifik serta analisis matematis dari masalah tersebut. Menerapkan aturan-aturan serta pengetahuan-pengetahuan melalui Struktur Sistem Pakar :
 
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
1.	Inferensi <br>
Aturan diekspresikan dalam bentuk kondisi IF-THEN. IF adalah kondisi yang telah ada dan THEN adalah aksi atau tanggapan lain yang akan timbul. Terdapat dua pendekatan dalam menyusun mekanisme inferens berbasis aturan : <br>
a.	Forward Chaining <br> 
Permasalahan telah diketahuikeadaan awalnya (bentuk IF) dan ingin diketahui akibatnya (bentuk THEN) <br>
Contoh : <br>
Awal fakta		: A,B,C,D,E <br>
Aturan		: 1. Jika A dan B maka F <br>
			  2. Jika C dan D maka G <br>
			  3. Jika F dan G maka H <br>
			  4. Jika E dan H maka I <br>
Keterangan : <br>
Pertama fakta A dan B diketahui, aturan 1 mengetahui F. fakta C dan D diketahui, aturan 2 mengetahui G. fakta F dan G diketahui, aturan 3 mengetahui H. aturan 4 I Karena H dan E diketahui.
b.	Backward Chaining
Interpreter memeriksa aturan dari fakta dalam basis data yaitu hipotesa. Menguji bagian THEN mencari yang sesuai. Proses berantai terus berlangsung sampai hipotesa terbukti kebenaranya <br>
Keterangan : <br>
Mengetahui I, dibuktikan E dan H (aturan 4). Membuktikan H, dibuktikan F dan G (aturan 3). Membuktikan F, dibuktikan A dan B (aturan 1). Membutktikan G, dibuktikan C dan D (aturan 2). 

2.	Pelacakan <br>
Teknik ini dipakai pada situasi dimana hasil yang dieksak tidak mungkin dilakukan, sehingga pemecahan yang diperoleh lebih bersifat cukup. Terdapat dua pendekatan dalam menyusun mekanisme inferens berbasis aturan : <br>
a.	Depth First Search <br>
Bermula dari node akar dan bergerak ke bawah untuk memeriksa semua anak turunan dari suatu cabang sebelum ke cabang lain. <br>
b.	Breadth First Search <br>
Pelacakan dilakukan terhadap semua cabang, baru dietruskan ke level yang lebih dalam. <br>

3.	Probabilitas <br>
Suatu kejadian yang menunjukankemungkinan terjadinya suatu kejadian. Nilainya dianta 0 dan 1. Kejadian yang mempunyai nilai probablitias 1 adalah kejadian yang pasti terjadi atau sesuatu telah terjadi. Terdapat tiga pendekatan dalam menyusun mekanisme inferens berbasis aturan : <br>
a.	Bayes <br>
Menyatakan seberapa jauh derajat kepercayaan subjektif harus berubah secara rasional ketika ada petunjuk baru <br>
Contoh : <br>
Jika selalu berbunyi = ya <br>
Maka status disk drive = tidak sempurna (cf = 0.8) <br>
Jadi suatu aturan mempunyai dua impilkasi penting. Pertama menyatakan user mampu membedakan antara "normal" da "suara aneh". Kedua bila confidence factor dinyatakan suatu probablitias status disk drive tidak sempurna didapat harga = 1 - 0.8 = 0.2 = 20 %. <br>
b.	Fuzzy <br>
Suatu cara yang tepat untuk memetakan suatu ruang input ke dalam suatu ruang output <br>
Contoh : <br>
IF disk drive berisi = yes (fv = 0.8) <br>
AND format disket menimbulkan kerusakan = yes (fv = 0.3) <br>
THEN status disk drive rusak (cf = 0.9) <br>
Dengan memakai kalkulus fuzzy dipilih nilai minimum 0.8 dan 0.3 <br>
Jadi, confidende factor untuk aturan adalah 0.3 * 0.9 = 27 <br>
c.	Confident Factor Union Methods <br>
Suatu alternative pendekatan untuk menentukan confidence factor dari beberapa aturan <br>
C (cf) = cf1 + cf2 - cf1 * cf2 <br>
Dimana : <br>
C (cf) = hasil akhir dari factor kepastian (cf) <br>
cf1    = nilai factor kepastian (cf) dari aturan 1 <br>
cf2    = nilai factor kepastian (cf) dari aturan 2 <br>
Contoh : <br>
cf1 = 0.2		cf2 = 0.5 <br>
C(cf) = 0.2 + 0.5 - 0.2 * 0.5 = 0.6 <br>
Bila aturan ke 3 dengan cf3 = 0.5, maka : <br>
C(cf) = 0.6 + 0.5 - 0.6 * 0.5 = 0.8 <br>

Mod merupakan operasi pembagian yang memberikan hasil sisa hasil bagi. Hasil dari mod harus harus lebih dari sama dengan NOL dan kurang dari pembagi dan memberikan hasil bilangan bulat. <br>
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
