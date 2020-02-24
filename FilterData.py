#FilterData.py
#26-03-2019
#Name: DUSHYANT PANCHAL
#Roll No.: 2018033
#Section & Group: A7

import pandas as pd

data=pd.read_excel("JournalsDataFromFound_TXT.xlsx")	#Read file having impact factors
OtherData=pd.read_excel("DownloadedDataAsExcel.xlsx")	#Read file with all data except impact factors
#print(IFdata.head())
#print(OtherData.head())

final=dict()	#For storing filtered data till written to a file

#Lists for storing corresponding columns
Rank=list()
Title=list()
H_index=list()
ImpactFactor=list()
SJR=list()
TotalDocs2017=list()
TotalDocs3yrs=list()
TotalRefs=list()
TotalCites=list()
CitableDocs=list()

CitesByDoc=list()
RefByDoc=list()

sourceID=list()

for i in range(len(data)):	#For each row in data
	h=data['H index'][i]

	found=-1
	for j in range(len(OtherData)):
		if(OtherData['H index'][j]==h): #If found row with same H index as iTH row in data
			if(OtherData['Title'][j]==data['Title'][i]):	#Check if titles also match to confirm
				found=j
				break

	if(found==-1):
		pass
	else:
		if(isinstance(OtherData['SJR'][found],int)):
			pass
		elif(isinstance(OtherData['SJR'][found],str)):	#To remove some discrepancies that I found in the data (At some places numbers were written like 0,1234 so python though them to be strings)
			OtherData['SJR'][found]=int(OtherData['SJR'][found][2:])
		else:	#For some rows, SJR column was empty, so these statements were required to remove them.
			continue

		#Once found data in the required format, append it to the corresponding lists.

		Title.append(data['Title'][i])
		H_index.append(data['H index'][i])
		ImpactFactor.append(data['Impact Factor'][i])

		Rank.append(OtherData['Rank'][found])
		SJR.append(OtherData['SJR'][found])
		TotalDocs2017.append(OtherData['Total Docs. (2017)'][found])
		TotalDocs3yrs.append(OtherData['Total Docs. (3years)'][found])
		TotalRefs.append(OtherData['Total Refs.'][found])
		TotalCites.append(OtherData['Total Cites (3years)'][found])
		CitableDocs.append(OtherData['Citable Docs. (3years)'][found])

		ind1=OtherData['Cites / Doc. (2years)'][found].find(',')
		ind2=OtherData['Ref. / Doc.'][found].find(',')
		
		OtherData['Cites / Doc. (2years)'][found]=int(OtherData['Cites / Doc. (2years)'][found][:ind1]+OtherData['Cites / Doc. (2years)'][found][ind1+1:])
		CitesByDoc.append(OtherData['Cites / Doc. (2years)'][found])

		OtherData['Ref. / Doc.'][found]=int(OtherData['Ref. / Doc.'][found][:ind2]+OtherData['Ref. / Doc.'][found][ind2+1:])
		RefByDoc.append(OtherData['Ref. / Doc.'][found])

		sourceID.append(OtherData['Sourceid'][found])


#Add the lists to our dataframe to be written to a file.
final['Title']=Title
final['Impact Factor']=ImpactFactor
final['Rank']=Rank
final['H index']=H_index
final['SJR']=SJR
final['Total Docs. (2017)']=TotalDocs2017
final['Total Docs. (3years)']=TotalDocs3yrs
final['Total Refs.']=TotalRefs
final['Total Cites (3years)']=TotalCites
final['Citable Docs. (3years)']=CitableDocs
final['Cites / Doc. (2years)']=CitesByDoc
final['Ref. / Doc.']=RefByDoc

final['Source ID']=sourceID

#Writing data to an excel file name 'FilteredData.xlsx'.
df=pd.DataFrame(final)
writer=pd.ExcelWriter('FilteredData.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()