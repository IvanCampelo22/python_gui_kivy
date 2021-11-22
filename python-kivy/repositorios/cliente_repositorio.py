from fabricas import fabricar_conexao


class ClienteRepositorio():

    @staticmethod
    def listar_clientes():
        fabrica = fabricar_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("select * from cliente")
            return cursor.fetchall()
        finally:
            fabrica.close()

    @staticmethod
    def inserir_clientes(cliente):
        fabrica = fabricar_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("insert into cliente (nome, idade) values (%s, %s)", (cliente.nome, cliente.idade))
        finally:
            fabrica.close()

    @staticmethod
    def editar_cliente(id_cliente, cliente):
        fabrica = fabricar_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("update cliente set nome=%(nome)s, idade=%(idade)s where idcliente=%(id_cliente)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))
        finally:
            fabrica.close()

    @staticmethod
    def remover_cliente(id_cliente):
        fabrica = fabricar_conexao.FabricaConexao.conectar()
        try:
            cursor = fabrica.cursor()
            cursor.execute("delete from cliente where idcliente=%s", (id_cliente,))
        finally:
            fabrica.close()
