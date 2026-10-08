"""Validate the complete Pages output, including the large release video."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
manifest = json.loads((root / ".github/media/verano.json").read_text(encoding="utf-8"))
site = root / "_site"
video = site / "assets/verano.mp4"

if video.stat().st_size != manifest["bytes"]:
    raise SystemExit("El tamaño del vídeo no coincide con la versión verificada.")

digest = hashlib.sha256()
with video.open("rb") as source:
    for chunk in iter(lambda: source.read(8 * 1024 * 1024), b""):
        digest.update(chunk)
if digest.hexdigest() != manifest["sha256"]:
    raise SystemExit("El SHA256 del vídeo no coincide con la versión verificada.")

files = [path for path in site.rglob("*") if path.is_file()]
if any(path.is_symlink() for path in site.rglob("*")):
    raise SystemExit("La publicación debe contener archivos y carpetas normales.")
site_bytes = sum(path.stat().st_size for path in files)
if site_bytes > 990_000_000:
    raise SystemExit(f"El sitio supera el presupuesto de 990 MB: {site_bytes} bytes.")
if not (site / "index.html").is_file():
    raise SystemExit("Falta index.html.")

print(f"Vídeo SHA256 verificado: {digest.hexdigest()}")
print(f"Sitio: {site_bytes:,} bytes en {len(files)} archivos; margen hasta 1 GB: {1_000_000_000 - site_bytes:,} bytes.")
