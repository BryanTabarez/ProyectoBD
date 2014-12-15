class FormulaMedica():
    "Formula medica"
    def __init__(self, num_registro, cod_medicamento, cantidad):
        self.__num_registro = num_registro
        self.__cod_medicamento = cod_medicamento
        self.__cantidad = cantidad

    def get_num_registro(self):
        return self.__num_registro

    def get_cod_medicamento(self):
        return self.__cod_medicamento

    def get_cantidad(self):
        return self.__cantidad

    def set_num_registro(self, num_registro):
        self.__num_registro = num_registro

    def set_cod_medicamento(self, cod_medicamento):
        self.__cod_medicamento = cod_medicamento

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
