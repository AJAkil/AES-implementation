from BitVector import *
import numpy as np
import pprint as pp

key = 'Thats my Kung Fu'

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


class KeyHandler:

    def __init__(self, utility, key='Thats my Kung Fu'):
        self.utils = utility
        self.key = key
        self.generated_keys = []

    def format_input(self):
        str_len = len(self.key)
        if str_len < 16:
            self.key = self.key.ljust(16, '0')
        elif str_len > 16:
            self.key = self.key[:16]
        return self.key

    def schedule_keys(self):
        # storing the key as a bitvector in the first array
        self.generated_keys.append(BitVector(textstring=self.key))
        prev_rc = BitVector(hexstring='01')

        for round in range(1, 11):

            current_key = self.generated_keys[len(self.generated_keys) - 1].get_text_from_bitvector()
            w = [
                BitVector(textstring=current_key[:4]),
                BitVector(textstring=current_key[4:8]),
                BitVector(textstring=current_key[8:12]),
                BitVector(textstring=current_key[12:16])
            ]

            # print(BitVector(textstring=w3).getHexStringFromBitVector())
            modified_word, next_rc = self.g(w[3], prev_rc, round)
            prev_rc = BitVector(textstring=next_rc.get_text_from_bitvector()[:1])
            # self.utils.print_bitvector(prev_rc, format="hex")
            # self.utils.print_bitvector(prev_rc, 'hex')

            # first word of next key
            w[0] = w[0] ^ modified_word

            # then find the consecutive words
            for i in range(1, 4):
                # # print('before w[i] = ', end='')
                # self.utils.print_bitvector(w[i], 'hex')
                # # print('before w[i-1] = ', end='')
                # self.utils.print_bitvector(w[i - 1], 'hex')

                w[i] = w[i - 1] ^ w[i]

            s = ''.join(bv.get_text_from_bitvector() for bv in w)

            self.generated_keys.append(BitVector(textstring=s))

    def g(self, word, prev_rc, round):
        # print(word.get_hex_string_from_bitvector())
        word = word.deep_copy()

        # circular left shift the byte
        word = word << 8

        # byte substitution
        word = self.utils.substitute(word.get_text_from_bitvector())

        rc_list = self.utils.generate_rounding_const(
            prev_rc,
            round
        )
        # self.utils.print_bitvector(prev_rc, format="hex")
        # print(len(rc_list[0]))
        s = ''.join(bv.get_text_from_bitvector() for bv in rc_list)
        rc = BitVector(textstring=s)
        # self.utils.print_bitvector(rc, format="hex")
        return word ^ rc, rc

    def print_keys(self):
        for key in self.generated_keys:
            hex_format = key.get_hex_string_from_bitvector()
            for i in range(0, len(hex_format), 2):
                print(hex_format[i:i + 2], end=' ')
            print()


class Utility:

    @staticmethod
    def substitute(word):
        result = ''
        for i in range(4):
            temp = BitVector(textstring=word[i])
            int_val = temp.intValue()
            s_val = Sbox[int_val]
            s_val = BitVector(intVal=s_val, size=8)
            result += s_val.get_text_from_bitvector()
        return BitVector(textstring=result)

    def generate_rounding_const(self, prev_rc, round):

        # self.print_bitvector(prev_rc, format="hex")
        hex_80 = BitVector(hexstring='80')
        rc2 = BitVector(hexstring='00')
        rc3 = BitVector(hexstring='00')
        rc4 = BitVector(hexstring='00')
        multiplier = BitVector(hexstring="02")
        rounding_constants = [rc2, rc3, rc4]

        if round > 1 and prev_rc <= hex_80:
            rounding_constants.insert(0, self.gf_multiply(prev_rc, multiplier))
        else:
            rounding_constants.insert(0, prev_rc)

        return rounding_constants

    @staticmethod
    def gf_multiply(bv1, bv2):
        AES_modulus = BitVector(bitstring='100011011')
        return bv1.gf_multiply_modular(bv2, AES_modulus, 8)

    @staticmethod
    def print_bitvector(bitvector, format):
        if format == 'string':
            print(f'BitVector in string: {bitvector.get_text_from_bitvector()}')
        elif format == 'hex':
            print(f'BitVector in hex: {bitvector.get_hex_string_from_bitvector()}')
        elif format == 'ASCII':
            print(f'BitVector in ASCII: {bitvector.get_bitvector_in_ascii()}')

    @staticmethod
    def format_to_matrix(hex_string='5468617473206d79204b756e67204675'):
        print('for hex_string', len(hex_string))
        matrix = []
        for i in range(0, len(hex_string), 2):
            matrix.append(hex_string[i:i + 2])

        matrix = np.transpose(np.array([matrix]).reshape(4, 4)).tolist()
        matrix = [[BitVector(hexstring=element) for element in row] for row in matrix]
        return matrix

    @staticmethod
    def byte_substitution(matrix_entry, inverse=False):
        matrix_entry = matrix_entry.deep_copy()
        int_val = matrix_entry.intValue()
        s_val = Sbox[int_val]
        s_val = BitVector(intVal=s_val, size=8)
        return s_val

    @staticmethod
    def print_matrix(matrix):
        pp.pprint([[elem.get_hex_string_from_bitvector() for elem in row] for row in matrix])

    def multiply_matrix(self, matrix, row, col):
        #self.print_matrix(Mixer)
        #self.print_matrix(matrix)
        result = [[BitVector(hexstring='00') for _ in range(col)] for _ in range(row)]
        entry = BitVector(hexstring='00')
        #self.print_matrix(result)

        for i in range(row):
            for j in range(col):
                for k in range(row):
                    entry = self.gf_multiply(Mixer[i][k], matrix[k][j])
                    temp = BitVector(hexstring=result[i][j].get_hex_string_from_bitvector()) ^ entry
                    result[i][j] = temp

        #self.print_matrix(result)
        return result

    @staticmethod
    def row_shift(single_row, row, is_left):
        """
        for cyclic row shifting of by amount=row left or right
        :param single_row: row to be shifted
        :param row: the amount to be shifted
        :param is_left: left shift or right shift
        :return: shifted row
        """
        hex_representation = [elem.get_hex_string_from_bitvector() for elem in single_row]

        if is_left:
            row = -row

        rolled = np.roll(np.array(hex_representation), row).tolist()
        bit_vector = [BitVector(hexstring=string) for string in rolled]
        return bit_vector


class Encrypt:
    def __init__(self, keys, state_matrix, utils):
        """
        constructor for encryption class
        :param keys: list of keys in form of BitVector
        :param state_matrix: the state matrix in hex_string
        :param utils: utility object
        """
        self.round_keys = keys
        self.current_state_matrix = state_matrix
        self.utils = utils

    def add_round_key(self, state_matrix, round=0):
        round_key = u.format_to_matrix(self.round_keys[round].get_hex_string_from_bitvector())
        if round == 0:
            state_matrix = u.format_to_matrix(state_matrix)

        # pp.pprint([[elem.get_hex_string_from_bitvector() for elem in row] for row in round_key])
        # pp.pprint([[elem.get_hex_string_from_bitvector() for elem in row] for row in state_matrix])

        # Element wise XOR
        result = [[state_matrix[row][col] ^ round_key[row][col]
                   for col in range(len(state_matrix))]
                  for row in range(len(state_matrix))]

        self.current_state_matrix = result

        # pp.pprint([[elem.get_hex_string_from_bitvector() for elem in row] for row in result])

    def matrix_byte_substitution(self, inverse):
        for row in range(len(self.current_state_matrix)):
            for col in range(len(self.current_state_matrix)):
                self.current_state_matrix[row][col] = self.utils.byte_substitution(self.current_state_matrix[row][col],
                                                                                   inverse=inverse)

        # self.utils.print_matrix(self.current_state_matrix)

    def shift_rows(self):
        for row_no, current_row in enumerate(self.current_state_matrix):
            self.current_state_matrix[row_no] = self.utils.row_shift(current_row, row_no, True)

        #self.utils.print_matrix(self.current_state_matrix)

    def mix_columns(self):
        mat_len = 4
        self.current_state_matrix = self.utils.multiply_matrix(self.current_state_matrix, mat_len, mat_len)

    def encrypt(self):
        pass


class Decrypt:
    pass


if __name__ == '__main__':
    keyHandler = KeyHandler(Utility())
    print(keyHandler.format_input())
    keyHandler.schedule_keys()
    keyHandler.print_keys()
    generated_keys = keyHandler.generated_keys
    u = Utility()
    text = BitVector(textstring='Two One Nine Two')
    print(f'length of text: {len(text.get_text_from_bitvector())}')
    # format the keys
    # u.format_to_matrix()
    encrypt = Encrypt(
        generated_keys,
        text.get_hex_string_from_bitvector(),
        u
    )
    encrypt.add_round_key(encrypt.current_state_matrix)

    for i in range(1, 10):
        encrypt.matrix_byte_substitution(inverse=False)
        encrypt.shift_rows()
        print(f'mix columns after round {i}')
        encrypt.mix_columns()
        u.print_matrix(encrypt.current_state_matrix)
        encrypt.add_round_key(encrypt.current_state_matrix, round=i)
        print(f'after round {i}')
        u.print_matrix(encrypt.current_state_matrix)

    encrypt.matrix_byte_substitution(inverse=False)
    encrypt.shift_rows()
    encrypt.add_round_key(encrypt.current_state_matrix, round=10)
    print('after round 10')
    u.print_matrix(encrypt.current_state_matrix)

    hex_matrix = [[elem.get_hex_string_from_bitvector() for elem in row] for row in encrypt.current_state_matrix]
    n = np.transpose(np.array(hex_matrix))
    hex_string = ''.join(elem for elem in n.reshape(16))
    print(hex_string)

    for elem in n.reshape(16):
        print(elem, end=' ')

    # DECRYPT part
    # round 0
    encrypt.add_round_key(hex_string)







