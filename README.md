<!--
  Antes de publicar no repositório Furubioo/Furubioo, personalize:
  1. Troque {REPO-LUMIERE} pelo link real do repositório do Lumière Cinema.
  2. Adicione seus links de contato (LinkedIn, e-mail etc.) onde quiser — não coloquei
     nenhum porque não tenho certeza de qual você quer deixar público.
  3. A seção "🐍 Minhas contribuições" (a cobrinha) só aparece depois de um pequeno
     setup via GitHub Actions — o passo a passo está comentado logo abaixo dela.
  4. Cores, tema e emojis são só ponto de partida — troque à vontade.
-->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6a11cb,100:2575fc&height=200&section=header&text=Fl%C3%A1vio%20Ara%C3%BAjo&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Estudante%20de%20Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o%20%40%20UNICAP&descAlignY=55&descSize=18" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1200&color=2575FC&center=true&vCenter=true&width=600&lines=Java+%C2%B7+Python+%C2%B7+C;Formado+em+T%C3%A9cnico+em+Redes+de+Computadores;Sempre+testando+algo+novo+no+PC+%F0%9F%94%A7)](https://github.com/Furubioo)

</div>

## 👋 Sobre mim

- 🎓 Cursando o 4º período de **Ciência da Computação** na UNICAP (programa C3)
- 🌐 Antes da faculdade, me formei **Técnico em Redes de Computadores**, com TCC sobre especificação de infraestrutura de rede
- 🔁 Comecei em Sistemas de Informação antes de migrar pra Ciência da Computação
- 🇧🇷 Brasileiro, baseado no Brasil

## 🔭 Agora

- 🔭 Buscando uma oportunidade de **estágio em desenvolvimento de software**
- 🌱 Aprofundando estruturas de dados, banco de dados e projeto de software na faculdade
- 👯 Aberto a colaborar em projetos acadêmicos ou pessoais
- ⚡ Fun fact: já rastreei uma queda do Windows até um bug do driver `tcpip.sys` usando WinDbg — só por curiosidade de entender o motivo

## 🛠️ Tecnologias

**Linguagens**

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)

**Já usei em projetos**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)

**Redes & ferramentas**

![Cisco Packet Tracer](https://img.shields.io/badge/Cisco_Packet_Tracer-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## 🎬 Projeto em destaque — Lumière Cinema

Sistema de venda de ingressos de cinema, com fluxos para usuário, crítico e administrador.

- Começou como uma aplicação **em terminal, em Java**, aplicando os padrões de projeto **MVC e Strategy**, com herança, sobrescrita e sobrecarga de métodos.
- Depois virou uma **aplicação web** (front-end em React, back-end em Spring Boot, H2 como banco de dados) — o código dessa parte foi gerado com apoio de ferramentas de IA; fiquei responsável pela configuração do ambiente, integração entre front e back, e resolução de bugs (lógica de sugestão de assentos, filtro de cupons, carregamento de pôsteres via TMDB, entre outros).

<p align="center">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white"/>
</p>

📎 [Ver repositório](https://github.com/Furubioo/{REPO-LUMIERE})

## 📊 Estatísticas do GitHub

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Furubioo&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" height="165"/>
  <img src="https://streak-stats.demolab.com?user=Furubioo&theme=tokyonight&hide_border=true" alt="GitHub Streak" height="165"/>
</p>

## 🐍 Minhas contribuições

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Furubioo/Furubioo/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Furubioo/Furubioo/output/github-snake.svg" />
  <img alt="Animação da cobrinha comendo o gráfico de contribuições" src="https://raw.githubusercontent.com/Furubioo/Furubioo/output/github-snake.svg" width="100%"/>
</picture>

<!--
  Pra essa imagem aparecer, crie o arquivo .github/workflows/snake.yml
  no repositório Furubioo/Furubioo com este conteúdo. Ele roda uma vez por dia
  sozinho e gera as duas imagens acima automaticamente:

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

## ⚽ Fora do teclado

- Acompanho futebol
- Monto e otimizo meu próprio PC (driver, BIOS, GPU) por hobby
- Curioso por eletrônica e circuitos elétricos

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2575fc,100:6a11cb&height=100&section=footer" width="100%"/>

</div>
