from typing import List, Union, Dict


class VectorUnsorted:
    def __init__(self, size) -> None:
        self.__size = size
        self.__pointer = -1
        self.__vector = []

    def __empty(self) -> str:
        return f"Lista vazia"

    def length(self):
        return len(self.__vector)

    # GET all / item
    def get_all(self) -> Union[Dict[int, int], str]:
        if self.__pointer == -1:
            return self.__empty()
        dic = {}
        for i in range(self.length()):
            dic.update({i: self.__vector[i]})
        return dic

    def get_item(self, item: int) -> Union[Dict[str, int], str]:
        if self.__pointer == -1:
            return self.__empty()
        else:
            for ind, _ in enumerate(self.__vector):
                if self.__vector[ind] == item:
                    return {ind: self.__vector[ind]}

            return f"Item {item} não existe na lista"

    def insert_item(self, item: int) -> Union[str, None]:

        if self.__size == (self.__pointer+1):
            return f"Capacidade máxima({self.__size}) atingida "

        if not isinstance(item, int):
            return f"Erro. O tipo do item deve ser int"

        else:
            self.__vector.append(item)
            self.__pointer += 1

    def remove_item(self, item: int = None, indice=None) -> Union[str, None]:

        if indice == None:

            if not isinstance(item, int):
                return f"Erro. O tipo do item deve ser int"

            if self.__pointer == -1:
                return self.__empty()

            else:
                for ind, _ in enumerate(self.__vector):
                    if self.__vector[ind] == item:
                        self.__vector.remove(item)

                        while ind < self.length()-1:
                            self.__vector[ind] = self.__vector[ind+1]
                            ind += 1

                        return f"Item {item} remvido com sucesso"

                return f"Item {item} não existe na lista"

        else:

            if not isinstance(indice, int):
                return f"Erro. O tipo do item deve ser int"

            if self.__pointer == -1:
                return self.__empty()

            else:
                for ind, _ in enumerate(self.__vector):
                    if ind == indice:
                        self.__vector.pop(indice)

                        while ind < self.length()-1:
                            self.__vector[ind] = self.__vector[ind+1]
                            ind += 1

                        return f"Item no índice: {indice}, removido com sucesso"

                return f"Índice {indice} não existe na lista"

    def remove_all_equals(self, item: int = None) -> Union[List[int], str, None]:

        if not isinstance(item, int):
            return f"Erro. O tipo do item deve ser int"

        if self.__pointer == -1:
            return self.__empty()

        if isinstance(self.get_item(item), dict):
            dic = {}
            for ind, i, in enumerate(self.__vector[::-1]):
                if i == item:
                    dic.update({ind: i})
                    self.__vector.remove(i)
                    dic. update({ind: i})

            return f"Removidos:{len(dic)} itens com valor {item}"

        else:

            return f"{item} não existe na lista"
