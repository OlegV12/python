
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        print(f"Масса асфальта, необходимого для покрытия дорожного полотна: {_length * _width * 25 * 5 / 1000} тонн")


a = Road(400, 30)

