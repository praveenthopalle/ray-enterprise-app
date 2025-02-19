import ray
import pandas as pd
import time

ray.init()

@ray.remote
def process_file(file):
    time.sleep(2)  # Simulating file processing delay
    df = pd.read_csv(file)
    print(f"Processed {file}")
    return df

def main():
    files = ["data1.csv", "data2.csv", "data3.csv"]
    results = ray.get([process_file.remote(file) for file in files])
    print("Data Processing Complete")

if __name__ == "__main__":
    main()
