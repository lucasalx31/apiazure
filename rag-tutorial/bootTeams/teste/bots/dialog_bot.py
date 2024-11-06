# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, ConversationState, UserState, TurnContext
from botbuilder.dialogs import Dialog

from helpers import DialogHelper

class DialogBot(ActivityHandler):
    def __init__(
        self,
        conversation_state: ConversationState,
        user_state: UserState,
        dialog: Dialog,
    ):
        if conversation_state is None:
            raise Exception("[DialogBot]: Missing parameter. conversation_state is required")
        if user_state is None:
            raise Exception("[DialogBot]: Missing parameter. user_state is required")
        if dialog is None:
            raise Exception("[DialogBot]: Missing parameter. dialog is required")

        self.conversation_state = conversation_state
        self.user_state = user_state
        self.dialog = dialog

        # Propriedades de estado para controlar a solicitação e validação da matrícula
        self.matricula_requested = conversation_state.create_property("matricula_requested")
        self.matricula_validated = user_state.create_property("matricula_validated")

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        # Salva quaisquer mudanças de estado que possam ter ocorrido durante a turn.
        await self.conversation_state.save_changes(turn_context, False)
        await self.user_state.save_changes(turn_context, False)

    async def on_message_activity(self, turn_context: TurnContext):
        # Checa se a matrícula já foi solicitada ou validada
        matricula_requested = await self.matricula_requested.get(turn_context, False)
        matricula_validated = await self.matricula_validated.get(turn_context, False)

        # Se a matrícula já foi validada
        if matricula_validated:
            # Obtendo o accessor do estado do diálogo
            dialog_state_accessor = self.conversation_state.create_property("DialogState")
            await DialogHelper.run_dialog(
                self.dialog,
                turn_context,
                dialog_state_accessor  # Passando o accessor
            )

        # Se a matrícula ainda não foi solicitada
        elif not matricula_requested:
            await turn_context.send_activity("Por favor, informe sua matrícula.")
            await self.matricula_requested.set(turn_context, True)

        # Se a matrícula foi solicitada mas ainda não foi validada
        elif matricula_requested and not matricula_validated:
            user_input = turn_context.activity.text
            if self.validate_matricula(user_input):
                await turn_context.send_activity("Matrícula validada com sucesso!")
                await self.matricula_validated.set(turn_context, True)
                await self.continue_dialog(turn_context)
            else:
                await turn_context.send_activity("Matrícula inválida. Tente novamente.")

       
        

    def validate_matricula(self, matricula):
        import cx_Oracle

        # Parâmetros de conexão
        oracle_dsn = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.0.3.2)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=vetorh)))"
        oracle_user = "VETORH_CONSULTA"
        oracle_password = "Drog638#"

        try:
            # Estabelecendo a conexão com o banco de dados
            with cx_Oracle.connect(user=oracle_user, password=oracle_password, dsn=oracle_dsn) as conn:
                # Usando o cursor dentro do contexto da conexão
                with conn.cursor() as cursor:
                    # Executando o comando SQL para buscar matrículas
                    comando = f"SELECT numcad FROM r034fun WHERE sitafa <> 7 and numcad = {matricula}"
                    cursor.execute(comando)

                    # Obtendo todos os resultados
                    results = cursor.fetchall()
                    # Extraindo matrículas em uma lista
                    numcad = [tupla[0] for tupla in results]
                    print(numcad)
                    if numcad:
                        numcad = str(numcad[0])
                    # Verificando se a matrícula fornecida está na lista
                    return matricula in numcad

        except cx_Oracle.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False  # Retorna False em caso de erro


    async def continue_dialog(self, turn_context: TurnContext):
        await turn_context.send_activity("Como posso ajudar?")
