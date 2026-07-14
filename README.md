# 🪞 MindMirror — Não Bộ Thứ Hai Bằng AI

> **Thu Thập → Tinh Lọc → Chuyển Hoá → Kiến Tạo**

MindMirror là vault Obsidian tiếng Việt giúp bạn biến thông tin rời rạc thành ngữ cảnh cá nhân, tri thức có cấu trúc và tài sản có thể sử dụng lại cùng AI.

## Bắt đầu trong 5 phút

1. Tải kho này bằng **Download ZIP**, GitHub Desktop hoặc lệnh:
   ```bash
   git clone https://github.com/trongdinh27-create/MindMirror-Template.git
   ```
2. Mở thư mục bằng Obsidian: **Open folder as vault**.
3. Mở file [[BẮT ĐẦU TỪ ĐÂY]].
4. Sao chép `Me.example.md` thành `Me.md`, hoặc chạy skill `mindmirror-ban-do-cuoc-doi` để AI phỏng vấn và điền giúp bạn.

## Kiến trúc thuần Việt

| Tầng | Câu hỏi chính | Kết quả |
|---|---|---|
| `1. Thu Thập/` | Điều gì vừa xuất hiện và không nên bị thất lạc? | Dữ liệu thô trong một hàng đợi đáng tin cậy |
| `2. Tinh Lọc/` | Điều này có nghĩa gì với tôi? | Ghi chú đã được làm rõ bằng ngôn ngữ cá nhân |
| `3. Chuyển Hoá/` | Tôi thật sự biết hoặc tin điều gì? | Luận điểm cốt lõi, khung tư duy và bản đồ tri thức |
| `4. Kiến Tạo/` | Tri thức này tạo ra giá trị gì? | Nội dung, quyết định, dự án, sản phẩm và tài sản số |
| `5. Hộp Công Cụ/` | Tôi cần mẫu và công cụ nào để vận hành? | Mẫu ghi chú, tệp đính kèm và sơ đồ |

Xem đầy đủ tại [[QUY ƯỚC MINDMIRROR]].

## Skill AI đi kèm

Nguồn chuẩn nằm trong `.claude/skills/`. Adapter cho Codex nằm trong `.agents/skills/`.

- `mindmirror-luu-tra-loi` — lưu nhanh một nội dung vào Thu Thập.
- `mindmirror-xu-ly` — xử lý nội dung theo bốn tầng.
- `mindmirror-tong-hop-tuan` — tổng kết tuần từ Nhật Ký Ngày.
- `mindmirror-ban-do-cuoc-doi` — xây hồ sơ cá nhân để AI hiểu người dùng.
- `mindmirror-co-van-ca-nhan` — tư vấn dựa trên ngữ cảnh thật trong vault.

## Cài skill cho Hermes (tuỳ chọn)

Nếu bạn dùng Hermes Agent, chạy:

```bash
python3 scripts/cai-skill-hermes.py
```

Sau đó mở phiên Hermes mới hoặc chạy `/reload-skills`. Adapter Hermes chỉ trỏ về skill chuẩn trong vault, nên lần sau `git pull` là workflow mới được dùng ngay.

## Cập nhật mà không mất dữ liệu

Dữ liệu cá nhân như `Me.md`, nhật ký, ghi chú, dự án và tệp đính kèm được `.gitignore` bảo vệ. Khi cập nhật bằng Git, các file hệ thống và skill được nâng cấp nhưng dữ liệu cá nhân không bị ghi đè.

```bash
git pull --ff-only
```

Hoặc chạy:

```bash
python3 scripts/cap-nhat.py
```

## Tác giả

**Trọng Đinh — MindMirror**  
Website: https://www.mindmirror.vn/  
Facebook: https://www.facebook.com/profile.php?id=61585320965090
