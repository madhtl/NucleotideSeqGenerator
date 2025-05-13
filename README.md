# DNA Sequence Generator in FASTA Format

## Task Description
This program generates a random DNA sequence consisting of nucleotides (A, C, G, T) based on user input. It outputs the generated sequence in **FASTA format**, inserts the user's name at a random position, and calculates and displays sequence statistics, including nucleotide composition and the **CG/AT ratio**. Additionally, it saves the sequence to a **FASTA file**, ensuring the sequence ID and description are included in the header.

### Requirements:
1. **DNA Sequence Generation**: 
   - The program generates a random DNA sequence consisting of nucleotides (A, C, G, T).
2. **User Input**:
   - The program asks the user for:
     - The length of the sequence (specified via `input()`).
     - The name (ID) of the sequence.
     - A description for the sequence.
3. **FASTA File Creation**:
   - The result is saved to a `.fasta` file. The file is named according to the sequence ID provided by the user.
   - The FASTA file header follows this format:
     ```
     >ID description
     ```
   - The generated DNA sequence follows the header.
4. **Sequence Statistics**:
   - The program calculates:
     - The percentage of each nucleotide (A, C, G, T).
     - The ratio of C + G nucleotides to A + T nucleotides.
5. **Name Insertion**:
   - The user's name is inserted at a random position in the sequence, but it does not affect the nucleotide statistics or sequence length.

---

## Changes and Performance Optimization
### Initial Implementation
The first version of the program (referred to as **MODIFIED 0**) was based on the AI-generated solution. We focused on basic functionality but later realized the need for performance improvements as the program handled larger datasets.
#### Test case (Ai Code):
Enter the sequence length: 10000
Enter the sequence ID: 123
Provide a description of the sequence: abc
Enter your name: Katarzyna
Execution time: 0.0177 seconds
Total memory used: 5.69 KiB
Peak memory usage: 96.54 KiB

### Performance Improvements
**Optimization 1**: Switching from a list of nucleotides to a string improved memory efficiency and reduced peak memory usage. Execution time was also decreased.
Execution time: 0.0162 seconds
Peak memory usage: 96.50 KiB

**Optimization 2**: Further optimization was achieved by using a file-like object that operates entirely in RAM, reducing execution time by 3x compared to the previous version.
#### Improved Results:
Execution time: 0.0049 seconds
Total memory used: 5.74 KiB
Peak memory usage: 96.19 KiB

**Optimization 3**: Trying to optimize file-writing methods led to using buffers. However, buffers introduced more memory usage. Hence, further fine-tuning resulted in the most efficient approach.
#### Final Results:
Execution time: 0.0249 seconds
Total memory used: 4.90 KiB
Peak memory usage: 27.44 KiB
## Code Optimization & Conclusion
After testing several methods and comparing their performance, the following approach was found to be the most memory-efficient while maintaining optimal execution time. The performance improvements are evident in the statistics above, where we minimized memory usage and execution time significantly.

---

## Simple Constraints (Handling User Input)
To ensure that users provide valid inputs and avoid potential errors, the program implements basic constraints when collecting input.





