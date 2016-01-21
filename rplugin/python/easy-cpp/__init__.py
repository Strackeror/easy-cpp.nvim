import neovim
import clang.cindex

@neovim.plugin
class Easy(object):
    def __init__(self, vim):
        self.vim = vim
        self.index = clang.cindex.Index.create()

    @neovim.command('EasyImpl')
    def impl(self):
        cfilename = self.vim.eval('expand("%:p")')
        self.vim.current.line = cfilename

