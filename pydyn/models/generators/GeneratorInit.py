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

from numpy import ones, zeros, angle, sin, cos, arange, pi, conj, r_

from pypower.idx_gen import PG, QG

def GeneratorInit(Pgen, U0, gen, baseMVA, gentype):
    """ Calculate initial conditions generators.

    @see: U{http://www.esat.kuleuven.be/electa/teaching/matdyn/}
    """
    ## Init
    global freq

    ngen, _ = Pgen.shape
    Xgen0 = zeros(ngen)
    Efd0 = zeros(ngen)
    d = arange(len(gentype))

    ## Define types
    type1 = d[gentype == 1]
    type2 = d[gentype == 2]

    ## Generator type 1: classical model
    x_tr = Pgen[type1, 6]

    omega0 = ones(len(type1)) * 2 * pi * freq

    # Initial machine armature currents
    Ia0 = (gen[type1, PG] - 1j * gen[type1, QG]) / conj(U0[type1, 0]) / baseMVA

    # Initial Steady-state internal EMF

    Eq_tr0 = U0[type1, 0] + 1j * x_tr * Ia0
    delta0 = angle(Eq_tr0)
    Eq_tr0 = abs(Eq_tr0)

    Xgen0[type1, :2] = r_[delta0, omega0, Eq_tr0]

    ## Generator type 2:
    xd = Pgen[type2, 5]
    xq = Pgen[type2, 6]
    xd_tr = Pgen[type2, 7]
    xq_tr = Pgen[type2, 8]

    omega0 = ones(len(type2)) * 2 * pi * freq

    # Initial machine armature currents
    Ia0 = (gen[type2, PG] - 1j * gen[type2, QG]) / conj(U0[type2, 0]) / baseMVA
    phi0 = angle(Ia0)

    # Initial Steady-state internal EMF
    Eq0 = U0[type2, 0] + 1j * xq * Ia0
    delta0 = angle(Eq0)

    # Machine currents in dq frame
    Id0 = -abs(Ia0) * sin(delta0 - phi0)
    Iq0 = abs(Ia0) * cos(delta0 - phi0)

    # Field voltage
    Efd0[type2] = abs(Eq0) - (xd - xq) * Id0

    # Initial Transient internal EMF
    Eq_tr0 = Efd0[type2, 0] + (xd - xd_tr) * Id0
    Ed_tr0 = -(xq - xq_tr) * Iq0

    Xgen0[type2, :3] = r_[delta0, omega0, Eq_tr0, Ed_tr0]

    ## Generator type 3:

    ## Generator type 4:

    return Efd0, Xgen0
