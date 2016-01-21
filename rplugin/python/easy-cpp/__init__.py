import os
import neovim
import clang.cindex

@neovim.plugin
class Easy(object):
    def __init__(self, vim):
        self.vim = vim
        self.index = clang.cindex.Index.create()

    @neovim.command('Test')
    def test(self):
        name = os.path.splitext(self.vim.current.buffer.name)[0]
        self.vim.command("vsplit " + name + ".cpp")
