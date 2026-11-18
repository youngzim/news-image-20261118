# BUILD REPORT — news-image-20261118

**Status: SIAP SUBMIT** (dari sisi artefak entri; langkah submission —
repo GitHub, bundle transcript, entry message — dilakukan terpusat oleh
agen utama). Deadline: 2026-11-20 00:00 UTC.

## Pendekatan

- Format: infografis satu halaman bergaya halaman depan koran,
  1024×1024. Masthead navy memuat tanggal secara dominan
  ("WEDNESDAY 18 NOVEMBER 2026") karena kriteria juri #1 menuntut gambar
  *menamai hari* yang dirangkumnya. Di bawahnya 2 panel hero + 6 panel
  grid; setiap panel = strip wilayah/bidang, ikon gambar vektor, headline
  tebal, dan satu baris ringkasan. Footer mencantumkan sumber.
- Keputusan teknis penting: requirements menyatakan program entri
  berjalan dengan **standard library only** (Python 3.13, tanpa instalasi,
  tanpa network). Pillow karena itu **hanya dipakai saat build**
  (`draw_entry.py`, disimpan di repo sebagai provenance gambar), dan
  program entri `main.py` menyalin `entry.png` byte-for-byte ke direktori
  output — pola yang secara eksplisit disarankan RULES.txt ("the simplest
  entry is a repository holding the image and a one-line program that
  copies it there"). Konsekuensi: deterministik secara konstruksi.
- Ikon digambar prosedural dengan Pillow (rudal menghujam pulau, bendera
  Tiongkok & Rusia di atas skyline, jembatan lengkung yang runtuh segmen
  tengahnya, kubah Capitol, partikel virus, jarum suntik, Bintang Daud,
  antena parabola Voyager + Bumi). Teks memakai Liberation Sans.
- Tiga iterasi visual dilakukan (overflow headline hero → auto-fit font;
  sub-teks meluber keluar panel → layout dihitung ulang; ikon jembatan &
  ledakan digambar ulang). Hasil akhir diperiksa visual pada ukuran
  penuh dan pada downscale 300 px (tanggal + semua headline tetap
  terbaca; sub-teks mengecil sebagaimana dialami semua entri).

## Berita yang dipakai (semuanya dilaporkan pada 18 Nov 2026, ≥2 sumber)

1. **AS menyerang situs rudal IRGC di Pulau Qeshm (Selat Hormuz);
   Iran membalas menyerang pangkalan AS di Bahrain & Kuwait.**
   Just Security Early Edition 18 Nov 2026 (melaporkan Reuters/WSJ) —
   https://www.justsecurity.org/165038/early-edition-november-18-2026/ ;
   Zark News Daily Briefing — https://zarknews.com/zark-news-daily-briefing-november-18-2026/ ;
   Horizon — https://www.horizonapp.link/en/2026/11/18
2. **Xi Jinping & Vladimir Putin bertemu di Shenzhen (APEC) menjelang
   KTT trilateral dengan Presiden Trump; Xi menolak proteksionisme,
   Putin mengkritik sanksi Barat.**
   Open Chronicle (AFP/AP) — https://openchronicle.org/2026/11/18/global-news-brief-key-developments-around-the-world-november-18-2026/ ;
   Just Security; Zark News (URL di atas).
3. **Serangan drone & rudal Ukraina menghancurkan lengkung jalan
   Jembatan Kerch (Krimea); lalu lintas dihentikan, 2 tewas.**
   BusinessWorld (rekaman terverifikasi Reuters) —
   https://bworldonline.com/world/2026/11/18/794660/ukraine-cripples-crimean-road-bridge-in-blow-to-putin-before-meeting-with-xi-and-trump/ ;
   eurotopics — https://www.eurotopics.net/en/367409/ukraine-critically-damages-road-bridge-to-crimea ;
   The Guardian (via AetherGlobe).
4. **Mary Peltola (Demokrat) mengalahkan Senator Dan Sullivan di
   Alaska → Demokrat menguasai Senat 56–44.**
   Open Chronicle (AP); Zark News; Horizon (URL di atas).
5. **Wabah Ebola di RD Kongo melewati 11.000 kasus — terbesar kedua
   dalam sejarah; anak-anak paling terdampak.**
   Zark News; Horizon (URL di atas).
6. **AS kehilangan status eliminasi campak setelah 26 tahun: 5.412
   kasus terkonfirmasi 2026 (per 12 Nov) dan 10 kematian.**
   Zark News (PAHO); Horizon (URL di atas).
7. **Knesset memilih Matan Kahana sebagai ketua — kemenangan bagi
   PM-terpilih Gadi Eisenkot, kemunduran bagi Netanyahu.**
   Just Security; Horizon (URL di atas).
8. **Voyager 1 mencapai jarak satu hari-cahaya dari Bumi
   (±16 miliar mil / 25,9 miliar km) pada 18 Nov 2026, 05.16 EST —
   objek buatan manusia pertama.**
   NASA Science — https://science.nasa.gov/ ;
   Smithsonian Magazine — http://www.smithsonianmag.com/blogs/air-space-museum/2026/11/18/nasas-voyager-1-has-reached-1-lightday-from-earth-it-is-the-first-humanmade-object-in-space-to-reach-that-distance/ ;
   USA Today — https://www.usatoday.com/story/tech/space/2026/11/18/nasa-voyager-1-light-day/92809727007/

Kedelapan cerita mencakup Timur Tengah, Asia, Eropa, AS (politik &
kesehatan), Afrika, Israel, dan antariksa — sesuai kriteria juri #2
(keleluasaan wilayah dan bidang).

## Hasil check lokal

### Uji sendiri (mereplikasi gate program/v1)
| Check | Hasil | Bukti |
| --- | --- | --- |
| run_completes (2× run, CWD berbeda) | LOLOS | `MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py` dan run kedua dari `/` ke `/tmp/out2`, keduanya exit 0 |
| run_deterministic | LOLOS | sha256 ketiga file identik: `db6fcf56d25859680dbb48c725b3a52f5cc2fe8cd8f820e1cb21b947fa053f00` (entry.png repo = out1 = out2) |
| Format PNG utuh | LOLOS | Walk chunk stdlib: IHDR + 3×IDAT + IEND, semua CRC32 cocok, file berakhir persis di EOF setelah IEND |
| Ukuran file ≤ 1 MiB | LOLOS | 146.332 byte (14% dari batas 1.048.576) |
| Dimensi ≤ 1024×1024 | LOLOS | Tepat 1024×1024 |
| Entrypoint stdlib-only | LOLOS | Impor main.py hanya `os`, `shutil`, `pathlib` |
| Inspeksi visual | LOLOS | Tidak ada teks terpotong/meluber; semua panel terlabel; tanggal terbaca pada 300 px |

### Kit resmi `makefun check --worktree` (tanpa transcript)
- **PASS** `competition_open` — waktu di dalam jendela kompetisi.
- **PASS** `snapshot` — 5 file, 165.757 byte, di dalam caps intake.
- **PASS** `license_osi` — LICENSE menyatakan SPDX MIT, OSI-approved.
- **PASS** `entrypoint` — "main.py at the root selects python3.13,
  which news-image-20261118 accepts".
- **FAIL** `transcripts_present` — memang belum ada transcript;
  bundling dilakukan agen utama di tingkat top-level setelah semua
  subagen selesai (sesuai teks fix resmi check itu sendiri).
- SKIP: seluruh check transcript turunan (tidak ada sesi untuk dibaca)
  dan `committed_secret` (tidak ada --dotenv).

## Spesifikasi file keluaran

- `entry.png`: PNG RGB 1024×1024, 146.332 byte,
  sha256 `db6fcf56d25859680dbb48c725b3a52f5cc2fe8cd8f820e1cb21b947fa053f00`
- Isi repo: `main.py` (entrypoint), `entry.png`, `draw_entry.py`
  (sumber gambar, build-time saja), `README.md`, `LICENSE` (MIT),
  `BUILD_REPORT.md` (file ini).

## Yang belum bisa diuji lokal (harus diingat agen utama)

1. **Gate scorer & juri AI bersifat server-side dan tersegel** —
   RULES.txt: "There is no local grade of this competition." Validitas
   byte-file sudah direplikasi lokal semaksimal mungkin; verdict juri
   (pairwise vs house images 13 Nov 2026) tidak bisa diprediksi lokal.
2. **Transcript gate** — menunggu bundle dari agen utama; check resmi di
   atas akan hijau setelah `--transcripts` diberikan, dengan catatan
   `thinking_in_window` (sesi harus ≥ 2026-11-18T00:00:00Z) dan
   `thinking_revised` (entrypoint harus direvisi ≥2 pesan asisten).
3. **Check saat submission (site-only)**: `repo_public`,
   `repo_created_after_open`, `commit_in_repo`, `duplicate_snapshot`,
   dan `repo_owner` — untuk yang terakhir, commit harus memuat
   `.makefun/owner.json` berisi `{"wallet": "<wallet akun>"}` kecuali
   owner GitHub repo adalah login GitHub akun Make.fun (belum saya
   tambahkan karena pilihan rute ada pada agen utama).
4. **Python 3.13 (grader) vs 3.12 (lokal)** — main.py hanya memakai
   fitur dasar yang identik di keduanya; risiko dinilai nihil, tetapi
   belum pernah dieksekusi di 3.13.
5. Batas runtime grader (60 detik, 512 MB) tidak relevan secara praktis:
   program hanya menyalin file 143 KB.
