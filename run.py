# #!/usr/bin/env python2
# # -*- coding: utf-8 -*-
# """
# Created on Sun May  7 18:16:51 2017
#
# @author: leigh

# from api import app
# app.run(debug=True)
import textract, json, sys
from datetime import datetime, timedelta
import re
import urllib
import ast
import os

# loop trhough resumes

def main():
    indir = 'PDFs/google/'
    employees = []
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f[0] is not '.':
                # print(indir + f)
                text = textract.process(indir + f)
                # print 'text', text
                employee = parseResume(text)
                employees.append(employee)
    json.dump(employees, open('demo_data.json', 'w'))

def parseResume(text):
    # Find the different sections
    # print text
    Name = text.splitlines()[0]
    NameSections = text.split(Name)
    # print NameSections[2]
    FirstName = NameSections[2].split('Contact')[1].split(' ')[1]
    # print FirstName
    Experience = findSection(text, 'Experience', 'Education')
    Summary = findSection(text, 'Summary', 'Experience')
    Education = findSection(text, 'Education', Name)
    # print Education
    years_working = 0
    employee = {
        "name": Name,
        "first_name": FirstName,
        "companies": parseCompanies(Experience),
        "gender":checkGender(FirstName),
        "education": parseEducation(Education),
        "age": estimateAge()
    }
    # print employee['education']
    return employee


# Chunk the companies from Experience
def parseCompanies(Experience):
    textArray = Experience.splitlines()
    # resume_pattern = ['company', 'date', 'description']
    companies = []
    clean_lines = cleanLines(textArray)
    all_lines_length = len(clean_lines)
    for index, clean_line in enumerate(clean_lines):
        dates = clean_line.split('-')
        name_line = parseName(clean_lines[index - 1])
        # if line has a date, chunk into companies
        if checkIfDate(dates[0]) is not None:
            # print 'is date'
            company = {}
            lines_after =  (index + 1) - all_lines_length
            company['name'] = name_line['name']
            company['position'] = name_line['position']
            # parse the dates
            start_date = checkIfDate(dates[0])
            end_date=checkIfDate(dates[1])
            # print type(end_date['date_exract'])
            company['start_date'] = start_date['date_exract'],
            company['end_date'] = end_date['date_exract'],
            company['years_working'] = end_date['years_working']
            company['definiton'] = checkForDefiniton(clean_lines, lines_after)
            companies.append(company)
            # print company
        # else:
        #     print 'is not'#, clean_line
        # print len(companies)
    return companies
def findSection( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def cleanLines(textArray):
    clean_lines = []
    # print type(textArray)
    for index, line in enumerate(textArray):
        # print index, line
        if re.match(r'^\r*$', line):
            # adjusted_index = int(index) - 1
            continue
        elif re.match(r'Page ', line):
            # adjusted_index = (int(index)) - 1
            continue
        else:
            clean_lines.append(line)
            # adjusted_index = adjusted_index + 1
    return clean_lines
def parseName(name):
    # Todo check if split by dash like the first one
    # if not split by -
    name_split = name.split(' at ')
    if (len(name_split) > 1):
        return {'name': name_split[1], 'position': name_split[0]}
    else:
        return {'name': '', 'position': name_split[0]}
def checkIfDate(date):
    # print date.strip(), 'what comes in '
    try:
        if datetime.strptime(date, "%B %Y "):
            # print datetime.strptime(date, "%B %Y "), 'is date'
            return {"date_exract": datetime.strptime(date, "%B %Y ").strftime("%B %Y")}
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
        if("(" and ")" and "month" in date):
            date_exract = date.split('(')[0]
            years_working = date.split('(')[1].strip(')')
            # print years_working
            # print date_exract, findSection(date, "(", ")"), 'date with parens'
            return {"date_exract": date_exract.strip(), "years_working": years_working}
    except:
        return False
def checkForDefiniton(clean_lines, lines_after):
    # parse lines until you find a date
    definition_text = []
    remaining_lines = clean_lines[lines_after: len(clean_lines)]
    # print remaining_lines
    # print lines_after, clean_lines[lines_after: len(clean_lines)]
    # for remaining lines in clean_lines
    for line in remaining_lines:
        if (checkIfDate(line) is None):
            definition_text.append(line)
        else:
            # remove the last line
            print line
            print checkIfDate(line)
            definition_text.pop()
            break
    return ' '.join([str(x) for x in definition_text])
def checkGender(FirstName):
    f = urllib.urlopen("https://api.genderize.io/?name=" + FirstName)
    results = f.read()
    gender = ast.literal_eval(results)['gender']
    print gender
    return gender
def parseEducation(ed_section):
    ed_lines = ed_section.splitlines()
    clean_ed_lines = cleanLines(ed_lines)
    education = []
    for (index, line) in enumerate(clean_ed_lines):
        # if it contains a date
        school = {}
        if ',' in line:
            degree_line = line.split(',')
            if '-' in degree_line[-1]:
                dates = degree_line[-1].split('-')
                school['start'] = dates[0].strip()
                school['end'] = dates[1].strip()
                school['name'] = clean_ed_lines[index - 1]
                education.append(school)
    return education
def estimateAge():
    print "test"
    # check education for highschool
    # check education for Degree
    # estimate age based on graduation
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
