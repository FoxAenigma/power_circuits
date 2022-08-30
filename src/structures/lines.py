class PILine:
    _distance: float
    _Zl: complex
    _Bc: complex
    
    _z: complex
    _y: complex

    def __init__(self, _distance, _Zl, _Bc):
        self._distance = _distance
        self._Zl = _Zl
        self._Bc = _Bc
        self.define_model()
        return

    def define_model(self):
       self._z = self._Zl*self._distance
       self._y = 1/self._z
       return


