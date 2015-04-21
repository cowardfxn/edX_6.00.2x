# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        


def simuldelayed(numViruses1, maxPop1, maxBirthProb1, clearProb1, resistances1,
                       mutProb1, numTrials, delaystep):
    viruses1 = []
    for i in range(numViruses1):
        viruses1.append(ResistantVirus(maxBirthProb1, clearProb1, resistances1,
                                        mutProb1))
    rst0 = []
    rst1 = []
    patient = TreatedPatient(viruses1, maxPop1)
    for i in range(numTrials):
        if i == delaystep:
            patient.addPrescription('guttagonol')
        rst0.append(patient.update())
        rst1.append(patient.getResistPop(['guttagonol']))
    
    return rst0

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    
    # Begin logging...
    print 'Begin...'
    
    delay0 = []
    delay75 = []
    delay150 = []
    delay300 = []
    for i in range(numTrials):
        delay0.append(simuldelayed(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 600, 0))
        delay75.append(simuldelayed(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 75))
        delay150.append(simuldelayed(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 150))
        delay300.append(simuldelayed(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 300))
    
    pylab.figure(1)
    pylab.hist(delay0)
    #pylab.subplot(221)
    pylab.title('delay step: 0')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(2)
    pylab.hist(delay75)
    #pylab.subplot(222)
    pylab.title('delay step: 75')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(3)
    pylab.hist(delay150)
    #pylab.subplot(223)
    pylab.title('delay step: 150')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(4)
    pylab.hist(delay300)
    #pylab.subplot(224)
    pylab.title('delay step: 300')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.show()
    # End logging...
    print 'End...'
    

    

#simulationDelayedTreatment(1000)

#
# PROBLEM 2
#

def simuldelayed2(numViruses1, maxPop1, maxBirthProb1, clearProb1, resistances1,
                       mutProb1, delaystep):
    viruses1 = []
    for i in range(numViruses1):
        viruses1.append(ResistantVirus(maxBirthProb1, clearProb1, resistances1,
                                        mutProb1))
    rst0 = []
    patient = TreatedPatient(viruses1, maxPop1)
    for i in range(150):
        rst0.append(patient.update())
    
    patient.addPrescription('guttagonol')
    
    if delaystep != 0:
        for i in range(delaystep):
            rst0.append(patient.update())
    
    patient.addPrescription('grimpex')
    
    for i in range(150):
        rst0.append(patient.update())    
    
    return rst0

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

    delay0 = []
    delay75 = []
    delay150 = []
    delay300 = []
    for i in range(numTrials):
        delay0.append(simuldelayed2(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, 0))
        delay75.append(simuldelayed2(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, 75))
        delay150.append(simuldelayed2(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, 150))
        delay300.append(simuldelayed2(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, 300))
    
    pylab.figure(1)
    pylab.hist(delay0)
    #pylab.subplot(221)
    pylab.title('delay step: 0')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(2)
    pylab.hist(delay75)
    #pylab.subplot(222)
    pylab.title('delay step: 75')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(3)
    pylab.hist(delay150)
    #pylab.subplot(223)
    pylab.title('delay step: 150')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.figure(4)
    pylab.hist(delay300)
    #pylab.subplot(224)
    pylab.title('delay step: 300')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials')
    
    pylab.show()
    # End logging...
    print 'End...'
    
simulationTwoDrugsDelayedTreatment(1000)
