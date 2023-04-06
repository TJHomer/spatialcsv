"""Main module."""
import pandas as pd
import csv


#def import_csv(filepath, skip=none, delimiters=','):
 #   pass



class Locations(object):
    def __init__(self, csv, lat=None, long=None, **kwargs):
        self.csv = csv
        self.lat = lat
        self.long = long


    def checks(self):
        with open(self.csv, 'r') as csvfile:
            head = csv.Sniffer().has_header(csvfile.read(1024))
                
            if head:
                pass
            else:
                print("This csv file does not seem to have a header. Please add column names in the top line of the csv.")
        '''
        except FileNotFoundError:
            print(f"File {self.csv} not found.")
        '''
        if self.lat in self.header():
            pass
        else:
            print(f"The value '{self.lat}' is not in the header.")
        if self.long in self.header():
            pass
        else:
            print(f"The value '{self.long}' is not in the header.")
        print("done")


    def header(self):
        with open(self.csv) as csvfile:
            reader = csv.DictReader(csvfile)
            header = reader.fieldnames
            print(list(header))
            return header



c = Locations('us-state-capitals.csv', lat='latitude', long='longitude')
c.checks()
