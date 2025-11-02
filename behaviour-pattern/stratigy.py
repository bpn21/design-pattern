# Without Stratigy Pattern

class ProcessInditicators:
    def __init__(self,indicator):
        self.indicator = indicator

    def process_inicator(self):
        if self.indicator == 'RSI':
            self.process_ris()
        if self.indicator == 'MACD':
            self.process_macd()
        if self.indocator == 'BOOLIGER':
            self.process_boolinger()

    
    def generated_output():
        pass    

    def process_rsi():
        pass

    def process_macd():
        pass

    def process_booinger():
        pass

# Using Stratigy Design Pattern

from abc import ABC, staticmethod

class Process(ABC):
    @staticmethod
    def process(self):
        raise NotImplementedError('Process method not implemented')


class ProcessRsi:
    def process(self):
        pass

class ProcessMacd:
    def process(self):
        pass

class ProcessBoolingerBand:
    def process(self):
        pass


class AssignStratigy:
    def __init__(self, data):
        self.data = data
        # self.stratigy = stratigy

    def set_stratigy(self, stratigy):
        self.stratigy = stratigy

    def process_stratigy(self):
        self.stratigy.process(self.data)

    
    
data = [100,130,150,200,130,150,120,122]

rsi = AssignStratigy(data)
rsi.set_stratigy(ProcessRsi)
rsi.process_stratigy()