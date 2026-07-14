---
tags: [he-thong, huong-dan, mindmirror]
---

# Quy Ước MindMirror

## 1. Kiến trúc 4 tầng

```text
1. Thu Thập
→ 2. Tinh Lọc
→ 3. Chuyển Hoá
→ 4. Kiến Tạo
```

### 1. Thu Thập

Nơi giữ tín hiệu thô trước khi bị quên. Chỉ cần nội dung, nguồn nếu có và thời điểm. Không phân loại sâu tại đây.

### 2. Tinh Lọc

Nơi làm rõ ý nghĩa bằng ngôn ngữ của chính người dùng.

- `Nhật Ký Ngày/`: dữ liệu sống và bối cảnh theo thời gian.
- `Ghi Chú Tinh Lọc/`: điều học được từ sách, video, cuộc trò chuyện, khách hàng hoặc trải nghiệm.
- `Tổng Kết Tuần/`: nhận diện kết quả, mô thức và ưu tiên tuần tới.

### 3. Chuyển Hoá

Nơi tri thức đủ rõ để dùng lại lâu dài.

- `Bản Đồ/`: điều hướng các cụm tri thức.
- `Bản Đồ/Bản Đồ Chủ Đề/`: trang tập hợp một lĩnh vực.
- `Tri Thức/Luận Điểm Cốt Lõi/`: một câu khẳng định có chủ ngữ, vị ngữ và quan điểm.
- `Tri Thức/Khung Tư Duy/`: cấu trúc, quy trình hoặc mô hình có thể áp dụng lặp lại.

### 4. Kiến Tạo

Nơi tri thức trở thành kết quả thật.

- `Đang Làm/`: có kết quả cần bàn giao và hạn hoàn thành.
- `Duy Trì/`: trách nhiệm hoặc hệ thống vận hành thường xuyên.
- `Để Sau/`: đáng cân nhắc nhưng chưa cam kết.
- `Tạm Dừng/`: đã kết thúc hoặc tạm ngưng; lưu trữ thay vì xoá.

## 2. Quy tắc loại ghi chú

| Loại | Đích | Điều kiện hoàn thành |
|---|---|---|
| Ghi nhanh | `1. Thu Thập/` | Giữ được tín hiệu, nguồn và ngày |
| Ghi chú tinh lọc | `2. Tinh Lọc/Ghi Chú Tinh Lọc/` | Có ý nghĩa cá nhân và câu hỏi mở |
| Luận điểm cốt lõi | `3. Chuyển Hoá/Tri Thức/Luận Điểm Cốt Lõi/` | Tiêu đề là câu khẳng định, có nguồn và ít nhất 2 liên kết liên quan |
| Khung tư duy | `3. Chuyển Hoá/Tri Thức/Khung Tư Duy/` | Có mục đích, thành phần, cách dùng và ví dụ |
| Dự án đang làm | `4. Kiến Tạo/Đang Làm/` | Có kết quả bàn giao, hạn hoàn thành và bước tiếp theo |

## 3. Quy tắc liên kết

- `up:` trong frontmatter dùng để link tới Bản Đồ Chủ Đề.
- Phần `## Liên kết` của Luận Điểm Cốt Lõi chỉ link các luận điểm liên quan.
- Không tạo note mồ côi: mỗi note Chuyển Hoá hoặc Kiến Tạo phải có ít nhất một đường quay về bản đồ/dự án.

## 4. Tương thích kỹ thuật

Tên tiếng Anh cũ chỉ dùng khi di chuyển vault cũ:

| Tên cũ | Tên chuẩn mới |
|---|---|
| RAW | Thu Thập |
| MINE | Tinh Lọc |
| CORE | Chuyển Hoá |
| MINT | Kiến Tạo |
| Literature Note | Ghi Chú Tinh Lọc |
| Statement | Luận Điểm Cốt Lõi |
| Framework | Khung Tư Duy |
| MOC | Bản Đồ Chủ Đề |

Không tạo mới thư mục theo tên cũ.
