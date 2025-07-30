"""Visualization utilities for NYC School SAT analysis."""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def plot_score_distribution(df: pd.DataFrame, score_column: str, 
                          title: str, xlabel: str, output_path: str = None) -> None:
    """Plot histogram of score distribution.
    
    Args:
        df: DataFrame containing the scores
        score_column: Column name to plot
        title: Plot title
        xlabel: X-axis label
        output_path: Optional path to save the figure
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df[score_column], bins=30, alpha=0.7, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_null_values(df: pd.DataFrame, output_path: str = None) -> None:
    """Plot bar chart of null values per column.
    
    Args:
        df: DataFrame to analyze
        output_path: Optional path to save the figure
    """
    null_values = df.isna().sum()
    
    plt.figure(figsize=(10, 6))
    null_values.plot(kind='bar',
                    xlabel='Column',
                    ylabel='Number of NaNs',
                    title='Number of NaNs per Column',
                    alpha=0.5, 
                    edgecolor='black')
    
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def save_analysis_results(data: pd.DataFrame, filename: str, output_dir: str = "outputs/reports") -> None:
    """Save analysis results to CSV file.
    
    Args:
        data: DataFrame to save
        filename: Name of the output file (without extension)
        output_dir: Directory to save the file
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    filepath = output_path / f"{filename}.csv"
    data.to_csv(filepath, index=True)
    print(f"Results saved to: {filepath}")