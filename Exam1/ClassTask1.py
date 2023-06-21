class ProductOrder:
    def __init__(self, order_id, product_dict, price_dict):
        self.order_id = order_id
        self.product_dict = product_dict
        self.price_dict = price_dict

    def __repr__(self):
        return f'Order("#{self.order_id}", Products {self.product_dict})'

    def calc_order_cost(self):
        total_cost = 0
        keys = self.product_dict.keys()
        for i in self.product_dict:
            total_cost += self.product_dict[i] * self.price_dict[i]

        return total_cost


class MemberProductOrder(ProductOrder):
    def __init__(self, order_id, product_dict, price_dict, membership='Regular'):
        ProductOrder.__init__(self, order_id, product_dict, price_dict)
        self.membership = membership

    def __repr__(self):
        return f'{self.membership} Order("#{self.order_id}", Products {self.product_dict})'



        return total_cost
