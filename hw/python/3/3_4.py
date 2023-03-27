from collections import Counter
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
blood_count = Counter(blood_types)
print(dict(blood_count))