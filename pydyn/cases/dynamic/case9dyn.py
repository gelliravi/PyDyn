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

from numpy import array

def case9dyn():
    """ PyDyn dynamic data file.

    @see: U{http://www.esat.kuleuven.be/electa/teaching/matdyn/}
    """
    ## General data

    freq = 50.0
    stepsize = 0.01
    stoptime = 1.0

    ## Generator data

    # [genmodel excmodel govmodel H D xd xq xd_tr xq_tr Td_tr Tq_tr]
    # [ genmodel    excmodel    govmodel    H       D       x       x'     ]

    gen = array([
        [1, 1, 1, 1.20, 0.02, 0.14, 0.14, 0, 0, 0, 0],
        [1, 1, 1, 2.40, 0.01, 0.14, 0.14, 0, 0, 0, 0],
        [2, 2, 1, 5.74, 0.02, 1.93, 1.77, 0.25, 0.25, 5.2, 0.81]
    ])

    ## Exciter data

    # [gen Ka  Ta  Ke  Te  Kf  Tf  Aex  Bex  Ur_min  Ur_max]
    exc = array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 50, 0.05, -0.17, 0.95, 0.04, 1, 0.014, 1.55, -1.7, 1.7]
    ])

    ## Governor data
    # [gen K  T1  T2  T3  Pup  Pdown  Pmax  Pmin]
    gov = array([
        [1.0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2.0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3.0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    return gen, exc, gov, freq, stepsize, stoptime
