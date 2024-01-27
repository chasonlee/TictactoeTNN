# -*- coding: utf-8 -*-
__author__ = 'Chason'
from TopologyNode import Node

class TopologicalNeuralNetwork:
    def __init__(self, inputNum, outputNum):
        self.inputNum = inputNum
        self.outputNum = outputNum
        self.hiddenNum = 0
        self.inputNodes = [Node(i) for i in range(inputNum)]
        self.outputNodes = [Node(i) for i in range(outputNum)]
        self.hiddenNodes = []
        self.beatFlag = False

    def init_network(self):
        for node in self.inputNodes:
            node.value = 0
        # for node in self.hiddenNodes:
        #     node.value = 0
        for node in self.outputNodes:
            node.value = 0
        self.beatFlag = False

    def get_input(self, board):
        lenBoard = len(board)
        if lenBoard * 2 != self.inputNum:
            print "Error: Board length and network inputs doesn't match."
            return
        for i in range(lenBoard):
            if board[i] != 0:
                self.inputNodes[i * 2 + board[i] - 1].value = 1

    def forward_propagation(self):
        for node in self.hiddenNodes:
            if node.get_input_num() > 0:
                node.activation(self.beatFlag)
        for node in self.outputNodes:
            if node.get_input_num() > 0:
                node.activation(self.beatFlag)
        self.beatFlag = not self.beatFlag

    def max_output(self):
        maxvalue = -2
        res = None
        for i, node in enumerate(self.outputNodes):
            if maxvalue < node.value:
                maxvalue = node.value
                res = i
        return res

    def create_hidden_node(self, value = 0, name = ""):
        node = Node(self.hiddenNum, self.beatFlag, value=value, name=name)
        self.hiddenNodes.append(node)
        self.hiddenNum += 1
        return node

    def show_structure(self, showInput = True, showHidden = True, showConnect = True, showOutput = True):
        print "/******************************************************************************************\\"
        if showInput:
            print "|\tInput nodes:\t"
            for node in self.inputNodes:
                print "\t", node.value,
                if node.id % 6 == 5:
                    print
            print
        if showHidden:
            for node in self.hiddenNodes:
                print "|\tHidden node%d(%s):\t%f"%(node.id, node.name, node.value)
            print

        if showConnect:
            for node in self.hiddenNodes:
                if node.get_input_num() > 0:
                    print "|\t%d neurons connected to hidden node%d(%s):"%(node.get_input_num(), node.id, node.name)
                    for i, inputNode in enumerate(node.inputs):
                        if inputNode.flag == None:
                            print "|\t\tinput node%d,\ttheta: %f" % (inputNode.id, node.thetas[i])
                        else:
                            print "|\t\thidden node%d(%s),\ttheta: %f"%(inputNode.id, inputNode.name, node.thetas[i])
            for node in self.outputNodes:
                if node.get_input_num() > 0:
                    print "|\t%d neurons connected to output node%d:"%(node.get_input_num(), node.id)
                    for i, inputNode in enumerate(node.inputs):
                        if inputNode.flag == None:
                            print "|\t\tinput node%d,\ttheta: %f" % (inputNode.id, node.thetas[i])
                        else:
                            print "|\t\thidden node%d(%s),\ttheta: %f"%(inputNode.id, inputNode.name, node.thetas[i])
            print

        if showOutput:
            print "|\tOutput nodes:\t"
            for node in self.outputNodes:
                print "\t%.6f"%node.value,
                if node.id % 3 == 2:
                    print

        print "\******************************************************************************************/"