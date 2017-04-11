# import the geocoding services you'd like to try
# sourced at https://gist.github.com/rgdonohue/c4beedd3ca47d29aef01

from geopy.geocoders import ArcGIS, Bing, Nominatim, OpenCage, GeocoderDotUS, GoogleV3, OpenMapQuest
import csv, sys

print('creating geocoding objects!')

arcgis = ArcGIS(timeout=100)
bing = Bing('EskjSss5VoskMkVH9455~Mw_sz22GdAR8PAJf_yOcRw~Ak7zshEQvx8HunHbrUjh7l9PsVYxVjAMd9q-2R3cNm9L4J8IQeqt4meCt-1esehh',timeout=100)
nominatim = Nominatim(timeout=100)
opencage = OpenCage('f579fc0ccbf975c8d822196eca92cf64',timeout=100)
googlev3 = GoogleV3(timeout=100)
openmapquest = OpenMapQuest(timeout=100)

# choose and order your preference for geocoders here
geocoders = [googlev3, bing, nominatim, arcgis, opencage, openmapquest]

def geocode(address):
    i = 0
    try:
        while i < len(geocoders):
            # try to geocode using a service
            location = geocoders[i].geocode(address)

            # if it returns a location
            if location != None:

                # return those values
                return [location.latitude, location.longitude]
            else:
                # otherwise try the next one
                i += 1
    except:
        # catch whatever errors, likely timeout, and return null values
        print(sys.exc_info()[0])
        return ['null','null']

    # if all services have failed to geocode, return null values
    return ['null','null']


print('geocoding addresses!')

# list to hold all rows
dout = []

with open('C:/Users/admin/Desktop/ICS2/Dublin_Leasehold.csv', mode='r') as fin:

    reader = csv.reader(fin)
    j = 0
    for row in reader:
        print('processing #',j)
        j+=1
        try:
            # configure this based upon your input CSV file
            address = row[4:]
            if address[0] == '':
                print('End of file')
                break
            parsed_address = ' ,'.join(address)
            result = geocode(parsed_address)
            print(result)
            # add the lat/lon values to the row
            row.extend(result)
            # add the new row to master list
            dout.append(row)
        except:
            print('you are a beautiful unicorn')

print('writing the results to file')

# print results to file
with open('C:/Users/admin/Desktop/ICS2/geocoded_leasehold.csv', 'w', newline = '') as fout:
    writer = csv.writer(fout)
    writer.writerows(dout)

print('all done!')