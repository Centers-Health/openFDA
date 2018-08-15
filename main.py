import requests
import sys

subsections = ["application_number","generic_name","route","pharm_class_moa","pharm_class_cs","pharm_class_pe", "pharm_class_epc"]
for subsection in subsections:
URL = "https://api.fda.gov/drug/label.json?api_key=WLm7AKMaBm8CYrA1pKJrcbmw8z36kFjv7XcqH3uJ&search="+sys.argv[1]+"&limit=-1"
data = requests.get(URL).json()

for result in data.get('results', []):

        if subsection in result['openfda']:
            print(result["openfda"][subsection])

    print("\n\n")
