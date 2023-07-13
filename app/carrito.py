class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def Add(self, paquete):
        id = str(paquete.id)
        if str(paquete.id) not in self.carrito.keys():
            self.carrito[id]={
                "paquete_id": paquete.id,
                "nombre": paquete.nombre,
                "precio": paquete.precio,
                "cantidad": 1,
            }      
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += paquete.precio      
        self.Save()

    def Save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def Remove(self, paquete):
        id = str(paquete.id)
        if str(paquete.id) in self.carrito.keys():
            del self.carrito[id]
        self.Save()

    def Sub(self, paquete):
        id = str(paquete.id)
        if str(paquete.id) in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= paquete.precio
            if self.carrito[id]["cantidad"] <= 0: self.Remove(paquete) 
        self.Save() 

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True