from ofold.utils import degree_to_note

def test_degree_to_note():
    assert(degree_to_note(60, 0, 0) == 60)
    a_minor = [57, 59, 60, 62, 64, 65, 67]
    for degree in range(7):
        assert(degree_to_note(57, 5, degree) == a_minor[degree])
    a_minor_ = [note - 12 for note in a_minor]
    a_minor_.reverse()
    for degree in range(7):
        assert(degree_to_note(57, 5, -degree) == a_minor_[degree])
