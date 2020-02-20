class PilhaNot:
    def __init__(self):
        self._pilha = []
    def __len__(self):
        return len(self._pilha)
    def is_empty(self):
        return len(self._pilha) == 0
    def push(self, elem):
        self._pilha.append(elem)
    def top(self):
        if self.is_empty( ):             
            return None       
        return self._pilha[-1] 
    def pop(self):         
        if self.is_empty( ):            
            return None         
        return self._pilha.pop( ) 
    def is_number (self, value):
            try:
                float(value)
                return True
            except ValueError:
                return False
