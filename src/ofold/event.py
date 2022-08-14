class Event:
  """Represents a musical event. Can have a pitch and duration.
  
  Parameters
  ----------
  pitch: float
    MIDI note number
  duration: float
    duration where 1 - whole note 0.5 - half note and likewise
  """
  def __init__(self, pitch, duration):
    self.pitch = pitch
    self.duration = duration

def parse_variable_name(name):
  """Will try to parse an omn style variable name into event list.
  
  Parameters
  ----------
  name: string
    note name of the style cs4g4 etc
     
  Returns
  -------
  A list of Events
  """
  state_graph = {
    "start" : ["note"],
    "note" : ["octave", "accidental", "end"],
    "accidental" : ["octave"],
    "octave" : ["note", "end"],
    "end" : None
  }
  characters = {
    "note" : ["c", "d", "e", "f", "g", "a", "b"],
    "accidental" : ["b", "s"],
    "octave" : ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  }
