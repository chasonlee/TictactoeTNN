# -*- coding: utf-8 -*-
__author__ = 'Chason'
import math

class Node:
    def __init__(self, id, flag = None, value = 0, name = "", threshold = 0.5):
        self.id = id
        self.flag = flag
        self.value = value
        self.name = name
        self.threshold = threshold
        self.inputs = []
        self.thetas = []

    def sigmoid(self, z):
        return 1.0 / (1.0 + math.exp(-z))

    def tanh(self, z):
        return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))

    def activation(self, beatFlag):
        inputNum = len(self.inputs)
        if inputNum != len(self.thetas):
            print "error: Input neurons and thetas must be the same size!"
            return
        elif inputNum == 0:
            # print "[id=%d, flag=%s, name=%s]warning: There are no inputs in this node."%(self.id, self.flag, self.name)
            return

        self.flag = not self.flag
        # ensure all input nodes are activated.
        for inputNode in self.inputs:
            if inputNode.flag != None and inputNode.flag == beatFlag:
                inputNode.activation(beatFlag)

        # calculate output value
        res = 0
        for inx in range(inputNum):
            res += self.inputs[inx].value * self.thetas[inx]
        res = self.sigmoid(res)
        self.value = res

    def output(self):
        if self.value > self.threshold:
            return True
        else:
            return False

    def add_input(self, neuron, theta):
        self.inputs.append(neuron)
        self.thetas.append(theta)

    def del_input(self, inx):
        if inx >= len(self.inputs) or inx >= len(self.thetas):
            print "error: Index of delete input operation out of range!"
            return False
        self.inputs.pop(inx)
        self.thetas.pop(inx)
        return True

    def get_input_num(self):
        return len(self.inputs)