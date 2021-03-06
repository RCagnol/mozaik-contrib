#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    
def create_experiments(model):
    return              [
                            #Spontaneous Activity 
                            #NoStimulation(model,duration=2*147*7),
                            #MeasureSpontaneousActivity(model,2*147*7,1),
                            #MeasureOrientationTuningFullfield(model,num_orientations=1,spatial_frequency=0.8,temporal_frequency=2,grating_duration=4*147*7,contrasts=[0,2,4,8,16,32,64,100],num_trials=10),
                            #MeasureFlatLuminanceSensitivity(model,step_duration=100*147*7,luminances=[0,2,4,8,16,32,64,100],num_trials=1),
                            #MeasureNaturalImagesWithEyeMovement(model,stimulus_duration=4*147*7,num_trials=10),
                            #MeasureOrientationTuningFullfield(model,num_orientations=1,spatial_frequency=0.8,temporal_frequency=2,grating_duration=147*7,contrasts=[100],num_trials=1),
                            #MapPhaseResponseWithBarStimulus(model,ParameterSet({
                            #                                        'x' : 0,
                            #                                        'y' : 0,
                            #                                        'length' : 1/0.8/2.0 * 6.0,
                            #                                        'width' :  1/0.8/4.0,
                            #                                        'orientation' : 0,
                            #                                        'max_offset' : 1/0.8/2.0 * 1.5,
                            #                                        'steps' : 3,
                            #                                        'duration' : 1000,
                            #                                        'flash_duration' : 500, 
                            #                                        'relative_luminance' : 0,
                            #                                        'num_trials' : 1
                            #                                        })),
                                                                    
                            #MapPhaseResponseWithBarStimulus(model,ParameterSet({
                            #                                        'x' : 0,
                            #                                        'y' : 0,
                            #                                        'length' : 1/0.8/2.0 * 6.0,
                            #                                        'width' :  1/0.8/4.0,
                            #                                        'orientation' : 0,
                            #                                        'max_offset' : 1/0.8/2.0 * 1.5,
                            #                                        'steps' : 3,
                            #                                        'duration' : 1000,
                            #                                        'flash_duration' : 500, 
                            #                                        'relative_luminance' : 1.0,
                            #                                        'num_trials' : 1
                            #                                        })),

                            #MapResponseToInterruptedBarStimulus(model,ParameterSet({
                            #                                        'x' : 0,
                            #                                        'y' : 0,
                            #                                        'length' : 1/0.8/2.0 * 12.0,
                            #                                        'width' :  1/0.8/4.0,
                            #                                        'orientation' : 0,
                            #                                        'max_offset' : 1/0.8/2.0 * 1.5,
                            #                                        'steps' : 3,
                            #                                        'duration' : 1000,
                            #                                        'flash_duration' : 500, 
                            #                                        'relative_luminances' : [1.0],
                            #                                        'num_trials' : 1,
			    #					    'gap_lengths' : [0.3,0.6]
                            #                                        })),

                    	    #MapResponseToInterruptedCornerStimulus(model,ParameterSet({
                            #                                        'x' : 0,
                            #                                        'y' : 0,
                            #                                        'length' : 1/0.8/2.0 * 12.0,
                            #                                        'width' :  1/0.8/4.0,
                            #                                        'orientation' : 0,
                            #                                        'max_offset' : 1/0.8/2.0 * 1.5,
                            #                                        'steps' : 1,
                            #                                        'duration' : 1000,
                            #                                        'flash_duration' : 500, 
                            #                                        'relative_luminances' : [1.0],
                            #                                        'num_trials' : 1,
			    #                                        'gap_length' : 0.3,
			    #                                        'angles' : [numpy.pi/4]
                            #                                        })),

                            MeasureSparse(model,ParameterSet({
                                   'time_per_image': 42, 
                                   'stim_size' : 5,
                                   'total_number_of_images' : 50, 
                                   'num_trials' : 1,
                                   'experiment_seed' : 13,
                                   'grid_size' : 10,
                                   'stim_size' : 5.5,
                                   'grid' : True
                            })),

            
                        ]

