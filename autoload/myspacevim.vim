function! myspacevim#before() abort
	set autowrite	
	call SpaceVim#custom#SPCGroupName(['`'], '+OpenCV')
	call SpaceVim#custom#SPC('noremap', ['`', '1'], '!cmake . && make -j4 && ./main', 'compile with cmake', 1)
endfunction

