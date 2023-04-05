class Store:
    def __init__(self,max_order) -> None:
        self.max_order=max_order
        self.order=0
    
    def got_call(self):
        if self.order==self.max_order:
            raise RuntimeError('Order Overflow')
        self.order+=1
    def delivery(self):
        if self.order<=0:
            raise RuntimeError('order should not be negative')
        self.order-=1
