### Rotina de Registro de Envio de Transferências, Malotes e Volumes

**OBJETIVO**  
Documento eletrônico para registro de envio de transferências, malotes e/ou volumes.

---

**ÁREA RELACIONADA**  
Estoque Central - Expedição.

---

**PRAZO**  
O sistema está preparado para realizar folha de despacho para o dia atual e para o próximo dia útil.

---

**RESPONSÁVEL**  
Gerente.

---

**DELEGÁVEL**  
Delegável ao farmacêutico, atendente e estoquista.

---

**PERIODICIDADE**  
Sempre que houver necessidade de envio de transferências, malotes e/ou volumes.

---

**PROCEDIMENTO**  

Para utilização da folha de despacho, é de suma importância que todo o processo de transferências, malotes e volumes, que é realizado frequentemente, tenha sido concluído. A data do documento deve ser a mesma do dia em que o motorista efetuar a coleta; o documento não pode ter data anterior. O sistema está preparado para realizar folha de despacho para o dia atual e para o próximo dia útil.

A tela abaixo será responsável por executar todo o processo de despacho. Explicamos os campos a seguir:

1. **Acessar a intranet**:  
   Clique no menu lateral esquerdo “Malotes”, entre com o usuário e senha, e clique em folha de despacho.

2. **DATA**:  
   Escolha a data correspondente ao dia da coleta. Estarão disponíveis o dia atual e o próximo dia útil.

3. **DESTINO**:  
   Selecionando o destino, todas as regras do sistema são aplicadas. O campo conterá pelo menos 3 locais de destino, podendo chegar a 5 dependendo da região.  
   - **DIV TRANSLOG**: Encarregada de realizar as transferências de “mercadorias” entre as filiais. Quando selecionada, o sistema traz somente os registros destinados a filiais operando com a mesma base da transportadora selecionada.  
   - **ROTA XX**: Para lojas atendidas por transporte próprio. Registre transferências cujo destino seja as filiais do mesmo roteiro de entrega.  
   - **ESTOQUE CENTRAL**: Ao selecionar, o sistema trará todos os registros pendentes na filial, independente do destino, para que possam ser inseridos no despacho e encaminhados à Logística.

4. **DANFE**:  
   Campo utilizado para filiais que precisam gerar NF de simples remessa para o transporte. Coloque nesse campo o número da NF gerada, que sairá impressa na finalização do despacho.

5. **LEITOR ÓPTICO**:  
   Insira no despacho qualquer registro passando o código de barras da etiqueta no leitor. Observação: haverá validação para impedir a inserção de registros que não estejam de acordo com o destino selecionado.

6. **Lupa**:  
   Este botão redireciona para uma nova página, onde será possível visualizar a impressão do despacho e consultar itens já inseridos que ainda não foram finalizados.

7. **Tabela Itens de despacho**:  
   Exibe todos os registros inseridos pelo leitor óptico, permitindo a inserção da quantidade de bacias enviadas (quando selecionado o Estoque Central) e a exclusão de registros inseridos de forma irregular (desde que o despacho não tenha sido salvo/impresso).  
   Observação: A coluna **XML NF** indicará se há uma nota para a transferência, permitindo o envio de um e-mail à transportadora com uma cópia em XML da nota (apenas quando solicitado pela Logística).

8. **IMPRESSORA**:  
   Finaliza o despacho aberto. O sistema gerará uma folha de despacho para impressão, que deve ser recortada e utilizada conforme necessário:  
   - Parte inferior direita: colocada no acrílico das bacias (somente para envio ao CD – Estoque Central).  
   - Parte inferior esquerda: para que o responsável pela coleta assine o material e o recibo seja arquivado na filial.  
   - Parte superior: entregue ao motorista que está efetuando a coleta.

Caso o despacho já tenha sido fechado e ocorram solicitações de transferência ou envio de volumes/malotes, deve-se abrir um novo despacho para registrar essas solicitações.  
Os canhotos devem ser guardados por no mínimo 3 meses.

9. **ALERTA**:  
   Ao selecionar a opção de Estoque Central e registrar um item com transportadora cadastrada para a filial destino, o sistema exibirá um “ALERTA”. Para continuar a operação, basta clicar em OK para permitir a inserção do registro na folha de despacho.

---

**Pesquisa de Despachos Finalizados**  
Tem como objetivo exibir todos os despachos finalizados para um destino e uma data específica.

- **Data**: Campo para selecionar a data da pesquisa dos despachos finalizados.  
- **Destino**: Selecionar o destino para o qual foi realizado o despacho: ESTOQUE CENTRAL ou DIV TRANSLOG.
