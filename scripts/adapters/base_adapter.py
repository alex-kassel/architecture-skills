import os
import shutil
import sys
import subprocess
from pathlib import Path

def _remove_target_cleanly(target_path: Path):
    """Safely remove target_path whether it is a physical file, dir, symlink, or NTFS Junction."""
    if not target_path.exists() and not target_path.is_symlink():
        return

    # Check if target is symlink or junction
    if target_path.is_symlink():
        try:
            target_path.unlink()
            return
        except Exception:
            pass

    # Try removing as junction / symlink directory
    if sys.platform == "win32":
        try:
            os.rmdir(target_path)
            return
        except Exception:
            pass
        try:
            subprocess.run(["cmd", "/c", "rmdir", str(target_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if not target_path.exists():
                return
        except Exception:
            pass

    # If physical directory
    if target_path.is_dir():
        shutil.rmtree(target_path)
    else:
        target_path.unlink()

def safe_link_or_copy(source_path: Path, target_path: Path) -> str:
    """
    Safely link or copy source_path to target_path using Windows NTFS Junctions / Symlinks.
    Returns string status: 'junctioned', 'symlinked', 'hardlinked', or 'copied'.
    """
    source_path = source_path.resolve()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if target already points to source
    if target_path.is_symlink() or (sys.platform == "win32" and target_path.exists() and target_path.is_dir()):
        try:
            if target_path.resolve() == source_path:
                return "already_linked"
        except Exception:
            pass

    # Cleanly remove existing target
    _remove_target_cleanly(target_path)

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
