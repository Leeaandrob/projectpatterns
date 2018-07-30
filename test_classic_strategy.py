from unittest import TestCase

from classic_strategy import (
    LineItem, Order, FidelityPromo, Customer, BulkItemPromo,
    LargeOrderPromo
)


class LineItemTest(TestCase):
    def test_total_jhon(self):
        """this test will verify if the method
        total will return the correct response"""
        obj = LineItem('banana', 4, .5)
        response = obj.total()

        self.assertEqual(response, 2.0)

    def test_total_ana(self):
        """this test will verify if the method
        total will return the correct response"""
        obj = LineItem('apple', 10, 1.5)
        response = obj.total()

        self.assertEqual(response, 15.0)


class OrderTest(TestCase):
    def test_total_joe_fidelity_promo(self):
        """test to verify the return of the method
        total"""
        joe = Customer('John Doe', 0)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5)]
        order = Order(joe, cart, FidelityPromo())
        self.assertEqual(order.total(), 17.0)

    def test_total_ana_fideliy_promo(self):
        """test to verify the return of the method
        total"""
        ana = Customer('Ana Smith', 1100)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
                LineItem('watermellon', 5, 5.0)]
        order = Order(ana, cart, FidelityPromo())

        self.assertEqual(order.total(), 42.0)

    def test_total_joe_bulk_item_promo(self):
        """test to verify the return of the method
        total"""
        joe = Customer('John Doe', 0)
        cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
        order = Order(joe, cart, BulkItemPromo())
        self.assertEqual(order.total(), 30.0)

    def test_total_joe_bulk_item_promo_long_order(self):
        """test to verify the return of the method
        total"""
        joe = Customer('John Doe', 0)
        cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
        order = Order(joe, cart, BulkItemPromo())
        self.assertEqual(order.total(), 10.0)

    def test_total_ana_bulk_item_promo(self):
        """test to verify the return of the method
        total"""
        ana = Customer('Ana Smith', 1100)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
                LineItem('watermellon', 20, 5.0)]
        order = Order(ana, cart, BulkItemPromo())

        self.assertEqual(order.total(), 117.0)

    def test_due_joe_fidelity_promo(self):
        """test to verify the return of the method
        due"""
        joe = Customer('John Doe', 0)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5)]
        order = Order(joe, cart, FidelityPromo())
        self.assertEqual(order.due(), 17.0)

    def test_due_ana_fideliy_promo(self):
        """test to verify the return of the method
        due"""
        ana = Customer('Ana Smith', 1100)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
                LineItem('watermellon', 5, 5.0)]
        order = Order(ana, cart, FidelityPromo())

        self.assertEqual(order.due(), 39.9)

    def test_due_joe_bulk_item_promo(self):
        """test to verify the return of the method
        due"""
        joe = Customer('John Doe', 0)
        cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
        order = Order(joe, cart, BulkItemPromo())
        self.assertEqual(order.due(), 28.5)

    def test_due_joe_bulk_item_promo_long_order(self):
        """test to verify the return of the method
        due"""
        joe = Customer('John Doe', 0)
        cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
        order = Order(joe, cart, BulkItemPromo())
        self.assertEqual(order.due(), 10.0)

    def test_due_ana_bulk_item_promo(self):
        """test to verify the return of the method
        total"""
        ana = Customer('Ana Smith', 1100)
        cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),
                LineItem('watermellon', 20, 5.0)]
        order = Order(ana, cart, BulkItemPromo())

        self.assertEqual(order.due(), 107.0)

    def test_total_joe_large_order_promo_with_long_order(self):
        """test to verify the return of the method
        total"""
        joe = Customer('John Doe', 0)
        cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
        order = Order(joe, cart, LargeOrderPromo())
        self.assertEqual(order.total(), 10.0)

    def test_due_joe_large_order_promo_with_long_order(self):
        """test to verify the return of the method
        due"""
        joe = Customer('John Doe', 0)
        cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
        order = Order(joe, cart, LargeOrderPromo())
        self.assertEqual(order.due(), 9.3)
