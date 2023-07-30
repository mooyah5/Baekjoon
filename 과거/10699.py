import datetime

today = datetime.datetime.today()
print(f'{today:%Y}-{today:%m}-{today:%d}')