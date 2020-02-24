#MainScript.py
#26-03-2019
#Name: DUSHYANT PANCHAL
#Roll No.: 2018033
#Section & Group: A7

import pandas as pd
import numpy as np

num_of_cols=11	#Number of columns available in the data

data=pd.read_excel("FilteredData.xlsx") #Read our filtered data

n=int(0.8*len(data))
#Select first ~80% as training data
train=data[:n]
test=data[n:]

Y=np.array(train['Impact Factor'])
Y=Y.reshape(len(Y),1)
#Y (list of impact factors) as a column matrix


combis=2**num_of_cols #2^11 - 1 = 2047 possible combinations

#Format for results to be shown
Results={'Columns Chosen':[], 'Mean Absolute Error':[], 'Mean Squared Error':[]}



for i in range(1,combis):	#for each combination
	num=i

	tempX=list()	#First store matrix as a list
	tempX.append([1]*n)	#for constant part

	cols=""	#String for representing names of columns selected in the results
	
	for k in range(num_of_cols):
		dig=num%2
		num=num//2
		if(dig==1):
			tempX.append(list(train[train.columns[k+2]])) #Add the column if required by current combination
			cols+=train.columns[k+2]+", " #update the string with new column added

	Results['Columns Chosen'].append(cols[:-2])	#update the results



	X_trans=np.array(tempX)	#Convert to numpy array
	X=X_trans.transpose()	#Transpose required for the formula

	temp=np.dot(X_trans,X)	#np.dot for simpler and faster matrix multiply
	beta_hat=np.dot(np.linalg.inv(temp),np.dot(X_trans,Y)) #np.linalg.inv for calculating inverse
	#FORMULA: BETA_HAT = (X'X)-1(X'Y)
	
	mean_sq=0	#Mean Squared Error
	mean_abs=0	#Mean Absolute Error

	for j in range(n,len(data)):	#Test our regression line on remaining 20% of the data
		Y_pred=beta_hat[0,0]	#Prediction of Impact Factor
		a=1
		num=i
		for k in range(num_of_cols):
			dig=num%2
			num=num//2
			if(dig==1):
				Y_pred+=beta_hat[a,0]*test[test.columns[k+2]][j]
				a+=1


		mean_sq+=(Y_pred-test['Impact Factor'][j])**2
		mean_abs+=abs(Y_pred-test['Impact Factor'][j])

	Results['Mean Squared Error'].append(mean_sq/len(test))	#Add Mean sq. Error to results
	Results['Mean Absolute Error'].append(mean_abs/len(test))	#Add Mean abs Error to results



#Display best possible combinations

minMSE=0
minMAE=0
MSE=Results['Mean Squared Error']
MAE=Results['Mean Absolute Error']

for i in range(1,combis-1):
	if(MSE[i]<MSE[minMSE]):
		minMSE=i
	if(MAE[i]<MAE[minMAE]):
		minMAE=i


#Display the combinations giving least errors
print("Combination giving least Mean Squared Error:-\n")

print(Results['Columns Chosen'][minMSE])
print("(Mean Squared Error: "+str(Results['Mean Squared Error'][minMSE])+")")
print("(Mean Absolute Error: "+str(Results['Mean Absolute Error'][minMSE])+")")

print("\nCombination giving least Mean Absolute Error:-\n")

print(Results['Columns Chosen'][minMAE])
print("(Mean Squared Error: "+str(Results['Mean Squared Error'][minMAE])+")")
print("(Mean Absolute Error: "+str(Results['Mean Absolute Error'][minMAE])+")")




#Store the results in an excel file called "Regression Analysis.xlsx"
df=pd.DataFrame(Results)
writer=pd.ExcelWriter('Regression Analysis.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()