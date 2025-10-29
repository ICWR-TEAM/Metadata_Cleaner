# 🧹 Image Metadata Cleaner

> 🔒 Hapus metadata tersembunyi dari gambar (EXIF, lokasi GPS, kamera, dll) dengan mudah langsung dari terminal.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pillow](https://img.shields.io/badge/Library-Pillow-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)
![Made with ❤️ in Python](https://img.shields.io/badge/Made%20with-❤️%20in%20Python-red.svg)

---

## ✨ Fitur Utama

✅ Menghapus semua metadata tersembunyi dari gambar (EXIF, kamera, GPS, dll)  
📁 Bisa membersihkan **satu file** atau **seluruh folder gambar**  
⚙️ Mendukung format `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`, `.webp`  
💾 Bisa menyimpan hasil di folder lain atau di tempat yang sama  
🧠 Tidak menurunkan kualitas gambar (data pixel tetap utuh)  
🧩 Sederhana, cepat, dan ringan tanpa ketergantungan besar  

---

## 🚀 Cara Menjalankan

### 1️⃣ Clone Repository

```bash
git clone https://github.com/USERNAME/image-metadata-cleaner.git
cd image-metadata-cleaner
```

### 2️⃣ Install Dependencies

Pastikan Python ≥ 3.7 sudah terpasang, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3️⃣ Jalankan Program

```bash
python3 remove.py
```

Kemudian ikuti prompt interaktif contoh seperti ini:

```bash
==========================
# Image Metadata Cleaner #
==========================
Masukkan path file atau folder gambar:
📂 > ex_input_dir
Masukkan direktori output (kosongkan jika ingin simpan di folder asal):
📁 > ex_output_dir
Masukkan suffix untuk nama file output (default: _cleaned):
🔤 > _cleaned

✅ test.jpeg dibersihkan → ex_output_dir/test_cleaned.jpeg
```

---

## 🧠 Contoh Penggunaan

🔹 Membersihkan Satu File

```bash
python3 remove.py
📂 > example.jpg
📁 > output_dir
🔤 > _cleaned
```

output: 

```bash
✅ example.jpg dibersihkan → output_dir/example_cleaned.jpg
```

🔹 Membersihkan Seluruh Folder

```bash
python3 remove.py
📂 > images/
📁 > cleaned_images/
🔤 > _safe
```

output: 

```bash
✅ photo1.jpg dibersihkan → cleaned_images/photo1_safe.jpg
✅ photo2.png dibersihkan → cleaned_images/photo2_safe.png
```

---

## 🧩 Struktur Proyek

```bash
image-metadata-cleaner/
├── remove.py            # Script utama
├── requirements.txt     # Dependency list
├── README.md            # Dokumentasi proyek
├── ex_input_dir/        # Contoh input (opsional)
└── ex_output_dir/       # Contoh output (opsional)
```

---

## 🧰 Teknologi yang Digunakan
| Komponen                  | Fungsi                                     |
| ------------------------- | ------------------------------------------ |
| 🐍 **Python 3**           | Bahasa utama                               |
| 🖼️ **Pillow (PIL Fork)** | Manipulasi gambar dan penghapusan metadata |

---

## 🧑‍💻 Kontributor

| Nama    | Peran     | Kontak                                |
| ------- | --------- | ------------------------------------- |
| 🧠 Billy | Developer | [GitHub](https://github.com/0xbillyyy) |

---

## 🪪 Lisensi

Proyek ini dilisensikan di bawah MIT License — silakan gunakan, modifikasi, dan distribusikan dengan bebas.

---

## 🌟 Dukung Proyek Ini

Jika kamu merasa proyek ini bermanfaat:

⭐ Star repositori di GitHub

💬 Buka Issue untuk saran atau fitur baru

🔄 Bagikan ke teman fotografer, desainer, atau digital artist

---

## 🧭 Roadmap (Rencana Pengembangan)

 - [ ] GUI versi sederhana (Tkinter / PyQt)

 - [ ] Mode drag & drop

 - [ ] Statistik metadata yang dihapus

 - [ ] CLI flags (--input, --output, --suffix)

🔹 Hasil di GitHub nanti akan terlihat seperti ini:

---

> “Privacy bukan tentang menyembunyikan sesuatu, tapi tentang memilih apa yang ingin kamu bagikan.” 💡
