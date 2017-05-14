# #!/usr/bin/env python2
# # -*- coding: utf-8 -*-
# """
# Created on Sun May  7 18:16:51 2017
#
# @author: leigh
# """
#

# from api import app
# app.run(debug=True)
import textract, json, sys
from datetime import datetime, timedelta
import re
# loop trhough resumes
text = textract.process("PDFs/google/AndrewLeeProfile.pdf")
# Find the different sections
def findSection( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

Name = text.splitlines()[0]
Experience = findSection(text, 'Experience', 'Education')
Summary = findSection(text, 'Summary', 'Experience')
Education = findSection(text, 'Experience', Name)
years_working = 0

def main():
    parseResume()

def parseResume():
    employee = {
        "name": Name,
        "first_name": "",
        "companies":parseCompanies(Experience),
        "gender":'test',
        'age':''
    }
    # json.dump(employee, open('demo_data.json', 'w'))

# Chunk the companies from Experience
def parseCompanies(Experience):
    textArray = Experience.splitlines()
    resume_pattern = ['company', 'date', 'description']
    companies = []

    adjusted_index = 0
    company_counter = 0
    for index, line in enumerate(textArray):
        company = {}
        if re.match(r'^\s*$', line):
            adjusted_index = int(index) - 1
            continue
        elif re.match(r'Page ', line):
            adjusted_index = (int(index)) - 1
            continue
        else:
            adjusted_index = adjusted_index + 1
            print adjusted_index, line
            if resume_pattern[company_counter] == 'company':
                company['name'] = line
                company_counter = company_counter + 1
            elif resume_pattern[company_counter] == 'date':
                company_counter = company_counter + 1
                company['date'] = line
            else:
                company_counter = 0
                company['description'] = line
        print company
    #     start_date = ''
    #     end_date = ''
    #     company_name = ''
    #     desctiption = ''
    #     # if pre_line = '' first line it's the company
    #     if(resume_pattern[index] == 'company'):
    #         company_name = line
    #         print company_name
    #     # check if line is a date split by a dash
    #     # if (line == 'October 2014 - Present' and '-' in line) :
    #     if (resume_pattern[index] =='date' and '-' in line) :
    #         dates = line.split('-')
    #         start_date=checkIfDate(dates[0])
    #         end_date=checkIfDate(dates[1])
    #         # Verify it is a date and not a String
    #         years_working=totalYears(start_date, end_date)
    #         company['start_date'] = start_date['date_exract'],
    #         company['end_date'] = end_date['date_exract'],
    #         company['years_working'] = end_date['date_exract']
    #     company['description'] = line
    #     companies.append( company)
    #     print company
def checkIfDate(date):
    print date.strip(), 'what comes in '
    try:
        if datetime.strptime(date, "%B %Y "):
            # print datetime.strptime(date, "%B %Y "), 'is date'
            return {"date_exract": datetime.strptime(date, "%B %Y ").strftime("%B %Y"), 'years_working':''}
    except:
        pass
    try:
        if(date.strip() == 'Present'):
            now = datetime.today().strftime("%B %Y ")
            # print datetime.strptime(now, "%B %Y "), 'is present'
            return {"date_exract": now, 'years_working':''}
    except:
        pass
    try:
        if("(" and ")" in date):
            date_exract = date.split('(')[0]
            years_working = date.split('(')[1].strip(')')
            print years_working
            # print date_exract, findSection(date, "(", ")"), 'date with parens'
            return {"date_exract": date_exract.strip(), "years_working": years_working}
    except:
        print 'is not parens'

def totalYears(start, end):
    # if end contains parens
    # return (end - start)
    print end, 'this it the end'
def estimateAge():
    print "test"
    # check education for highschool
    # check education for Degree
    # estimate age based on graduation

def estimateExperienceYears():
    print "test"
    # find earliest date for estimateExperienceYears
    # find present or latest date
    # calculate years

if __name__ == '__main__':
    main()

# import sys, json, numpy as np
#
# #Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     #Since our input would only be having one line, parse our JSON data from that
#     return json.loads(lines[0])
#
# def main():
#     #get our data as an array from read_in()
#     lines = read_in()
#
#     #create a numpy array
#     np_lines = np.array(lines)
#
#     #use numpys sum method to find sum of all elements in the array
#     lines_sum = np.sum(np_lines)
#     json.dump(lines_sum, open('demo_data.json', 'w'))
#     #return the sum to the output stream
#     print lines_sum
#
# #start process
# if __name__ == '__main__':
#     main()
#!flask/bin/python
# from flask import Flask, make_response
# import pandas as pd
#
# app = Flask(__name__)
#
# dummy_data = {
#     0: pd.DataFrame({'name':['A', 'B', 'C', 'D'], 'value':[4, 2, 8, 5]}),
#     1: pd.DataFrame({'name':['A', 'B', 'C'], 'value':[13, 29, 9]}),
#     2: pd.DataFrame({'name':['A', 'B', 'C','D', 'E', 'F'], 'value':[3, 12, 9, 21, 15, 7]})
#     }
#
# @app.route('/')
# def index():
#     return make_response(open('index.html').read())
#
#
# @app.route('/api/<int:id>')
# def api(id):
#     return make_response(dummy_data[id].to_json(orient='records'))
#
#
# if __name__ == '__main__':
#     app.run(debug = True)
