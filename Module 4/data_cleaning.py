import pandas as pd

def apply_mapping(df, column_name):

    if column_name in complete_mapping:
        mapping = complete_mapping[column_name]
        # Create a copy of the column
        original_values = df[column_name].copy()
        
        # Apply mapping but handle missing keys by keeping original value
        df[column_name] = df[column_name].apply(lambda x: mapping.get(x, x))
        
        # Check for NaN values that might have been introduced
        if df[column_name].isna().any():
            # For any NaN values, restore the original value
            na_mask = df[column_name].isna()
            df.loc[na_mask, column_name] = original_values[na_mask]
            
            # Print warning about values not found in mapping
            missing_values = original_values[na_mask].unique()
            print(f"Warning: {len(missing_values)} values in {column_name} not found in mapping dictionary")
            
    return df

# Complete application:
def clean_data(input_file, output_file):
  
    # Load data
    df = pd.read_csv(input_file)
    print(f"Original data has {len(df)} rows and {len(df.columns)} columns")
    
    # Store original row count
    original_row_count = len(df)
    
    # Apply mappings to each column
    for column_name in df.columns:
        df = apply_mapping(df, column_name)
        # Verify row count hasn't changed
        if len(df) != original_row_count:
            print(f"ERROR: Row count changed after mapping {column_name}!")
            print(f"Original: {original_row_count}, New: {len(df)}")
    
    # Verify final results
    print(f"Cleaned data has {len(df)} rows and {len(df.columns)} columns")
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Saved cleaned data to {output_file}")
    
    return df

# Usage example:
clean_data("C:/Users/Fatima/Downloads/cleaned_data.csv", "cleaned_antimicrobial_resistance_data.csv")
