#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = [
    "1. Thu Thập",
    "2. Tinh Lọc/Nhật Ký Ngày",
    "2. Tinh Lọc/Ghi Chú Tinh Lọc",
    "2. Tinh Lọc/Tổng Kết Tuần",
    "3. Chuyển Hoá/Bản Đồ/Bản Đồ Chủ Đề",
    "3. Chuyển Hoá/Tri Thức/Luận Điểm Cốt Lõi",
    "3. Chuyển Hoá/Tri Thức/Khung Tư Duy",
    "4. Kiến Tạo/Đang Làm",
    "4. Kiến Tạo/Duy Trì",
    "4. Kiến Tạo/Để Sau",
    "4. Kiến Tạo/Tạm Dừng",
    "5. Hộp Công Cụ/Mẫu",
]
errors = []
for rel in required:
    if not (root / rel).is_dir():
        errors.append(f"Thiếu thư mục: {rel}")

for p in root.rglob("*"):
    if ".git" in p.parts or not p.is_file() or p.name == "Me.md" or p.name == "kiem-tra.py":
        continue
    if p.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml"}:
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    if "/Users/" in text or "C:\\Users\\" in text:
        errors.append(f"Có đường dẫn máy cá nhân: {p.relative_to(root)}")

for p in (root / ".claude/skills").glob("*/SKILL.md"):
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"Frontmatter lỗi: {p.relative_to(root)}")
    if not re.search(r"^name:\s*mindmirror-[a-z0-9-]+\s*$", text, re.M):
        errors.append(f"Tên skill không chuẩn: {p.relative_to(root)}")
    if not re.search(r"^description:\s*.+$", text, re.M):
        errors.append(f"Thiếu description: {p.relative_to(root)}")

for p in (root / ".agents/skills").glob("*/SKILL.md"):
    text = p.read_text(encoding="utf-8")
    targets = re.findall(r"`(\.\./\.\./\.\./\.claude/skills/[^`]+/SKILL\.md)`", text)
    if len(targets) != 1 or not (p.parent / targets[0]).resolve().exists():
        errors.append(f"Adapter Codex hỏng: {p.relative_to(root)}")

if errors:
    print("KIỂM TRA THẤT BẠI")
    for e in errors:
        print("-", e)
    raise SystemExit(1)
print(f"KIỂM TRA THÀNH CÔNG — {len(required)} thư mục, skill và adapter hợp lệ")
