from dataclasses import dataclass

import tensorflow as tf


@dataclass
class Machine:
        _num1: int
        _num2: int
        opcode: ''


class Solution:
    def __init__(self, payload):
        self._num1 = payload._num1
        self._num2 = payload._num2

    @tf.function
    def add(self):
        return tf.add(self._num1, self._num2)

    @tf.function
    def sub(self):
        return tf.add(self._num1, self._num2)

    @tf.function
    def mul(self):
        return tf.add(self._num1, self._num2)

    @tf.function
    def div(self):
        return tf.add(self._num1, self._num2)

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

        # 사칙연산 완성시킬것

        return result

if __name__ == '__main__':
    pass