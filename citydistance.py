''' 
Work out the distance between two user specified cities using the haversine formula
'''    
from pygeocoder import Geocoder
import numpy as np
import sys


def get_distance(locA, locB):
    earth_rad = 6371.0
    dlat = np.deg2rad(locB[0]-locA[0])
    dlong = np.deg2rad(locB[1]-locA[1])
    a = np.sin(dlat/2) * np.sin(dlat/2) + \
        np.cos(np.deg2rad(locA[0])) * np.cos(np.deg2rad(locB[0])) * \
        np.sin(dlong/2) * np.sin(dlong/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return earth_rad * c

def get_latlongs(location):
    return Geocoder.geocode(location)[0].coordinates

def main():
    #get city 1
    print 'Type the first city: '
    cityA = raw_input()

    #get city 2
    print 'Type the second city: '
    cityB = raw_input()

    #find distances in kilometers
    try:
        distance = get_distance(get_latlongs(cityA),
                                 get_latlongs(cityB))
        print "{0:.2f}".format((distance)), ' km'
    except:
        print 'Error occured. Are the input cities correct?'


if __name__ == '__main__':
    main()