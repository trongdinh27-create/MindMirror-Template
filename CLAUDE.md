# Hướng dẫn AI làm việc với MindMirror

## Khởi động

1. Đọc `Me.md` nếu file tồn tại; nếu chưa có, hướng dẫn người dùng sao chép `Me.example.md` thành `Me.md`.
2. Đọc `QUY ƯỚC MINDMIRROR.md` trước khi tạo, đổi tên hoặc di chuyển note.
3. Viết bằng tiếng Việt. Khi cần dùng thuật ngữ tiếng Anh, thêm nghĩa tiếng Việt ở lần xuất hiện đầu tiên.

## Kiến trúc

```text
1. Thu Thập → 2. Tinh Lọc → 3. Chuyển Hoá → 4. Kiến Tạo
```

- `1. Thu Thập/`: tín hiệu thô.
- `2. Tinh Lọc/`: ý nghĩa cá nhân, nhật ký và tổng kết.
- `3. Chuyển Hoá/`: luận điểm, khung tư duy và bản đồ tri thức.
- `4. Kiến Tạo/`: dự án, nội dung, sản phẩm và hành động.
- `5. Hộp Công Cụ/`: mẫu, tệp đính kèm và sơ đồ.

## Quy tắc ghi

- Không ép mọi capture (thu thập) phải đi đủ bốn tầng.
- Không đưa một ghi chú thô thẳng thành Luận Điểm Cốt Lõi nếu chưa có ý nghĩa cá nhân rõ.
- Tiêu đề Luận Điểm Cốt Lõi phải là một câu khẳng định hoàn chỉnh.
- `up:` chứa Bản Đồ Chủ Đề; `## Liên kết` của Luận Điểm Cốt Lõi chỉ chứa các luận điểm liên quan.
- Dự án ở `Đang Làm` phải có hạn hoàn thành và kết quả bàn giao.
- Lưu trữ vào `Tạm Dừng`; không xoá dữ liệu người dùng nếu chưa được yêu cầu rõ.

## Skill

Nguồn chuẩn của skill nằm tại `.claude/skills/`. Adapter Codex tại `.agents/skills/` chỉ trỏ về nguồn chuẩn, không sao chép toàn bộ quy trình.
