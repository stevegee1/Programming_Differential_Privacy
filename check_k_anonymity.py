import pandas as pd
import sys

def isKAnonymized(df, k):

  # for each row in the dataframe
  for index, row in df.iterrows():
    # Build a query that matches rows identical to the current one
    query = ' & '.join([f'`{col}` == @{col}' for col in df.columns])

    # Create a dictionary of column values for every evaluation
    local_vars = {col: row[col] for col in df.columns}

    # filter rows that match this row
    rows = df.query(query, local_dict = local_vars)

    if rows.shape[0] < k:
      return False

  return True

def main():
  # Expect csv file and k value
  if len(sys.argv) != 3:
    print("Usage: python check_k_anonymity.py <csv_file> <k>")
    sys.exit(1)
  csv_file = sys.argv[1]
  k = int(sys.argv[2])

  # Load CSV
  df = pd.read_csv(csv_file)
  # Run check
  result = isKAnonymized(df, k)

  print(f"Dataset satisfies {k}-Anonymity: {result}")

if __name__ == "__main__":
  main()


