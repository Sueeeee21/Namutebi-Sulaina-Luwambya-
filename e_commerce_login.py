users = {
    "admin_user": {"password": "admin123", "role": "Admin", "access": 3},
    "customer1": {"password": "cust456", "role": "Customer", "access": 1},
    "customer2": {"password": "cust789", "role": "Customer", "access": 1},
    "cashier1": {"password": "cash101", "role": "Cashier", "access": 2}
}

coupons = {
    "SAVE10": 10,
    "SAVE20": 20,
    "WELCOME": 15,
    "VIP50": 50
}

tax = {
    "Uganda": 18,
    "Kenya": 16,
    "Tanzania": 18,
    "Rwanda": 18,
    "Kampala": 18,
    "Default": 0
}

user_name = None
user_role = None
user_access = None


def login():
    global user_name, user_role, user_access
    
    print("\n" + "="*50)
    print("WELCOME TO E-COMMERCE SYSTEM")
    print("="*50)
    
    tries = 0
    while tries < 3:
        print(f"\nAttempt {tries + 1}/3")
        name = input("Username: ")
        pwd = input("Password: ")
        
        if name in users:
            if users[name]["password"] == pwd:
                user_name = name
                user_role = users[name]["role"]
                user_access = users[name]["access"]
                print(f"\nLogin success! Welcome {user_role}: {name}")
                return True
            else:
                print("Wrong password")
        else:
            print("User not found")
        
        tries = tries + 1
    
    print("\nToo many tries. Access denied.")
    return False


def logout():
    global user_name, user_role, user_access
    
    if user_name != None:
        print(f"\n{user_name} logged out")
        user_name = None
        user_role = None
        user_access = None
        return True
    return False


def check_coupon(code, amount):
    code = code.upper()
    
    if code not in coupons:
        return False, 0, "Coupon not found"
    
    discount_percent = coupons[code]
    
    if code == "VIP50":
        if user_role != "Admin" and user_role != "Cashier":
            return False, 0, "Only Admin/Cashier can use this"
    
    if code == "SAVE20" or code == "VIP50":
        if amount < 100000:
            return False, 0, "Need at least 100000 for this coupon"
    
    return True, discount_percent, f"Coupon {code} = {discount_percent}%"


def get_tax(place):
    place = place.strip().title()
    
    if place in tax:
        return tax[place]
    else:
        print(f"Location {place} not found. Using default.")
        return 0


def calculate_price(subtotal, coupon_code, location):
    result = {
        "sub": subtotal,
        "coupon_disc": 0,
        "volume_disc": 0,
        "after_disc": subtotal,
        "tax_rate": 0,
        "tax_amt": 0,
        "final": subtotal,
        "msg": []
    }
    
    # Apply coupon
    if coupon_code != "":
        valid, percent, message = check_coupon(coupon_code, subtotal)
        result["msg"].append(message)
        
        if valid:
            disc_amount = subtotal * (percent / 100)
            result["coupon_disc"] = disc_amount
            result["after_disc"] = result["after_disc"] - disc_amount
        else:
            result["msg"].append("No coupon discount applied")
    else:
        result["msg"].append("No coupon used")
    
    # Volume discount
    if subtotal >= 500000:
        if coupon_code == "":
            if subtotal >= 1000000:
                vol_percent = 15
            else:
                vol_percent = 10
            
            vol_amount = result["after_disc"] * (vol_percent / 100)
            result["volume_disc"] = vol_amount
            result["after_disc"] = result["after_disc"] - vol_amount
            result["msg"].append(f"Volume discount: {vol_percent}%")
        else:
            result["msg"].append("No volume discount with coupon")
    
    elif subtotal >= 250000:
        if coupon_code == "":
            vol_percent = 5
            vol_amount = result["after_disc"] * (vol_percent / 100)
            result["volume_disc"] = vol_amount
            result["after_disc"] = result["after_disc"] - vol_amount
            result["msg"].append(f"Volume discount: {vol_percent}%")
    
    else:
        result["msg"].append("No volume discount")
    
    # Tax
    tax_rate = get_tax(location)
    result["tax_rate"] = tax_rate
    
    if tax_rate > 0:
        tax_amount = result["after_disc"] * (tax_rate / 100)
        result["tax_amt"] = tax_amount
        result["msg"].append(f"Tax ({location}): {tax_rate}%")
    else:
        result["msg"].append(f"No tax for {location}")
    
    # Final
    result["final"] = result["after_disc"] + result["tax_amt"]
    
    return result


def show_result(r):
    print("\nDETAILS:")
    print(f"Subtotal:        {r['sub']:,.2f}")
    
    if r['coupon_disc'] > 0:
        print(f"Coupon discount: {r['coupon_disc']:,.2f}")
    
    if r['volume_disc'] > 0:
        print(f"Volume discount: {r['volume_disc']:,.2f}")
    
    total_disc = r['coupon_disc'] + r['volume_disc']
    if total_disc > 0:
        pct = (total_disc / r['sub']) * 100
        print(f"Total saved:     {total_disc:,.2f} ({pct:.1f}%)")
    
    print("-" * 40)
    print(f"After discounts: {r['after_disc']:,.2f}")
    
    if r['tax_amt'] > 0:
        print(f"Tax:             {r['tax_amt']:,.2f}")
    
    print("=" * 40)
    print(f"FINAL PRICE:     {r['final']:,.2f}")
    print("=" * 40)


def show_coupons():
    print("\n" + "="*50)
    print("AVAILABLE COUPONS")
    print("="*50)
    
    for code in coupons:
        discount = coupons[code]
        
        if code == "VIP50":
            if user_role == "Admin" or user_role == "Cashier":
                print(f"{code}: {discount}%")
            else:
                print(f"{code}: {discount}% (Admin/Cashier only)")
        else:
            print(f"{code}: {discount}%")


def show_locations():
    print("\n" + "="*50)
    print("TAX RATES BY LOCATION")
    print("="*50)
    
    for place in tax:
        rate = tax[place]
        print(f"{place}: {rate}% VAT")


def show_menu():
    print("\n" + "="*50)
    print(f"MENU ({user_role})")
    print("="*50)
    print("1. Calculate Price")
    print("2. View Coupons")
    print("3. View Locations")
    print("4. Logout")
    
    if user_role == "Admin":
        print("5. View Users")
        print("6. Manage Coupons")
    
    if user_role == "Cashier":
        print("5. Generate Receipt")
    
    print("0. Exit")
    print("="*50)


def calc_price():
    print("\n" + "="*50)
    print("PRICE CALCULATOR")
    print("="*50)
    
    while True:
        try:
            amt = float(input("Enter amount: "))
            if amt < 0:
                print("Amount cannot be negative")
                continue
            break
        except:
            print("Invalid number")
    
    coupon = input("Coupon code (press Enter to skip): ")
    loc = input("Location (default Kampala): ")
    
    if loc == "":
        loc = "Kampala"
    
    res = calculate_price(amt, coupon, loc)
    
    print("\nMessages:")
    for m in res["msg"]:
        print(f"- {m}")
    
    show_result(res)


def view_users():
    print("\n" + "="*50)
    print("ALL USERS")
    print("="*50)
    
    for name in users:
        data = users[name]
        print(f"{name} | Role: {data['role']} | Access: {data['access']}")


def manage_coupons():
    print("\n" + "="*50)
    print("MANAGE COUPONS")
    print("="*50)
    
    print("Current coupons:")
    for code in coupons:
        print(f"  {code}: {coupons[code]}%")
    
    print("\nFeature coming soon...")


def main():
    if not login():
        print("Login failed. Exiting...")
        return
    
    while True:
        show_menu()
        choice = input("\nSelect: ")
        
        if choice == "1":
            calc_price()
        
        elif choice == "2":
            show_coupons()
        
        elif choice == "3":
            show_locations()
        
        elif choice == "4":
            if logout():
                break
        
        elif choice == "5":
            if user_role == "Admin":
                view_users()
            elif user_role == "Cashier":
                print("\nReceipt generator coming soon...")
        
        elif choice == "6" and user_role == "Admin":
            manage_coupons()
        
        elif choice == "0":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()