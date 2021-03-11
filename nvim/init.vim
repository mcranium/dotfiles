" Specify a directory for plugins
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" List of plugins.
" Make sure you use single quotes

" Shorthand notation
Plug 'jalvesaq/Nvim-R'
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'
Plug 'gaalcaras/ncm-R'
Plug 'preservim/nerdtree'
Plug 'Raimondi/delimitMate'
Plug 'patstockwell/vim-monokai-tasty'
Plug 'itchyny/lightline.vim'
Plug 'Shougo/unite.vim'
Plug 'rafaqz/citation.vim'
Plug 'jalvesaq/zotcite'
" Plug 'vim-scripts/nexus.vim'

" Initialize plugin system
call plug#end()
" Set a Local Leader

" With a map leader it's possible to do extra key combinations
" like <leader>w saves the current file
let mapleader = ","
let g:mapleader = ","
set timeout timeoutlen=1500


" Plugin Related Settings

" NCM2
autocmd BufEnter * call ncm2#enable_for_buffer()    " To enable ncm2 for all buffers.
set completeopt=noinsert,menuone,noselect           " :help Ncm2PopupOpen for more
                                                    " information.

" NERD Tree
map <leader>nn :NERDTreeToggle<CR>                  " Toggle NERD tree.

" Monokai-tasty
let g:vim_monokai_tasty_italic = 1                  " Allow italics.
colorscheme vim-monokai-tasty                       " Enable monokai theme.

" LightLine.vim 
set laststatus=2              " To tell Vim we want to see the statusline.
let g:lightline = {
   \ 'colorscheme':'monokai_tasty',
   \ }


" General NVIM/VIM Settings

" Mouse Integration
set mouse=a                   " Enable mouse support in all modes

" Tabs & Navigation
map <leader>nt :tabnew<cr>    " To create a new tab.
map <leader>to :tabonly<cr>     " To close all other tabs (show only the current tab).
map <leader>tc :tabclose<cr>    " To close the current tab.
map <leader>tm :tabmove<cr>     " To move the current tab to next position.
map <leader>tn :tabn<cr>        " To swtich to next tab.
map <leader>tp :tabp<cr>        " To switch to previous tab.


" Line Numbers & Indentation
set backspace=indent,eol,start  " To make backscape work in all conditions.
set ma                          " To set mark a at current cursor location.
set number                      " To switch the line numbers on.
set expandtab                   " To enter spaces when tab is pressed.
set smarttab                    " To use smart tabs.
set autoindent                  " To copy indentation from current line 
                                " when starting a new line.
set si                          " To switch on smart indentation.


" Search
set ignorecase                  " To ignore case when searching.
set smartcase                   " When searching try to be smart about cases.
set hlsearch                    " To highlight search results.
set incsearch                   " To make search act like search in modern browsers.
set magic                       " For regular expressions turn magic on.


" Brackets
set showmatch                   " To show matching brackets when text indicator 
                                " is over them.
set mat=2                       " How many tenths of a second to blink 
                                " when matching brackets.


" Errors
set noerrorbells                " No annoying sound on errors.


" Color & Fonts
syntax enable                   " Enable syntax highlighting.
set encoding=utf8                " Set utf8 as standard encoding and 
                                 " en_US as the standard language.

" Files & Backup
set nobackup                     " Turn off backup.
set nowb                         " Don't backup before overwriting a file.
set noswapfile                   " Don't create a swap file.
set ffs=unix,dos,mac             " Use Unix as the standard file type.


" Return to last edit position when opening files
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" Doesn't work somehow
let g:citation_vim_mode="bibtex"
let g:citation_vim_bibtex_file="~/Zotero/my_zotero.bib"

" let g:citation_vim_mode="zotero"
" let g:citation_vim_zotero_path="~/Zotero/"
" let g:citation_vim_zotero_version=5

let g:citation_vim_cache_path='~/.vim/undodir'
let g:citation_vim_outer_prefix="["
let g:citation_vim_inner_prefix="@"
let g:citation_vim_suffix="]"
let g:citation_vim_et_al_limit=2
let g:citation_vim_reverse_order=0
" To do something with Zotero start commands with comma u (unite key)
nmap <leader>u [unite]
nnoremap [unite] <nop>
" Insert citation comma u c
nnoremap <silent>[unite]c       :<C-u>Unite -buffer-name=citation-start-insert -default-action=append      citation/key<cr>
" Open file under a citation: comma u co
nnoremap <silent>[unite]co :<C-u>Unite -input=<C-R><C-W> -default-action=start -force-immediately citation/file<cr>
" Show all info: comma u ci
nnoremap <silent>[unite]ci :<C-u>Unite -input=<C-R><C-W> -default-action=preview -force-immediately citation/combined<cr>


" Adjusting the split size
noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize -3<CR>
noremap <silent> <C-Down> :resize +3<CR>

" Clipboard functionality
set clipboard=unnamedplus

" disable _ to <- behaviour
let R_assign = 0
