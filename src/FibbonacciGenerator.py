from typing import List


def generate_fibonacci_sequence(
    n_elements: int, sequence: List[int] = None
) -> List[int]:
    """
    Generate a Fibonacci sequence of length n_elements.

    Args:
        n_elements (int): The length of the Fibonacci sequence to generate.
        sequence (List[int]): The current state of the Fibonacci sequence.

    Returns:
        List[int]: A list containing the first N Fibonacci numbers.
    """
    if n_elements < 0:
        raise ValueError("n_elements must be greater than or equal to 0")

    if sequence is None:
        sequence = []

    while len(sequence) < n_elements:
        if len(sequence) < 2:
            sequence.append(len(sequence))
        else:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

    return sequence[:n_elements]
