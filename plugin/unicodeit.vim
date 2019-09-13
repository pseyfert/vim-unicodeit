" Replace LaTeX by unicode.
" Author:      Paul Seyfert
" Version:     0.0.0
" WebPage:     none://yet
" Description: Render LaTeX code as unicode
" License:     AGPL v3, see LICENSE for more details.

let s:save_cpo = &cpo
set cpo&vim
" obtain the main directory of the plugin, to call the python script
" and also to patch/bodge the sys.path in python for importing
" the main unicodeit module
let g:unicode_plugin_path = expand('<sfile>:p:h:h')

function! UnicodeIt()
  if has('python3')
    let s:plugin_py = g:unicode_plugin_path . '/plugin.py'
    execute ':py3 unicode_plugin_path = "' . g:unicode_plugin_path . '"'
    execute ':py3file ' . s:plugin_py
    unlet s:plugin_py
  else
    echo "ERROR: no python 3 support detected"
  endif
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
