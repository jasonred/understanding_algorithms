from UndoCommand import UndoCommand

class RemoveLastCommand(UndoCommand):
    def __init__(self, source):
        super().__init__()
        self.source_list = source

    def execute(self):
        # Remove the last item from the source list
        self.source_list.pop()
        pass
