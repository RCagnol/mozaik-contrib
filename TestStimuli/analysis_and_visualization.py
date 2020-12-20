import numpy
import mozaik
import pylab
from mozaik.visualization.plotting import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore
from mozaik.tools.circ_stat import circular_dist
import sys
sys.path.append('/home/jan/projects/mozaik/contrib')

def perform_analysis_and_visualization(data_store):

    RetinalInputMovie(data_store,ParameterSet({}),plot_file_name="mov",fig_param={'dpi' : 300,'figsize': (2,1)}).plot({'*.title' : None})

    import pylab
    pylab.show()

