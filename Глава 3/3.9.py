from random import randint as ri

new_list = [ri(1, 20) for i in range(ri(8, 12))]
print(new_list)
past_ind = 1
for i in range(len(new_list) - 1):
    new_list.insert(past_ind, new_list[past_ind - 1] + new_list[past_ind])
    past_ind += 2
print(new_list)
