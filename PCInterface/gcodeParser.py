# Trace
# Copyright (C) 2015  Hugo LEVY-FALK
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

SEPARATOR = ('\n', ' ', '(')

class Pile:
    def __init__(self, in_str):
        self.in_str = in_str
        self.next = None
    def token(self):
        while len(self.in_str) > 0:
            yield self.pop()
    def pop(self):
        r = self.peek()
        self.next = None
        return r
    def peek(self):
        if not self.next:
            self.next = self.in_str[0]
            self.in_str = self.in_str[1:]
        return self.next

def parse(gcode):
    pile = Pile(gcode+'\n')
    for c in pile.token():
        if c is ' ': continue
        elif c is '(' :
            com = ''
            while pile.peek() is not ')':
                com += pile.pop()
            pile.pop() # removes the ')'
            yield ('__comment__', c)
        elif c is '\n': yield ('__next__', '__next__')
        else: yield (c, parse_num(pile))

def parse_instr(gcode):
    name = ""
    value = 0
    args = {}
    for i in parse(gcode):
        if not i[0] == '__next__':
            if i[0] in ('G', 'M'):
                name = i[0]
                value = i[1]
            elif i[0] in 'XYZIJKN':
                args[i[0]] = i[1]
            elif i[0] == '__comment__':
                if name is "":
                    name = 'comment'
                args['comments'] = i[1]
        elif name is not "":
            yield {'name':name, 'value':value, 'args':args}
            name = ""
            value = 0
            args = {}
    yield {'name':name, 'value':value, 'args':args}


def parse_num(pile):
    r = ''
    while pile.peek() not in SEPARATOR:
        r += pile.pop()
    return float(r)


# s = """G01 X-3.0 Y4
# N1 G02 Z3"""
if __name__ == '__main__':
    with open("gcode.ngc") as f:
        for i in parse_instr(f.read()): print(i)