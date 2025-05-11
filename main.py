import random
import time
import os


# PURPOSE:
# This program generates a random DNA sequence in FASTA format based on user input.
# It inserts the user's name into the sequence, calculates nucleotide composition,
# and saves the sequence to a file in FASTA format.

def generate_dna_sequence(length, name):
    """Generates a random DNA sequence and inserts the user's name at a random position."""
    # Nucleotides that make up a DNA sequence
    nucleotides = ['A', 'C', 'G', 'T']  # (we don't need to store individual nucleotides)

    # Generate a random sequence of specified length
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))

    # Insert the user's name at a random position
    random_position = random.randint(0, len(sequence))
    sequence = sequence[:random_position] + name + sequence[random_position:]

    return sequence


def calculate_statistics(sequence):
    """Calculates and returns the nucleotide percentages and CG/AT ratio."""
    # Calculate nucleotide counts
    A_count = sequence.count('A')
    C_count = sequence.count('C')
    G_count = sequence.count('G')
    T_count = sequence.count('T')

    # Calculate total sequence length (excluding the name inserted)
    total_length = len(sequence)

    # Percentages of each nucleotide
    A_percent = (A_count / total_length) * 100
    C_percent = (C_count / total_length) * 100
    G_percent = (G_count / total_length) * 100
    T_percent = (T_count / total_length) * 100

    # CG and AT ratios
    cg_ratio = (C_count + G_count) / (A_count + T_count) * 100

    # Return the statistics
    return A_percent, C_percent, G_percent, T_percent, cg_ratio


def save_to_fasta(sequence_id, description, sequence):
    """Saves the sequence to a FASTA file with the name as the sequence ID."""
    file_name = f"{sequence_id}.fasta"
    with open(file_name, "w") as file:
        file.write(f">{sequence_id} {description}\n")
        file.write(sequence)
    print(f"The sequence was saved to the file {file_name}")


def main():
    # Get user inputs
    sequence_length = int(input("Enter the sequence length: "))
    sequence_id = input("Enter the sequence ID: ")
    description = input("Provide a description of the sequence: ")
    user_name = input("Enter your name: ")

    # Generate the DNA sequence
    sequence = generate_dna_sequence(sequence_length, user_name)

    # Save the sequence to a FASTA file
    save_to_fasta(sequence_id, description, sequence)

    # Calculate statistics
    A_percent, C_percent, G_percent, T_percent, cg_ratio = calculate_statistics(sequence)

    # Display sequence statistics
    print("Sequence statistics:")
    print(f"A: {A_percent:.1f}%")
    print(f"C: {C_percent:.1f}%")
    print(f"G: {G_percent:.1f}%")
    print(f"T: {T_percent:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
