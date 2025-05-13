import random
import time
import tracemalloc
from io import StringIO
from collections import Counter
tracemalloc.start()


# PURPOSE:
# This program generates a random DNA sequence in FASTA format based on user input.
# It inserts the user's name into the sequence, calculates nucleotide composition,
# and saves the sequence to a file in FASTA format.

def generate_dna_sequence_to_file(filename, length, description, name):
    """Generates a random DNA sequence and inserts the user's name at a random position."""
    # Nucleotides that make up a DNA sequence
    #nucleotides = ['A', 'C', 'G', 'T']
    # MODIFIED 0 (we don't need to store individual nucleotides)
    nucleotides = 'ACGT'
    #with immutable strings, the performance is faster and peak memory smaller.
    # buffer = io.StringIO()
    # MODIFIED 1
    # Generate a random sequence of specified length
    # overhead from repeated generator calls and function lookups
    # sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    # MODIFIED 0
    # buffer.write(''.join(random.choices(nucleotides, k=length)))
    # MODIFIED 1
    #seq = ''.join(random.choices(nucleotides, k=length))
    #MODIFIED 2
    # Insert the user's name at a random position
    # random_position = random.randint(0, len(sequence))
    # MODIFIED 0 (creating a new random object is memory extensive)
    pos = random.randint(0, length)
    #sequence = sequence[:random_position] + name + sequence[random_position:]
    # MODIFIED 0
    #seq = buffer.getvalue()
    # MODIFIED 1
    counts = {'A':0, 'T':0, 'G':0, 'C':0}
    total_len=0
    with open(filename, "w") as f:
        f.write(">seq {description}\n")
        buffer = StringIO()
        for i in range(length):
            if i == pos:
                buffer.write(name)
            nt = random.choice(nucleotides)
            buffer.write(nt)
            counts[nt]+=1
            total_len+=1
            if i % 1000 == 0:  # Every 1000 nts, flush to disk
                f.write(buffer.getvalue())
                buffer = StringIO()
        f.write(buffer.getvalue())  # Flush remaining
    #counts = Counter(seq)
    #MODIFIED 2
    #final_seq = seq[:pos] + name + seq[pos:]
    #MODIFIED 2
    #return sequence
    #changed to returning sequence and counts
    #MODIFIED2
    #return final_seg, seq, counts
    return total_len, counts



def calculate_statistics(total_length, counts):
    """Calculates and returns the nucleotide percentages and CG/AT ratio."""
    # Calculate nucleotide counts
    # I believe counting the entire seq for letter occurences is very inefficent, better to
    # pass it from the previous method when generating
    #A_count = sequence.count('A')
    #C_count = sequence.count('C')
    #G_count = sequence.count('G')
    #T_count = sequence.count('T')

    # Calculate total sequence length (excluding the name inserted)
    #total_length = len(sequence)
    #MODIFIED 2
    #for nucleotide, count in counts.items():
    #MODIFIED 2
    #print(f"{nucleotide}: {count, count / total_length * 100:}")
    #MODIFIED 2
    print("Nucleotide composition (%):")
    for nt in "ACGT":
        count = counts[nt]
        percent = (count / total_length) * 100
        print(f"{nt}: {count} ({percent:.2f}%)")

    # Percentages of each nucleotide
    #better to not have it hard-coded
    #A_percent = (A_count / total_length) * 100
    #C_percent = (C_count / total_length) * 100
    #G_percent = (G_count / total_length) * 100
    #T_percent = (T_count / total_length) * 100
    # CG and AT ratios
    #cg_ratio = (C_count + G_count) / (A_count + T_count) * 100
    cg = counts['C'] + counts['G']
    at = counts['A'] + counts['T']
    ratio = (cg / at * 100) if at != 0 else 0
    print(f"CG/AT Ratio: {ratio:.2f}%")

    # Return the statistics
    #return A_percent, C_percent, G_percent, T_percent, cg_ratio


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
    #MODIFIED 3 (Added input constraints)
    if sequence_length <= 0:
        raise ValueError("Sequence length must be greater than 0.")
    sequence_id = input("Enter the sequence ID: ")
    description = input("Provide a description of the sequence: ")
    user_name = input("Enter your name: ")
    if not (sequence_id and description and user_name.isalpha()):
        raise ValueError("Invalid input. Please provide all input data")
    start_time = time.time()
    # Generate the DNA sequence
    file_name = f"{sequence_id}.fasta"
    total_len, counts = generate_dna_sequence_to_file(file_name, sequence_length,description, user_name)

    # Save the sequence to a FASTA file
    #MODIFIED 2 (we don't need this method anymore)
    #save_to_fasta(sequence_id, description, final)

    # Calculate statistics
    calculate_statistics(total_len, counts)
    #del sequence, final, counts
    '''
    # Display sequence statistics
    print("Sequence statistics:")
    print(f"A: {A_percent:.1f}%")
    print(f"C: {C_percent:.1f}%")
    print(f"G: {G_percent:.1f}%")
    print(f"T: {T_percent:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")
    '''
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    snap_before = tracemalloc.take_snapshot()
    main()
    snap_after = tracemalloc.take_snapshot()
    curr, peak = tracemalloc.get_traced_memory()
    print(f"Total memory used: {curr/1024:.2f} KiB")  # current = memory used at end
    print(f"Peak memory usage: {peak/1024:.2f} KiB")  # peak = highest usage

