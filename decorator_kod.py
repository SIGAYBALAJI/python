def check_account_decorator(func):
    def wrapper(kod_id):
        blocked_kod_id=(123,345,456,678,890)
        if kod_id in  blocked_kod_id:
            print("cannot process  blocked_kod_id",kod_id)
        else:
            func(kod_id)
    return wrapper



@check_account_decorator
def process_account(kod_id):
    print("can process kodnest id",kod_id)
process_account(int(input("enter the kod_id")))
