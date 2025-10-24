import os
import hashlib
import folium


def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		lastid = result.id
		newid = lastid + 1
	else:
		lastid = 0
		newid = 1
	return lastid, newid
def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

def getjustnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
	else:
		newid = 1
	return newid

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

def split_string(string):
	string2 = string.split()
	return string2[0].lower()

def getFulanID(fulan):
	if fulan == "January":
		fulanTetun = "Janeiru"
		fulanID = "1"
	if fulan == "February":
		fulanTetun = "Fevreiru"
		fulanID = "2"
	if fulan == "March":
		fulanTetun = "Marsu"
		fulanID = "3"
	if fulan == "April":
		fulanTetun = "Abril"
		fulanID = "4"
	if fulan == "May":
		fulanTetun = "Maiu"
		fulanID = "5"
	if fulan == "June":
		fulanTetun = "Junhu"
		fulanID = "6"
	if fulan == "Jully":
		fulanTetun = "Julhu"
		fulanID = "7"
	if fulan == "August":
		fulanTetun = "Agustu"
		fulanID = "8"
	if fulan == "September":
		fulanTetun = "Setembru"
		fulanID = "9"
	if fulan == "October":
		fulanTetun = "Outubru"
		fulanID = "10"
	if fulan == "November":
		fulanTetun = "Novembru"
		fulanID = "11"
	if fulan == "December":
		fulanTetun = "Dezembru"
		fulanID = "12"
	return fulanID, fulanTetun

def make_markers_and_add_to_map(map, house):
    folium.Marker(
            location = [house.latitude, house.longitude],
            popup = house.description,
            tooltip = house.title,
            icon = folium.Icon(icon='fa-home', prefix='fa')
        ).add_to(map)
