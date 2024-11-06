# Envio de Documentos

## 1. Divisão dos documentos:

### 1.1 Acessar o arquivo
Acessar o arquivo ‘Base SQL Automatização RCT’ em `G:\RH\RESCISÕES\REGIÕES\RCT - EQUIPE RH`, clicar na aba ‘Enviar documentos de Rescisão’ e atualizar o SQL (não precisa alterar a fonte):
- Depois de atualizado, clicar em salvar.

### 1.2 Classificar
Classificar por `Esc.Resp` e `Data Env.Doc`.

### 1.3 Filtrar na aba ‘Data Env.Doc (O)’
Selecionar o dia atual em que os documentos precisam ser enviados, na coluna `Esc.Resp (C)` filtrar a `RH Matriz` e na coluna `Cidade (D)` desmarcar `Joinville`:
- Os casos que ficarem na planilha, é necessário realizar o envio de documentos no Rubi.

### 1.4 Anexar os documentos
Acessar `Rubi/Colaboradores/Ficha Cadastral/Complementar`:
- Incluir a matrícula do colaborador e clicar na aba documentos. É necessário anexar os documentos de rescisão, na ficha complementar conforme o motivo de desligamento:

#### Motivos de desligamento e documentos:
- **02 – Iniciativa da empresa Sem Justa causa**
  - 29 – Comprovante Líquido
  - 30 – Comprovante FGTS
  - 31 – Guia FGTS
  - 32 – Extrato do FTGS
  - 35 – Seguro Desemprego
  - 36 – Cartão Ponto
- **04– Iniciativa do empregado Sem Justa causa**
  - 29 – Comprovante Líquido
  - 32 – Extrato do FTGS
  - 36 – Cartão Ponto
- **12 – Fim de Contrato Trabalho no Prazo**
  - 29 – Comprovante Líquido
  - 30 – Comprovante FGTS
  - 31 – Guia FGTS
  - 32 – Extrato do FTGS
  - 36 – Cartão Ponto
- **13 – Fim Antecipado Contrato – Iniciativa Empresa**
  - 29 – Comprovante Líquido
  - 32 – Extrato do FTGS
  - 36 – Cartão Ponto
- **14 – Fim Antecipado Contrato – Iniciativa Empregado**
  - 29 – Comprovante Líquido
  - 32 – Extrato do FTGS
  - 36 – Cartão Ponto

- Os documentos 29 - Comprovante Líquido e 30 - Comprovante FGTS estarão salvos na pasta: `G:\RH - Comprovantes RCT\2024\Mês Atual` - Selecionar a pasta com o dia anterior.
- O restante dos arquivos estará salvos na pasta do colaborador: `G:\RH\RESCISÕES\REGIÕES\2024`.
- O Gerente não tem o documento 36 – Cartão Ponto, pois não faz marcação.
- Para as RCTs zeradas, anexar o documento 29 – Comprovante Líquido em branco salvo em: `G:\RH\RESCISÕES\REGIÕES\RCT - EQUIPE RH`.

### 1.5 Acessar Rubi
Acessar `Rubi/Rescisões/Listar/Disparo Automático Documentos RCT para Filial`:
- Seguir os parâmetros abaixo e incluir no campo ‘Colaborador’ as matrículas que ficaram na planilha do SQL, separados por vírgula.
- Assim que finalizar a geração dos documentos, aparecerá um relatório indicando se o envio deu certo.
  - Se a escrita estiver em vermelho, significa que o documento enviado faz parte da cidade de JLLE.
  - Importante identificar se foi gerado 2 e-mails com as documentações, caso tenha sido gerado apenas um e-mail, é necessário verificar se todos os documentos estão anexados na ficha complementar.

### 1.6 Solicitar Carta de Desligamento
Acessar `Rubi/Rescisões/Solicitar Carta de Desligamento-RH` e alterar o campo `Documentos Enviados` para: ‘S’:
- Observar a data do campo ‘Último ASO’, para analisar se será necessário realizar o exame demissional. O prazo do exame é de 135 dias. Desta forma, se o exame estiver fora do prazo, verificar no e-mail do RCT se o robô fez o agendamento:
  - Se perceber que não foi agendado, comunicar a Camila Negri.

## 2. Divisão dos documentos para os escritórios

### 2.1 Acessar o arquivo
Acessar o arquivo ‘Base SQL Automatização RCT ‘no caminho `G:\RH\RESCISÕES\REGIÕES\RCT - EQUIPE RH`, clicar na aba ‘Enviar documentos de Rescisão’ e atualizar o SQL (não precisa alterar a fonte):
- Depois de atualizado, clicar em salvar.

### 2.2 Classificar
Classificar por `Esc.Resp` e `Data Env.Doc`.

### 2.3 Filtrar na aba ‘Data Env.Doc (O)’
Selecionar o dia atual em que os documentos precisam ser enviados e na coluna `Esc.Resp` filtrar os escritórios e o CD:
- Na planilha ficarão os casos que precisam ser enviados no dia e quem é o responsável pelo processo.

### 2.4 Enviar mensagem
Enviar a mensagem abaixo, via Teams no grupo Escritório – Rescisões, junto com a divisão de documentos (copiar da planilha e colar abaixo do texto):

## 3. Imprimir os casos de Jlle
Realizar o mesmo procedimento a partir do item 2.1 a 2.3, filtrando apenas os colaboradores da cidade de Jlle e após o envio dos documentos, conforme os itens 1.2  1.6, fazer a impressão para futura homologação agendada no momento da solicitação da carta de desligamento (descrito no campo ‘observação’).

## 4. Envio de Documentos via Contraktor

### 4.1 Fazer o envio de documentos
Conforme os itens 1.2 a 1.6, acessar o caminho `Rubi/Rescisões/Listar/Sequência de Documentos/008 - Documentos de Rescisão`:
- Seguir os parâmetros abaixo e clicar em ok:
- Salvar o arquivo em PDF na pasta do colaborador selecionado, como ‘38 – Documentos Rescisórios’.

### 4.2 Acessar o link
Acessar o link: [Contraktor Login](https://app.contraktor.com.br/auth/login) 
- Login: `ana.pinheiro@clamed.com.br`
- Senha: `Clamed@2024` (fazer um padrão?)

### 4.3 Importar Arquivo
Clicar em `Novo Contrato/importar Arquivo/Escolher a partir do computador/Prosseguir`:
- Na Aba ‘Geral’, manter o padrão abaixo e salvar:
- Seguir para a Aba ‘Anexos’ e anexar os demais documentos em ordem numérica, conforme o item 1.3 e deixar todos os campos flegados.
- Por fim, ir na aba ‘Participantes’ e selecionar o ex-colaborador e a analista responsável pela Ilha da Rescisão, para realizarem as assinaturas:
  - Deve-se considerar contratada para o ex-colaborador e Contratante para a analista responsável.
  - Flegar o campo – ‘Quero que as assinaturas sejam realizadas na ordem acima’.
  - Clicar em `Solicitar assinatura eletrônica`.
- Quando o documento for assinado por todos, chegará no e-mail um aviso da Contraktor, informando que o documento está disponível para download.

### 4.4 Realizar o download
Realizar o download do documento, salvar na ficha complementar no motivo `47 – Rescisão – Docs. Assinados` e disponibilizar no `Rubi/Rescisões/Listar/Disparo Automático Documentos RCT para Filial`:
- Após o envio dos documentos, será possível seguir o mesmo procedimento a partir do item 1.6.
