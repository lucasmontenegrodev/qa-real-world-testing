# TC-005 - Banco Inter: Login e Acesso a Conta

| Campo | Valor |
|---|---|
| ID | TC-005 |
| Site | Banco Inter — bancointer.com.br |
| Funcionalidade | Login e Acesso |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar pagina de login | 1. Acessar bancointer.com.br. 2. Clicar em "Acessar conta". | Formulario de login exibido com campos de CPF e senha | Formulario exibido corretamente | PASS |
| 2 | Mascara de CPF no campo | 1. Digitar CPF sem formatacao: 12345678900. | Campo formata automaticamente: 123.456.789-00 | Mascara aplicada corretamente | PASS |
| 3 | Login com CPF invalido | 1. Digitar CPF com formato invalido. 2. Tentar avancar. | Mensagem de validacao informando CPF invalido | Validacao exibida corretamente | PASS |
| 4 | Seguranca — HTTPS e certificado | 1. Verificar barra de endereco do browser. | Conexao segura com HTTPS e certificado valido | HTTPS ativo com certificado valido | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Fluxo de acesso bem implementado. Mascara de CPF funciona corretamente e a validacao de formato e clara. Conexao segura verificada. Nenhum bug encontrado.