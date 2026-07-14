#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = root / ".claude/skills"
dest_root = Path.home() / ".hermes/skills/mindmirror-vault"
dest_root.mkdir(parents=True, exist_ok=True)
count = 0
for skill_file in sorted(source.glob("*/SKILL.md")):
    text = skill_file.read_text(encoding="utf-8")
    name_match = re.search(r"^name:\s*(.+)$", text, re.M)
    desc_match = re.search(r"^description:\s*(.+)$", text, re.M)
    if not name_match or not desc_match:
        continue
    name = name_match.group(1).strip()
    desc = desc_match.group(1).strip()
    target = dest_root / name / "SKILL.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        f"---\nname: {name}\ndescription: {desc}\n---\n\n"
        f"# Adapter Hermes cho MindMirror\n\n"
        f"Đọc và thực hiện đầy đủ workflow chuẩn tại:\n\n"
        f"`{skill_file.resolve()}`\n\n"
        f"File trong vault là nguồn chuẩn; không sao chép quy trình vào adapter này.\n",
        encoding="utf-8",
    )
    count += 1
print(f"Đã cài {count} adapter vào {dest_root}")
print("Mở phiên Hermes mới hoặc chạy /reload-skills để tải lại menu skill.")
