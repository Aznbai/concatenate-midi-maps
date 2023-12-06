import os
import csv
from pathlib import Path


# Root of folders containing the maps
root_dir = Path(__file__).resolve().parent
folder = root_dir / "midi-main"

# Create output file
concatFile = 'ALL-MIDI-MAPS.csv'

# Iterate thru folders inside the root
with open(concatFile, 'w', newline='') as csvfile:
    csvwriter = None  # init csvwriter 

    for folderName, subFolder, files in os.walk(folder):
        for file in files:
            if file.endswith('.csv'):
                hersteller = os.path.basename(folderName)
                modell = os.path.splitext(file)[0]

                with open(os.path.join(folderName, file), 'r') as csvfile_sourceFile:
                    csvreader = csv.reader(csvfile_sourceFile)

                    # init csvwriter if not yet
                    if csvwriter is None:
                        csvwriter = csv.writer(csvfile)
                        header_sourceFile = next(csvreader)
                        header_sourceFile = [header.upper() for header in header_sourceFile]
                        csvwriter.writerow(header_sourceFile)

                    # write data into concatFile without first two colums
                    for row in csvreader:
                        row = [row[i].upper() for i in range(len(row))]
                        csvwriter.writerow(row)

print('CSV-files were concatenated. Headers transformed to uppercase')
