
class Complejo:
    
    def __int__(self,real,imaginario):
        
        self.imaginario = imaginario
        self.real = real 
        self.norma      
    def conjugado(self):
        self.real=-real
        self.imaginario=-imaginario
        
    def calcula_norma(self):
        self.norma=((self.real)**2+(self.imaginario)**2)**(1/2)      
    def pow(self,n):
        
        numero= self.real+ 1j*self.imaginario
        numero1= numero**n
        c= Complejo(numero1.real,numero1.imaginario)
        return c
        
            
        
        
        
