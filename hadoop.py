import os
os.system("tput setaf 5")
print("\tElasticity in Hadoop using LVM")
os.system("tput setaf 6")

def increase ():
	size = int(input("\tEnter Size to Increase : "))
	os.system(f"lvextend --size +{size}G /dev/hadoop/hadoop-dn")
	os.system(f"resize2fs /dev/hadoop/hadoop-dn")
	os.system("jps")
	print(f"Size Increased Successfully by {size} GB")

def decrease ():
	present = int(input("\tEnter Present Size of Disk (Before Reduce) : "))
	desire = int(input("\tEnter Size After Reducing the Disk : "))
	os.system("hadoop-daemon.sh stop datanode")
	os.system("umount /hadoop-lvm")
	os.system("e2fsck -f /dev/hadoop/hadoop-dn")
	os.system(f"resize2fs /dev/hadoop/hadoop-dn {desire}G")
	os.system(f"lvreduce --size -{present - desire}G /dev/hadoop/hadoop-dn -f")
	os.system("mount /dev/hadoop/hadoop-dn /hadoop-lvm")
	os.system("hadoop-daemon.sh start datanode")
	os.system("jps")
	print(f"Size Decreased Successfully by {present - desire} GB")


while (True):
	
	print('\t1. Increase the Size of Datanode')
	print('\t2. Decrease the Size of Datanode')
	print('\t3. Exit')
	ch = input('\tEnter Your choice : ')
	
	if ch == '1':
		increase()
	elif ch == '2':
		decrease()
	elif ch == '3':
		exit()
	else:
		print('Invalid Choice. Try Again !!!')
