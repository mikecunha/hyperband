#!/usr/bin/env python

"a more polished example of using hyperband"
"includes displaying best results and saving to a file"

import sys
import pickle
from pprint import pprint

from hyperband import Hyperband

#from hyperband.defs.gb import get_params, try_params
#from hyperband.defs.rf import get_params, try_params
#from hyperband.defs.xt import get_params, try_params
#from hyperband.defs.rf_xt import get_params, try_params
#from hyperband.defs.sgd import get_params, try_params
#from hyperband.defs.keras_mlp import get_params, try_params
#from hyperband.defs.polylearn_fm import get_params, try_params
#from hyperband.defs.polylearn_pn import get_params, try_params
#from hyperband.defs.xgb import get_params, try_params
from hyperband.defs.meta import get_params, try_params

try:
	output_file = sys.argv[1]
	if not output_file.endswith( '.pkl' ):
		output_file += '.pkl'
except IndexError:
	output_file = 'results.pkl'

print("Will save results to", output_file)

#

hb = Hyperband( get_params, try_params )
results = hb.run( skip_last = 1 )

print("{} total, best:\n".format( len( results )))

for r in sorted( results, key = lambda x: x['loss'] )[:5]:
	print("loss: {:.2%} | {} seconds | {:.1f} iterations | run {} ".format(
		r['loss'], r['seconds'], r['iterations'], r['counter'] ))
	pprint( r['params'] )
	print()

print("saving...")

with open( output_file, 'wb' ) as f:
	pickle.dump( results, f )
