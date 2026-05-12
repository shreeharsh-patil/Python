# Python program to create a list from range
lst_from_range = list(range(5))
print("List from range:", lst_from_range)

print("\nSet creation and usage")
# Python program to create a set
set_from_range = set(range(5))
print(set_from_range)

s1 = {1, 2, 1, 3, 4, 5, 2, 2}
print("Pruned distinct set elements:", s1)

s_char = set("Shreeharsh")
print("Set from characters:", s_char)

print("\nUpdating sets")
update_list = [1, 2, 3, 4, 7]
s_upd = set(update_list)
print("Original set:", s_upd)
s_upd.update([20, 4])
print("After update:", s_upd)

print("\nRemoving elements")
del_list = [1, 2, 3, 4, 7]
s_del = set(del_list)
print("Original set:", s_del)
s_del.remove(4)
print("After remove(4):", s_del)

print("\nFrozensets")
# Frozensets
s_fs = {20, 30, 40}
print("Base set:", s_fs)
fs1 = frozenset(s_fs)
print("Frozen:", fs1)

fs2 = frozenset("Shreeharsh")
print("Frozen set from characters:", fs2)
