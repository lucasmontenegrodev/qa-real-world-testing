# TC-004 - Instagram: Acessibilidade e Responsividade no Desktop

| Campo | Valor |
|---|---|
| ID | TC-004 |
| Site | Instagram — instagram.com |
| Funcionalidade | Layout Desktop e Acessibilidade |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (3/4 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Layout geral no desktop | 1. Acessar instagram.com no browser desktop. | Feed centralizado, sidebar de navegacao visivel, sem elementos cortados | Layout correto | PASS |
| 2 | Navegacao por teclado | 1. Usar Tab para navegar pelos elementos da pagina. | Foco visivelmente indicado em cada elemento navegavel | Foco visivel na maioria dos elementos | PASS |
| 3 | Zoom de 150% | 1. Aplicar zoom de 150% no browser. | Layout adaptado sem sobreposicao de elementos | Layout adaptado corretamente a 150% | PASS |
| 4 | Alt text das imagens | 1. Inspecionar imagens do feed no DevTools. 2. Verificar atributo alt. | Atributo alt descritivo em todas as imagens | Imagens do feed tem alt text generico "Foto de [usuario]" sem descricao do conteudo — prejudica usuarios de leitores de tela | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 3 | 1 | 75% |

---

## Observacoes

O alt text generico e uma limitacao conhecida de plataformas de conteudo gerado pelo usuario, mas ainda assim representa uma barreira de acessibilidade real para usuarios com deficiencia visual.