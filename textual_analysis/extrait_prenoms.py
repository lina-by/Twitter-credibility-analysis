import pandas as pd
import json
# 304425 début fille
# -2 dans les indices par rapport au excel
document = pd.read_csv("../nat2020_csv/nat2020.csv", sep=';')
# print(document[123:124])


def store_names(names, filename):
    with open(filename+".json", "w") as write_file:
        json.dump(names, write_file, indent=4)


def extract_name(n):
    l = []
    # 667363
    for i in range(n):
        if document.at[i, "annais"] == "XXXX":
            l.append(document.at[i, "preusuel"])
    return(l)


if __name__ == '__main__':
    store_names(extract_name(667363), 'prenoms')
