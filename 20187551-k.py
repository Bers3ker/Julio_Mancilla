def comparar_vlans_native(vlan_native, vlans):
    mensaje = "Las vlans son iguales y cumplen con el requerimiento" if vlan_native == vlans[0] else "Las vlans son diferentes y no cumplen con el requerimiento"
    print(mensaje)

def comparar_vlans(vlans_input, vlans):
    vlans_input_list = list(map(int, vlans_input.split(',')))
    mensaje = "Las vlans son iguales y cumplen con el requerimiento" if vlans_input_list == vlans else "Las vlans son diferentes y no cumplen con el requerimiento"
    print(mensaje)

def main():
    
    vlansw1 = [10, 20, 30]
    navsw1 = 99

    
    vlansw2 = [40, 50, 60]
    navsw2 = 200

    resp1 = int(input("Ingresar Vlan Nativa SW1: "))
    comparar_vlans_native(resp1, [navsw1])

    resp2 = input("Ingresar Vlans del SW1 separadas por comas (por ejemplo, '10,20,30'): ")
    comparar_vlans(resp2, vlansw1)

    resp3 = int(input("Ingresar Vlan Nativa SW2: "))
    comparar_vlans_native(resp3, [navsw2])

    resp4 = input("Ingresar Vlans del SW2 separadas por comas (por ejemplo, '40,50,60'): ")
    comparar_vlans(resp4, vlansw2)

if __name__ == "__main__":
    main()

