import numpy as np

#Extra task: Vector maths with NumPy
genes = ["geneA", "geneB", "geneC", "geneD", "geneE"]
control = [120, 340, 15, 800, 60]
treated = [240, 340, 60, 200, 30]

#1.Add the lists
print("Task1. Add the lists.")
new = control + treated
print(new)
#the lists get concatenated

#2. Make arrays
print("Task2. Make arrays and add them.")
control_array = np.array(control)
treated_array = np.array(treated)
new_array = control_array + treated_array
print(new_array)

#Calculate the fold change.
print("Task3. Calculate the fold change.")
fold_change = treated_array / control_array
print(fold_change)

#Calculate the log2 fold change.
print("Task4. Calculate the log2 fold change.")
log_fold = np.log2(fold_change)
print(log_fold)

#Normalise the samples.
print("Task5. Normalise the samples.")
c_sum = np.sum(control_array)
t_sum = np.sum(treated_array)

c_norm = control_array / c_sum
t_norm = treated_array / t_sum

norm_fold = t_norm / c_norm
norm_log_fold = np.log2(norm_fold)
print(norm_log_fold)
