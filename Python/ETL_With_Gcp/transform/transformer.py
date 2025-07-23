import pandas as pd
import os

def transform_file(file_path):
    df = pd.read_csv(file_path)
    
    df.dropna(inplace=True)                    
    df.columns = [col.lower() for col in df.columns]  
    
    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", f"cleaned_{os.path.basename(file_path)}")
    df.to_csv(output_path, index=False)
    print(f"Transformed and saved: {output_path}")
