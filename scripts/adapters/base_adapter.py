import os
import shutil
import sys
from pathlib import Path

def safe_link_or_copy(source_path: Path, target_path: Path) -> str:
    """
    Safely link or copy source_path to target_path without wiping existing unmanaged files.
    Returns string status: 'symlinked' or 'copied'.
    """
    source_path = source_path.resolve()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # If target exists and points to source, do nothing
    if target_path.is_symlink():
        try:
            current_target = target_path.resolve()
            if current_target == source_path:
                return "already_linked"
        except Exception:
            pass
        target_path.unlink()

    # Try symlinking first
    try:
        if source_path.is_dir():
            os.symlink(source_path, target_path, target_is_directory=True)
        else:
            os.symlink(source_path, target_path, target_is_directory=False)
        return "symlinked"
    except (OSError, PermissionError, NotImplementedError):
        # Graceful fallback to physical copy
        if source_path.is_dir():
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
        else:
            shutil.copy2(source_path, target_path)
        return "copied"
