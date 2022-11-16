from typing import List, Union, Dict

class VectorUnsorted:
    def __init__(self, size) -> None:
        self.__size = size
        self.__pointer = -1
        self.__vectors = []
    
    def __empty(self)->str:
        return f"Lista vazia"

    def get_all(self)-> Union[List[int], str]:
        if self.__pointer == -1:
            return self.__empty()
        return self.__vectors
    
    def get_item(self, item: int) -> Union[Dict[str, int], str]:
        if self.__pointer == -1:
            return self.__empty()
        else:
            for i in self.__vectors:
                if self.__vectors[i] == item:
                    return {i:self.__vectors[i]}
            
            return f"Item {item} não existe na lista"
        

    
