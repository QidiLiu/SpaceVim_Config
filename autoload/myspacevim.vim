function! myspacevim#before() abort
	call SpaceVim#custom#SPCGroupName(['`'], '+OpenCV')
	call SpaceVim#custom#SPC('noremap', ['`', '1'], 'make -j4 && ./main', 'compile with make', 1)
endfunction

