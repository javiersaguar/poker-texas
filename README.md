# Póker · Gestor de fichas

App web para **contar fichas y apuestas** jugando al póker **Texas Hold'em** con **de 2 a 8 jugadores** en un mismo dispositivo (móvil o iPad). La app lleva las fichas, las apuestas, el bote y las rondas de **Pre-flop, Flop, Turn y River** — vosotros ponéis las cartas.

## Características

- **De 2 a 8 jugadores** en un solo dispositivo (pásalo en cada turno); mesa configurable antes de empezar.
- La mesa se reorganiza sola según cuántos jugáis, y el asiento en turno se trae a la vista en pantallas pequeñas.
- Fichas por denominación: 0,20 · 0,50 · 1 · 2 · 5 €.
- Rondas de apuestas completas: **Pre-flop → Flop → Turn → River → Showdown**.
- **Ciegas configurables**: ajústalas de 10 en 10 céntimos o escribe la cantidad a mano (la grande es siempre el doble); también se puede jugar sin ciegas.
- Marcas de **repartidor (D), ciega pequeña (CP) y ciega grande (CG)** en la mesa, rotando cada mano.
- Acciones: pasar, apostar, igualar, subir, retirarse y **all-in**.
- Botón **Poner X** que añade automáticamente las fichas justas para igualar (cambia fichas grandes solo si hace falta).
- Reparto del bote a un ganador o **empate** (reparto justo en fichas).
- Cambio de fichas grandes por pequeñas del mismo valor.
- **Recompra**: quien se queda sin fichas —o muy por debajo del resto— puede volver a entrar, y esa entrada cuenta en las cuentas finales.
- **Pantalla entre manos**: al repartir el bote se ve quién ha ganado y cómo va cada uno, y desde ahí se elige jugar otra mano, recomprar o cerrar la partida.
- **Finalizar partida**: pantalla de resultados con lo que ha puesto y ganado cada uno y **quién paga cuánto a quién** (número mínimo de pagos).
- Detección de jugadores eliminados y fin de partida.
- Pantalla de inicio con opción de **continuar la última partida** (se guarda sola en el navegador).
- Diseño responsive pensado para **móvil e iPad**; la partida se guarda sola en el navegador.

## Icono en la pantalla de inicio (iPhone / iPad)

La app trae su propio icono —una ficha con una pica sobre el tapete verde— para cuando se añade a la pantalla de inicio:

1. Abre la web en **Safari** (en iOS el icono solo lo coge Safari, no Chrome).
2. Botón **Compartir** → **Añadir a pantalla de inicio**.
3. Aparece el icono y el nombre **Póker**; toca **Añadir**.

Al abrirla desde ahí se lanza a pantalla completa, sin la barra de Safari.

> iOS guarda el icono en el momento de añadirla. Si cambias el icono, hay que **borrar el acceso directo y volver a añadirlo** para ver el nuevo.

Los archivos están en `icons/` y se generan a partir de `icons/icon.svg`:

```bash
python3 icons/build-icons.py   # necesita Pillow y Chromium instalados
```

| Archivo | Para qué |
| --- | --- |
| `icons/apple-touch-icon-180.png` | icono de la pantalla de inicio en iOS/iPadOS |
| `icons/icon-192.png`, `icons/icon-512.png` | Android y escritorio (vía `manifest.webmanifest`) |
| `icons/icon-maskable-512.png` | Android, con margen para que el sistema lo recorte |
| `icons/favicon-32.png`, `icons/icon.svg` | pestaña del navegador |

## Uso

Es una app estática: toda la lógica vive en `index.html` (los iconos y el `manifest.webmanifest` solo hacen falta para instalarla en la pantalla de inicio). Basta con abrir el archivo en el navegador, o servirlo:

```bash
# opción rápida con Python
python -m http.server 8000
# luego abre http://localhost:8000
```

## Despliegue en Vercel

1. Entra en [vercel.com](https://vercel.com) e inicia sesión con GitHub.
2. **Add New… → Project** e importa el repositorio `poker-texas`.
3. **Framework Preset:** `Other`. Sin build command ni output directory (es estático).
4. **Deploy**. Vercel servirá `index.html` en la raíz automáticamente.

El `vercel.json` incluido desactiva la caché del HTML para que cada despliegue llegue al móvil sin tener que forzar recarga.

No hay dependencias ni paso de compilación.

## Licencia

MIT — úsalo y modifícalo libremente.
