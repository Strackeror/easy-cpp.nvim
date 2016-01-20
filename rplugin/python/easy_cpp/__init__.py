import neovim

@neovim.plugin
class Easy(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('Test')
    def test(self):
        self.vim.command('vsplit')
