import math
import matplotlib.pyplot as plt
from pylab import savefig

#red is c should be recording
#blue is b should be orignal	

def frequency_plot(a,b,c):
	
	plt.plot(a,b,'b',label = 'original')
	plt.legend()
	plt.plot(a,c,'r',label = 'recording')
	plt.legend()

	plt.xlabel('Time(sec)',fontsize=15)			# you can change units
	plt.ylabel('Frequency(Hz)',fontsize=15)		# you can change units
	plt.title('SOUND ANALYSIS',fontsize=20)

	savefig('foo.png', bbox_inches='tight')
	# plt.show()

