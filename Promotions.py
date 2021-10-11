class Promotions():
    def __init__(self, code_prom, discount_percent):
        self.code_prom = code_prom
        self.discount_percent = discount_percent

    def show_promotion(self):
        """[Retorna la informacion de la promocion]
        """
        return (f"Promotion's Code: {self.code_prom}\nDiscount Percentage: {self.discount_percent}%")