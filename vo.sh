#!/data/data/com.termux/files/usr/bin/bash
# vo.sh — generate VO memakai suara Google TTS di HP (via TTS Util + adb)
# Pakai:  ./vo.sh "teks yang mau diucapkan" namafile.wav
#         ./vo.sh --file naskah.txt namafile.wav
set -u

ADB="adb"
SER="${ANDROID_SERIAL:-192.168.1.54:40003}"
APP="com.danefinlay.ttsutil/.ui.MainActivity"
OUTDIR="/sdcard/ISO"          # folder output di HP (sudah dipilih di app)
REMOTE="$OUTDIR/output.wav"

# koordinat (layar 1080x2436)
XY_CLEAR="572 934"
XY_EDIT="540 1114"
XY_SAVE="242 934"
XY_YES="888 1418"

txt=""
out=""
if [ "${1:-}" = "--file" ]; then
    txt="$(cat "$2")"; out="$3"
else
    txt="${1:-}"; out="${2:-}"
fi
[ -z "$txt" ] && { echo "Pemakaian: $0 \"teks\" out.wav   |   $0 --file naskah.txt out.wav"; exit 1; }
[ -z "$out" ] && out="vo-$(date +%s).wav"

A() { "$ADB" -s "$SER" "$@" >/dev/null 2>&1; }

echo "[1/6] pastikan HP tersambung..."
"$ADB" -s "$SER" get-state >/dev/null 2>&1 || { echo "  HP tidak tersambung. Jalankan: adb connect $SER"; exit 1; }

echo "[2/6] taruh teks ke clipboard (${#txt} char)..."
termux-clipboard-set "$txt" || { echo "  gagal set clipboard (Termux:API?)"; exit 1; }

echo "[3/6] buka TTS Util..."
A shell am start -W -n "$APP"
for i in $(seq 1 15); do
    if "$ADB" -s "$SER" shell dumpsys window 2>/dev/null | grep -q "danefinlay"; then break; fi
    A shell am start -n "$APP"; sleep 1
done
sleep 1

echo "[4/6] kosongkan kolom, tempel teks..."
A shell input tap $XY_CLEAR
sleep 0.4
A shell input tap $XY_EDIT
sleep 0.4
A shell input keyevent 279      # PASTE
sleep 0.6

echo "[5/6] tekan Save + konfirmasi YES..."
A shell input tap $XY_SAVE
sleep 1.2
A shell input tap $XY_YES

echo "[6/6] tunggu file selesai ditulis..."
prev=$(A shell stat -c %s "$REMOTE" 2>/dev/null || echo 0)
tries=0
while [ $tries -lt 90 ]; do
    cur=$("$ADB" -s "$SER" shell stat -c %s "$REMOTE" 2>/dev/null | tr -d '\r')
    cur=${cur:-0}
    if [ "$cur" -gt 2000 ] && [ "$cur" = "$prev" ] && [ "$cur" != "0" ]; then break; fi
    prev="$cur"; tries=$((tries+1)); sleep 1
done

"$ADB" -s "$SER" pull "$REMOTE" "$out" >/dev/null 2>&1
if [ -s "$out" ]; then
    dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out" 2>/dev/null)
    printf 'OK  %s  (%s detik)\n' "$out" "${dur:-?}"
else
    echo "GAGAL: file tidak terbentuk. Cek folder output di app ($OUTDIR)."; exit 1
fi
