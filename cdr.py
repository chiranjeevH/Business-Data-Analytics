#%%
from typing import ItemsView
import pandas as pd
from pandas import ExcelWriter
from collections import defaultdict

#Reading excel file 
myfile = pd.read_excel("test_Cdr_Case.xlsx", sheet_name="TEST")



def incoming_calls(myfile):
    global df_1 

    myfile= myfile[myfile['Call Type']=="'IN'"]
    callingno = list(myfile["Calling No"])
    calledno = list(myfile[" Called No"])
    calltimes = {}  
    for i in range(len(callingno)):
            pair = str(callingno[i]) + "-" + str(calledno[i])
            if pair in calltimes:
                calltimes[pair] += 1
            else:
                calltimes[pair] = 1   

    # print(calltimes)
    
    incsortedindesc = sorted(calltimes, key=calltimes.get, reverse=True)
    numbers, times = [i for i in incsortedindesc], [calltimes[i] for i in incsortedindesc]
    dataFrame = pd.DataFrame({"Numbers": numbers, "Times": times})
    print(dataFrame)
    # writer = ExcelWriter("test_Cdr_Case.xlsx", mode="a", engine="openpyxl")
    # dataFrame.to_excel(writer, "incomingcount")
    # writer.save()
    # print("Dataframe saved")


# incoming_calls(myfile)                    
# print(df_2)

def outgoing_calls(myfile):
    global df_2

    
    myfile= myfile[myfile['Call Type']=="'OUT'"]
    callingno = list(myfile["Calling No"])
    calledno = list(myfile[" Called No"])
    calltimes = {}
    for i in range(len(callingno)):
            pair = str(callingno[i]) + "-" + str(calledno[i])
            if pair in calltimes:
                calltimes[pair] += 1
            else:
                calltimes[pair] = 1   

    # print(calltimes)

    outsortedindesc = sorted(calltimes, key=calltimes.get, reverse=True)
    numbers, times = [i for i in outsortedindesc], [calltimes[i] for i in outsortedindesc]
    dataFrame = pd.DataFrame({"Numbers": numbers, "Times": times})
    print(dataFrame)
    # writer = ExcelWriter("test_Cdr_Case.xlsx", mode="a", engine="openpyxl")
    # dataFrame.to_excel(writer, "outgoingcount")
    # writer.save()
    # print("Dataframe saved")

def only_incoming_calls(myfile):
    # from collections import defaultdict
    mobile_number = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    record = defaultdict(lambda: 0)
    outgoing_number_list = []
    for i in range(len(mobile_number)):
        # print(mobile_number[i])
        # print(call_type[i])
        if call_type[i] == "'IN'":
            record[mobile_number[i]] += 1
        elif call_type[i] == "'OUT'":
            outgoing_number_list.append(mobile_number[i])
    print("The length of incoming calls numbers", len(record.keys()))
    print("The length of outgoing list", len(outgoing_number_list))
    for i in outgoing_number_list:
        if i in record.keys():
            record.pop(i, None)
    
    print(list(record.items()))


def only_outgoing_calls(myfile):
    # from collections import defaultdict
    mobile_number = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    record = defaultdict(lambda: 0)
    incoming_number_list = []
    for i in range(len(mobile_number)):
        # print(mobile_number[i])
        # print(call_type[i])
        if call_type[i] == "'OUT'":
            record[mobile_number[i]] += 1
        elif call_type[i] == "'IN'":
            incoming_number_list.append(mobile_number[i])
        print(record.items())
    print("The length of outgoing calls numbers", len(record.keys()))
    print("The length of incoming list", len(incoming_number_list))
    for i in incoming_number_list:
        if i in record.keys():
            record.pop(i, None)
    
    print(list(record.items()))


# outgoing_calls(myfile)
# with ExcelWriter('test1.xlsx') as writer:
#     df_1.to_excel(writer, sheet_name='Sheet1')
#     df_2.to_excel(writer, sheet_name='Sheet2')

# writer.save()

def max_durations(myfile):
    durations = list(myfile[" Dur(s)"])
    calling_no = list(myfile["Calling No"])
    called_no = list(myfile[" Called No"])
    durations = list((i, int(number.replace("'", ""))) for i, number in enumerate(durations))
    durations.sort(key= lambda x: x[1], reverse=True)
    durations = durations[:10]
    high_duration_numbers = []
    for index, duration in durations:
        high_duration_numbers.append((calling_no[index], called_no[index], duration))
    
    print(high_duration_numbers)



def min_durations(myfile):
    durations = list(myfile[" Dur(s)"])
    calling_no = list(myfile["Calling No"])
    called_no = list(myfile[" Called No"])
    durations = list((i, int(number.replace("'", ""))) for i, number in enumerate(durations))
    durations.sort(key= lambda x: x[1])
    durations = durations[:50]
    lowest_duration_numbers = []
    for index, duration in durations:
        lowest_duration_numbers.append((calling_no[index], called_no[index], duration))
    
    print(lowest_duration_numbers)


# callingno = list(myfile["Calling No"])
# calledno = list(myfile[" Called No"])
# calltimes = {}
# for i in range(len(callingno)):
#     pair = str(callingno[i]) + "-" + str(calledno[i])
#     if pair in calltimes:
#         calltimes[pair] += 1
#     else:
#         calltimes[pair] = 1   

# # print(calltimes)
       
# sortedindesc = sorted(calltimes, key=calltimes.get, reverse=True)
# for r in sortedindesc:
#      print(r, calltimes[r])


 
   
         
def cell1_count(myfile):  
    cell1_count = {}
    calling_no = list(myfile["Calling No"])
    cell1 = list(myfile[" Cell1"])
    for i in range(len(calling_no)):
        if calling_no[i] in cell1_count.keys():
            if cell1[i] in cell1_count[calling_no[i]].keys():
                cell1_count[calling_no[i]][cell1[i]] += 1
            else:
                cell1_count[calling_no[i]][cell1[i]] = 1
        else:
            cell1_count[calling_no[i]] = {}
            cell1_count[calling_no[i]][cell1[i]] = 1
    
    return cell1_count

def hi_n_low_cell1(myfile):
    cells= cell1_count(myfile)
    calling_numbers = list(set(list(myfile["Calling No"])))
    for i in calling_numbers:
        counts = cells[i]
        counts = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]))
        highest_cell1 = counts[-1]
        lowest_cell1 = counts[0]
        # print(i, highest_cell1, lowest_cell1)
        DF= i, highest_cell1, lowest_cell1

    dataFrame = pd.DataFrame(DF,columns=(['Calling_no'], ['highest_cell1'], ['lowest_cell1']))
    writer = ExcelWriter("test_Cdr_Case.xlsx", mode="a", engine="openpyxl")
    dataFrame.to_excel(writer, "hi_n_low_cell1")
    writer.save()
    print(" max duration Dataframe saved")

def cell1_in_count(myfile):
    cell1_count = {}
    calling_no = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    cell1 = list(myfile[" Cell1"])
    for i in range(len(calling_no)):
        if call_type[i] == "'IN'":
            if calling_no[i] in cell1_count.keys():
                if cell1[i] in cell1_count[calling_no[i]].keys():
                    cell1_count[calling_no[i]][cell1[i]] += 1
                else:
                    cell1_count[calling_no[i]][cell1[i]] = 1
            else:
                cell1_count[calling_no[i]] = {}
                cell1_count[calling_no[i]][cell1[i]] = 1

    dataFrame = pd.DataFrame({'Calling_no':calling_no[i], "cell1":cell1[i], "time":cell1_count[calling_no[i]]})
    writer = ExcelWriter("test_Cdr_Case.xlsx", mode="a", engine="openpyxl")
    dataFrame.to_excel(writer, "cell1_in_count")
    writer.save()
    print(" max duration Dataframe saved")
    # print(cell1_count)
        
def cell1_out_count(myfile):
    cell1_count = {}
    calling_no = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    cell1 = list(myfile[" Cell1"])
    for i in range(len(calling_no)):
        if call_type[i] == "'OUT'":
            if calling_no[i] in cell1_count.keys():
                if cell1[i] in cell1_count[calling_no[i]].keys():
                    cell1_count[calling_no[i]][cell1[i]] += 1
                else:
                    cell1_count[calling_no[i]][cell1[i]] = 1
            else:
                cell1_count[calling_no[i]] = {}
                cell1_count[calling_no[i]][cell1[i]] = 1

    print(cell1_count)

def only_outgoing_sms(myfile):
    # from collections import defaultdict
    mobile_number = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    record = defaultdict(lambda: 0)
    outgoing_number_list = []
    for i in range(len(mobile_number)):
        # print(mobile_number[i])
        # print(call_type[i])
        if call_type[i] == "'SMO'":
            record[mobile_number[i]] += 1
        elif call_type[i] == "'SMT'":
            outgoing_number_list.append(mobile_number[i])
    print("The length of incoming calls numbers", len(record.keys()))
    print("The length of outgoing list", len(outgoing_number_list))
    for i in outgoing_number_list:
        if i in record.keys():
            record.pop(i, None)

    print(list(record.items()))

def only_incoming_sms(myfile):
    # from collections import defaultdict
    mobile_number = list(myfile["Calling No"])
    call_type = list(myfile["Call Type"])
    record = defaultdict(lambda: 0)
    outgoing_number_list = []
    for i in range(len(mobile_number)):
        # print(mobile_number[i])
        # print(call_type[i])
        if call_type[i] == "'SMT'":
            record[mobile_number[i]] += 1
        elif call_type[i] == "'SMO'":
            outgoing_number_list.append(mobile_number[i])
    print("The length of incoming calls numbers", len(record.keys()))
    print("The length of outgoing list", len(outgoing_number_list))
    for i in outgoing_number_list:
        if i in record.keys():
            record.pop(i, None)

    print(list(record.items()))


  

def incoming_sms(myfile):
    
    
    myfile = myfile[myfile['Call Type'] == "'SMT'"]
    callingno = list(myfile["Calling No"])
    calledno = list(myfile[" Called No"])  
    calltimes = {} 

    for i in range(len(callingno)):
        pair = str(callingno[i]) + "-" + str(calledno[i])
        if pair in calltimes:
            calltimes[pair] += 1
        else:
            calltimes[pair] = 1
    incsortedindesc = sorted(calltimes, key=calltimes.get, reverse=True) 
    numbers, times = [i for i in incsortedindesc], [calltimes[i] for i in incsortedindesc]
    dataFrame = pd.DataFrame({"Numbers": numbers, "max_count_sms": times}) 
    print(dataFrame)


def outgoing_sms(myfile):

    myfile = myfile[myfile['Call Type'] == "'SMO'"]
    callingno = list(myfile["Calling No"])
    calledno = list(myfile[" Called No"])  
    calltimes = {}  
    for i in range(len(callingno)):
        pair = str(callingno[i]) + "-" + str(calledno[i])
        if pair in calltimes:
            calltimes[pair] += 1
        else:
            calltimes[pair] = 1
    incsortedindesc = sorted(calltimes, key=calltimes.get, reverse=True)
    numbers, times = [i for i in incsortedindesc], [calltimes[i] for i in incsortedindesc]
    dataFrame = pd.DataFrame({"Numbers": numbers, "max_count_sms": times})
    print(dataFrame)

    
      

        
        



# incoming_calls(myfile)
# outgoing_calls(myfile)
# only_incoming_calls(myfile)
# only_outgoing_calls(myfile)
# max_durations(myfile)
# min_durations(myfile) 
# cell1_count(myfile)
# hi_n_low_cell1(myfile)
# cell1_in_count(myfile)
# cell1_out_count(myfile) 
# only_outgoing_sms(myfile)
# only_incoming_sms(myfile)
# incoming_sms(myfile)             # //
# outgoing_sms(myfile)             //






# %%

# %%




