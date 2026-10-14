import json


def load_categories():
    with open("Data/cate.json", encoding="utf-8") as f:
        return json.load(f)


def load_products(q=None):
    with open("Data/products.json", encoding="utf-8") as f:
        prods = json.load(f)

    if q:
        q = q.casefold()
        prods = [
            p for p in prods
            if q in p.get("name", "").casefold()
        ]

    return prods


if __name__ == "__main__":
    print(load_categories())
    print(load_products())