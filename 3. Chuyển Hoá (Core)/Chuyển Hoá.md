---
type: moc
folder: 3. Chuyển Hoá (Core)
cssclasses: [moc]
---

# 🧠 Chuyển Hoá (Core)

> Nơi tri thức được tinh lọc và kết nối.

- **Tuyên Ngôn** (Permanent Notes) — Những điều bạn thực sự tin
- **Khung Tư Duy** (Frameworks) — Mô hình tư duy cá nhân của bạn
- **Bản Đồ** (Maps) — Bản đồ điều hướng tri thức
- **Ghi chú vĩnh viễn** (Permanent Notes) — Ý tưởng đã tinh lọc hoàn toàn

---

## 💬 Tuyên Ngôn (Permanent Notes)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "3. Chuyển Hoá (Core)/Dots/Permanent Notes"
SORT file.mtime DESC
```

---

## 🔲 Khung Tư Duy (Frameworks)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "3. Chuyển Hoá (Core)/Dots/Frameworks"
SORT file.mtime DESC
```

---

## 🗺️ Bản Đồ (Maps)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "3. Chuyển Hoá (Core)/Bản Đồ (Maps)"
SORT file.mtime DESC
```

---

## 📌 Ghi chú vĩnh viễn (Permanent Notes)

```dataview
TABLE
  file.ctime as "📅 Ngày tạo",
  file.mtime as "🔄 Cập nhật"
FROM "3. Chuyển Hoá (Core)/Dots/Ghi chú vĩnh viễn (Permanent Notes)"
SORT file.mtime DESC
```
