def generate_melody(num_notes=32, key='C', scale='major'):
    """
    Generate a random melody using Magenta's music API.
    
    :param num_notes: Number of notes in the melody.
    :param key: The key of the melody (e.g., 'C').
    :param scale: The scale of the melody (e.g., 'major').
    :return: A NoteSequence containing the generated melody.
    """
    # Define a basic scale
    if scale == 'major':
        scale_intervals = [0, 2, 4, 5, 7, 9, 11]  # Major scale intervals
    elif scale == 'minor':
        scale_intervals = [0, 2, 3, 5, 7, 8, 10]  # Minor scale intervals
    else:
        raise ValueError("Scale must be 'major' or 'minor'")

    # Create a NoteSequence
    melody = music_pb2.NoteSequence()

    # Generate random notes in the scale
    for i in range(num_notes):
        note_pitch = np.random.choice(scale_intervals) + 60  # Middle C as base
        note_duration = np.random.choice([0.25, 0.5, 1.0])  # Quarter, half, or whole note
        start_time = i * 0.5  # Space notes evenly by 0.5 seconds

        # Add the note to the sequence
        melody.notes.add(
            pitch=note_pitch,
            start_time=start_time,
            end_time=start_time + note_duration,
            velocity=80
        )
    
    melody.total_time = num_notes * 0.5
    melody.tempos.add(qpm=120)  # Set tempo to 120 BPM
    return melody

# Generate a melody
melody_sequence = generate_melody()

# Save to a MIDI file
mm.sequence_proto_to_midi_file(melody_sequence, "generated_melody.mid")
print("Melody generated and saved as 'generated_melody.mid'")