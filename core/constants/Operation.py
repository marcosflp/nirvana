class OperationStrategy:
    AVERAGE = 'AVERAGE'
    COUNT = "COUNT"
    MAX = 'MAX'
    MIN = "MIN"
    SUM = 'SUM'

    @property
    def available_strategies(self):
        return [self.AVERAGE, self.COUNT, self.MAX, self.MIN, self.SUM]
