from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.seat = None
        self.engine = None
        self.computer = None
        self.gps = None

class Manual:
    def __init__(self):
        self.content = []
    
    def add_content(self, content):
        self.content.append(content)


class Manual():
    pass

class Builder(ABC):

    @abstractmethod
    def reset(self)->None:
        pass

    @abstractmethod
    def setSeats(self, seat:int)->None:
        pass
    
    @abstractmethod
    def setEngine(self, engine:str)->None:
        pass

    @abstractmethod
    def setTripComputer(self, computer:str)->None:
        pass

    @abstractmethod
    def setGPS(self, gps:bool):
        pass
    
class CarBuilder(Builder):
    def __init__(self)->None:
        self.reset()
    
    def reset(self)->None:
        self._car = Car()
    
    def setSeats(self, seat:int):
        self._car.seat = seat

    def setEngine(self, engine:str):
        self._car.engine = engine
    
    def setTripComputer(self, computer:str):
        self._car.computer = computer
    
    def setGPS(self, gps:bool):
        self._car.gps = gps
    
    def getResult(self):
        product  = self._car
        return product

class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()
    
    def reset(self)->None:
        self._manual = Manual()
    
    def setSeats(self, seats:int)->None:
        self.manual.add_content(f"Seats: {seats}")
    
    def setEngine(self,engine:str)->None:
        self.manual.add_content(f"Engine: {engine}")
    
    def setTripComputer(self, computer:str)->None:
        self.manual.add_content(f"Trip Computer: {computer}")
    
    def setGps(self, gps:bool)->None:
        self.manual.add_content(f"Gps: {gps}")
    
    def getResult(self, gps:bool)->None:
        result = self.manual
        return result

class Director():
    def makeFerarri(self, builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine("Ferarri manchine")
        builder.setGps(True)
        builder.setTripComputer("Debian os")

    def makeSuv(self, builder):
        builder.reset()
        builder.setSeats(4)
        builder.setEngine("Mercedez benz ")
        builder.setGps(True)
        builder.setTripComputer("Mercedez os")

class Application:
    def make_car(self):
        director = Director()
        car_builder = CarBUilder()
