#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    
def create_experiments(model):
    return              [
                           #Spontaneous Activity 
                           NoStimulation(model,ParameterSet({'duration' : 2*147*7})),

                           #GRATINGS
                           MeasureOrientationTuningFullfield(model,ParameterSet({'num_orientations':1,'spatial_frequency':0.8,'temporal_frequency' : 2,'grating_duration' : 147*7,'contrasts' : [100],'num_trials':1})),
                       
                           
                           #IMAGES WITH EYEMOVEMENT
                           #MeasureNaturalImagesWithEyeMovement(model,stimulus_duration=3*147*7,num_trials=2),

                           #GRATINGS WITH EYEMOVEMENT
                           #MeasureDriftingSineGratingWithEyeMovement(model,spatial_frequency=0.8,temporal_frequency=2,stimulus_duration=147*7,num_trials=10,contrast=100),
                        ]

