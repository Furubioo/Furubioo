<!--
  Antes de publicar no repositório Furubioo/Furubioo, personalize:
  1. Troque {REPO-LUMIERE} pelo nome real do repositório do Lumière Cinema (usado 2x: no link e no card de repositório).
  2. Troque os placeholders de LinkedIn/e-mail na seção de contato — não incluí nenhum real porque não tenho certeza de qual você quer deixar público.
  3. A seção de atividade (gráfico animado de contribuições) só aparece depois de um pequeno setup via GitHub Actions — o workflow está comentado logo abaixo dela.
  4. Todos os widgets (stats, streak, ícones) têm versão clara e escura, trocando automaticamente com o tema do GitHub de quem visita.
-->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=200&section=header&text=Fl%C3%A1vio%20Ara%C3%BAjo&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Estudante%20de%20Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o%20%40%20UNICAP&descAlignY=55&descSize=16" width="100%"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1400&color=8FD3FF&center=true&vCenter=true&width=620&lines=Ci%C3%AAncia+da+Computa%C3%A7%C3%A3o+%C2%B7+UNICAP;Java+%C2%B7+Python+%C2%B7+C;Full-stack%3A+React+%2B+Spring+Boot" />
  <img alt="Typing SVG" src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1400&color=2C5364&center=true&vCenter=true&width=620&lines=Ci%C3%AAncia+da+Computa%C3%A7%C3%A3o+%C2%B7+UNICAP;Java+%C2%B7+Python+%C2%B7+C;Full-stack%3A+React+%2B+Spring+Boot" />
</picture>

<br/><br/>

![Status](https://img.shields.io/badge/status-aberto_a_oportunidades_de_est%C3%A1gio-2ea44f?style=for-the-badge)

</div>

## Sobre

Estudante do 4º período de Ciência da Computação na UNICAP (programa C3), com formação técnica anterior em Redes de Computadores. Migrei de Sistemas de Informação para Ciência da Computação em busca de uma base mais sólida em desenvolvimento de software, e hoje me interesso especialmente por aplicações full-stack, estruturas de dados e infraestrutura.

## Tech Stack

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=java,py,c&theme=dark" />
  <img alt="Linguagens" src="https://skillicons.dev/icons?i=java,py,c&theme=light" />
</picture>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=react,spring,git,github,figma&theme=dark" />
  <img alt="Frameworks e ferramentas" src="https://skillicons.dev/icons?i=react,spring,git,github,figma&theme=light" />
</picture>
</p>

## Projeto em destaque

**Lumière Cinema** — sistema de venda de ingressos de cinema com fluxos para usuário, crítico e administrador.

A aplicação começou em Java, rodando via terminal e aplicando os padrões de projeto MVC e Strategy, com herança, sobrescrita e sobrecarga de métodos. Depois foi estendida para uma aplicação web, com front-end em React, back-end em Spring Boot e H2 como banco de dados — o código dessa etapa foi gerado com apoio de ferramentas de IA, e minha contribuição foi a configuração do ambiente, a integração entre front e back-end e a resolução de bugs (lógica de sugestão de assentos, filtro de cupons, carregamento de pôsteres via TMDB, entre outros).

<p align="center">
<a href="https://github.com/Furubioo/{REPO-LUMIERE}">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo={REPO-LUMIERE}&theme=tokyonight&hide_border=true" />
    <img alt="Lumière Cinema" src="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo={REPO-LUMIERE}&theme=default&hide_border=true" />
  </picture>
</a>
</p>

## Atividade

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=Furubioo&show_icons=true&theme=tokyonight&hide_border=true" />
  <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=Furubioo&show_icons=true&theme=default&hide_border=true" height="165"/>
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=Furubioo&theme=tokyonight&hide_border=true" />
  <img alt="GitHub Streak" src="https://streak-stats.demolab.com?user=Furubioo&theme=default&hide_border=true" height="165"/>
</picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Furubioo/Furubioo/output/github-snake-dark.svg" />
  <img alt="Gráfico animado de contribuições" src="https://raw.githubusercontent.com/Furubioo/Furubioo/output/github-snake.svg" width="100%"/>
</picture>

<!--
  Setup do gráfico animado acima — crie .github/workflows/snake.yml no repositório
  Furubioo/Furubioo com este conteúdo (roda sozinho, uma vez por dia):

  name: Snake
  on:
    schedule:
      - cron: "0 0 * * *"
    workflow_dispatch:
  jobs:
    build:
      runs-on: ubuntu-latest
      permissions:
        contents: write
      steps:
        - uses: Platane/snk@v3
          with:
            github_user_name: Furubioo
            outputs: |
              dist/github-snake.svg
              dist/github-snake-dark.svg?palette=github-dark
        - uses: crazy-max/ghaction-github-pages@v4
          with:
            target_branch: output
            build_dir: dist
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
-->

## Contato

<!-- troque "#" pelos seus links reais -->
<p align="center">
<a href="#"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="#"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" width="100%"/>
</div>
