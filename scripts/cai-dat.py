#!/usr/bin/env python3
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
me = root / "Me.md"
example = root / "Me.example.md"
if not me.exists():
    shutil.copy2(example, me)
    print("Đã tạo Me.md từ bản mẫu.")
else:
    print("Me.md đã tồn tại; không ghi đè.")
print("Mở vault trong Obsidian và đọc BẮT ĐẦU TỪ ĐÂY.md.")
