# Desarrollando historias — Pak Paxtor

Presentación HTML sobre autoría e IA en el audiovisual profesional.

**Ver la presentación:** https://pakpaxtor.github.io/pakpaxtor-showcase/

## Archivos

- `index.html`: presentación, con estilos, scripts y tipografías incluidos.
- `assets/`: imágenes, audio y copias de los vídeos preparadas para web.
- `.nojekyll`: mantiene la publicación como archivos estáticos.
- `.github/workflows/pages.yml`: prepara y publica la web, incorporando el vídeo grande desde un Release de GitHub.

Los vídeos de esta publicación conservan su contenido y duración, con compresión para facilitar la reproducción en internet. Los originales de mayor tamaño se conservan fuera de este repositorio.

## Publicación en GitHub Pages

En **Settings → Pages**, seleccionar **GitHub Actions**. Cada cambio en `main` ejecuta el despliegue.

`El último verano` se publica en 1080p desde el Release `verano-web-1080p-v1`. El flujo descarga el MP4 a `assets/verano.mp4`, comprueba su tamaño y SHA256, y publica el sitio completo. Así el vídeo puede superar los 100 MiB del Git ordinario y reproducirse directamente desde GitHub Pages.

El archivo local `assets/verano.mp4` se conserva para abrir la presentación en el ordenador, pero está excluido de Git. Después de clonar el repositorio, se puede recuperar con:

```sh
gh release download verano-web-1080p-v1 --repo PakPaxtor/pakpaxtor-showcase --pattern verano-1080p-alta-calidad.mp4 --output assets/verano.mp4
```

## Actualizar la presentación

1. Editar `index.html` o sustituir los archivos en `assets/`, conservando sus nombres y rutas.
2. Mantener los archivos de Git por debajo de 100 MiB. El sitio publicado tiene un presupuesto de 990 MB, con margen hasta el límite de 1 GB.
3. Para sustituir `El último verano`, subir su nueva versión a un Release y actualizar `.github/media/verano.json` con el tag, nombre, tamaño y SHA256.
4. Subir los cambios a la rama `main`. GitHub Actions vuelve a publicar la web automáticamente.

La presentación y sus materiales pertenecen a sus respectivos titulares. Su publicación no concede una licencia de reutilización.
