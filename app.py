from enum import Enum
from math import ceil
import sys
from typing import Dict
from random import Random


AVAILABLE_KEYS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7]

class CellType(Enum):
    POSITION = "P"  # Next Position
    COMMAND = "C"   # Command
    VALUE = "V"     # Value

class Cell:
    type: CellType
    value: int

    def __init__(self, cell_type: CellType, value: int):
        self.type = cell_type
        self.value = value

    @staticmethod
    def p_cell(value):
        return Cell(CellType.POSITION, value)
    
    @staticmethod
    def c_cell(value):
        return Cell(CellType.COMMAND, value)
    
    @staticmethod
    def v_cell(value):
        return Cell(CellType.VALUE, value)

class Block:
    cell_dictionary: Dict[int, Cell]

    def __init__(self, cell_dictionary: Dict[int, Cell]):
        self.cell_dictionary = cell_dictionary

    @classmethod
    def init(
            cls,
            current_position_cell_key: int, 
            next_block_key: int = None, 
            ascii_dec_value: int = None,
            is_first_char: bool = False
            ):
        instance = cls({})
        p_cell = Cell.p_cell(next_block_key)
        c_and_v_cells = instance.c_and_v_cells_from_ascii_dec_value(
            ascii_dec_value, 
            instance.__first_value_cell_key_by_position_cell_key(current_position_cell_key),
            is_first_char
        )
        cell_dictionary = {current_position_cell_key: p_cell}
        cell_dictionary.update(c_and_v_cells)
        return Block(cell_dictionary)

    def next_block_key(self) -> int:
        return self.__p_cell().value
    
    def ascii_dec_value(self) -> int:
        command_cell = self.__c_cell()

        if self.__is_null_by_command_value(command_cell.value):
            return None
        else:
            plus_value = self.__ascii_plus_dec_value_by_command_value(command_cell.value)
            value_cells: Dict[int, int] = {}
            
            for value_cell_key in self.__value_cell_keys_by_command_key(command_cell.value):
                value_cell = self.cell_dictionary.get(value_cell_key)
                if value_cell and value_cell.value is not None:
                    value_cells[value_cell_key] = value_cell.value
            can_subdivide_with_ten = len(value_cells) > 1 and value_cells.get(3) == 1
            current_value = None
            for key, value in value_cells.items():
                if key != 3:
                    print(f'{int(f"{key}0")} if {can_subdivide_with_ten} else {int(f"{key}{value}")}')
                    current_value = int(f"{key}0") if can_subdivide_with_ten else int(f"{key}{value}")
            if current_value is None:
                return current_value
            else:
                return current_value + plus_value

    def c_and_v_cells_from_ascii_dec_value(
            self,
            ascii_dec_value: int,
            first_value_cell_key: int,
            is_first_char: bool = False
            ) -> Dict[int, Cell]:
        def parse_ascii_digits(n: int):
            s = str(n)
            d1 = int(s[0])
            d2 = int(s[1])
            return d1, d2
        

        if ascii_dec_value == None:
            c_cell_value = Random().choice([4, 6])
            v_cell_key = Random().choice(self.__value_cell_keys_by_command_key(first_value_cell_key - 1))
            v_cell_value = Random().choice(AVAILABLE_KEYS)
            return {
                first_value_cell_key - 1: Cell.c_cell(c_cell_value),
                v_cell_key: Cell.v_cell(v_cell_value)
            }

        elif 32 <= ascii_dec_value <= 99:
            d1, d2 = parse_ascii_digits(ascii_dec_value)
            v_cell_key = first_value_cell_key + (d1 - 3)
            v_cell_key = v_cell_key if v_cell_key < 10 else v_cell_key - 9

            result = { }

            if is_first_char:
                result[first_value_cell_key - 1] = Cell.c_cell(5)

            if d2 == 0:
                result[first_value_cell_key] = Cell.v_cell(1)
                result[v_cell_key] = Cell.v_cell(1)
            else:
                result[v_cell_key] = Cell.v_cell(d2)

            
            return result
        
        elif 100 <= ascii_dec_value <= 167:
            d1, d2 = parse_ascii_digits(ascii_dec_value - 68)
            c_cell_value = 9 if is_first_char else 1
            return {
                first_value_cell_key - 1: Cell.c_cell(c_cell_value),
                first_value_cell_key + d1: Cell.v_cell(d2)
            }
        
        elif 168 <= ascii_dec_value <= 235:
            d1, d2 = parse_ascii_digits(ascii_dec_value - 68 * 2)
            c_cell_value = 8 if is_first_char else 2
            return {
                first_value_cell_key - 1: Cell.c_cell(c_cell_value),
                first_value_cell_key + d1: Cell.v_cell(d2)
            }
        
        elif 236 <= ascii_dec_value <= 255:
            d1, d2 = parse_ascii_digits(ascii_dec_value - 68 * 3)
            c_cell_value = 7 if is_first_char else 3
            return {
                first_value_cell_key - 1: Cell.c_cell(c_cell_value),
                first_value_cell_key + d1: Cell.v_cell(d2),
            }

    def __value_cell_keys_by_command_key(self, command_key: int) -> list[int]:
        start_key = command_key + 1 if command_key + 1 < 10 else (command_key + 1) - 9
        return AVAILABLE_KEYS[start_key:start_key + 7]

    def __ascii_plus_dec_value_by_command_value(self, command_value: int) -> int:
        plus_value = 0
        if command_value in [1, 9]:
            plus_value = 68
        elif command_value in [2, 8]:
            plus_value = 2 * 68
        elif command_value in [3, 7]:
            plus_value = 3 * 68
        return plus_value

    def __is_null_by_command_value(self, command_value) -> bool:
        return command_value in [4, 6]

    def __first_value_cell_key_by_position_cell_key(self, position_key) -> int:
        return position_key + 2 if position_key + 2 < 10 else (position_key + 2) - 9

    def __p_cell(self) -> Cell:
        return next(cell for cell in self.cell_dictionary.values() if cell.type == CellType.POSITION)

    def __c_cell(self) -> Cell:
        return next(cell for cell in self.cell_dictionary.values() if cell.type == CellType.COMMAND)

class Board:
    block_dictionary: Dict[int, Block]
    formatted_x = []
    formatted_y = []


    def __init__(self, block_dictionary: Dict[int, Block]):
        self.block_dictionary = block_dictionary
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        x = block_row + i + 1
                        y = block_col + j + 1
                        self.formatted_x.append(x)
                        self.formatted_y.append(y)

    def print_board(self):

        print("+-------+-------+-------+")
        for i in range(len(self.formatted_x)):

            if i % 9 == 0:
                print("|", end='')
            if i % 3 == 0 and i % 9 != 0:
                print(" |", end='')

            try:
                current_block = self.block_dictionary.get(self.formatted_x[i])
                current_cell = current_block.cell_dictionary.get(self.formatted_y[i])
                print(f" {current_cell.value}", end='')
            except:
                print(f" .", end='')

            if (i + 1) % 9 == 0:
                print(" |")
            if (i + 1) % 27 == 0:
                print("+-------+-------+-------+")

class Main:
    def main(self, argv):
        encryptable_word = argv[1]
        with_shuffle = argv[2] if len(argv) > 2 else False

        print(f"Encryptable word: {encryptable_word}")

        board_list = self.__init_sudoku_structure(encryptable_word, with_shuffle)
        for board in board_list:
            board.print_board()

    def __init_sudoku_structure(self, encryptable_word: str, with_shuffle: bool = False) -> list[Board]:
        random = Random()
        boards_count = self.__boards_count(encryptable_word)
        board_list: list[Board] = []
        block_list: list[Block] = []

        encryptable_word_chars_map = [{"index": i + 1, "char": ord(c)} for i, c in enumerate(encryptable_word)]
        
        if with_shuffle:
            random.shuffle(encryptable_word_chars_map)

        available_block_indexes = [1,2,3,4,5,6,7,8,9]

        for index, item in enumerate(encryptable_word_chars_map):
            current_position = item["index"]
            next_position = encryptable_word_chars_map[index + 1]["index"] if index + 1 < len(encryptable_word_chars_map) else random.choice(available_block_indexes)
            available_block_indexes.remove(current_position)

            block_list.append(Block.init(
                current_position,
                next_position,
                item["char"],
                current_position == 1
            ))

        total_blocks = boards_count * 9
        current_count = len(block_list)

        if current_count < total_blocks:
            last_index = block_list[-1].cell_dictionary.keys()
            last_position = max(last_index) if last_index else current_count

            for i in range(current_count + 1, total_blocks + 1):
                current_position = i
                next_position = i + 1 if i < total_blocks else 1  # körbe mutat
                block_list.append(Block.init(
                    current_position,
                    next_position,
                    None,
                    False
                ))

        board_blocks = {i + 1: c for i, c in enumerate(block_list)}
        return [Board(board_blocks)]

    def __boards_count(self, encryptable_word: str):
        return ceil(len(encryptable_word) / 9)

if __name__ == "__main__":
    main = Main()
    main.main(sys.argv)
