from etl.extract import Extract

extract = Extract()

data = extract.extract_all()

for name, df in data.items():
    print("=" * 40)
    print(name)
    print("Rows:", df.count())
    df.show(5)