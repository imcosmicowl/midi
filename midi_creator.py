from midiutil.MidiFile import MIDIFile
from midi2audio import FluidSynth


def write_midi_file(midi_file, filename: str = "out.midi"):
    """
    writes midi into a file
    :param midi_file:
    :param filename:
    :return:
    """
    with open(filename, "wb") as midi_file:
        mf.writeFile(midi_file)


def midi2wave(midifile, outputfile='output.wav'):
    fs = FluidSynth()
    fs.midi_to_audio(midifile, outputfile)


if __name__ == '__main__':
    # create your MIDI object
    track = 0  # Track numbers are zero-origined
    channel = 0  # MIDI channel number
    pitch = 60  # MIDI note number
    time = 0  # In beats
    duration = 1  # In beats
    volume = 100  # 0-127, 127 being full volume

    mf = MIDIFile(1)  # only 1 track
    track = 0  # the only track

    time = 0  # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)
    program = 86
    mf.addProgramChange(track, channel, time, program)

    # add some notes
    channel = 0
    volume = 100

    pitch = 60  # C4 (middle C)
    time = 0  # start on beat 0
    duration = 1  # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)

    pitch = 64  # E4
    time = 2  # start on beat 2
    duration = 1  # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)

    pitch = 67  # G4
    time = 4  # start on beat 4
    duration = 1  # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)

    # write it to disk
    with open("output.mid", 'wb') as outf:
        mf.writeFile(outf)

    midi2wave("output.mid")
