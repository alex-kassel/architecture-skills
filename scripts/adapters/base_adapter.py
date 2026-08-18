import os
import shutil
import sys
import subprocess
from pathlib import Path

def safe_link_or_copy(source_path: Path, target_path: Path) -> str:
    """
    Safely link or copy source_path to target_path using Windows NTFS Junctions / Symlinks.
    Returns string status: 'junctioned', 'symlinked', 'hardlinked', or 'copied'.
    """
    source_path = source_path.resolve()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # If target exists and is a symlink/junction
    if target_path.is_symlink():
        try:
            current_target = target_path.resolve()
            if current_target == source_path:
                return "already_linked"
        except Exception:
            pass
        target_path.unlink()

    # Remove existing physical file/directory before linking
    if target_path.exists():
        if target_path.is_dir():
            shutil.rmtree(target_path)
        else:
            target_path.unlink()

    # Attempt Junction / Symlink / Hardlink
    try:
        if source_path.is_dir():
            if sys.platform == "win32":
                # Use NTFS Junction on Windows (works for normal non-admin users)
                res = subprocess.run(
                    ["cmd", "/c", "mklink", "/J", str(target_path), str(source_path)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if res.returncode == 0:
                    return "junctioned"
                os.symlink(source_path, target_path, target_is_directory=True)
                return "symlinked"
            else:
                os.symlink(source_path, target_path, target_is_directory=True)
                return "symlinked"
        else:
            if sys.platform == "win32":
                try:
                    os.symlink(source_path, target_path, target_is_directory=False)
                    return "symlinked"
                except Exception:
                    os.link(source_path, target_path)
                    return "hardlinked"
            else:
                os.symlink(source_path, target_path, target_is_directory=False)
                return "symlinked"
    except Exception:
        # Fallback to physical copy if link creation is strictly disallowed
        if source_path.is_dir():
            shutil.copytree(source_path, target_path)
        else:
            shutil.copy2(source_path, target_path)
        return "copied"
