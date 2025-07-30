"""Data processing utilities for NYC School SAT analysis."""

import pandas as pd


def load_schools_data(file_path: str) -> pd.DataFrame:
    """Load schools data from CSV file.
    
    Args:
        file_path: Path to the schools CSV file
        
    Returns:
        DataFrame with schools data
    """
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing values.
    
    Args:
        df: Raw schools DataFrame
        
    Returns:
        DataFrame with NaN values removed
    """
    return df.dropna()


def calculate_total_sat(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total SAT score by summing math, reading, and writing scores.
    
    Args:
        df: Schools DataFrame with individual SAT section scores
        
    Returns:
        DataFrame with total_SAT column added
    """
    df = df.copy()
    df['total_SAT'] = df['average_math'] + df['average_reading'] + df['average_writing']
    return df


def get_math_threshold(percentage: float = 0.8, max_score: int = 800) -> float:
    """Calculate the minimum score threshold for best math results.
    
    Args:
        percentage: Percentage of maximum score (default 0.8 for 80%)
        max_score: Maximum possible SAT section score (default 800)
        
    Returns:
        Minimum score threshold
    """
    return max_score * percentage