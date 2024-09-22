import pickle
num = [8, 15, 12, 10]
ser = pickle.dumps(num)
print(ser)
ser_rev = pickle.loads(ser)
print(ser_rev)


