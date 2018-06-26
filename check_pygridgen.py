import sys
import matplotlib
from matplotlib import style

import pygridgen

matplotlib.use('agg')
style.use('classic')

if '--strict' in sys.argv:
    sys.argv.remove('--strict')
    status = pygridgen.teststrict(*sys.argv[1:])
else:
    status = pygridgen.test(*sys.argv[1:])

sys.exit(status)
