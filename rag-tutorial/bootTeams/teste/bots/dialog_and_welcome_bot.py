# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os.path

from typing import List
from botbuilder.core import MessageFactory, TurnContext
from botbuilder.schema import Attachment, ChannelAccount

from helpers import DialogHelper
from .dialog_bot import DialogBot


class DialogAndWelcomeBot(DialogBot):

    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                # Envia mensagem de boas-vindas
                welcome_card = self.create_adaptive_card_attachment()
                response = MessageFactory.attachment(welcome_card)
                await turn_context.send_activity(response)
                
                # Inicia o diálogo para que o bot responda automaticamente
                await DialogBot.run_dialog(
                    self.dialog,
                    turn_context,
                    self.conversation_state.create_property("DialogState"),
                )

    # Load attachment from file.
    def create_adaptive_card_attachment(self):
        relative_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(relative_path, "../cards/welcomeCard.json")
        with open(path) as card_file:
            card = json.load(card_file)

        return Attachment(
            content_type="application/vnd.microsoft.card.adaptive", content=card
        )
