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
    time = 0  # In beats
    volume = 127  # 0-127, 127 being full volume

    mf = MIDIFile(1)  # only 1 track
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)
    program = 95 # instrument
    mf.addProgramChange(track, channel, time, program)

    # add some notes
    channel = 0

    time = 0  # start on beat 0
    duration = 16  # In beats
    mf.addNote(track, channel, 97, time, duration, volume)
    mf.addNote(time, channel, 12, time, duration, volume)

    time = 16
    duration = 16
    mf.addNote(track, channel, 104, time, duration, volume)
    mf.addNote(track, channel, 20, time, duration, volume)

    # write it to disk
    with open("output.mid", 'wb') as outf:
        mf.writeFile(outf)

    midi2wave("output.mid")
