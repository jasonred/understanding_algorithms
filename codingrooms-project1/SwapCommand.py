from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, source, index1, index2):
        # Type your code here.
        super().__init__()
        self.source_list = source
        self.index1 = index1
        self.index2 = index2

    def execute(self):
        # Type your code here.
        # Swap the items back to undo the original swap
        value1 = self.source_list[self.index1]
        value2 = self.source_list[self.index2]
        self.source_list[self.index1] = value2
        self.source_list[self.index2] = value1
