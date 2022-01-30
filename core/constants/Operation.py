class OperationStrategy:
    AVERAGE = 'AVERAGE'

    @property
    def available_strategies(self):
        return [self.AVERAGE]
