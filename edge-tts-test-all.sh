#!/data/data/com.termux/files/usr/bin/bash
# Bikin sampel semua suara edge-tts yang bisa bahasa Indonesia
set -u
BASE=/data/data/com.termux/files/home/video/tts-samples/id-voices
OUT=$BASE
MONT=$BASE/montage
DEST=/sdcard/Download/tts-suara
mkdir -p "$OUT" "$MONT" "$DEST"

TEKS="Setiap hari kita mengisi bensin tanpa pernah bertanya, dari mana asalnya."

# voice|nama tampilan|gender
VOICES=(
  "id-ID-ArdiNeural|Ardi|pria"
  "id-ID-GadisNeural|Gadis|wanita"
  "en-US-AndrewMultilingualNeural|Andrew|pria"
  "en-US-AvaMultilingualNeural|Ava|wanita"
  "en-US-BrianMultilingualNeural|Brian|pria"
  "en-US-EmmaMultilingualNeural|Emma|wanita"
  "en-AU-WilliamMultilingualNeural|William|pria"
  "de-DE-FlorianMultilingualNeural|Florian|pria"
  "de-DE-SeraphinaMultilingualNeural|Seraphina|wanita"
  "fr-FR-RemyMultilingualNeural|Remy|pria"
  "fr-FR-VivienneMultilingualNeural|Vivienne|wanita"
  "it-IT-GiuseppeMultilingualNeural|Giuseppe|pria"
  "ko-KR-HyunsuMultilingualNeural|Hyunsu|pria"
  "pt-BR-ThalitaMultilingualNeural|Thalita|wanita"
)

ANN="id-ID-GadisNeural"   # pengumum label di montage
i=0
LIST=$MONT/list.txt
: > "$LIST"

for v in "${VOICES[@]}"; do
  i=$((i+1))
  n=$(printf "%02d" $i)
  voice="${v%%|*}"; rest="${v#*|}"; nama="${rest%%|*}"; gender="${rest#*|}"

  # 1) sampel suara kandidat
  f="$OUT/$n-$nama-$gender.mp3"
  timeout 90 edge-tts --voice "$voice" --text "$TEKS" --write-media "$f" >/dev/null 2>&1
  if [ -s "$f" ]; then ok="OK"; else ok="GAGAL"; fi
  echo "[$n] $nama ($gender) -> $ok"

  # 2) label (dibacakan oleh Gadis) + sampel, jadi satu bagian montage
  l="$MONT/$n-label.mp3"
  timeout 90 edge-tts --voice "$ANN" --text "Nomor $i. $nama." --write-media "$l" >/dev/null 2>&1
  if [ -s "$l" ] && [ -s "$f" ]; then
    printf "file '%s'\nfile '%s'\n" "$l" "$f" >> "$LIST"
  fi
  sleep 1
done

echo "--- bikin montage ---"
if [ -s "$LIST" ]; then
  ffmpeg -hide_banner -loglevel error -f concat -safe 0 -i "$LIST" -c:a libmp3lame -q:a 4 "$BASE/semua-suara.mp3" -y 2>&1 | tail -3
fi

echo "--- salin ke penyimpanan HP ---"
cp -f "$OUT"/*.mp3 "$BASE/semua-suara.mp3" "$DEST"/ 2>/dev/null
ls -la "$BASE" "$DEST"
