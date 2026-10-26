# Como evoluir este perfil

O README foi montado para crescer sem refazer o visual. O que muda com o tempo fica em poucos lugares.

## O que editar, e onde

| Mudança | Onde | Depois |
| --- | --- | --- |
| Cargo, empresa, status ("estagiário em …", ocultar o status) | `scripts/visuals/content.py` → `IDENTIDADE` | `python3 scripts/visuals/build.py` |
| Nova tecnologia | `content.py` → `TECNOLOGIAS` (copie o ícone para `assets/icons/`; informe a `prova`) | `build.py` |
| Novo projeto | nova subseção `###` em **Projetos** no README (texto + links; imagem só se agregar) | — |
| Primeira experiência profissional | nova seção **Experiência** logo abaixo de **Tecnologias** (modelo abaixo) | — |
| Certificações, eventos, publicações | seção curta antes de **Formação** | — |
| Novos números do acervo (61, 124 exercícios) | tabela de **Estudos em código** | — |
| Formação (período, conclusão) | seção **Formação** | — |

## Modelo para Experiência

```markdown
## Experiência

**Estagiário(a) em <área>** — <Empresa> · <mês/ano> – atual
- O que construiu ou manteve, com a tecnologia e o resultado verificável.
- Seu papel (o que foi seu e o que foi da equipe).
```

Dados confidenciais ficam de fora: descreva a tecnologia e o tipo de problema, sem nomes de clientes, métricas internas ou código.

## Regras que valem sempre

1. Só entra o que você consegue provar no código ou em um documento seu. Cada tecnologia em `content.py` tem uma `prova`.
2. Uso de IA nos projetos continua declarado, no nível exato em que aconteceu.
3. Poucos elementos por tela. Uma animação nova só entra se explicar algo que o texto não explica.
4. Quando um projeto antigo deixar de representar você, mova-o para dentro de um `<details>` em vez de apagar o histórico.
5. Imagens animadas sempre com versão estática (`prefers-reduced-motion`) e versão para celular, como as atuais.

## Gerar os SVGs

```bash
python3 scripts/visuals/build.py
```

Só biblioteca padrão do Python. Os ícones de `assets/icons/` vêm do projeto skill-icons (licença MIT em `LICENSE-skill-icons.txt`); os logotipos pertencem aos seus donos.
