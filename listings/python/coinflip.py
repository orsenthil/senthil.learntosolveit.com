import random
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def Nchoosek(N, k):
    return math.factorial(N) / (math.factorial(k) * math.factorial(N - k))

def binomial(n,k, p):
    return Nchoosek(n, k) * math.pow(p, k) * math.pow(1-p, n-k)


def run_experiment(n_flips, n_experiments, p_heads=0.5):
    """
    Simulate coin flips and count number of heads.

    :param n_flips: Number of coin flips per experiment.
    :param n_experiments: Number of experiments to run.
    :param p_heads: Probability of getting heads (default 0.5 for a fair coin)

    :return: List of head counts for each experiment.
    """
    results = []

    for experiment in range(n_experiments):
        flips = [random.random() < p_heads for _ in range(n_flips)]
        heads_count = sum(flips)
        results.append(heads_count)

    return results


def compare_theoretical_vs_experimental():
    """Compare theoretical binomial distribution with experimental results."""
    # Parameters
    n_flips = 10          # Number of coin flips per experiment
    n_experiments = 1000  # Number of experiments to run
    p_heads = 0.5         # Probability of heads (fair coin)

    # Run the experiment
    print(f"Running {n_experiments} experiments with {n_flips} coin flips each...")
    results = run_experiment(n_flips, n_experiments, p_heads)

    # Count occurrences of each number of heads
    result_counts = Counter(results)

    # Convert to probabilities
    experimental_probs = {k: v/n_experiments for k, v in result_counts.items()}

    # Calculate theoretical probabilities using your binomial function
    theoretical_probs = {k: binomial(n_flips, k, p_heads) for k in range(n_flips + 1)}

    # Prepare data for plotting
    k_values = list(range(n_flips + 1))
    theoretical_values = [theoretical_probs[k] for k in k_values]
    experimental_values = [experimental_probs.get(k, 0) for k in k_values]

    # Plot the results
    plt.figure(figsize=(12, 6))

    # Bar width and positions
    width = 0.35
    x = np.array(k_values)

    # Create bars
    plt.bar(x - width/2, theoretical_values, width, label='Theoretical Probability')
    plt.bar(x + width/2, experimental_values, width, label='Experimental Probability')

    # Add labels and title
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.title(f'Binomial Distribution: {n_flips} coin flips, p(heads)={p_heads}')
    plt.xticks(k_values)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a text box with statistics
    mean_theoretical = n_flips * p_heads
    var_theoretical = n_flips * p_heads * (1 - p_heads)
    mean_experimental = sum(k * count for k, count in result_counts.items()) / n_experiments

    stats_text = f"Theoretical Mean: {mean_theoretical}\n"
    stats_text += f"Theoretical Variance: {var_theoretical}\n"
    stats_text += f"Experimental Mean: {mean_experimental:.2f}"

    plt.figtext(0.15, 0.8, stats_text, bbox=dict(facecolor='white', alpha=0.8))

    # Show plot
    plt.tight_layout()
    #plt.show()
    plt.savefig('coinflip.png')

    # Print summary
    print("\nSummary:")
    print(f"Theoretical Mean: {mean_theoretical}")
    print(f"Theoretical Variance: {var_theoretical}")
    print(f"Experimental Mean: {mean_experimental:.2f}")

    # Print probabilities table
    print("\nProbabilities Table:")
    print("Heads | Theoretical | Experimental | Difference")
    print("-" * 50)
    for k in k_values:
        theo = theoretical_probs[k]
        exp = experimental_probs.get(k, 0)
        diff = exp - theo
        print(f"{k:5d} | {theo:.6f} | {exp:.6f} | {diff:.6f}")

compare_theoretical_vs_experimental()