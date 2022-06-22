from dataclasses import dataclass
import tensorflow as tf
from icecream import ic
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

@dataclass
class Machine(object):
    num1: int
    num2: int
    opcode: str

    @property
    def num1(self) -> int: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def opcode(self) -> str: return self._opcode

    @opcode.setter
    def opcode(self, opcode): self._opcode = opcode


class Solution:
    def __init__(self, payload):
        self._num1 = payload._num1
        self._num2 = payload._num2

    @tf.function
    def add(self):
        return tf.add(self._num1, self._num2)

    @tf.function
    def sub(self):
        return tf.subtract(self._num1, self._num2)

    @tf.function
    def mul(self):
        return tf.multiply(self._num1, self._num2)

    @tf.function
    def div(self):
        return tf.divide(self._num1, self._num2)

class UseModel:
    def __init__(self):
        pass

    def calc(self, num1, num2, opcode):
        model = Machine()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        solution = Solution(model)
        if opcode == '+':
            result = solution.add()
        elif opcode == '-':
            result = solution.sub()
        elif opcode == '*':
            result = solution.mul()
        elif opcode == '/':
            result = solution.div()

        return result

if __name__ == '__main__':
    num1 = 1
    num2 = 4
    opcode = '+'
    result = UseModel().calc(num1, num2, opcode)
    ic(result)
