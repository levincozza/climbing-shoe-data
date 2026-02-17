import json
import requests
from main import (
    Shoe, Gender, FootWidth, HeelWidth, Downturn, Stiffness, 
    AsymCurve, ClosureSystem, UpperMaterial, Lining, 
    ClimbingStyle, ClimbingGrade, ToeShape, Volume, Source
)

def get_product_ids(filename):
    with open(f"{filename}", "r") as file:
        data = json.load(file)
    

    product_ids = []
    for product in data:
        product_ids.append(product["id"])

    return product_ids

def open_json_as_list(filename):
    with open(f"{filename}", "r") as file:
        return json.load(file)

def save_list_as_json(filename, list):
    with open(f"{filename}", "w") as file:
        json.dump(list, file, indent=4)

def generate_product_link_json(product_ids):
    new_products_list = []
    for product in product_ids:
        id = str(product)
        default_size_cm = 29.74
        
        new_product = {
            "id": id,
            "product_link": f"https://mountainfootwearproject.com/{id}",
            "product_api_link": f"https://mountainfootwearproject.com/api/products/{id}",
            "sizing_api_link": f"https://mountainfootwearproject.com/api/products/{id}/length/{default_size_cm}"
        }
        new_products_list.append(new_product)
    
    return new_products_list

def populate_shoes_data(product_links_filename):
    shoes = []
    data = open_json_as_list(product_links_filename)
    for product in data:
        product_api_url = product["product_api_link"]
        sizing_api_url = product["sizing_api_link"]
        try:
            shoe = parse_shoe_data(product_api_url, sizing_api_url)
            shoes.append(shoe)
            print(f"Successfully parsed {shoe.brand} {shoe.model}")
        except Exception as e:
            print(f"Failed to parse {product_api_url}: {e}")
    
    return shoes


def parse_gender(str):
    str = str.title()
    if 'Men' in str:
        return Gender.MEN
    elif 'Women' in str:
        return Gender.WOMEN
    elif 'Kid' in str:
        return Gender.KID
    else:
        print(f"'{str}' Unknown -> Defaulting to Men's shoe")
        return Gender.MEN

def parse_foot_width(str):
    if "Men's Wide" in str:
        return FootWidth.WIDE
    elif "Men's Medium" in str or "Women's Wide" in str:
        return FootWidth.MEDIUM
    elif "Men's Narrow" in str or "Women's Medium" in str:
        return FootWidth.NARROW
    elif "Women's Narrow" in str:
        return FootWidth.EXTRA_NARROW
    elif "Kid" in str:
        return FootWidth.KIDS
    else:
        print(f"'{str}' Unknown -> Defaulting to Medium FootWidth")
        return FootWidth.MEDIUM

def parse_heel_width(str):
    if "Narrow" in str:
        return HeelWidth.NARROW
    elif "Medium" in str:
        return HeelWidth.MEDIUM
    elif "Adjustable" in str or "Kid" in str:
        print("Adjustable heel found?")
        return HeelWidth.KIDS
    else:
        print(f"'{str}' Unknown -> Defaulting to Medium HeelWidth")
        return HeelWidth.MEDIUM

def parse_downturn(str):
    if "Flat" in str:
        return Downturn.FLAT
    elif "Medium" in str:
        return Downturn.MEDIUM
    elif "Aggressive" in str:
        return Downturn.AGGRESSIVE
    else:
        print(f"'{str}' Unknown -> Defaulting to Medium Downturn")
        return Downturn.MEDIUM

def parse_stiffness(str):
    if "Very Soft" in str:
        return Stiffness.EXTRA_SOFT
    elif "Soft" in str:
        return Stiffnes.SOFT
    elif "Medium" in str:
        return Stiffness.MEDIUM
    elif "Stiff" in str:
        return Stiffness.STIFF
    else:
        print(f"'{str}' Unknown -> Defaulting to Medium Stiffness")
        return Stiffness.MEDIUM

def parse_asymmetric_curve(str):
    if "High" in str:
        return AsymCurve.HIGH
    elif "Low" in str:
        return AsymCurve.LOW
    elif "Medium" in str:
        return AsymCurve.MEDIUM
    else:
        print(f"'{str}' Unknown -> Defaulting to Medium AsymCurve")
        return AsymCurve.MEDIUM

# TODO: PARSE_CLOSURE_SYSTEM
# this is super tedious so here is a response where AI is generating template stuff, it did way too much though so forget a lot of it

def parse_shoe_data(product_api_url, sizing_api_url):
    
    product_response = (requests.get(product_api_url)).json
    sizing_response = (requests.get(sizing_api_url)).json

    # TODO: FIX
    shoe = Shoe(
        brand=f"{product_response["brand"]}",
        model=f"{product_response["model"]}",
        gender=parse_gender(product_response["gender"]),
        size_delta=int(sizing_response["traditionalFit"]) - int(sizing_response["size"]),
        foot_width=parse_foot_width(product_response["footWidth"]),
        heel_width=parse_heel_width(product_response["heelWidth"]),
        downturn=parse_downturn(),
        stiffness=parse_stiffness(),
        asymmetric_curve=parse_asymmetric_curve(),
        closure_system=parse_closure_system(),
        rubber_type=f"{}",
        sole_thickness=parse_sole_thickness(),
        upper_material=parse_upper_material(),
        lining=parse_upper_material(),

        climbing_style=parse_climbing_style(),
        climbing_grade=parse_climbing_grade(),
        toe_shape=parse_toe_shape(),
        volume=parse_volume(),
        source=Source.MFW,

        description:f"{}",
        price:0.0,
        

        ...
    )



if __name__ == "__main__":
    


    

    
    
