# TC-010 - Spotify: Navegacao e Performance

| Campo | Valor |
|---|---|
| ID | TC-010 |
| Site | Spotify Web Player — open.spotify.com |
| Funcionalidade | Navegacao e Performance |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao entre secoes | 1. Navegar entre Home, Buscar e Biblioteca usando o menu lateral. | Transicao fluida entre secoes sem recarregar a pagina | Navegacao fluida com transicoes rapidas | PASS |
| 2 | Carregamento de album | 1. Acessar a pagina de um album com mais de 15 faixas. | Todas as faixas carregadas com titulo, duracao e numero | Faixas carregadas corretamente | PASS |
| 3 | Performance no DevTools | 1. Abrir DevTools > Network. 2. Navegar pela aplicacao. | Requisicoes respondendo em menos de 500ms | Requisicoes respondendo em media em 180ms | PASS |
| 4 | Persistencia do player ao navegar | 1. Iniciar reproducao de musica. 2. Navegar para outra secao. | Reproducao continua sem interrupcao ao mudar de pagina | Player persistido corretamente durante a navegacao | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Performance excelente. Spotify Web Player e um exemplo de SPA (Single Page Application) bem implementada — navegacao sem reload e player persistente sao diferenciais tecnicos bem executados.