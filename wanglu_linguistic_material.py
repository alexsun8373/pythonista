from objc_util import *
import sys
import ui
import sqlite3
from sqlite3 import Error
import speech

#TODO
#1.add name for each chapter, for example chapter3("特别名词")
#2.change word to element in database, becase chapter is word, chapter5 is phrase


#database structure
# 			id								chapter							section								number								 element
#	 each word only			chapter in book			section in book		number in each section			word or phrase
#				1										3										2											1										ability	
#				2										3										2											2										abstract
# 		 ...								 ...								 ...									 ...									  ...
#			 50(dummy)						3										3											1										cabinet
#			 51(dummy)						3										2											2										cable 
# 		 ...								 ...								 ...									 ...									  ...
#			 512(dummy)						4										2											1										abnormal
#			 513(dummy)						4										2											2										academic   

debug = False
G_DB_ROW_LENGTH = 1
g_current_db_index = 1	#the element  in databse(the number in the database)
g_db_id = 1							#the identify number in database(each element only has one)	
g_db_element = ''				#the element(word or phrase) in database
g_db_chapter = 3				#the chapter number in database
g_db_section = 2				#the section number in datavse


def button_next_tapped(sender):
	global g_current_db_index
	global G_DB_ROW_LENGTH	
	global g_db_id
	global g_db_element
	global g_db_chapter
	global g_db_section
	
	try:
		conn = sqlite3.connect("wanglu_linguistic_material.db")
		cursor = conn.cursor()
		if g_current_db_index == G_DB_ROW_LENGTH:
			g_current_db_index = 1
		cursor.execute("""SELECT * FROM wanglu_linguistic_material WHERE chapter=? AND section=? AND number=?""",(g_db_chapter,g_db_section,g_current_db_index,))	
		row = cursor.fetchone()
		g_current_db_index = g_current_db_index + 1
		g_db_id = row[1]
		g_db_element = row[4]
		speech.say(g_db_element,'en-UK',0.5)		
		conn.close
		
	except Error:
		print(Error)
def fun1(_self,_cmd):
	print('test')
def fun2(_self,_cmd):
	print('test')
def fun3(_self,_cmd):
	print('test')
def button_details_tapped(sender):
	global g_db_element
	global debug
	global v 
	try:
		label_englishshow.text = g_db_element
		UIReferenceLibraryViewController = ObjCClass('UIReferenceLibraryViewController')
		UIViewController = ObjCClass('UIViewController')
		input = g_db_element
		
		methods = [fun1,fun2,fun3]
		protocols=['ARSCNViewDelegate']
		referenceViewController = create_objc_class('referenceViewController',UIViewController,methods=methods,protocols=protocols)
		referenceViewController = UIReferenceLibraryViewController.alloc().initWithTerm_(input).autorelease()
		
		ObjCInstance(v).addSubview_(referenceViewController.view())
		
		rootVC = UIApplication.sharedApplication().keyWindow().rootViewController()
		tabVC = rootVC.detailViewController()

		referenceViewController.setTitle_('Definition: {0}{1}{0}'.format('\'', input))
		referenceViewController.setPreferredContentSize_(CGSize(540, 540))
		referenceViewController.setModalPresentationStyle_(2)       
		#tabVC.addTabWithViewController_(referenceViewController)
		tabVC.presentViewController_animated_completion_(referenceViewController, True, None)
		
	except Error:
		print(Error)
def button_pronounce_tapped(sender):
	global g_db_element
	try:
		speech.say(g_db_element,'en-UK',0.5)
	except Error:
		print(Error)
		
def textfield_wordtypein_tapped(sender):
	global g_db_element
	global debug
	try:
		label_englishshow.text = g_db_element
		if debug == True:
			print("textfield_wordtypein_tapped function")
	except Error:
		print(Error)
			
def textfield_chapter_tapped(sender):
	global  g_db_chapter
	try:
		g_db_chapter = int(sender.text)
	except Error:
		print(Error)

def textfield_section_tapped(sender):
	global g_db_section
	try:
		g_db_section = int(sender.text)
	except Error:
		print(Error)


v = ui.load_view()
label_englishshow = v['label_englishshow']
label_chinese_meaningshow = v['label_chinese&meaningshow']
textfield_wordtypein = v['textfield_wordtypein']


textfield_chapter = v['textfield_chapter']
textfield_section = v['textfield_section']
textfield_chapter.text = str(g_db_chapter)
textfield_section.text = str(g_db_section)
#get the row length of database
conn = sqlite3.connect('wanglu_linguistic_material.db')
cursor = conn.cursor()
cursor.execute("select * from wanglu_linguistic_material")
results = cursor.fetchall()	
G_DB_ROW_LENGTH = len(results)
conn.close
#end
v.present('sheet')

