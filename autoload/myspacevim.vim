function! myspacevim#before() abort
	set autowrite	
	noremap h i
	noremap H I
	noremap j h
	noremap J 6h
	noremap i k
	noremap I 6k
	noremap k j
	noremap K 6j
	noremap L 6l
	call SpaceVim#custom#SPCGroupName(['`'], '+OpenCV')
	call SpaceVim#custom#SPC('noremap', ['`', '1'], '!cmake . && make -j4 && ./main', 'compile with cmake', 1)
endfunction
