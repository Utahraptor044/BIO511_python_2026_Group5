import numpy as np

genes = ["geneA", "geneB", "geneC", "geneD", "geneE"]
control = [120, 340, 15, 800, 60]
treated = [240, 340, 60, 200, 30]

ct = control + treated

print(ct)

arr_control = np.array(control)

arr_treated = np.array(treated)

ct = arr_control + arr_treated

print(ct)

fc = arr_treated/arr_control

print(fc)

fclog2 = np.log2(fc)

print(fclog2)

norm_arr_control = arr_control/np.sum(arr_control)

norm_arr_treated = arr_treated/np.sum(arr_treated)

""" print(norm_arr_control)
print(norm_arr_treated) """

norm_fc = norm_arr_treated/norm_arr_control

""" print(norm_fc) """

norm_fclog2 = np.log2(norm_fc)

print(norm_fclog2)