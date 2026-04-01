# TC-008 - YouTube: Acessibilidade e Navegacao por Teclado

| Campo | Valor |
|---|---|
| ID | TC-008 |
| Site | YouTube — youtube.com |
| Funcionalidade | Acessibilidade e Navegacao |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (3/4 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao por teclado na pagina inicial | 1. Acessar youtube.com. 2. Usar Tab para navegar pelos elementos. | Foco visivelmente indicado em todos os elementos interativos | Foco visivel na maioria dos elementos | PASS |
| 2 | Atalhos de teclado no player | 1. Com video aberto, usar K (pause), J (voltar 10s), L (avancar 10s), M (mute). | Todos os atalhos funcionando corretamente | Atalhos funcionando corretamente | PASS |
| 3 | Contraste de texto | 1. Verificar contraste do texto cinza sobre fundo branco nos titulos secundarios. | Contraste minimo de 4.5:1 conforme WCAG AA | Texto cinza claro sobre fundo branco com contraste insuficiente nos metadados dos videos (canal e visualizacoes) | FAIL |
| 4 | Zoom de 200% | 1. Aplicar zoom de 200% na pagina inicial. | Layout adaptado sem perda de conteudo ou sobreposicao | Layout adaptado corretamente a 200% | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 3 | 1 | 75% |

---

## Observacoes

O contraste insuficiente e um problema de acessibilidade real que afeta usuarios com baixa visao. Os metadados dos videos (nome do canal, numero de visualizacoes) sao exibidos em cinza claro que nao atinge o contraste minimo recomendado pela WCAG 2.1 nivel AA.