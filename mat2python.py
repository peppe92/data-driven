import scipy
from scipy import io
def mat2python(patient=1,repetition_number=0):
	'''This function read the SO1.mat file. The experiment is repeated 3 times, repetition_number can take values 0,1,2'''
	print(" I am loading the "+str(repetition_number)+" repetition of the protocol")
	oxy,fs,trial,y,classes=scipy.io.loadmat("./data/S0"+str(patient)+".mat")["data"][0][repetition_number][0,0]
	return oxy,trial[:,0],classes
