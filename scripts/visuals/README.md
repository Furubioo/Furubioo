# Geradores dos SVGs do perfil

Os arquivos de `assets/` são gerados por estes scripts (Python 3, só biblioteca padrão).

```bash
python3 scripts/visuals/build.py                  # tudo
python3 scripts/visuals/build.py --only activity  # só o calendário (usado pelo workflow diário)
```

Cada composição sai em 4 variantes: desktop e celular, animada e estática
(a estática é usada por `prefers-reduced-motion`).

- `hero.py`, `cinema.py`, `ong.py`, `lab.py`: cenas (textos e dados vêm dos repositórios do perfil).
- `activity.py`: calendário a partir da página pública de contribuições, sem token.
- `lib.py`, `common.py`, `widgets.py`: funções de animação SMIL e componentes compartilhados.
