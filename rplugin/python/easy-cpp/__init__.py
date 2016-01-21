import os
import neovim
import clang.cindex
import sys

@neovim.plugin
class Easy(object):
    def __init__(self, vim):
        self.vim = vim
        self.index = clang.cindex.Index.create()
        sys.stderr = open('/tmp/easy-error.log', 'a')
        sys.stdout = open('/tmp/easy-cpp-debug.log', 'a', 0)
        print "New Instance"

    @neovim.command('Test')
    def test(self):
        name = os.path.splitext(self.vim.current.buffer.name)[0]
        self.vim.command("vsplit " + name + ".cpp")

    @neovim.command('TestClang')
    def clang_parse(self):
        name = self.vim.current.buffer.name
        unit = self.index.parse(name, ['-x', 'c++'])
        print unit.spelling
        curpos = self.vim.current.window.cursor
        sourceloc = unit.get_location(name, curpos)
        cursor = unit.cursor.from_location(unit, sourceloc)
        print cursor.kind
        print cursor.type.spelling
        for c in cursor.get_children():
            print c.kind
        print "end"
        #cursor = Cursor.from_location(unit, SourceLocation.from_position(unit, name, curpos[0], curpos[1]))
