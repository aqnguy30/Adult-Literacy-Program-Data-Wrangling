#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:42:14 2020

@author: anhnguyen
"""
#import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read-in the data
Student = pd.read_excel('Student.xlsx')
Tutor = pd.read_excel('Tutor.xlsx')
Match_History = pd.read_excel('Match_History.xlsx')

#double-check data head first 5 entries
Student.head(n=5) 
Tutor.head(n=5)  
Match_History.head(n=5)

# 1. Which tutors have a Dropped status and have achieved their certification after 4/01/2018?
print(Tutor[(Tutor['TutorStatus'] == 'Dropped') & (Tutor['CertDate'] > '4/1/2018')])
print('TutorID above have a Dropped status and have achieved their certification after 4/01/2018')
print('For the original given input, TutorID 107 have a Dropped status and have achieved their certification after 4/01/2018\n')
#TutorID 107 have a Dropped status and have achieved their certification after 4/01/2018

# 2. What is the average length of time a student stayed (or has stayed) in the program? 
#use by replacing the current date for ongoing tutoring 
Match_History = Match_History.replace({np.nan:pd.Timestamp.now()})
print(Match_History)
student_mean = pd.DataFrame( Match_History['EndDate'] -  Match_History['StartDate']).mean()
#display the result
print('The average length of time a student stayed (or has stayed) in the program:')
print(student_mean)
print('\n')
#The average length of time a student stayed (or has stayed) in the program is 497 days

# 3. Identify all students who have been matched in 2018 with a tutor whose status is Temp Stop.
Tutor_Match = pd.merge(Tutor.iloc[:,:3],Match_History.iloc[:,1:3], on = "TutorID")
Tutor_Match = Tutor_Match.drop('CertDate',axis =1)
#print(Tutor_Match)
#display the result
print(Tutor_Match[(Tutor_Match['TutorStatus']=='Temp Stop')])
print('StudentID above who have been matched in 2018 with a tutor whose status is Temp Stop')
print('For the original given input, StudentID 3001 who have been matched in 2018 with a tutor whose status is Temp Stop\n')
#StudentID 3001 who have been matched in 2018 with a tutor whose status is Temp Stop

# 4. List the Read scores of students who were ever taught by tutors whose status is Dropped.
#based on StudentID, merge Match_history and students data frames
Tutor_Match1 = pd.merge( Match_History.iloc[:,1:3], Student.iloc[:,:3], on = "StudentID")
#print(Tutor_Match1)
TS = pd. merge(Tutor_Match.iloc[:,:3], Tutor_Match1.iloc[:,:4], on= ["StudentID","TutorID"])
#print(TS)
#display the result
print('List the Read scores of students who were ever taught by tutors whose status is Dropped:')
print(TS[(TS['TutorStatus']=='Dropped')])
print('ReadScore above of students who were ever taught by tutors whose status is Dropped')
print('For the original given input, ReadScore = 1.3 of students who were ever taught by tutors whose status is Dropped\n')
#ReadScore = 1.3 of students who were ever taught by tutors whose status is Dropped

# 5. List the tutors who taught two or more students. 
#count the value of TutorID
v = Match_History.TutorID.value_counts()
#print(v)
#display the result
print('List the tutors who taught two or more students:')
print(Match_History[Match_History.TutorID.isin(v.index[v.gt(1)])])
print('TutorID above who taught two or more students')
print('For the original given input, TutorID 100 and 104 who taught two or more students\n')
#TutorID 100 and 104 who taught two or more students

# 6. Display a list of all students, their read score, their tutors, and tutors status. 
TS1 = TS[['StudentID','ReadScore','TutorID','TutorStatus']].copy()
print('The list of all students, their read score, their tutors, and tutors status:')
print(TS1)
print('\n')
#store TS1 in Student_Tutor.xlsx 
TS1.to_excel('Student_Tutor.xlsx',  index = False)
Tutor6=Tutor[['TutorID','TutorStatus']] #create data frame of columns TutorID and TutorStatus, then so on
Student6=Student[['StudentID','ReadScore']] 
match = Match_History[['TutorID','StudentID']] 
Student6.merge(match.merge(Tutor6, on="TutorID"), on="StudentID")

# 7. For each student group, list the number of tutors who have been matched with that group.
#create TU
TU = pd.merge( Match_History.iloc[:,1:3], Student.iloc[:,:2], on = "StudentID")
#display dataframe with the respected Student groups which containing the Tutor ID
print(Student[['StudentID','StudentGroup']].merge(match.merge(Tutor['TutorID'], on="TutorID"), on="StudentID"))
#display the result
print('For student group 1, list of tutor(s) who have been matched with that group:')
print(TU.loc[(TU['StudentGroup']==1),'TutorID'].value_counts())
print('For student group 2, list of tutor(s) who have been matched with that group:')
print(TU.loc[(TU['StudentGroup']==2),'TutorID'].value_counts())
print('For student group 3, list of tutor(s) who have been matched with that group:')
print(TU.loc[(TU['StudentGroup']==3),'TutorID'].value_counts())
print('For student group 4, list of tutor(s) who have been matched with that group:')
print(TU.loc[(TU['StudentGroup']==4),'TutorID'].value_counts())
print('For the original given input:')
print('For student group 1, list of 1 tutor(s) who have been matched with that group:')
print('For student group 2, list of 3 tutor(s) who have been matched with that group:')
print('For student group 3, list of 3 tutor(s) who have been matched with that group:')
print('For student group 4, list of 1 tutor(s) who have been matched with that group:')
#For student group 1, list of 1 tutor(s) who have been matched with that group
#For student group 2, list of 3 tutor(s) who have been matched with that group
#For student group 3, list of 3 tutor(s) who have been matched with that group
#For student group 4, list of 1 tutor(s) who have been matched with that group

# 8. List all active students who started in May and June. 
#display the result
print('\nList all active students who started in May and June:')
print(Match_History[(Match_History['StartDate'] > '5/1/2018') & (Match_History['EndDate'] > '11/1/2020')])
print('StudentID above are all active students who started in May and June')
print('For the original given input, StudentID 3003, 3006, 3001 are all active students who started in May and June\n')

# 9. Find students who have not been tutored yet.
#display the result
print(pd.merge(Student[['StudentID']],Match_History[['TutorID','StudentID']], how='outer'))
print('StudentID above having NaN values for TutorID who have not been tutored yet')
print('For the original given input, StudentID 3007 who have not been tutored yet\n')
#StudentID 3007 who have not been tutored yet

# 10. Find tutors who did not tutor any students.
#display the result
print(pd.merge(Tutor[['TutorID']],Match_History[['TutorID','StudentID']], how='outer'))
print('TutorID above having NaN values for StudentID who did not tutor any students')
print('For the original given input, TutorID 105, 107 who did not tutor any students\n')
#TutorID 105, 107 who did not tutor any students
#Happy Ending