# TC-007 - YouTube: Busca e Reproducao de Video

| Campo | Valor |
|---|---|
| ID | TC-007 |
| Site | YouTube — youtube.com |
| Funcionalidade | Busca e Reproducao |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (4/5 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por termo valido | 1. Acessar youtube.com. 2. Digitar "testes de software" na busca. 3. Pressionar Enter. | Videos relevantes exibidos com titulo, canal, visualizacoes e duracao | Resultados exibidos corretamente | PASS |
| 2 | Filtro por data de upload | 1. Na pagina de resultados, aplicar filtro "Este mes". | Apenas videos publicados no mes atual exibidos | Filtro aplicado corretamente | PASS |
| 3 | Reproducao do video | 1. Clicar em um video. 2. Verificar reproducao automatica. | Video inicia automaticamente com controles visiveis | Video reproduzido corretamente | PASS |
| 4 | Controles do player | 1. Testar pause, avancar 10s, volume e tela cheia. | Todos os controles funcionando corretamente | Controles funcionando corretamente | PASS |
| 5 | Legenda automatica | 1. Ativar legenda automatica em um video em portugues. | Legenda exibida com sincronizacao adequada com o audio | Legenda com atraso visivelmente perceptivel em relacao ao audio em varios momentos | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug Encontrado

**BUG-YT-001 — Legenda automatica com atraso em relacao ao audio**

| Campo | Valor |
|---|---|
| Severidade | Media |
| Prioridade | Media |
| Data | 20/03/2026 |

Passos para reproduzir:
1. Acessar youtube.com
2. Abrir qualquer video em portugues com mais de 5 minutos
3. Ativar legendas automaticas (CC)
4. Assistir e comparar o texto da legenda com o audio

Resultado Esperado: Legenda sincronizada com o audio com atraso maximo perceptivel de 1 segundo

Resultado Obtido: Legenda com atraso visivelmente superior a 1 segundo em varios trechos, especialmente em falas rapidas

Observacao: Este comportamento pode variar conforme o video e a qualidade do audio. O problema e mais pronunciado em videos com falas rapidas ou sotaque regional.