"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TO/DO
        line_ids = [line['item_id'] for line in self.lines]

        try:
            matching_line_id = line_ids.index(item['id'])
            self.lines[matching_line_id]['qty'] += qty
        except ValueError:
            self.lines.append({
                'item_id': item['id'],
                'name': item['name'],
                'price': item['price'],
                'qty': qty
            })

    def remove_item(self, item_id: int) -> None:
        # TO/DO
        try:
            del self.lines[item_id]
        except IndexError:
            print(f'Error: there is no item with index {item_id}')

    def clear(self) -> None:
        # TO/DO
        self.lines.clear()

    def total(self) -> float:
        # TO/DO - round ONCE, at the end
        total_cost = sum([line['price'] * line['qty'] for line in self.lines])
        return round(total_cost, 2)

    def __repr__(self) -> str:
        # TO/DO
        return f'<{self.__class__.__name__} {len(self.lines)} items, ${self.total():.2f}>'


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
