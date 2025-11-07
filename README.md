<p align="center">
  <img src="assets/logos/Logo_Kelas.png" alt="Logo Kelas" width="250">
</p>

# WebForge SMA 1 Ambon - Arsip Tugas Informatika 12-F1

Kumpulan tugas Informatika di kelas **12-F1** sebagai arsip tugas-tugas **Web Development** dan dokumentasi kode lewat **GIT**.  
**Angkatan 2023–2026**, bersifat **FOS (Free and Open Source)** untuk digunakan oleh teman sekelas dan adik kelas yang memilih **Jurusan IT**.  
**Kelompok 4 PUNYA.**



<p align="center">
  <img src="assets/logos/Logo_Sekolah.png" alt="Logo Sekolah" width="250">
</p>



## Timeline Tugas

### 14/10/2025 — Tugas Koding Pertama: Latihan CSS
**Kesulitan:** ![EASY](https://img.shields.io/badge/EASY-brightgreen)

**File:**  
[Download ZIP Langsung](https://github.com/SyafiqKarmen/WebForge_SMA1Ambon/raw/main/assets/zips/TugasLatihanCSS_14-10-2025.zip?download=1)

**Source Code:**  
[Lihat Source Code Latihan CSS](src/SourceCodeTugasLatihanCSS)

> Mempelajari implementasi CSS dalam HTML: Internal, External, dan Inline.

---

### 23/10/2025 — Pengenalan Django & Struktur Proyek
**Kesulitan:** ![EASY](https://img.shields.io/badge/EASY-brightgreen)

**File:** Tidak ada (materi pemahaman dasar Django)

**Keterangan:**  
> Memahami cara kerja struktur proyek Django (folder `project_sisfodik`, `manage.py`, dan konfigurasi dasar).

---

### 08/11/2025 — Frontend Website (Django + Tailwind)
**Kesulitan:** ![MEDIUM](https://img.shields.io/badge/MEDIUM-yellow)

**Tujuan:**  
Membuat tampilan frontend website menggunakan **Django templates** dan **Tailwind CSS** agar styling otomatis masuk ke produksi selama development.

**File:**  
- `input.css` → Tailwind CSS utama  
- `project_sisfodik/static/css/output.css` → hasil build Tailwind  
- Template HTML di folder `project_sisfodik/templates/`

**Keterangan:**  
> Projek WebDev ini menggunkana framework css tailwind bukan bootstrap atau css vanilla

---

## Panduan Setup & Development

```bash
# Masuk ke folder proyek
cd C:\Users\LENOVO\WebForge_SMA1Ambon\src\Absen_Sedderhana-Kelompok_4\

# Aktifkan virtual environment
env\Scripts\activate

# Jalankan Tailwind CSS watcher untuk development di terminal lain selain env
npx tailwindcss -i ./input.css -o ./project_sisfodik/static/css/output.css --watch

# Jalankan Django server
python manage.py runserver
