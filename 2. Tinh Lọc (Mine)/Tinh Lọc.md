---
type: moc
folder: 2. Tinh Lọc (Mine)
cssclasses: [moc]
---

# 🔍 Tinh Lọc (Mine)

> Khai thác tri thức từ bên trong và bên ngoài.

- **Nhật ký ngày** (Daily Notes) — Nhật ký tư duy hàng ngày
- **Nhật ký tuần** (Weekly Notes) — Tổng hợp và nhìn lại mỗi tuần
- **Ghi Chú Học Tập** (Literature Notes) — Tinh hoa từ sách, khoá học, bài học kinh nghiệm

---

## 📅 Nhật ký ngày (Daily Notes)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "2. Tinh Lọc (Mine)/Nhật ký ngày (Daily Notes)"
SORT file.name DESC
```

---

## 📆 Nhật ký tuần (Weekly Notes)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "2. Tinh Lọc (Mine)/Nhật ký tuần (Weekly Notes)"
SORT file.name DESC
```

---

## 📚 Ghi Chú Học Tập (Literature Notes)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "2. Tinh Lọc (Mine)/Ghi Chú Học Tập (Literature Notes)"
SORT file.ctime DESC
```
