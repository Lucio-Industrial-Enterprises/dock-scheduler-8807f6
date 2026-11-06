import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_base_fees_and_weight_rates(self):
        for zone, weight, expected in (
            ("local", 0.5, 5.75),
            ("local", 1, 6.5),
            ("local", 4, 11.0),
            ("regional", 0.5, 8.75),
            ("regional", 1, 9.5),
            ("regional", 4, 14.0),
        ):
            with self.subTest(zone=zone, weight=weight):
                self.assertEqual(shipping_quote(weight, zone), expected)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
