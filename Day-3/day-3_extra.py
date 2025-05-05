print("Welcome to Pizza Deliveries!")

#rates for the pizza
small_pizza_rate = 15
medium_pizza_rate = 20
large_pizza_rate = 25

#rates for the extras
pepperoni_small_pizza = 2
pepperoni_large_medium_pizza = 3
extra_cheese = 1

pizza_cost = 0
print(f"""This is our rate chart 
Pizzas =>
      Small Pizza(S): ${small_pizza_rate}
      Medium Pizza(M): ${medium_pizza_rate}
      Large Pizza(L): ${large_pizza_rate}
Extras =>
      Pepperoni Small Pizza: +${pepperoni_small_pizza}
      Pepperoni for Large and Medium Pizza: +${pepperoni_large_medium_pizza}
      Extra Cheese: +${extra_cheese}
""")

order_pizza = input("What pizza would you like to order(S/M/L): ")

extra_pep = input("Would you like too add peperoni(Y/N): ")
add_cheese = input("Would you like too add Extra Cheese(Y/N): ")

if order_pizza == "S":
    pizza_cost += small_pizza_rate 
    if extra_pep == "Y":
        pizza_cost += pepperoni_small_pizza
        
    if add_cheese == "Y":
        pizza_cost += extra_cheese
else:
    if order_pizza == "M":
        pizza_cost += medium_pizza_rate
    elif order_pizza == "L":
        pizza_cost += large_pizza_rate
    
    
    if extra_pep == "Y":
        pizza_cost += pepperoni_large_medium_pizza
    
    if add_cheese == "Y":
        pizza_cost += extra_cheese
    
print(f"Your Pizza bill is: ${pizza_cost}")