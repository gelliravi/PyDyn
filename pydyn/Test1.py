# Copyright (C) 2009 Stijn Cole
# Copyright (C) 2010-2011 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pylab import close, figure, xlabel, ylabel, hold, plot, axis, legend

from pydyn.Pdoption import Pdoption
from pydyn.rundyn import rundyn

def Test1():
    """ test script """
    pdopt = Pdoption()
    pdopt[4] = 0     # no progress info
    pdopt[5] = 1     # no plots

    ## Modified Euler
    # Set options
    pdopt[0] = 1     # Modified Euler

    # Run dynamic simulation
    print  '> Modified Euler...'
    Angles1, Speeds, Eq_tr, Ed_tr, Efd, PM, Voltages, Stepsize1, Errest, Time1 = \
        rundyn('casestagg', 'casestaggdyn', 'staggevent', pdopt)

    ## Runge-Kutta
    # Set options
    pdopt[0] = 2     # Runge-Kutta

    # Run dynamic simulation
    print 'Done.\n> Runge-Kutta...'
    Angles2, Speeds, Eq_tr, Ed_tr, Efd, PM, Voltages, Stepsize2, Errest, Time2 = \
        rundyn('casestagg', 'casestaggdyn', 'staggevent', pdopt)

    ## Fehlberg
    # Set options
    pdopt[0] = 3     # Runge-Kutta Fehlberg
    pdopt[1] = 1e-4  # tol = 1e-4
    pdopt[2] = 1e-4  # minimum step size = 1e-4

    # Run dynamic simulation
    print 'Done.\n> Runge-Kutta Fehlberg...'
    Angles3, Speeds, Eq_tr, Ed_tr, Efd, PM, Voltages, Stepsize3, Errest, Time3 = \
        rundyn('casestagg', 'casestaggdyn', 'staggevent', pdopt)

    ## Higham-Hall
    # Set options
    pdopt[0] = 4     # Runge-Kutta Higham-Hall
    pdopt[1] = 1e-4  # tol = 1e-4
    pdopt[2] = 1e-4  # minimum step size = 1e-4

    # Run dynamic simulation
    print 'Done.\n> Runge-Kutta Higham-Hall...'
    Angles4, Speeds, Eq_tr, Ed_tr, Efd, PM, Voltages, Stepsize4, Errest, Time4 = \
        rundyn('casestagg', 'casestaggdyn', 'staggevent', pdopt)
    print 'Done.\n'

    ## Plots
    # Plot angles
    close("all")
    figure
    hold(True)
    xlabel('Time [s]')
    ylabel('Generator angles [deg]')
    p1 = plot(Time1, Angles1[:, :1], '-.b')
    p2 = plot(Time2, Angles2[:, :1], ':r')
    p3 = plot(Time3, Angles3[:, :1], '--g')
    p4 = plot(Time4, Angles4[:, :1], 'm')
    Group1 = hggroup
    Group2 = hggroup
    Group3 = hggroup
    Group4 = hggroup
    set(p1, 'Parent', Group1)
    set(p2, 'Parent', Group2)
    set(p3, 'Parent', Group3)
    set(p4, 'Parent', Group4)
    set(get(get(Group1,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    set(get(get(Group2,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    set(get(get(Group3,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    set(get(get(Group4,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    legend('Modified Euler','Runge-Kutta','Fehlberg','Higham-Hall')
    axis([0, Time1(-1), -1, 1])
    axis('auto y')

    figure
    hold(True)
    p1 = plot(Time1, Stepsize1, ':b')
    p2 = plot(Time3, Stepsize3, '--g')
    p3 = plot(Time4, Stepsize4, 'm')
    Group1 = hggroup
    Group2 = hggroup
    Group3 = hggroup
    set(p1,'Parent',Group1)
    set(p2,'Parent',Group2)
    set(p3,'Parent',Group3)
    set(get(get(Group1,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    set(get(get(Group2,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    set(get(get(Group3,'Annotation'),'LegendInformation'),
        'IconDisplayStyle','on')
    xlabel('Time [s]')
    ylabel('Step size')
    legend('Modified Euler and Runge-Kutta','Fehlberg','Higham-Hall')
    axis([0, Time1(-1), -1, 1])
    axis('auto y')
