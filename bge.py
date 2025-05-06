class Scene:
    name='Scene'
    objects= {}
    pass

class sensor:
    def returnState(self):
        return True
    positive = returnState
    pass
class worldPosition:
    x=y=z=0.0

class gameObject:
    name='Cube'
    def __init__(self):
        Scene.objects[self.name]=self
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    worldPosition=worldPosition()
    def endObject(self):
        self=None

class controller:
    owner = gameObject()
    sensors = {'Always':sensor(),'Ray':sensor()}

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