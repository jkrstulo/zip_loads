

import numpy as np
import timeit as timeit




# #
# # load a network case studies


import pandapower as pp
import pandapower.networks as ppnets
import pandapower.converter as ppconv
import pandapower.plotting as ppplt
import pandapower.topology as pptop

import networkx as nx

from time import clock



# net = ppnets.panda_four_load_branch()
# net.trafo.shift_degree=0
# net.line.c_nf_per_km = 0

net = ppnets.four_loads_with_branches_out()
# pp.create_line(net,from_bus=8, to_bus=9,length_km=0.05, name='line9',std_type='NAYY 4x120 SE')

# net = ppnets.case9()

# net = ppnets.simple_mv_open_ring_net()
# net = ppnets.create_cigre_network_mv()
# net = ppnets.create_cigre_network_mv(with_der=False)
# net = ppnets.create_cigre_network_lv()
# net = ppnets.mv_oberrhein()
# net.trafo.shift_degree=0

net.load['const_p'] = 0.8
net.load['const_i'] = 0.1
net.load['const_z'] = 0.1

# pandapower PF
pp.runpp(net, numba=False, voltage_depend_loads=True)

print (net.res_bus)


pp.runpp(net, numba=False, voltage_depend_loads=False)

print (net.res_bus)







