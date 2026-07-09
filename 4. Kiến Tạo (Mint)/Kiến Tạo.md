---
type: moc
folder: 4. Kiến Tạo (Mint)
cssclasses: [moc]
---

# 🚀 Kiến Tạo (Mint)

> Tri thức được đúc thành giá trị thật.

- **Đang Làm** (Active) — Dự án đang thực hiện ngay bây giờ
- **Đang Ủ** (Background) — Ý tưởng đang tiến triển chậm
- **Để Sau** (Later) — Ý tưởng cần quay lại sau

---

## ⚡ Đang Làm (Active)

```dataview
TABLE
  file.ctime as "📅 Ngày bắt đầu",
  file.mtime as "🔄 Cập nhật"
FROM "4. Kiến Tạo (Mint)/Đang Làm (Active)"
SORT file.mtime DESC
```

---

## 🌱 Đang Ủ (Background)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "4. Kiến Tạo (Mint)/Đang Ủ (Background)"
SORT file.mtime DESC
```

---

## 🕐 Để Sau (Later)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "4. Kiến Tạo (Mint)/Để Sau (Later)"
SORT file.mtime DESC
```
