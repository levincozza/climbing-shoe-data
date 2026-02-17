import json

def get_product_ids(filename):
    with open(f"{filename}", "r") as file:
        data = json.load(file)
    

    product_ids = []
    for product in data:
        product_ids.append(product["id"])

    return product_ids

def save_list_as_json(filename, list):
    with open(f"{filename}", "w") as file:
        json.dump(list, file, indent=4)

def generate_product_link_json(product_ids):
    new_products_list = []
    for product in product_ids:
        id = str(product)
        default_size_cm = 30.0
        
        new_product = {
            "id": id,
            "product_link": f"https://mountainfootwearproject.com/{id}",
            "product_api_link": f"https://mountainfootwearproject.com/api/products/{id}",
            "sizing_api_link": f"https://mountainfootwearproject.com/api/products/{id}/length/{default_size_cm}"
        }
        new_products_list.append(new_product)
    
    return new_products_list


if __name__ == "__main__":
    product_ids = get_product_ids("raw_data/mfw_products.json")
    product_links = generate_product_link_json(product_ids)
    save_list_as_json("raw_data/mfw_product_links.json", product_links)


    

    
    
