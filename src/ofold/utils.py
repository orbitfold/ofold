def degree_to_note(root, mode, degree):   
    """Convert a list of relative degrees to midi note numbers.

    Parameters
    ----------
    key - MIDI note number for the root note
    mode - a number for the mode (0 - Ionian (major), 
           1 - Dorian, ..., 5 - Aeolian (minor), ...)
    degree - a scale degree number relative to root (root is 0), can be negative

    Returns
    -------
    an integer signifying MIDI note numbers
    """
    intervals = [2, 2, 1, 2, 2, 2, 1]
    intervals = intervals[mode:] + intervals[:mode]
    scale = [0]
    for interval in intervals:
        scale.append(scale[-1] + interval)
    root_mod = degree // 7
    return (root + 12 * root_mod) + scale[degree % 7]

    
def degrees_to_notes(root, mode, degrees):
    """Convert a list of relative degrees to midi note numbers.

    Parameters
    ----------
    key - MIDI note number for the root note
    mode - a number for the mode (0 - Ionian (major), 
           1 - Dorian, ..., 5 - Aeolian (minor), ...)
    degrees - a list of scale degrees relative to root (root is 0), can be negative

    Returns
    -------
    a list of integers signifying MIDI note numbers
    """
    assert((0 <= root) and (root <= 127))
    assert((0 <= mode) and (mode <= 7))
    return [degree_to_note(root, mode, degree) for degree in degrees]


def degrees_to_midi(root, mode, degrees, durations, filename):
    pass
