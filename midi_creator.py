from midiutil.MidiFile import MIDIFile
from midi2audio import FluidSynth


def write_midi_file(midi_object, filename: str = "out.midi") -> None:
    """
    Writes midi object into a file.

    :param midi_object:
    :param filename: str
            Filename to store mide object.
    :return:
    """
    with open(filename, "wb") as outf:
        midi_object.writeFile(outf)


def midi2wave(midifile: str, output_file: str = 'output.wav'):
    """
    Transform midi file into .wav file.

    :param midifile: str
            Midi filename location.
    :param output_file: str
            Filename to store .wav.
    :return:
    """
    fs = FluidSynth()
    fs.midi_to_audio(midifile, output_file)


# TODO:
# extend function functionality.
def pleasant_loop(midi_object, loop_duration: int, length: int) -> None:
    """
    Creates pleasant loop from midi_object.

    :param midi_object:
            Midi object.
    :param loop_duration: int
            Total loop duration.
    :param length: int
            Duration of every note.
    :return: None
    """

    for step in range(loop_duration):
        midi_object.addNote(track, channel, 108, step, length, volume)


if __name__ == '__main__':
    # create your MIDI object
    track = 0  # Track numbers are zero-origined
    channel = 0  # MIDI channel number
    time = 0  # In beats
    volume = 127  # 0-127, 127 being full volume

    mf = MIDIFile(1)  # only 1 track
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)
    # 89 muy mystic
    # 90 = q 89 xro un poco reber y expanded
    # 93 chachistic but short
    # 94 cool but short
    # 95 most mystic & relaxing
    # 73 piccolo
    # 52 mystic but in mid range freq

    program = 95  # instrument
    mf.addProgramChange(track, channel, time, program)

    # add some notes
    channel = 0

    time = 0  # start on beat 0
    duration = 16  # In beats
    mf.addNote(track, channel, 108, time, duration, volume)
    mf.addNote(time, channel, 98, time, duration, volume)

    time = 16
    duration = 16
    mf.addNote(track, channel, 115, time, duration, volume)
    mf.addNote(track, channel, 105, time, duration, volume)

    # write it to disk
    write_midi_file(mf)

    midi2wave("out.midi")
