class Coord:
    def __init__(self, row, col):
        self.x = col
        self.y = row

d_coord_dict = {
    "U": Coord(-1, 0),
    "R": Coord(0, 1),
    "D": Coord(1, 0),
    "L": Coord(0, -1),
}

d_opposite_dict = {
    "U": "D",
    "R": "L",
    "D": "U",
    "L": "R",
}


class Square(Coord):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.__val = None
    
    @property
    def val(self):
        return self.__val
    
    @val.setter
    def val(self, val):
        self.__val = val

class Grid:
    def __init__(self, row_l, col_l):
        self.data = {}
        self.row_l = row_l
        self.col_l = col_l
        for row in range(row_l):
            row_dict = {}
            for col in range(col_l):
                row_dict[col] = Square(row, col)
            self.data[row] = row_dict
    
    def in_range(self, x, y):
        return 0 <= x < self.col_l and 0 <= y < self.row_l
    
    def get_square(self, x, y):
        return self.data[y][x]

    def set_square(self, x, y, val):
        self.data[y][x].val = val

    def generate_empty_grid(self):
        _data = {}
        for row in range(self.row_l):
            _row_dict = {}
            for col in range(self.col_l):
                _row_dict[col] = Square(row, col)
            _data[row] = _row_dict
        return _data

class Ball:
    def __init__(self, d):
        self.__d = d
    
    @property
    def d(self):
        return self.__d
    
    @d.setter
    def d(self, d):
        self.__d = d

class BallGrid(Grid):
    def __init__(self, n):
        self.n = n
        super().__init__(n, n);
    
    def init_ball(self, x, y, d):
        super().set_square(x, y, Ball(d))
    
    def cnt_ball(self):
        cnt = 0
        for y in self.data:
            for x in self.data[y]:
                if(self.data[y][x].val != None):
                    cnt += 1
        return cnt

    def _play(self):
        _data = self.generate_empty_grid()
        for y in range(self.n):
            for x in range(self.n):
                square = self.get_square(x, y)
                ball = square.val
                if not ball:
                    continue
                
                d_coord = d_coord_dict[ball.d]

                _x = x + d_coord.x
                _y = y + d_coord.y

                if not self.in_range(_x, _y):
                    ball.d = d_opposite_dict[ball.d]
                    _x = x
                    _y = y
                
                if _data[_y][_x].val:
                    if _data[_y][_x] == "crush":
                        continue
                    _data[_y][_x].val = "crush"
                    continue

                _data[_y][_x].val = ball
        
        for y in _data:
            for x in _data[y]:
                if _data[y][x].val == "crush":
                    _data[y][x].val = None
        
        self.data = _data

    def play(self):
        for _ in range(self.n * 2):
            self._play()

t = int(input())

s = ""

for _ in range(t):
    n, m = map(int, input().split())
    ball_grid = BallGrid(n)

    for _ in range(m):
        row, col, d = input().split()
        [x, y] = int(col) - 1, int(row) - 1
        ball_grid.init_ball(x, y, d)
    ball_grid.play()
    s += str(ball_grid.cnt_ball()) + "\n"

print(s.strip())