import pygeoip
gi = pygeoip.GeoIP('/home/munishgrover/Desktop/GeoLiteCity.dat')  #accessing geolocation from files
def TargetIP(target):
	rec = gi.record_by_name(target)
	city = rec['city']     			#to know city name
	region = rec['region_code']		#to know regioncode
	country = rec['country_name']		#to know country name
	long = rec['longitude']			#to know longitude
	lat = rec['latitude']			#to know latitude
	print '[*] Target: ' + target + ' Geo-located. '
	print '[+] Adress: '+str(city)+', '+str(region)+', '+str(country)
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
f=open('mailinfo','rw+')	#add a original message to created file named mailinfo
l=f.readlines()			
for myline in l:			#printing out details
	if myline.startswith('Delivered-To: '):
		print("Email send to: ",myline)	
	elif myline.startswith('Received: from '):
		target=(myline[-16:-3])
		break
	
host =(target)	#setting ip address
target = host	#target as my host
TargetIP(target)	#getting ip address matching from database
