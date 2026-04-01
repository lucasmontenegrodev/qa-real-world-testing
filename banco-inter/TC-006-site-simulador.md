# TC-006 - Banco Inter: Site Institucional e Simulador

| Campo | Valor |
|---|---|
| ID | TC-006 |
| Site | Banco Inter — bancointer.com.br |
| Funcionalidade | Site Institucional e Simulador de Produtos |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao pelo menu principal | 1. Acessar bancointer.com.br. 2. Navegar pelos itens do menu. | Todos os links funcionando e paginas carregando corretamente | Navegacao fluida sem links quebrados | PASS |
| 2 | Simulador de credito | 1. Acessar a pagina de emprestimo pessoal. 2. Usar o simulador de valor e prazo. | Simulacao atualizada ao mover os sliders de valor e prazo | Simulacao atualizada corretamente em tempo real | PASS |
| 3 | Responsividade no desktop | 1. Redimensionar a janela do browser para 1024px. | Layout adaptado sem elementos sobrepostos | Layout adaptado corretamente | PASS |
| 4 | Velocidade de carregamento | 1. Abrir DevTools > Network. 2. Recarregar a pagina. 3. Verificar tempo de carregamento. | Pagina carregando em menos de 3 segundos | Pagina carregada em aproximadamente 1.8s | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Site institucional bem otimizado. Simulador de credito responsivo e intuitivo. Performance dentro do esperado para um site financeiro.