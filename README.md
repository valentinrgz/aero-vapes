# Aero Vapes

Sitio estático (catálogo + carrito + checkout por WhatsApp) para Aero Vapes.

## Estructura

- `index.html` — el sitio final, listo para publicar en cualquier hosting estático (Vercel, Netlify, GitHub Pages, etc.). Es autocontenido: no necesita build ni backend.
- `template.html` — el HTML/CSS/JS del sitio, con un placeholder `__PRODUCTS_JSON__` en vez de los datos de productos.
- `build.py` — genera `index.html` combinando `template.html` con el catálogo (`PRODUCTS`) definido ahí mismo, incrustando las fotos de `aero-images/` como base64.
- `aero-images/` — fotos de producto ya comprimidas (usadas por `build.py`).

## Cómo actualizar stock o precios

1. Abrí `build.py`.
2. Buscá el sabor que corresponda dentro del array `PRODUCTS` y cambiá su `"stock"` (o `"price"` del modelo).
   - `stock: 0` lo muestra como "Agotado" en la tienda.
3. Corré:

   ```bash
   python3 build.py
   ```

4. Commiteá y pusheá `index.html` (y `build.py` si cambiaste algo ahí).

## Cómo publicarlo

Cualquier hosting estático sirve. Por ejemplo, con Vercel:

```bash
npx vercel --prod
```

O conectá este repo de GitHub directamente desde el dashboard de Vercel/Netlify y apuntá el build output a `index.html` (no hace falta build command).
