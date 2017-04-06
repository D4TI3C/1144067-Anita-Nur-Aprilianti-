# MASALAH DAN RUANG KEADAAN

## Latar Belakang Masalah
Mendefinisikan permaalahan ke dalam bentuk representai algoritma 

## Permasalahan dan Solusi Masalah
 Kecerdasan buatan akan menghasilkan output berupa solusi dari suatu masalah dengan pengetahuan yang ada pada Knowledge Base dan memiliki Inference Engine untuk mengambil kesimpulan berdasarkan pengetahuan. Cara mendekripsikan masalah dengan baik :
1. Menedinisikan suatu keadaan ruang
2. Menetapkan satu atau lebih keadaan awal
3. Menetapkan satu atau lebih tujuan
4. Menetapkan kumpulan aturan

Contoh :
"Game Petani Menyebrang"
Seorang petani akan menyebrangkan seekor ayam, seekor harimau dan gabah dengan sebuah perahu yang melalui sungai. Perahu hanya bisa memuat petani dan satu penumpang lainnya (ayam, gajah atau harimau). Jika ditinggal oleh petani tersebut, maka gabah akan dimakan ayam dan gabah akan dimakan oleh harimau.
 
Penyelesaian :
1. Identifikasi ruang keadaan
Permalasahan ini dilambangkan dengan (jumlah ayam, gabah, harimau dan petani) <br>
Contoh : daerah asal (0,1,1,1) = pulau kiri tidak ada ayam, ada gabah, ada harimau, ada petani

2. Kondisi awal dan akhir <br>
Kondisi Awal <br>
Pulau Kiri   = (1,1,1,1) <br>
Pulau Kanan  = (0,0,0,0) <br>

Kondisi Akhir <br> 
Pulau Kiri  = (0,0,0,0) <br>
Pulau Kanan = (1,1,1,1) <br>

3. Aturan - aturan

Aturan Ke- | Pulau Kanan | 
---------|-----------|
1 | Ayam Menyebrang    | 
2 | Gabah Menyebrang   | 
3 | Harimau Menyebrang | 
4 | Ayam Kembali       | 
5 | Gabah Kembali      | 
6 | Harimau Kembali    | 
7 | Petani Kembali     |

4. Solusi yang ditemukan

Pulau Kiri | Pulau Kanan | Aturan yang dipakai |
---------|----------|--------------|
(1,1,1,1) | (0,0,0,0) | 1       |
(1,0,1,0) | (0,1,0,1) | 7       |
(1,0,1,1) | (0,1,0,0) | 3       |
(0,0,1,0) | (1,1,0,1) | 4       |
(0,1,1,1) | (1,0,0,0) | 2       |
(0,1,0,0) | (1,0,1,1) | 7       |
(0,1,0,1) | (1,0,1,0) | 1       |
(0,0,0,0) | (1,1,1,1) | SOLUSI  |

## Kesimpulan  
Untuk dapat menyelesaikan sebuah sistem kecerdasan buatan, maka suatu permalasahan harus ditentukan dulu ruang keadannya

## Saran 
Sebaiknya selalu diadakan praktik setiap minggu agar mahasiswa dapat lebih mengetahui tentang materi kecerdasan buatan
