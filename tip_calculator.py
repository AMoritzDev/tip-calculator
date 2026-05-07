def calculate_tip(price, tip):
    if price <= 0:
        return "Price must be more than 0"
    if tip < 0 or tip > 100:
        return "Tip must be between 0 and 100"
    total = price * (1 + (tip / 100))
    return f"Total is: {round(total, 2)} dollars"