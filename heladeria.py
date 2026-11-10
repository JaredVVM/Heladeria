
class helado():
     def __init__(self, sabores):
        self.sabores = sabores

     def preparar_helado(self):
           for ing, cant in self.inventario.items():
                    if inventario.get(ing, 0) < cant:
                        print(f"No hay suficiente {ing}")
                        return

           for ing, cant in self.inventario.items():
                inventario[ing] -= cant
           
class cono():
      def __init__(self, inventario_cono):
            self.inventario = inventario_cono

      def preparar_cono(self):
        for ing, cant in self.inventario.items():
                    if inventario.get(ing, 0) < cant:
                        print(f"No hay suficiente {ing}")
                        return

        for ing, cant in self.inventario.items():
                inventario[ing] -= cant
          
cono_chico = cono({"cono_chico": 1})    
cono_mediano = cono( {"cono_mediano": 1} ) 
cono_grande = cono({"cono_grande": 1})

helado_vainilla   = helado({"Vainilla": 1, "Vainilla": 1, "Extras": 0})
helado_chocolate  = helado({"Chocolate": 1, "Chocolate": 0, "Extras": 0})
helado_fresa      = helado({"Fresa": 1, "Fresa": 0, "Extras": 0})
helado_mango      = helado({"Mango": 1, "Mango": 0, "Extras": 0})
helado_limon      = helado({"Limon": 1, "Limon": 0, "Extras": 0})
helado_coco       = helado({"Coco": 1, "Coco": 0, "Extras": 0})
helado_nuez       = helado({"Nuez": 1, "Nuez": 0, "Extras": 0})
helado_piñon      = helado({"Piñon": 1, "Piñon": 0, "Extras": 0})
helado_galleta    = helado({"Galleta": 1, "Galleta": 0, "Extras": 0})
helado_cafe       = helado({"Cafe": 1, "Cafe": 0, "Extras": 0})
helado_platano    = helado({"Platano": 1, "Platano": 0, "Extras": 0})
helado_guayaba    = helado({"Guayaba": 1, "Guayaba": 0, "Extras": 0})
helado_tamarindo  = helado({"Tamarindo": 1, "Tamarindo": 0, "Extras": 0})
helado_durazno    = helado({"Durazno": 1, "Durazno": 0, "Extras": 0})
helado_sandia     = helado({"Sandia": 1, "Sandia": 0, "Extras": 0})
helado_queso_mora = helado({"Queso": 1, "Mora": 1, "Extras": 0})
helado_pistache   = helado({"Pistache": 1, "Pistache": 0, "Extras": 0})
helado_queso      = helado({"Queso": 1, "Queso": 0, "Extras": 0})
helado_zarzamora  = helado({"Zarzamora": 1, "Zarzamora": 0, "Extras": 0})
helado_maracuya   = helado({"Maracuya": 1, "Maracuya": 0, "Extras": 0})
helado_ninguno    = helado({"Ninguno": 0, "Chocolate":0, "sandia": 0 })

inventario = {
    "Vainilla": 10, "Chocolate": 10, "Fresa": 10, "Mango": 10,
    "Limon": 10, "Coco": 10, "Nuez": 10, "Piñon": 10,
    "Galleta": 10, "Cafe": 10, "Platano": 10, "Guayaba": 10,
    "Tamarindo": 10, "Durazno": 10, "Sandia": 10, "Melon": 10,
    "Pistache": 10, "Queso": 10, "Zarzamora": 10, "Maracuya": 10,
    "cono_chico": 10, "cono_mediano": 10, "cono_grande": 10, "Mora": 1, "Ninguno":1
}

sabores  = [
    "Vainilla", "Chocolate", "Fresa", "Mango",
    "Limon", "Coco", "Nuez", "Piñon",
    "Galleta", "Cafe", "Platano", "Guayaba",
    "Tamarindo", "Durazno", "Sandia",
    "Pistache", "Queso", "Zarzamora", "Maracuya", "Ninguno"
]

tamaños = ["cono_chico", "cono_mediano", "cono_grande"]

while True:
    print("MENU")
    print("Que tamaño de cono desea:")
    print("1. Chico")
    print("2. Mediano")
    print("3. Grande")
    print("4. salir")
    print("5. Mostrar inventario")
    opcion = input("Elegir tamaño")

    if opcion == "1":
        print("Cono chico elegido")
        cono_chico.preparar_cono()
        for i, sabor in enumerate(sabores, start=1):
            print(f"{i}. {sabor} (Inventario: {inventario[sabor]})")
        eleccion1 = int(input("Elige tu primer sabor: "))
        eleccion2 = int(input("Elige tu segundo sabor: "))
        if 1 <= eleccion1 <= len(sabores) and 1 <= eleccion2 <= len(sabores):
                    sabor1 = sabores[eleccion1 - 1]
                    sabor2 = sabores[eleccion2 - 1]

                    if inventario[sabor1] > 0 and inventario[sabor2] > 0:
                        inventario[sabor1] -= 1
                        inventario[sabor2] -= 1
                        print(f"Has pedido un cono chico de {sabor1} y {sabor2}.")
                    else:
                        print("Alguno de los sabores está agotado.")

    if opcion == "2":
        print("Cono mediano elegido")
        cono_mediano.preparar_cono()
        for i, sabor in enumerate(sabores, start=1):
            print(f"{i}. {sabor} (Inventario: {inventario[sabor]})")
        eleccion1 = int(input("Elige tu primer sabor: "))
        eleccion2 = int(input("Elige tu segundo sabor: "))
        if 1 <= eleccion1 <= len(sabores) and 1 <= eleccion2 <= len(sabores):
                    sabor1 = sabores[eleccion1 - 1]
                    sabor2 = sabores[eleccion2 - 1]

                    if inventario[sabor1] > 0 and inventario[sabor2] > 0:
                        inventario[sabor1] -= 1
                        inventario[sabor2] -= 1
                        print(f"Has pedido un cono mediano de {sabor1} y {sabor2}.")
                    else:
                        print("Alguno de los sabores está agotado.")

    if opcion == "3":
        print("Cono mediano elegido")
        cono_mediano.preparar_cono()
        for i, sabor in enumerate(sabores, start=1):
            print(f"{i}. {sabor} (Inventario: {inventario[sabor]})")
        eleccion1 = int(input("Elige tu primer sabor: "))
        eleccion2 = int(input("Elige tu segundo sabor: "))
        if 1 <= eleccion1 <= len(sabores) and 1 <= eleccion2 <= len(sabores):
                    sabor1 = sabores[eleccion1 - 1]
                    sabor2 = sabores[eleccion2 - 1]

                    if inventario[sabor1] > 0 and inventario[sabor2] > 0:
                        inventario[sabor1] -= 1
                        inventario[sabor2] -= 1
                        print(f"Has pedido un cono grande de {sabor1} y {sabor2}.")
                    else:
                        print("Alguno de los sabores está agotado.")


    if opcion == "4":
          break
    
    if opcion == "5":
          print(inventario)
    
  







    
    
    
    
        
     