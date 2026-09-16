"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TO/DO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        if qty < 1:
            raise ValueError('qty must be greater than or equal to 1')

        if not item['available']:
            raise OutOfStockError('This item is not in stock')

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
        # TO/DO: raise KeyError if the item is not in the cart
        try:
            del self.lines[item_id]
        except IndexError:
            raise KeyError(f'Item with id {item_id} is not in the cart')

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")

    # NOTE: I added the relevant, friendly message as the message parameter
    # passed to the exception's constructor
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f'Failed to add item to the cart: {e}')

    try:
        cart.add_item(miso, 1)
    except OutOfStockError as e:
        print(f'Failed to add item to the cart: {e}')

    try:
        cart.remove_item(gyoza['id'])
    except KeyError as e:
        print(f'Faild to remove item: {e}')

