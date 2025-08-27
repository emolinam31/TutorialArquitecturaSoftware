from abc import ABC, abstractmethod 
from django.http import HttpRequest, HttpResponse

class ImageStorage(ABC):
    
    @abstractmethod #metodo abstracto ( cualquier clase que herede de esta clase debe implementar este metodo )
    
    def store(self, request: HttpRequest):
        pass
    
    