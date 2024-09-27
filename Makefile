show_cases:
	collect-only

run_tests:
	echo "before tests"
	#source $HOME/Users/Serjan777/miniconda3/activate
	#conda activate skillbox_2; \
	pytest
	#conda deactivate;
	echo "after tests"