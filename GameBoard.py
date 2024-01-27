# -*- coding: utf-8 -*-
__author__ = 'Chason'
import random

class GameBoard:
    def __init__(self, ROW = 3, COL = 3, WIN_NUM = 3):
        self.ROW = ROW
        self.COL = COL
        self.WIN_NUM = WIN_NUM

        self.winner = 0
        self.EMPTY_NUM = 0
        self.PLAYER1_NUM = 1
        self.PLAYER2_NUM = 2
        self.DRAW = 3

        self.PLAYER1_CHAR = '#'
        self.PLAYER2_CHAR = '*'
        self.MAPS = '.'
        self.turns = 0
        self.board = [0 for i in range(ROW * COL)]
        self.last_move = -1

    def resume_board(self):
        self.turns = 0
        self.board = [0 for i in range(self.ROW * self.COL)]

    def print_piece(self, inx):
        if inx == self.PLAYER1_NUM:
            print self.PLAYER1_CHAR,
        elif inx == self.PLAYER2_NUM:
            print self.PLAYER2_CHAR,
        else:
            print self.MAPS,

    def show_board(self):
        for i, p in enumerate(self.board):
            self.print_piece(p)
            if (i + 1) % self.COL == 0:
                print
        print

    def move(self, loc, player):
        if 0 <= loc < self.ROW * self.COL:
            if self.board[loc] == 0:
                self.board[loc] = player
                self.turns += 1
                self.last_move = loc
                return True
            else:
                # print "Occupy error: location %d is not empty."
                return False
        else:
            print "Location error: can not move to %d."%loc
            return False

    def rnd_move(self, player):
        rnd = int(self.ROW * self.COL * random.random())
        return self.move(rnd, player)

    def safe_rnd_move(self, player):
        while self.turns < self.ROW * self.COL and not self.rnd_move(player):
            pass

    def judge(self, loc):
        player = self.board[loc]
        r = loc / self.COL
        c = loc % self.COL
        for i in range(4):
            if i == 0:
                dr = -1
                dc = -1
            elif i == 1:
                dr = -1
                dc = 0
            elif i == 2:
                dr = -1
                dc = 1
            else:
                dr = 0
                dc = 1
            nr = r + dr
            nc = c + dc
            count = 1
            while nr >= 0 and nr < self.ROW and nc >= 0 and nc < self.COL:
                if self.board[nr * self.COL + nc] == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            dr = -dr
            dc = -dc
            nr = r + dr
            nc = c + dc
            while nr >= 0 and nr < self.ROW and nc >= 0 and nc < self.COL:
                if self.board[nr * self.COL + nc] == player:
                    count = count + 1
                    nr = nr + dr
                    nc = nc + dc
                else:
                    break
            if count >= self.WIN_NUM:
                return player

        if self.turns >= self.ROW * self.COL:
            return self.DRAW
        return None