from PIL import Image
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS

def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_info_from_image(img):
	"""
	Returns location (latitude , longitude) and timestamp from image metadata
	"""
	exifdata = img.getexif()
	geo_data = get_geotagging(exifdata)
	cords = get_coordinates(geo_data)
	
	date_time = exifdata[36867]

	return cords  , date_time

if __name__ == "__main__":

	filename= "../2.jpeg"
	img = Image.open(filename)

	cords , date_time = get_info_from_image(img)
	print(cords)
	print(date_time)
