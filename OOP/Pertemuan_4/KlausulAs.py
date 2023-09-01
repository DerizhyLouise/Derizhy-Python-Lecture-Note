import sys

def convert (Juubi):
    'mengubah ke integer'
    try:
        return int(Juubi)
    except (ValueError, TypeError) as e:
        print("Konversi error : {}".format(str(e)), file=sys.stderr)
        return -1

print(convert([1,2,3]))