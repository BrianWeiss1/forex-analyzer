import datetime

from src.testGrabData import grabHistoricalDataBTC

def calltimes(ticker, times, startTime='2023-07-30 9:45'):
    def combine_lists(lst):
        """Combines 3 lists of dictionaries into one list of dictionaries.

        Args:
            lst: A list of 3 lists of dictionaries.

        Returns:
            A list of dictionaries.
        """
        combined_list = []
        for sublist in lst:
            combined_list.extend(sublist)
        return combined_list

    input_format = "%Y-%m-%d %H:%M"

    initial_time = datetime.datetime.strptime(startTime, input_format)
    duration_to_add = datetime.timedelta(minutes=5001)
    lst = []
    apikey2 = 'a9b4c87998c9ca386388f1eceaf3e64391f61f8d'
    time = initial_time
    for i in range(times):
        lst.append(grabHistoricalDataBTC(ticker, time, apikey2))
        time = time + duration_to_add
        print(time)

    f = open('documents/dataCryptoTest2.txt', 'w')
    f.write(str(combine_lists(lst)))
    f.close()


calltimes("BTCUSD", 10, "2022-07-30 9:45")