# import printing functions model - all functions in file will be avaiable in this program
import printing_functions
# start with designs that need to be printed 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)