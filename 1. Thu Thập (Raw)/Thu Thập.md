---
type: moc
folder: 1. Thu Thập (Raw)
cssclasses: [moc]
---

# 📥 Thu Thập — RAW

> Bắt được ý tưởng trước khi nó biến mất.

- Bất kỳ ý tưởng, link, đoạn trích, quan sát → vào đây **trước tiên**. Không format. Không phán xét.
- **Quy tắc 30 giây**: Capture mất dưới 30 giây → ghi vào đây ngay.
- **Mục tiêu cuối tuần**: Thu Thập = 0 file (đã xử lý hết).

---

## 🗂️ Tất cả ghi chú đang chờ xử lý

```dataview
TABLE
  file.ctime as "📅 Ngày capture",
  file.mtime as "🔄 Cập nhật"
FROM "1. Thu Thập (Raw)"
WHERE file.name != "Thu Thập"
SORT file.ctime DESC
```
