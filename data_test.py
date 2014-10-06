import sys,csv,DB2


__author__ = "Vidya Venkiteswaran"


def data_extraction(Filename):
	try:
		with open(Filename,'r') as f:
			print "I have file"
			f.readline()
	except IOError as e:
		return e


def data_preparation(Filename):
	try:
		num_lines = 0
		sum_size_of_house = 0.0
		X = []
		Y = []
		X_new = []
		max_size = sys.float_info.min
		min_size = sys.float_info.max

		with open(Filename,'rb') as f:
			reader = csv.reader(f)
			for line in reader:
				num_lines = num_lines + 1
				sum_size_of_house = sum_size_of_house + float(line[0])
				print line[0]
				if(float(line[0]) > max_size):
					max_size = float(line[0])
				if(float(line[0]) < min_size):
					min_size = float(line[0])
				X.append(float(line[0]))
				Y.append(float(line[1]))
			# num_lines = sum(1 for line in reader)
			try:
				average_size_house = sum_size_of_house/num_lines
			except ZeroDivisionError,zero_error:
				print zero_error
				sys.exit(0)
			sigma = max_size - min_size

		for house in X:
			X_new.append((house - average_size_house)/sigma)

		print "Number of records in file is %d " % num_lines
		print "Mean of size of house %f " % average_size_house
		print "Max size of house %f " % max_size
		print "Min size of house %f " % min_size
		print "SD of size of house %f " % sigma

		for house,house_new in zip(X,X_new):
			print house,house_new

	except IOError as e:
		return e
		sys.exit(0)


def update_status_DB2(logfile):
	db = DB2.connect('dbname', 'username', 'password')
	cursor = db.cursor()
	

# def jarFile():
# 	invoke jar


if __name__ == '__main__':

	filename = raw_input()

	error_extraction = data_extraction(filename)
	if(error_extraction):
		print error_extraction
		sys.exit(0);

	log_data = data_preparation(filename)

	



