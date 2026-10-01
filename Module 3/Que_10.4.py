class OOPsException(Exception):
    pass

try:
    raise OOPsException()
except OOPsException:
    print("Caught an oops")

