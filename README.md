# Póker · Gestor de fichas

App web para **contar fichas y apuestas** jugando al póker **Texas Hold'em** con hasta 4 jugadores en un mismo dispositivo (móvil o iPad). La app lleva las fichas, las apuestas, el bote y las rondas de **Pre-flop, Flop, Turn y River** — vosotros ponéis las cartas.

## Características

- 4 jugadores en un solo dispositivo (pásalo en cada turno).
- Fichas por denominación: 0,20 · 0,50 · 1 · 2 · 5 €.
- Rondas de apuestas completas: **Pre-flop → Flop → Turn → River → Showdown**.
- Acciones: pasar, apostar, igualar, subir, retirarse y **all-in**.
- Reparto del bote a un ganador o **empate** (reparto justo en fichas).
- Cambio de fichas grandes por pequeñas del mismo valor.
- Detección de jugadores eliminados y fin de partida.
- Diseño responsive pensado para **móvil e iPad**; la partida se guarda sola en el navegador.

## Uso

Es una app estática de un solo archivo (`index.html`). Basta con abrir el archivo en el navegador, o servirlo:

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

No hay dependencias ni paso de compilación.

## Licencia

MIT — úsalo y modifícalo libremente.
