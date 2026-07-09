---
name: MindMirror-Chat-Loc-Tri-Thuc
description: >
  Chắt lọc tri thức từ BẤT KỲ nguồn nào — file PDF, Word, sách (epub),
  ảnh chụp, ghi chú, transcript, link bài viết, hay video YouTube — thành
  các Ghi chú Vĩnh viễn (Permanent Notes) trong Core của vault. Bạn chỉ cần
  kéo/thả file, dán link, hoặc chỉ đường dẫn — skill tự trích nội dung, rút ra
  các luận điểm cốt lõi, và tạo sẵn Permanent Notes theo template kèm auto-link.
  Trigger: "chắt lọc", "chắt lọc file", "chắt lọc sách", "chắt lọc PDF",
  "chắt lọc tài liệu này", "chắt lọc video này", "chắt lọc youtube",
  "biến file này thành permanent note", "rút kiến thức từ", "distill", "chắt lọc tri thức".
---

# MindMirror — Chắt Lọc Tri Thức (Mọi nguồn → Permanent Notes)

## Mục đích
Biến **bất kỳ nguồn nào** (file / link / video) thành nhiều Permanent Notes sẵn dùng trong Core — tự động: trích nội dung → phân tích → đặt tên → tạo file → gắn link. Học viên chỉ cần đưa nguồn vào.

---

## ⚠️ Quy tắc NGÔN NGỮ (bắt buộc — ưu tiên cao nhất)
**LUÔN LUÔN viết TOÀN BỘ Permanent Note bằng tiếng Việt** — bất kể nguồn gốc bằng ngôn ngữ nào (Anh, Việt hay khác).
- Mọi phần đều bằng tiếng Việt tự nhiên: tên file, Luận điểm, Ứng dụng thực tế, Liên kết, cả phần báo cáo ở Bước 6.
- Nguồn tiếng Anh → **dịch Ý sang tiếng Việt**, KHÔNG để nguyên câu tiếng Anh trong phần diễn giải.
- **Ngoại lệ duy nhất:** mục "Bằng chứng / Ví dụ" được giữ 1–2 trích dẫn gốc gần nguyên văn (để bảo toàn tính xác thực). Thuật ngữ chuyên ngành phổ biến (vd *Grand Slam Offer*, *Value Equation*) có thể để nguyên, nhưng giải thích quanh nó vẫn phải bằng tiếng Việt.

---

## ⚠️ Đường dẫn CỐ ĐỊNH của vault (dùng đúng, KHÔNG đoán)
- **Ghi Permanent Notes vào:** `3. Chuyển Hoá (Core)/Kiến Thức/Ghi chú vĩnh viễn (Permanent Notes)/`
- **Template mẫu:** `5. Công Cụ (Toolbox)/Mẫu (Template)/Template - Permanent Notes.md`
- **Quét để auto-link:** thư mục Permanent Notes ở trên + `3. Chuyển Hoá (Core)/Kiến Thức/Frameworks/` + `3. Chuyển Hoá (Core)/Bản Đồ (Maps)/`

---

## BƯỚC 1 — Nhận nguồn & nhận diện loại
Học viên có thể: kéo/thả file, dán đường dẫn, hoặc dán link (bài viết/YouTube).
Nếu chưa rõ nguồn, hỏi: *"Bạn kéo file vào đây, hoặc dán link/đường dẫn giúp tôi nhé."*

---

## BƯỚC 2 — Trích xuất nội dung (định tuyến theo loại nguồn)

| Nguồn | Cách trích |
|---|---|
| **`.pdf` (có chữ)** | Tool **Read** với tham số `pages`. PDF >10 trang: đọc theo cụm ≤20 trang/lần cho tới hết. |
| **`.docx` `.doc` `.rtf`** | Bash: `textutil -convert txt -encoding UTF-8 -stdout "ĐƯỜNG_DẪN"` (ép UTF-8 để giữ dấu tiếng Việt) |
| **`.txt` `.md` `.csv`** | Tool **Read** trực tiếp. |
| **`.html` `.htm`** | Bash: `textutil -convert txt -encoding UTF-8 -stdout "FILE"` |
| **`.epub`** | Bash: `unzip -o "FILE.epub" -d /tmp/epub_$$` → Read các file `.xhtml/.html` bên trong. |
| **Ảnh** `.png` `.jpg` `.jpeg` `.webp` | Tool **Read** (Claude đọc được chữ trong ảnh — hoá đơn, slide, ảnh chụp trang sách). |
| **Link bài viết (URL web)** | Tool **WebFetch** với URL + prompt "trích toàn văn nội dung chính". |
| **YouTube** (`youtube.com/watch` · `youtu.be/…`) | Xem **Phụ lục A** bên dưới (lấy transcript). |
| **Audio/Video nội máy** `.mp3 .m4a .mp4 .mov` | Xem **Phụ lục B** (cần công cụ chuyển giọng nói → chữ). |

> Sách/tài liệu dài: chia theo **chương/mục logic**, xử lý từng phần rồi gộp — tránh sót và tránh trùng luận điểm.

---

## BƯỚC 3 — Phân tích & chắt lọc
Đọc toàn bộ, rút ra:
1. **Luận điểm** — quan điểm defend được (không phải sự kiện đơn thuần).
2. **Phân biệt cốt lõi** — điểm tương phản làm rõ ranh giới hai khái niệm.
3. **Hệ quả đáng nhớ** — kết luận không hiển nhiên từ một quan sát.
4. **Nguyên tắc / công thức** — framework, quy tắc lặp lại được.

Bỏ qua: dữ kiện thuần (số/ngày không kèm nhận định), câu dẫn–kết hình thức, ví dụ (giữ lại làm "Bằng chứng").

---

## BƯỚC 4 — Đề xuất danh sách Permanent Notes (chốt trước khi tạo)
```
📋 Từ "{tên nguồn}" tôi rút ra {N} luận điểm có thể thành Permanent Note:

1. "{câu khẳng định 1}"
2. "{câu khẳng định 2}"
...

→ Tạo tất cả, hay chọn/bỏ cái nào?
   [Enter] = tạo hết   ·   [1,3] = chỉ số 1 và 3   ·   [sửa X] = đổi tên số X trước
```
**Quy tắc đặt tên** (bắt buộc): câu khẳng định có **chủ ngữ + vị ngữ**, thể hiện quan điểm/phân biệt/hệ quả (10–20 từ).
❌ "PKM và tri thức"  ·  ✅ "Tích trữ thông tin không phải là quản lý tri thức".

---

## BƯỚC 5 — Tạo file Permanent Notes
Mỗi note = 1 file `.md` trong `3. Chuyển Hoá (Core)/Kiến Thức/Ghi chú vĩnh viễn (Permanent Notes)/`, theo template:

```markdown
---
up:
  - "[[MOC/nguồn phù hợp — nếu có]]"
created: {HÔM NAY — YYYY-MM-DD}
tags: [statement, core, {tag-chủ-đề}]
source: "{tên sách/tài liệu/video gốc}"
dimension: []
---

## Luận điểm
{2–4 câu — VIẾT LẠI bằng lời của học viên. KHÔNG copy nguyên văn nguồn. Nắm tinh thần, không sao chép chữ.}

## Bằng chứng / Ví dụ
{Trích dẫn hoặc ví dụ từ nguồn gốc minh chứng cho luận điểm — nơi DUY NHẤT được trích gần nguyên văn.}

## Ứng dụng thực tế
{Khi nào áp dụng? Hành động cụ thể? Nếu chưa rõ → "Cần test — chưa xác định ứng dụng cụ thể."}

## Liên kết
- {≥2–3 wikilink tới note/framework/MOC liên quan trong vault}
```

---

## BƯỚC 6 — Auto-link & báo cáo
- Quét 3 thư mục ở phần "đường dẫn cố định" → tìm note trùng chủ đề → chèn `[[wikilink]]` vào mục **Liên kết**; nếu có MOC phù hợp thì thêm vào `up:`.
- Báo cáo:
```
✅ Đã tạo {N} Permanent Notes từ "{tên nguồn}":
1. [[Tên note 1]]
2. [[Tên note 2]]
📁 3. Chuyển Hoá (Core)/Kiến Thức/Ghi chú vĩnh viễn (Permanent Notes)/

Tiếp theo:  [1] chắt lọc nguồn khác  ·  [2] gộp các note này thành 1 MOC chủ đề
```

---

## ✅ Checklist trước khi lưu (mỗi note)
- [ ] Tên file là câu khẳng định (chủ ngữ + vị ngữ).
- [ ] "Luận điểm" viết lại bằng lời mới — không copy nguyên văn nguồn.
- [ ] `source:` điền tên nguồn gốc; `created:` là ngày hôm nay.
- [ ] Có đủ **Bằng chứng** + **Ứng dụng thực tế**.
- [ ] ≥2 wikilink trong mục **Liên kết**.

---

## Phụ lục A — Lấy transcript YouTube

**Cách 1 (tốt nhất — gọi qua module để không phụ thuộc PATH):**
```bash
mkdir -p /tmp/yt && python3 -m yt_dlp --skip-download --write-auto-subs --write-subs \
  --sub-langs "vi,en,en-orig" --sub-format vtt \
  -o "/tmp/yt/%(id)s.%(ext)s" "URL_YOUTUBE"
```
Rồi làm sạch `.vtt` → transcript (bỏ header / timestamp / tag / dòng trùng của auto-sub):
```bash
grep -vE '^WEBVTT|^Kind:|^Language:|-->|^[0-9]+$|^[[:space:]]*$' /tmp/yt/*.vtt \
  | sed -E 's/<[^>]+>//g' | awk '!seen[$0]++'
```
→ Đưa transcript sạch vào **Bước 3** để chắt lọc. (Cảnh báo `ffmpeg not found` là **vô hại** — lấy phụ đề không cần ffmpeg.)

**Nếu máy học viên chưa có `yt-dlp`** — chọn 1 trong 3:
1. Cài 1 lần: `pip3 install -U yt-dlp` (cần Python) — rồi chạy lại Cách 1.
2. Vào video → nút **"..." → Show transcript** → copy → **dán thẳng vào chat** cho tôi chắt lọc.
3. Gửi file phụ đề (`.srt`/`.vtt`) nếu đã có.

---

## Phụ lục B — Audio/Video nội máy
Cần công cụ speech-to-text (chưa chắc có sẵn). Ưu tiên:
1. Nếu máy có `whisper` + `ffmpeg`: `whisper "FILE" --language Vietnamese --output_format txt` → đọc file `.txt` → chắt lọc.
2. Nếu không có: báo học viên **cung cấp transcript** (tự chạy Whisper/ dịch vụ chuyển lời), rồi tôi chắt lọc từ transcript đó.

---

## Lưu ý khi demo
- **PDF scan / ảnh mờ:** nếu không lấy được chữ (không có text layer) → báo: *"File này là ảnh scan, cần bản có chữ hoặc OCR trước."* Đừng bịa nội dung.
- **Luôn dừng ở Bước 4** cho học viên duyệt danh sách trước khi tạo hàng loạt — để họ thấy mình kiểm soát.
- **Ngôn ngữ:** LUÔN viết toàn bộ note bằng **tiếng Việt** (xem "Quy tắc NGÔN NGỮ" ở đầu skill). Nguồn ngoại ngữ → dịch ý sang tiếng Việt; chỉ giữ trích dẫn gốc ở mục "Bằng chứng".
