numero_acl_ipv4 = int(input("¿Cuál es el número de ACL IPv4? "))

if 1 <= numero_acl_ipv4 <= 99:
    print("Esta es una ACL IPv4 estándar.")
elif 100 <= numero_acl_ipv4 <= 199:
    print("Esta es una ACL IPv4 extendida.")
else:
    print("Esto no es una ACL IPv4 estándar o extendida.")