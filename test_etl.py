from etl.extract import Extract

extract = Extract()
data = extract.extract_all()

for name, df in data.items():
    print(f"{name}: {df.count()} rows")