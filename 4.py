#!/usr/bin/env python

import hashlib
import itertools

def hashCode(key, pattern):
	for it in itertools.count(start=1):
		keyToTest = key+str(it)
		hash = hashlib.md5(keyToTest.encode()).hexdigest()
		if hash.startswith(pattern):
			return it

key = 'bgvyzdsv'

print(hashCode(key, '0000'), hashCode(key, '00000'))