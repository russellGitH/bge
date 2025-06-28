class Scene:
    name='Scene'
    objects= {}
    pass

class sensor:
    def returnState(self):
        return True
    positive = returnState
    pass
class sensors:
    def __getitem__(self, item):
        return sensor()
    pass

class worldPosition:
    x=y=z=0.0

class blenderObject:
    data=None
    def copy(self):
        pass
    
class gameObject:
    name='Cube'
    worldPosition = worldPosition()
    def __init__(self):
        Scene.objects[self.name]=self
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
        
    def get(self,value): #if own.get('start'):own['start']
        if hasattr(self,value):return True
        else:return False
        
    def replaceMesh(self, mesh_name='',visual=True,phys=True):
        pass

    def endObject(self):
        self=None
    
    #Text object
    blenderObject=blenderObject()
    
class controller:
    owner = gameObject()
    sensors = sensors()

class logic:
    @classmethod
    def getCurrentController(cls):
        return controller()
        pass

    @classmethod
    def getCurrentScene(cls):
        return Scene()
        pass

    pass
