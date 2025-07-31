import shutil
import random
import time
import threading


#Production -> 24 Hours = 24*60*60 SEC total RunTime WITH var(60 SEC/1 MIN * 10 TIMES / 1 MIN) seconds * (30 RUNS * Time For Each Run)
#Test -> 1 Minutes = 60 SEC total Runtime WITH var(10 SEC * 10 TIMES / 1 SEC) seconds * (10 RUNs * Time for each run)

stop_event = threading.Event()


def copyFile(source,target):
	try:
		shutil.copy(source,target)
		print(f"File '{source}' copied to '{target}' successfully.")
	except FileNotFoundError:
		print(f"Error: Source file '{source}' not found.")
	except Exception as e:
		print(f"An error has occurred: {e}")


def algorithm(cal2NLevel =2,saltSensitivityThreshold=0.5):
	for x in range(1,int(saltSensitivityThreshold*100)):#take advantage multi-core threads
		salt = random.random() * random.random() + random.random() / 2
	if cal2NLevel == 0 or cal2NLevel ==1: 
		return 1
	
	return algorithm(cal2NLevel -1,saltSensitivityThreshold) + algorithm(cal2NLevel-2,saltSensitivityThreshold)

def simulate_run(numOfTimes=10,timeVariances=5):
	startTime = time.perf_counter()
	for x in range (1,numOfTimes):
		print(f"Execute Time : {time.perf_counter() - startTime}")
		algorithm(30,0.2)
		time.sleep(random.randint(1,timeVariances))
	print(f"Execute Time : {time.perf_counter() - startTime}")

def simulate_type():
	parts = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"ton","nian","anti","de","un","ed","ism","pre","auto","bio","homo","hetero","micro","marco","in","mis","non","re","semi","super","trans","able","er","ful","ing","ity","ation","ive","ative","less","ly","ment","ness","ous","s","es","y"]
	endParagraphSymbol = ["...",".","!"]
	paragraph = []
	paragraphWordLength = 1024*1024
	for x in range(0,paragraphWordLength,1):
		length = random.randint(1,20)
		word = []
		for construct_word in range(1,length,1):
			#random capital or lower case
			firstAlphabet = random.choice(parts)
			word.append(firstAlphabet)
		paragraph.append(''.join(word))
		if random.randint(0,10) < 5 and x != paragraphWordLength -1:
			paragraph.append(" ")
	paragraph.append(random.choice(endParagraphSymbol))
	return paragraph

def simulate_fileWrite(howManyRuns=30,variancesOfTime=600,ops="CopyFile",totalRunTime=24*60*60):
	timeCount = []
	source = "content.txt"
	target = "target.txt"			
	for runCount in range(0,howManyRuns,1):
		totalTime = sum(timeCount)
		executeTime = 0
		startTime = time.perf_counter()
		if runCount == howManyRuns - 1 and totalTime < totalRunTime:
			executeTime = totalRunTime - totalTime
		elif totalTime >= totalRunTime:
			executeTime = 0 #just do it really quick to fulfill runsCount
		else:
			executeTime = random.randint(1,variancesOfTime)
		timeCount.append(executeTime)
		print(f"Total Run Time So Far: {totalTime}") #{totalTime.4f} floating point
		print(f"Start Typing of {runCount}:\n")		
		with open(source, "w") as file:
			file.write("I now have content\n")
			file.write("Okay automate.\n")
			file.write(''.join(simulate_type()))
		print("End Typing.\n")
		print("Start IO Copy-Operations:\n")
		copyFile(source,target)
		print("End IO Operations.\n")

		if not stop_event.is_set():
			print(f"Start Thread Sleep: {executeTime} seconds.")
			time.sleep(executeTime)
			print("End Thread Sleep")
		#readjust to actualexecuteTime for better accounting
		timeCount.append(time.perf_counter() - startTime - executeTime)

def work_task():
	#1 Day 1 MINUTES with simulate_run(10,5) * 5 minutes
	for runs in range(1,24): #24 hours
		simulate_run(10*5,5)
		time.sleep(25*60) #sleep 30 MINUTES
		simulate_run(10*3,5)
		time.sleep(27*60) #sleep 30 MINUTES

	#1 Day		100 RUNS, 30 MINUTES a piece variances, 24 HOURS			86400 secods
	simulate_fileWrite(100,30*60,"CopyFile",24*60*60)
	#simulate_fileWrite(10,10,"CopyFile",60)


# Main program

try:
	if __name__ == "__main__":
		print("Start Task\n")
		worker_thread = threading.Thread(target = work_task)
		worker_thread.start()
		#enable keyboard interrupt
		while True:
			if worker_thread.is_alive() == False:
				break;
			time.sleep(random.random()) #responsiveness check
except KeyboardInterrupt:
	stop_event.set()
