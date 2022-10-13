money_brought = 50
one_USB_Stick_Cost = 6
total_USB_Sticks = money_brought // one_USB_Stick_Cost
money_left = money_brought - (one_USB_Stick_Cost * total_USB_Sticks)

print("She can buy " + str(total_USB_Sticks) + " USB sticks for £" + str(money_brought))
print("and be left with £" + str(money_left))