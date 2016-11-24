

class DataObj:
    data = {}


class Step(DataObj):
    position = [0.,0.,0.]


class Track(DataObj):
    steps = []


class Event(DataObj):
    tracks=[]


class Run(DataObj):
    events=[]
