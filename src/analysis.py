"""Analysis functions for NYC School SAT performance."""

import pandas as pd


def get_best_math_schools(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """Get schools with the best math results above threshold.
    
    Args:
        df: Schools DataFrame with math scores
        threshold: Minimum math score threshold
        
    Returns:
        DataFrame with schools meeting math threshold, sorted by math score
    """
    best_math = df[df['average_math'] >= threshold]
    return best_math[['school_name', 'average_math']].sort_values(
        by='average_math', ascending=False
    )


def get_top_schools_by_total_sat(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Get top N schools by total SAT score.
    
    Args:
        df: Schools DataFrame with total_SAT column
        top_n: Number of top schools to return (default 10)
        
    Returns:
        DataFrame with top N schools by total SAT score
    """
    return df[['school_name', 'total_SAT']].sort_values(
        by='total_SAT', ascending=False
    ).head(top_n)


def get_borough_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate statistics by borough including standard deviation.
    
    Args:
        df: Schools DataFrame with borough and total_SAT columns
        
    Returns:
        DataFrame with borough statistics (count, mean, std)
    """
    stats = df.groupby('borough').agg({
        'school_name': 'count',
        'total_SAT': ['mean', 'std']
    }).round(2)
    
    # Flatten column names
    stats.columns = ['num_schools', 'average_SAT', 'std_SAT']
    
    return stats.sort_values(by='std_SAT', ascending=False)


def get_largest_std_borough(df: pd.DataFrame) -> pd.DataFrame:
    """Get the borough with the largest standard deviation in SAT scores.
    
    Args:
        df: Schools DataFrame with borough and total_SAT columns
        
    Returns:
        DataFrame with the borough having largest standard deviation
    """
    borough_stats = get_borough_stats(df)
    return borough_stats.head(1)