from entidades import cliente
from repositorios import cliente_repositorio

clientes = cliente.Cliente("João", 29)

cliente_repositorio.ClienteRepositorio.listar_clientes()
cliente_repositorio.ClienteRepositorio.inserir_clientes(clientes)
#.ClienteRepositorio.editar_cliente(1, clientes)
#cliente_repositorio.ClienteRepositorio.remover_cliente(25)
