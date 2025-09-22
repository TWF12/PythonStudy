class Clock:
    id = None
    price = None
    

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
clock1.ring()


clock2 = Clock()
clock2.id = "002569"
clock2.price = 39.99
clock2.ring()
