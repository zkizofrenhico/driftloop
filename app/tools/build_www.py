"""Copia el juego (index.html de la raíz del repo) a la app, con las fuentes incluidas en vez de Google Fonts."""
import pathlib
root = pathlib.Path(__file__).resolve().parents[2]
game = (root / 'index.html').read_text(encoding='utf-8').split('\n')
fonts = (pathlib.Path(__file__).parent / 'fonts.html').read_text(encoding='utf-8').rstrip('\n').split('\n')
i = next(k for k, l in enumerate(game) if l.startswith('<link rel="preconnect" href="https://fonts.googleapis.com"'))
j = next(k for k, l in enumerate(game) if 'fonts.googleapis.com/css2' in l)
out = game[:i] + fonts + game[j + 1:]
(root / 'app' / 'www' / 'index.html').write_text('\n'.join(out), encoding='utf-8')
print('www/index.html actualizado:', len(out), 'líneas')
