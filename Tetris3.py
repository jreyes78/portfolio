import curses
from random import choice
 
 
class TetrisGame:
    """Tetris Game - class-based version. """
    pieces = [
        [(0, 0), (0, -1), (0, 1), (1, 1)],
        [(0, 0), (0, -1), (0, 1), (-1, 1)],
        [(0, 0), (0, -1), (1, -1), (1, 0)],
        [(0, 0), (1, -1), (1, 0), (0, 1)],
        [(0, 0), (-1, -1), (-1, 0), (0, 1)],
        [(0, 0), (0, -1), (0, 1), (0, 2)],
        [(0, 0), (-1, 0), (0, -1), (1, 0)]
    ]
    mapping = [lambda x, y: (x, y), lambda x, y: (-y, x), lambda x, y: (-x, -y), lambda x, y: (y, -x)]
    piece_char = '*'
    board_size = 20
    board_borders = [  # Explicit is better than implicit.
        '*',  # Left-side
        '*',  # Right-side
        '*',  # Top-side
        '*',  # Bottom-side
        '*',  # Top-left
        '*',  # Top-right
        '*',  # Bottom-left
        '*'   # Bottom-right
    ]
    key_up = ord('w')
    key_down = ord('s')
    key_left = ord('a')
    key_right = ord('d')
    start_y = 2
 
    def __init__(self):
        curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        # Create windows and borders.
        self.win = curses.newwin(self.board_size, self.board_size, 0, 0)
        self.win.nodelay(1)
 
    def check_collision(self, crds, s):
        """Collision detection."""
        chk = all([self.win.inch(c[1], c[0]) & 255 == 32 for c in crds])
        for c in crds:
            if (chk and s == 1) or s == 0:
                self.win.addch(c[1], c[0], self.piece_char if s == 1 else 32)
        if s == 0:
            return True
        else:
            return chk
 
    def put_piece(self, piece, s):
        """Put piece on the board."""
        coords = []
        for p in piece[3]:
            x, y = p
            x, y = self.mapping[piece[2]](x, y)
            coords.append((x + piece[0], y + piece[1]))
        return self.check_collision(coords, s)
 
    def move_piece(self, piece, key, d):
        """Move piece into board"""
        if key == self.key_left:
            piece[0] = piece[0] - d
        elif key == self.key_right:
            piece[0] = piece[0] + d
        elif key in [self.key_down, -1]:
            piece[1] = piece[1] + d
        elif key == self.key_up:
            if piece[2] + d > self.start_y:
                piece[2] = 0
            elif piece[2] + d < 0:
                piece[2] = self.start_y
            else:
                piece[2] = piece[2] + d
 
    def kill_lines(self, score):
        """Kill filled lines and increase board score."""
        for i in range(self.board_size - 1):
            if all([chr(self.win.inch(i, x)) == self.piece_char for x in range(1, self.board_size - 1)]):
                self.win.deleteln()
                self.win.move(1, 1)
                self.win.insertln()
                score += 1
 
                if score % 10 == 0:
                    self.win.timeout(300 - (score * 2))
 
        return score
 
    def get_start_position(self):
        """Return start position x, y, rotation, random piece."""
        start_x = self.board_size / 2 - 1
        start_y = self.start_y
        start_rotation = 0
        return [start_x, start_y, start_rotation, choice(self.pieces)]
 
    def start(self):
        piece_position = self.get_start_position()
        score = self.put_piece(piece_position, 1) ^ 1
        self.win.timeout(300)
 
        while True:
            self.win.border(*self.board_borders)
            key = self.win.getch()
 
            self.put_piece(piece_position, 0)
            self.move_piece(piece_position, key, 1)
 
            if not self.put_piece(piece_position, 1):
                self.move_piece(piece_position, key, -1)
                self.put_piece(piece_position, 1)
                if piece_position[1] == self.start_y:
                    break
 
                if key in [self.key_down, -1]:
                    score = self.kill_lines(score)
                    piece_position = self.get_start_position()
                    self.put_piece(piece_position, 1)
 
        curses.endwin()
        print("Score: {}".format(score))
 
 
if __name__ == '__main__':
    tetris = TetrisGame()
    tetris.start()
