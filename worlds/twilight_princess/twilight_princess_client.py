"""Client for the Twilight Princess Archipelago Randomizer"""
import asyncio
from CommonClient import (
    CommonContext,
    ClientCommandProcessor,
    get_base_parser,
    gui_enabled,
    logger,
    server_loop,
)
import Utils
from Utils import Version


class TPCommandProcessor(ClientCommandProcessor):
    """Twilight Princess Client Command Processor"""


class TPCommonContext(CommonContext):
    """Twilight Princess Client Common Context Class"""

    command_processor = TPCommandProcessor
    game = "Twilight Princess"
    items_handling = 0b011

    def __init__(self, server_address, password) -> None:
        super().__init__(server_address, password)
        self.auth = None
        self.client = None
        self.locations_checked = []
        self.items_received = []
        self.is_connected = False
        self.send_index = 0
        self.server_version: Version = Version(4, 2, 0)
        self.finished_game = False

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        if not self.auth:
            logger.info("Enter slot name: ")
            self.auth = await self.console_input()

        await self.send_connect()

    def run_gui(self) -> None:
        from kvui import GameManager

        class TPManager(GameManager):
            """Twilight Princess Client Game Manager"""

            logging_pairs: list(tuple) = [("Client", "Archipelago")]
            base_title = "Archipelago Twilight Princess Client"

        self.ui = TPManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
