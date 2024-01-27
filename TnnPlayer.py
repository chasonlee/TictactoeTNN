# -*- coding: utf-8 -*-
__author__ = 'Chason'
import math
from TopologicalNeuralNetwork import TopologicalNeuralNetwork
class TnnPlayer:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3, tnn = None):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM
        self.tnn = TopologicalNeuralNetwork(ROW * COL * 2, ROW * COL)

    def ai_tnn(self):
        pass

    def hard_code_tnn(self):
        #Avoid conflict
        for i in range(self.ROW * self.COL):
            self.tnn.outputNodes[i].add_input(self.tnn.inputNodes[i * 2], -100)
            self.tnn.outputNodes[i].add_input(self.tnn.inputNodes[i * 2 + 1], -100)

        # Center occupy
        node = self.tnn.create_hidden_node(name="center occupy")
        node.add_input(self.tnn.inputNodes[self.ROW * self.COL - 1], -20)
        node.add_input(self.tnn.inputNodes[self.ROW * self.COL], -20)
        bias = self.tnn.create_hidden_node(1, name="bias")
        node.add_input(bias, 30)
        self.tnn.outputNodes[int(self.ROW * self.COL / 2)].add_input(node, 5)

        #Defence
        for i in range(self.ROW):
            for j in range(self.COL):
                for m, n in [(1, 1), (1, 0), (1, -1), (0, -1)]:
                    for inv in [1, -1]:
                        ti = i + inv * m
                        tj = j + inv * n
                        last_node = None
                        for k in range(1, max(self.ROW, self.COL)):
                            if  0 <= ti < self.ROW and 0 <= tj < self.COL:
                                if last_node == None:
                                    pass
                                    node = self.tnn.create_hidden_node(name="src[%d, %d] def[%d, %d]*%d"%(i, j, ti, tj, k))
                                    node.add_input(self.tnn.inputNodes[(ti * self.COL + tj) * 2 + 1], 2)
                                    self.tnn.outputNodes[i * self.COL + j].add_input(node, 1)
                                else:
                                    # 2 defence
                                    lti = ti - inv * m
                                    ltj = tj - inv * n
                                    bias = self.tnn.create_hidden_node(value=1, name="hidden bias:src[%d, %d] def[%d, %d]*%d"%(i, j, ti, tj, k))
                                    node = self.tnn.create_hidden_node(name="and src[%d, %d] def[%d, %d]*%d"%(i, j, ti, tj, k))
                                    node.add_input(self.tnn.inputNodes[(ti * self.COL + tj) * 2 + 1], 20)
                                    node.add_input(self.tnn.inputNodes[(lti * self.COL + ltj) * 2 + 1], 20)
                                    node.add_input(bias, -30)
                                    self.tnn.outputNodes[i * self.COL + j].add_input(node, 3)

                                    # skip 2 defence
                                    # self.tnn.outputNodes[i * self.COL + j].add_input(self.tnn.inputNodes[(ti * self.COL + tj) * 2 + 1], 0.5)

                                ti = ti + inv * m
                                tj = tj + inv * n
                                last_node = node
                            else:
                                break