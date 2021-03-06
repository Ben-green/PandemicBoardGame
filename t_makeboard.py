#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest
import sqlite3
from makeboard import startinggame


class T( unittest.TestCase ):

# This def should test if the createcountry
	def test_setup (self):
		sg = startinggame ()
		sg.setup ( )
		with sqlite3.connect('pandemic.db') as conn:
			cursor = conn.cursor()
			tobedone = 'SELECT * FROM countries;'
			cursor.execute( tobedone)
			answer = cursor.fetchone ( )
		self.assertEqual(answer,None,'The table for countries was not created.')

	def test_setupboard (self):
		sg = startinggame ()
		sg.setupboard ('testboard.txt')
		with sqlite3.connect('pandemic.db') as conn:
			cursor = conn.cursor()
			tobedone = 'SELECT * FROM countries;'
			cursor.execute( tobedone)
			answer = cursor.fetchone ( )
			col1 = answer [0]
			col2 = answer [1]
			col4 = answer [3]
		self.assertEqual(col1,'Atlanta','The country name was not added to the database')
		self.assertEqual(col2,2,'The number of countries was not added to the database')
		self.assertEqual(col4,'Newyork','The names of connecting countries were not added to the database')

	def test_setupresearch (self):
		sg = startinggame ()
		sg.setupresearch( )
		with sqlite3.connect('pandemic.db') as conn:
			cursor = conn.cursor()
			tobedone = """SELECT research FROM countries WHERE name is 'Atlanta';"""
			cursor.execute( tobedone)
			answer = cursor.fetchone ()
		answerR = answer [0]
		self.assertEqual(answerR,1,'A research station cannot be found in Atlanta.')


	def test_setupcubes (self):
		sg = startinggame ()
		sg.setupcubes( )
		with sqlite3.connect('pandemic.db') as conn:
			cursor = conn.cursor()
			tobedone = """SELECT nocubes FROM cubes WHERE col is 'Red';"""
			cursor.execute( tobedone)
			answer = cursor.fetchone ()
		answerR = answer [0]
		self.assertEqual(answerR,20,'The amount of Red cubes is wrong.')
	
	def test_setupplayerdeck (self):
		sg = startinggame ()
		sg.setupplayerdeck ('testboard.txt')
		with sqlite3.connect('pandemic.db') as conn:
			cursor = conn.cursor()
			tobedone = 'SELECT * FROM playerdeck;'
			cursor.execute( tobedone)
			answer = cursor.fetchall ()
			col1 = answer [0]
			col2 = answer [1]
			col3 = answer [2]
		self.assertEqual(col1,'Atlanta','Player card not found')
		self.assertEqual(col2,'Chicago','Player card not found')
		self.assertEqual(col4,'Denver','Player card not found')
