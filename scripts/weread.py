"""Backward-compatible script entrypoint.

Prefer `weread2notion sync` for new workflows.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def run():
    """在补充源码路径后加载并运行兼容入口。"""
    from weread2notion.cli import main

    main()


if __name__ == "__main__":
    run()
