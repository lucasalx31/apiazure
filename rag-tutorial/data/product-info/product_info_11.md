# Bloqueio pelo Robô

1. Conferir na planilha SQL, aba **Bloqueio Rescisão**, filtrar pelo dia de bloqueio, se todas as cartas estão assinadas. As que não estiverem, solicitar para as filiais via e-mail.
   - **Caminho:** `G:\RH\RESCISÕES\REGIÕES\RCT - EQUIPE RH`  
   - **Base SQL:** **Automatização RCT - USAR ESTÁ**

2. Após todas estarem com “S”, agendar o robô para que inicie o processo de bloqueio da:
   - **Comissão Farmácia**
   - **Gympass**
   - **Convênio Farmácia**
   - **Quimidrol**
   - **Plano Odontológico**
   - **Unimed**
   - **Santander/Itaú/Bradesco**

   **Caminho:** **Personalizadas > Agendamentos Robô**

3. Após dividir entre a equipe as rescisões para cálculo e avisar a equipe de inovação sobre o agendamento para dar sequência. Quando terminar, vai notificar por e-mail com planilhas em anexo, enviar para a Quimidrol e Unimed realizar o cancelamento em sistema.

   - **E-mails:**
     - **Quimidrol:** `filialjoinville@quimidrol.com.br`
     - **Unimed:** 
       - `exclusaopj@unimedjoinville.com.br`
       - `exclusaopj@unimedjoinville.com.br`
       - `Sabrina Felix <exclusaopj@joinville.unimedsc.com.br>`

4. **Folha mês anterior**
   - Salvar na pasta a folha do mês anterior ao cálculo.
     - **Caminho:** `Cálculo > Ficha Financeira > Cadastro`

5. **Vales**
   - **Caminho:** `Cálculo > Lançamento > Vales`
   - Salvar a tela de vales lançados na pasta.

6. Tirar uma relação do relatório 100 das matrículas que estão realizando o bloqueio no caminho abaixo, e informar a competência que deseja.
   - **Caminho:** `Cálculo > Lançamento > Vales > Listar > 100`
   - Este print deverá ser salvo na pasta de rescisão do colaborador como “Saldo em Aberto”, e neste relatório que irá sair se o colaborador possui os empréstimos do Bradesco, Santander ou Itaú.

7. **Santander**
   - Entrar no site: [Santander](https://www.creditoconsignadosantander.com.br/default.aspx) com o login e senha abaixo.
     - **Login:** `efe9442`
     - **Senha:** `29291981`
   - Clicar em “consulta saldo devedor” e informar o nº do CPF do colaborador(a) sem os pontos. Este print com o valor deve ser salvo na pasta de rescisão como `278 - Emp. Santander`.

8. **Bradesco**
   - Os colaboradores que tiverem empréstimo do Bradesco, deverão enviar um e-mail para `relatorio.descontoemfolha@bradesco.com.br` constando nome e CPF. Após receber o retorno com o saldo devedor, deverá salvar na pasta de rescisão do colaborador como `248 - Emp. Bradesco`.
   - Quando for calcular a rescisão, precisa verificar o valor que irá descontar os 35% e solicitar o boleto para pagamento com data do vencimento conforme prazo do contas a pagar.
     - **Caminho:** `G:\RH\RESCISÕES\REGIÕES\Diversos_RCT`
     - **Aut Pgto Consignado CEF - BRADESCO - SANTANDER**

9. **Itaú**
   - Os colaboradores que tiverem empréstimo do Itaú, deverão enviar um e-mail para `dayane.melo@clamed.com.br` solicitando o saldo devedor, informando matrícula e nome completo. Após retorno, deve ser salvo na pasta como `289 - Emp. Itaú`.

10. **Unimed**
    - Acessar o site: [Unimed](https://sw.joinville.unimedsc.com.br/empresa/) e informar o usuário de acesso:
      - **SC:** `274795 - 01` 
      - **Senha:** `29291981`
      - **Demais localidades:** `274796 – 01` 
      - **Senha:** `29291981`
    - Clicar em **Movimentação** (exclusão de beneficiários) > **Relatório** – **Usuários ativos** (ordenados por nome).
    - Clicar em **Consulta participação ainda não faturado** (para fins rescisórios) > **Localizar beneficiário**.
    - Pesquisar pela matrícula do colaborador(a), conferir nome e se está como “Titular”. Se tiver, pode clicar em cima do nome para abrir a tela pra bloqueio. Após receber o relatório, salvar na pasta como `746 - Unimed Total RCT`.
    - Caso o colaborador não tiver Unimed, dar print da pesquisa e salvar na pasta as duas telas: `Unimed 4795` e `4796`.

11. Preencher a planilha para envio de exclusão:
    - **Caminho:** `G:\RH\RESCISÕES\REGIÕES\Formulários Unimed para enviar`
    
    **Observação:** Os casos que não tiverem, deverão ser verificados com muita atenção. Pois após 180 dias, o colaborador(a) já tem direito à adesão do plano. Caso já tenha passado este prazo, verificar na ficha complementar se não tem o documento de renúncia do plano salvo. No último caso, questionar o pessoal do plano se o colaborador(a) tem plano ativo.

12. **Ponto**
    - Conferir se a filial fechou o ponto do colaborador(a). Se o ponto já estiver OK, precisará integrar no ronda e emitir o cartão ponto para salvar na pasta de rescisão como `36 – Cartão Ponto`.
    - Caso o ponto tenha divergência, enviar um e-mail para a filial conforme abaixo solicitando a correção do mesmo ou ligar:
      ```
      Boa tarde Sr. Gerente,
      Por gentileza, ajustar o ponto da colaboradora (nome da colaboradora), verificamos que constam várias divergências. 
      Lembrando que é de extrema importância que o ponto seja corrigido no dia do desligamento do colaborador. 
      Do contrário, prejudica o colaborador, causa retrabalho e temos que fazer uma retificação de rescisão para o E-social.
      ```

## Bloqueio manual
### Comissão Farmácia
1. Abrir o programa da comissão **Recursos Humanos**, colocar login e senha.
2. Ir em **relatórios** – **Vendas por vendedor**.
   - O período é sempre do dia 26 do mês anterior até o dia que está bloqueando.
   - Colocar a filial (o nome e dar ENTER) e depois o vendedor (nome e dar ENTER que ele já traz a matrícula do colaborador).
   - Clicar no ícone abaixo da manutenção conforme grifado no print acima.

3. Esse print com o valor deve ser salvo na pasta de rescisão como `320 – Comissão`. Se não tiver comissão, deve salvar o print do mesmo jeito.
4. Lembrando que quando for do Desenvolvimento, não precisa inserir filial e nome, apenas deverá clicar em “gerar arquivo”. Os avisos que aparecer no final da importação pode clicar em “OK”.
5. Os arquivos ficam salvos em `C:\Sistemas\RH\Arquivos`, abrir Excel “vendas vendedores” e filtrar pela matrícula do colaborador. Esse print com o valor deve ser salvo na pasta de rescisão como `320 – Comissão`.
6. Quando o colaborador(a) for farmacêutico, é preciso salvar também o valor das aplicações de testes COVID. Abrir o arquivo do PowerBI salvo na sua pasta pessoal.
   - Selecionar o colaborador(a) que está realizando o bloqueio, conferir se a matrícula é a mesma e o mês da competência. Após clicar em “atualizar” para trazer o valor atualizado.
   - Esse print com o valor deve ser salvo na pasta de rescisão como `320 – Comissão Teste COVID`.

### Gympass
1. Acessar o [Gympass](https://gympass.com/pt-br/companies/) clicar “entrar” e informar o login e senha.
   - **Usuário:** `kiane2102@gmail.com`
   - **Senha:** `Bastos2402`
2. Ir em **Para Empresas**, em **colaboradores**, informar a matrícula e clicar na flecha e em remover. Após salvar o print na pasta como `862 – Gympass`.

### Conf. Folha do mês anterior (Gympass)
- Neste último processo deverá ser salva a última folha fechada do colaborador, para ver o valor descontado de gympass ou até mesmo para verificar eventos para descontar na rescisão do colaborador(a).
- Salvar o print na pasta de rescisão do colaborador(a) como `Desc. Plano Gympass folha mês/ano`.

### Convênio Farmácia
1. Acessar o link: [Convênios](https://convenios.clamed.com.br/login/index.php) e colocar seu login e senha.
2. Na busca, coloca a matrícula, se certifica que está flegado os ativos e depois vai em buscar. Após, clica no ícone para retirar o extrato e salva na pasta como `Convênio Farmácia`.

### Quimidrol
1. Acessar o [Quimidrol](https://www.quimidrol.com.br/) com o login e senha.
   - **Login:** `jeferson`
   - **Senha:** `Panda101`
2. Conferir o nome da colaboradora na lista de bloqueio.

### Plano Odontológico
1. Acessar o site: [Odontológico](https://www.unimed.com.br/) com o login e senha.
   - **Login:** `exclusao`
   - **Senha:** `456789`
2. Ir no menu e clicar em **Grupo** > **Colaboradores** > **Gestão de colaboradores** > **Ações** > **Excluir**. 
3. Clicar em “salvar” e emitir o relatório.

### Unimed
1. Acessar o site: [Unimed](https://sw.joinville.unimedsc.com.br/empresa/) e informar o usuário de acesso:
   - **SC:** `274795 - 01` 
   - **Senha:** `29291981`
   - **Demais localidades:** `274796 – 01` 
   - **Senha:** `29291981`
2. Clicar em **Movimentação** (exclusão de beneficiários) > **Relatório** – **Usuários ativos** (ordenados por nome).
3. Clicar em **Consulta participação ainda não faturado** (para fins rescisórios) > **Localizar beneficiário**.
4. Pesquisar pela matrícula do colaborador(a), conferir nome e se está como “Titular”. Se tiver, pode clicar em cima do nome para abrir a tela pra bloqueio. Após receber o relatório, salvar na pasta como `746 - Unimed Total RCT`.
5. Caso o colaborador não tiver Unimed, dar print da pesquisa e salvar na pasta as duas telas: `Unimed 4795` e `4796`.

### Finalização
- Repetir o mesmo processo para todos os colaboradores que estão sendo bloqueados. Quando finalizar todos os processos, conferir se todos os arquivos e relatórios estão salvos na pasta de rescisão do colaborador(a) e verificar se as exclusões foram solicitadas para cada plano.
