# TTS Gratis untuk Dokumenter (Bahasa Indonesia)

Dicek: 17 Okt 2026 · lingkungan: Termux Android (aarch64)

## A. Jalan LANGSUNG di Termux ini — tanpa API key ✅ SUDAH DIUJI

| Tool | Suara Indonesia | Output | Catatan |
|---|---|---|---|
| **edge-tts** | **2 native**: `id-ID-ArdiNeural` (pria), `id-ID-GadisNeural` (wanita) + **12 multilingual** (Andrew/Ava/Brian/Emma dll) yang bisa ngomong Indonesia | mp3 24 kHz | Paling praktis. Gratis, tanpa daftar. **Tak resmi** (bisa berubah/diblokir kapan saja). |
| **gTTS** | 1 suara | mp3 64 kbps | Google Translate TTS. Paling simpel. |
| **Suara Google HP** (TTS Util + adb) | 4 suara (Suara I–IV) | wav 24 kHz | Offline, asli HP. Tapi lewat app + adb, agak ribet. |
| **espeak** | 1 suara | wav | Offline, tapi robotik. Buat cadangan darurat. |

Bukti uji: `~/video/tts-samples/` → ardi.mp3 (4.9s), gadis.mp3 (6.3s), gtts.mp3 (6.3s), multi-andrew-id.mp3 (5.7s)

## B. Open-source lokal (butuh komputer/GPU, bukan Termux)

| Model | Ukuran | Bahasa ID? | Catatan |
|---|---|---|---|
| Piper (ONNX) | ~63 MB | ✅ 1 suara | Offline, cepat, CPU. (sudah dihapus atas permintaan) |
| facebook/mms-tts-ind (VITS) | ~290 MB | ✅ 1 suara | Butuh torch+transformers (mentok di Termux) |
| pocket-tts-indonesian | ~438 MB | ✅ 4 suara (kloning) | Butuh tokenizers/sentencepiece (mentok di Termux) |
| Kokoro | 82M | ❌ (en/ja/zh/es/fr/hi/it/pt) | Apache 2.0, cepat |
| MeloTTS | - | ❌ (en/es/fr/zh/jp/kr) | MIT, gratis komersial |
| Qwen3-TTS | 1.7B | ❌ (10 bahasa, bukan ID) | Apache 2.0, butuh GPU 6GB+ |
| Chatterbox | 350M | ⚠️ 23+ bahasa | MIT, butuh GPU 4GB+ |
| XTTS-v2 / F5-TTS / Fish Speech | besar | ⚠️ | Kloning suara, butuh GPU |

## C. Online gratis (lewat browser, manual)

| Layanan | Kuota gratis | Key? | Catatan |
|---|---|---|---|
| **ElevenLabs** | 10.000 karakter/bln | ya (daftar) | Kualitas terbaik. **Non-komersial** di paket gratis. |
| **Google Cloud TTS** | 1 jt char/bln (Chirp3/Neural2), 4 jt (WaveNet/Standard) | ya + billing | Kuota besar, kualitas bagus. |
| **Amazon Polly** | 12 bln free (akun lama) / kredit $200 (akun baru) | ya | Standar industri. |
| TTSMaker / Cartesia / MiniMax / CAMB.AI / Crikk / VEED | bervariasi | sebagian tanpa daftar | Enak buat tes cepat, kurang cocok untuk batch otomatis. |

## Rekomendasi

1. **edge-tts** — paling pas: jalan langsung di Termux, tanpa key, punya 2 suara Indonesia native + suara multilingual. Cocok buat VO 8 bab.
2. Kalau mau kualitas paling natural dan non-komersial: **ElevenLabs** (kuota 10rb karakter ~ pas untuk naskah dokumenter ini).
3. Kalau butuh offline penuh: **suara Google HP** (4 suara) atau **Piper**.

Catatan: naskah dokumenter ini kira-kira ~7.000–9.000 karakter, jadi kuota gratis ElevenLabs kemungkinan cukup untuk sekali produksi.
