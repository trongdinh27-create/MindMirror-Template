#!/usr/bin/env python3
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
if not (root / ".git").exists():
    raise SystemExit("Vault này được tải bằng ZIP nên không thể cập nhật bằng Git. Hãy dùng GitHub Desktop hoặc git clone cho lần cài tiếp theo.")
subprocess.run(["git", "pull", "--ff-only"], cwd=root, check=True)
print("Đã cập nhật file hệ thống và skill. Dữ liệu cá nhân được giữ nguyên bởi .gitignore.")
