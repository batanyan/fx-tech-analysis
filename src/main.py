import pandas as pd


def main():
    df = pd.read_csv("/Users/btnyn/dev/fx-tech-analysis/data/sample.csv")
    print(df.head())

if __name__ == "__main__":
    main()
