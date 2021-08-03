states = {
	'RO': {
		'AB': 'Alba',
		'AR': 'Arad',
		'AG': 'Arges',
		'BC': 'Bacau',
		'BH': 'Bihor',
		'BN': 'Bistrita-Nasaud',
		'BT': 'Botosani',
		'BR': 'Braila',
		'BV': 'Brasov',
		'B': 'Bucuresti',
		'BZ': 'Buzau',
		'CL': 'Calarasi',
		'CS': 'Caras-Severin',
		'CJ': 'Cluj',
		'CT': 'Constanta',
		'CV': 'Covasna',
		'DB': 'Dambovita',
		'DJ': 'Dolj',
		'GL': 'Galati',
		'GR': 'Giurgiu',
		'GJ': 'Gorj',
		'HR': 'Harghita',
		'HD': 'Hunedoara',
		'IL': 'Ialomita',
		'IS': 'Iasi',
		'IF': 'Ilfov',
		'MM': 'Maramures',
		'MH': 'Mehedinti',
		'MS': 'Mures',
		'NT': 'Neamt',
		'OT': 'Olt',
		'PH': 'Prahova',
		'SJ': 'Salaj',
		'SM': 'Satu Mare',
		'SB': 'Sibiu',
		'SV': 'Suceava',
		'TR': 'Teleorman',
		'TM': 'Timis',
		'TL': 'Tulcea',
		'VL': 'Valcea',
		'VS': 'Vaslui',
		'VN': 'Vrancea',
	}
}


def state_ios_get(state: str):
	state_ios = None
	for ios, name in states['RO'].items():
		if name == state:
			state_ios = ios
			break
	return state_ios


def data_to_php(data: dict):
	php_format = '<?php \n$places = array(\n'

	for ios, places in data.items():
		php_format += f'\t\'{ios}\' => array(\n'
		for place in places:
			php_format += f'\t\t\'{place}\',\n'
		php_format += '\t),\n'

	php_format += ');'
	return php_format


def main():
	import csv

	file = open('fan_courier.csv', mode='r')
	next(file)  # remove header
	fan_courier = csv.reader(file)

	data = {}
	for cols in fan_courier:
		state, place = cols
		state_ios = state_ios_get(state)

		data[state_ios] = [place] if state_ios not in data else data[state_ios] + [place]

	file.close()

	php_format = data_to_php(data)
	file = open('RO.php', 'w')
	file.write(php_format)
	file.close()


if __name__ == '__main__':
	main()
