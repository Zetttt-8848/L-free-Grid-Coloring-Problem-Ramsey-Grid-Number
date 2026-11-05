"""R10-authorized serialization repair; original audit stays unchanged."""
import sys,runpy
sys.set_int_max_str_digits(10000)
runpy.run_path('research_round2/checks/general_neighbor_verify.py',run_name='__main__')
