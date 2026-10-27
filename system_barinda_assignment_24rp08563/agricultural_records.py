# Author: System Sylvere Barinda
# RegNo: 24rp08563 | Email: systembarinda@gmail.com
# Question 8: Agricultural Production Records

def agri_records() -> None:
    crop: str = "Maize"
    qty_kg: float = 1500.5
    price_per_kg: float = 400.0
    is_sold: bool = False
    
    revenue = qty_kg * price_per_kg
    print(f"Crop: {crop}, Revenue: {revenue:,.2f} RWF, Sold: {is_sold}")
    for val in [crop, qty_kg, price_per_kg, is_sold]:
        print(type(val))

if __name__ == "__main__":
    agri_records()
