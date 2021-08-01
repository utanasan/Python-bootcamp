def calc_dice_score(lst):
   if lst[0][0]==lst[0][1] or lst[1][0]==lst[1][1] or lst[2][0]==lst[2][1]:
       return 0
   else:
       return lst[0][0]+lst[0][1]+lst[1][0]+lst[1][1]+lst[2][0]+lst[2][1]

print(calc_dice_score([(1,2),(3,4),(5,6)]))
print(calc_dice_score([(1,1),(5,6),(6,4)]))
print(calc_dice_score([(4,5),(5,4),(4,5)]))
