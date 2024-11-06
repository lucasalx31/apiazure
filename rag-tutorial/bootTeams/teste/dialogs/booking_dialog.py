import requests
from botbuilder.dialogs import WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.core import MessageFactory
from botbuilder.schema import InputHints
from .cancel_and_help_dialog import CancelAndHelpDialog

class BookingDialog(CancelAndHelpDialog):
    def __init__(self, dialog_id: str = None):
        super(BookingDialog, self).__init__(dialog_id or BookingDialog.__name__)

        # Define o diálogo com um único passo para chamar a API
        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [self.api_call_step],
            )
        )
        self.initial_dialog_id = WaterfallDialog.__name__

    async def api_call_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """Passo único para capturar a entrada do usuário e obter uma resposta da API."""
        user_input = step_context.context.activity.text  # Entrada do usuário no chat
        user_id = step_context.context.activity.from_property.id
        # Chama a API com a entrada do usuário
        api_response = self.call_chat_api(user_input,user_id)
        
        # Envia a resposta da API para o usuário
        message = MessageFactory.text(api_response, api_response, InputHints.ignoring_input)
        await step_context.context.send_activity(message)

        # Substitui o diálogo para continuar escutando as próximas entradas do usuário
        #return await step_context.replace_dialog(self.initial_dialog_id)

    def call_chat_api(self, user_input, user_id):
        """Função para fazer a chamada à API Flask e obter uma resposta baseada na entrada do usuário."""
        try:
            response = requests.post(
                "http://localhost:5000/chat",  # URL do servidor Flask
                json={"input": user_input, "user_id": user_id}
            )
            while response.status_code != 200:
                continue
            if response.status_code == 200:
                return response.json().get("reply", "Desculpe, não entendi sua solicitação.")
            return "Desculpe, houve um problema ao conectar-se com o servidor."
        except Exception as e:
            return f"Erro ao chamar a API: {e}"
