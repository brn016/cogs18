from FinalProject import *
import pytest


assert len(sort_state(state_one_year("California",2010)[0])) == 11
assert (state_one_year("California",2010)[0]["Cause"] == (["All Causes"])).all
assert (state_one_year("California",2010)[0]["Deaths"] == ([234012])).all