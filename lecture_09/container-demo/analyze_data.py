#!/usr/bin/env python3
"""
Simple data analysis script for containerization demo.
This demonstrates a realistic research workflow that can be containerized.
"""

import sys
import numpy as np


def analyze_data(data_size=100):
    """
    Perform simple data analysis.

    Parameters
    ----------
    data_size : int
        Number of data points to generate

    Returns
    -------
    dict
        Analysis results
    """
    # Generate sample data
    data = np.random.randn(data_size)

    # Perform analysis
    results = {"mean": np.mean(data), "std": np.std(data), "min": np.min(data), "max": np.max(data), "count": len(data)}

    return results


def main():
    """Run the analysis and print results."""
    print("=" * 50)
    print("Containerized Data Analysis Demo")
    print("=" * 50)

    results = analyze_data(1000)

    print("\nAnalysis Results:")
    print(f"  Sample size: {results['count']}")
    print(f"  Mean:        {results['mean']:.4f}")
    print(f"  Std Dev:     {results['std']:.4f}")
    print(f"  Min:         {results['min']:.4f}")
    print(f"  Max:         {results['max']:.4f}")
    print("\n✅ Analysis completed successfully!")
    print("=" * 50)

    return 0


if __name__ == "__main__":
    sys.exit(main())
