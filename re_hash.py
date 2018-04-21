import math


class hashing_rehashing:
	def __init__(self):
		self.charecter_set = "acdegilmnoprstuw"

		self.hash_value = 7
		self.hash_multi = 37


		self.taking_data_from_user()

	def hash(self, input_str):
		length_of_str = len(input_str)
		return_hash = self.hash_value
		for i in range(length_of_str):
			try:
				return_hash = (return_hash*self.hash_multi + self.charecter_set.index(input_str[i]))
			except:
				pass
		return return_hash

	def re_hash(self, encoded_hash):
		temp = encoded_hash
		decoded = ""
		re_hash_str = []
		i = 0
		while encoded_hash > self.hash_multi:
			re_hash_str.append(int(math.floor(encoded_hash%self.hash_multi)))
			encoded_hash /= self.hash_multi
		for i in range(len(re_hash_str)-1, -1, -1):
			decoded += self.charecter_set[re_hash_str[i]]
		return decoded

	def taking_data_from_user(self):
		print "1-hash\n2-re_hash"
		ch = input()
		if ch == 1:
			print "Enter string:"
			input_str = raw_input()
			print self.hash(input_str)
		elif ch == 2:
			print "Enter hash value:"
			hash_value = input()
			print self.re_hash(hash_value)
		else:
			print "Choose correct option"

obj = hashing_rehashing()