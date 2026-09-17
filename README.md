<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=190&section=header&text=Fl%C3%A1vio%20Ara%C3%BAjo&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o%20%40%20UNICAP&descAlignY=58&descSize=16" width="100%"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=17&pause=1600&color=8FD3FF&center=true&vCenter=true&width=560&lines=Backend+%2B+full-stack;Estruturas+de+dados;Java+%C2%B7+Python+%C2%B7+C" />
  <img alt="Áreas de foco" src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=17&pause=1600&color=2C5364&center=true&vCenter=true&width=560&lines=Backend+%2B+full-stack;Estruturas+de+dados;Java+%C2%B7+Python+%C2%B7+C" />
</picture>

<br/><br/>

![Status](https://img.shields.io/badge/status-aberto_a_oportunidades_de_est%C3%A1gio-2ea44f?style=for-the-badge)

</div>

## Sobre

<table>
<tr><td><b>Quem sou</b></td><td>Estudante de Ciência da Computação, com formação técnica anterior em Redes de Computadores.</td></tr>
<tr><td><b>O que estudo</b></td><td>Ciência da Computação — UNICAP (programa C3), depois de migrar de Sistemas de Informação.</td></tr>
<tr><td><b>Interesses</b></td><td>Desenvolvimento full-stack, estruturas de dados e infraestrutura.</td></tr>
<tr><td><b>Construindo</b></td><td>Aplicações práticas que consolidam esses conceitos — como o Lumière Cinema, abaixo.</td></tr>
</table>

## Tech Stack

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=java,py,c,html,css,js&theme=dark" />
  <img alt="Linguagens" src="https://skillicons.dev/icons?i=java,py,c,html,css,js&theme=light" />
</picture>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=react,vite,spring&theme=dark" />
  <img alt="Frameworks e bibliotecas" src="https://skillicons.dev/icons?i=react,vite,spring&theme=light" />
</picture>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=git,github,maven,vercel&theme=dark" />
  <img alt="Ferramentas e plataformas" src="https://skillicons.dev/icons?i=git,github,maven,vercel&theme=light" />
</picture>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=figma&theme=dark" />
  <img alt="Design" src="https://skillicons.dev/icons?i=figma&theme=light" />
</picture>
</p>

## Projeto em destaque — Lumière Cinema

Sistema de venda de ingressos de cinema, desenvolvido em equipe para a disciplina de Programação Orientada a Objetos da UNICAP, com fluxos distintos para usuário, crítico e administrador.

<p align="center">
<a href="https://github.com/Furubioo/Sistema-de-Cinema-JAVA-">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo=Sistema-de-Cinema-JAVA-&theme=tokyonight&hide_border=true" />
    <img alt="Repositório Sistema-de-Cinema-JAVA-" src="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo=Sistema-de-Cinema-JAVA-&theme=default&hide_border=true" />
  </picture>
</a>
</p>

**Funcionalidades**
- Preços diferenciados por tipo de usuário (comum, crítico, estudante)
- Aplicação de cupons promocionais
- Sugestão de assentos e pôsteres de filme via API do TMDB
- Persistência em arquivo na versão terminal, evoluindo para um banco H2 na versão web

**Conceitos aplicados**
- Orientação a objetos: herança, sobrescrita e sobrecarga de métodos
- Padrões de projeto MVC e Strategy (este último para as regras de preço)
- Tratamento de exceções, incluindo uma exceção personalizada na base de código

```mermaid
flowchart LR
    subgraph T["Versão terminal — Java"]
        direction LR
        TV["View"] --> TC["Controller"]
        TC --> TM["Model + Strategy"]
        TM --> TP[("Arquivo")]
    end
    subgraph W["Versão web"]
        direction LR
        WF["React + Vite"] --> WB["Spring Boot"]
        WB --> WD[("H2")]
    end
    T -->|evoluiu para| W
```

**Evolução**
O projeto começou como uma aplicação em terminal, em Java. Depois foi estendido para uma aplicação web (front-end em React + Vite, back-end em Spring Boot, H2 como banco de dados) — o código dessa etapa foi gerado com apoio de ferramentas de IA, e minha contribuição foi a configuração do ambiente, a integração entre front-end e back-end, e a resolução de bugs.

## Em exploração agora

- Estruturas de dados não lineares — árvores e algoritmos de ordenação
- Projeto e modelagem de banco de dados
- Análise e projeto de software

## Projetos

<p align="center">
<a href="https://side-da-ong-partilhar.vercel.app">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo=SiteOngPartilhar&theme=tokyonight&hide_border=true" />
    <img alt="Repositório SiteOngPartilhar" src="https://github-readme-stats.vercel.app/api/pin/?username=Furubioo&repo=SiteOngPartilhar&theme=default&hide_border=true" />
  </picture>
</a>
</p>

<p align="center"><b>Site institucional — ONG Partilhar</b> · HTML, CSS e JavaScript, publicado na Vercel</p>

## Formação

<table>
<tr><td><b>Ciência da Computação</b></td><td>UNICAP — Programa C3 · desde fev/2025 · 4º período em curso</td></tr>
<tr><td><b>Técnico em Redes de Computadores</b></td><td>ETE Pastor Isaac Martins Rodrigues · 2020–2022</td></tr>
</table>

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

## Contato

<p align="center">
<a href="#"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="#"><img src="https://img.shields.io/badge/Email-2C5364?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" width="100%"/>
</div>
