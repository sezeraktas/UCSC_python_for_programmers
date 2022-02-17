#1

def totalCost (sales_price, tax_rate = 8.25):
    return sales_price * (1 + (tax_rate/100))
    
print("%.2f" %totalCost(200, 10))


#2

def DoBreakfast(meat = "bacon", eggs = "over easy eggs", potatos = "hash browns", toast = "white toast", beverage = "coffee"):
    print ("Here is your ", meat, "and " , eggs, "with ", potatos, " and", toast, ".", "", "Can I bring you more ", beverage, " ?")

(DoBreakfast("chicken", "boiled eggs", "fried potatos", "brown toast", "tea"))