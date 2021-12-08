#!/usr/bin/env python
# coding: utf-8

import re
import sylnwp
import sylwp

#fo = [('Barbara','MaP','SaM','SaP'),('Celarent','MeP','SaM','SeP')] #list of all first figure syllogisms
syls = [('Cesare','PeM','SaM','SeP'),('Camestres','PaM','SeM','SeP'),('Festino','PeM','SiM','SoP'),('Baroco','PaM','SoM','SoP'),('Darapti','MaP','MaS','SiP'),('Felapton','MeP','MaS','SoP'),('Disamis','MiP','MaS','SiP'),('Datisi','MaP','MiS','SiP'),('Bocardo','MoP','MaS','SoP'),('Ferison','MeP','MiS','SoP'),('Bamalip','PaM','MaS','SiP'),('Camenes','PaM','MeS','SeP'),('Dimatis','PiM','MaS','SiP'),('Fesapo','PeM','MaS','SoP'),('Fresison','PeM','MiS','SoP')] # list of tuples matching syllogism names to their formal description

problems = [('Disamis','MiP','MaS','SiP'),]

def premises(syllogism): # given a name returns the premises assiociated with it
	for i in syls:
		if i[0] == syllogism:
			return (i[1], 'premise'), (i[2], 'premise'), (i[3], 'conclusion')
#def figure(syllogism):
#	for i in fo:
#		if i[0][0] == syllogism[0]:
#			return i[1], i[2]

def barbara(a,b):
	if a[0] == b[2] and a[1] == 'a' and b[1] == 'a' and a[2] != b[0] and a[0] != a[2]:
		return b[0]+'a'+a[2]
	else:
		return 'OoO'
#def barbari(a,b):
#	if a[0] == b[2] and a[1] == 'a' and b[1] == 'a' and a[2] != b[0] and a[0] != a[2]:
#		return b[0]+'i'+a[2]
def celarent(a,b):
	if a[0] == b[2] and a[1] == 'e' and b[1] == 'a' and a[2] != b[0] and a[0] != a[2]:
		return b[0]+'e'+a[2]
	else:
		return 'OoO'
def darii(a,b):
	if a[0] == b[2] and a[1] == 'a' and b[1] == 'i' and a[2] != b[0] and a[0] != a[2]:
		return b[0]+'i'+a[2]
	else:
		return 'OoO'
def ferio(a,b):
	if a[0] == b[2] and a[1] == 'e' and b[1] == 'i' and a[2] != b[0] and a[0] != a[2]:
		return b[0]+'o'+a[2]
	else:
		return 'OoO'
#def celaront(a,b):
#	if a[0] == b[2] and a[1] == 'e' and b[1] == 'a' and a[2] != b[0] and a[0] != a[2]:
#		return b[0]+'o'+a[2]

def contradict(s):
	if s == 'SaP':
		return 'SoP'
	if s == 'SoP':
		return 'SaP'
	if s == 'SeP':
		return 'SiP'
	if s == 'SiP':
		return 'SeP'

def contrcheck(a,b):
	if a[0] == b[0] and a[2] == b[2]:
		if a[1] == 'a' and (b[1] == 'e' or b[1] == 'o'):
			return 'contradiction'
		elif a[1] == 'i' and (b[1] == 'e'):
			return 'contradiction'
		elif a[1] == 'e' and (b[1] == 'a' or b[1] == 'i'):
			return 'contradiction'	
		elif a[1] == 'o' and (b[1] == 'a'):
			return 'contradiction'


def clues(syllogism):
	syl = syllogism
	first = re.search('[aeoi]',syl)
	first_index = syl.index(first.group())
	syl = syl[syl.index(first.group())+1:]
	second = re.search('[aeoi]',syl)
	second_index = first_index+syl.index(second.group())+1
	syl = syl[syl.index(second.group())+1:]
	third = re.search('[aeoi]',syl)
	third_index = second_index+syl.index(third.group())+1
	syl = syl[syl.index(third.group())+1:]
	return (first.group(), first_index), (second.group(), second_index), (third.group(), third_index)

def syl(syllogism): #
	p1, p2, concl = premises(syllogism) # get the premises and conclusion and add the premises to the proof
	proof = [p1, p2]
	step = [p1, p2]
	clue1, clue2, clue3 = clues(syllogism) # gives the premise/conclusion letters and their indices in syllogism
	if 'c' in syllogism[1:]:
			contr = contradict(concl[0])
			add = ('$\lnot$ '+concl[0], 'a.p.b.c.')
			proof.append(add)
			proof.append((contr, 'negation, '+str(proof.index(add)+1)))
			for i in step:
				if syllogism[0] == 'B':
					result = barbara(i[0],contr)
					for p in proof:
						if contrcheck(result,p[0]) == 'contradiction':
							add1 = (result, 'Barbara, '+str(proof.index(i)+1)+', '+str(proof.index(add)+2))
							proof.append(add1)
							proof.append((concl[0], 'contradiction, '+str(proof.index(add1)+1)+', '+str(proof.index(p)+1)))
							break
						else:
							result1 = barbara(contr,i[0])
							if contrcheck(result1,p[0]) == 'contradiction':
								add1 = (result1, 'Barbara, '+str(proof.index(i)+1)+', '+str(proof.index(add)+2))
								proof.append(add1)
								proof.append((concl[0], 'contradiction, '+str(proof.index(add1)+1)+', '+str(proof.index(p)+1)))
								break
	if 's' in syllogism[clue1[1]:clue2[1]]:
		add = (p1[0][2]+p1[0][1]+p1[0][0], 'simplex, '+str(proof.index(p1)+1))
		proof.append(add)
		step[0] = add
	if 'p' in syllogism[clue1[1]:clue2[1]]:
		add = (p1[0][2]+'i'+p1[0][0], 'per accidens, '+str(proof.index(p1)+1))
		proof.append(add)
		step[0] = add
	if 's' in syllogism[clue2[1]:clue3[1]]:
		add = (p2[0][2]+p2[0][1]+p2[0][0], 'simplex, '+str(proof.index(p2)+1))
		proof.append(add)
		step[1] = add
	if 'p' in syllogism[clue2[1]:clue3[1]]:
		add = (p2[0][2]+'i'+p2[0][0], 'per accidens, '+str(proof.index(p2)+1))
		proof.append(add)
		step[1] = add
	if ('m' in syllogism[clue1[1]:clue2[1]]) or ('m' in syllogism[clue2[1]:clue3[1]]):
		step[0],step[1] = step[1],step[0]
#	if syllogism[0] == 'B' and val == 'w':
#		result = barbari(step[0][0],step[1][0])
#		proof.append((result, 'Barbari, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
	if syllogism[0] == 'B' and not ('c' in syllogism[1:]):
		result = barbara(step[0][0],step[1][0])
		proof.append((result, 'Barbara, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
#	if syllogism[0] == 'C' and val =='w':
#		result = celaront(step[0][0],step[1][0])
#		proof.append((result, 'Celaront, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
	if syllogism[0] == 'C':
		result = celarent(step[0][0],step[1][0])
		proof.append((result, 'Celarent, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
	if syllogism[0] == 'D':
		result = darii(step[0][0],step[1][0])
		proof.append((result, 'Darii, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
	if syllogism[0] == 'F':
		result = ferio(step[0][0],step[1][0])
		proof.append((result, 'Ferio, '+str(proof.index(step[0])+1)+', '+str(proof.index(step[1])+1)))
	if 'p' in syllogism[clue3[1]:]:
		proof.append((proof[-1][0][2]+'i'+proof[-1][0][0], 'per accidens, '+str(proof.index(proof[-1])+1)))
	if 's' in syllogism[clue3[1]:]:
		proof.append((proof[-1][0][2]+proof[-1][0][1]+proof[-1][0][0], 'simplex, '+str(proof.index(proof[-1])+1)))
	if proof[-1][0] == concl[0]:
		return syllogism,proof
	else:
		return syllogism, "there was something wrong with the proof"



def pretty_print():
	labels = ['labelOnlyA={\\footnotesize \\textbf{+}},','labelOnlyAB={\\footnotesize \\textbf{+}},','labelOnlyB={\\footnotesize \\textbf{+}},','labelOnlyAC={\\footnotesize \\textbf{+}},','labelABC={\\footnotesize \\textbf{+}},','labelOnlyBC={\\footnotesize \\textbf{+}},','labelOnlyC={\\footnotesize \\textbf{+}},']
	print '\documentclass[16pt,a4paper]{article}'
	print '\usepackage[utf8]{inputenc}'
	print '\usepackage[T2A,T1]{fontenc}'
	print '\usepackage{graphicx}'
	print '\usepackage{pbox}'
	print '\usepackage{multicol}'
	print '\setlength{\columnsep}{1cm}'
	#print '\usepackage{amssymb}'
	print '\usepackage{longtable}'
	print '\usepackage{venndiagram}'
	print '\pagenumbering{gobble}'
	#print '\usepackage[cm]{fullpage}'
	#print '\usepackage[lmargin=0cm,rmargin=0cm, bottom=0cm, top=0cm]{geometry}'
	#print '\usepackage{hyperref}'
	print '\\begin{document}'
	print '\\begin{multicols}{2}'
	#print '\\begin{longtable}{ c  c }'
	#print 'Proof & Venn reductio ad absurdum \\\\'
	for s in syls:
		result = syl(s[0])
		print '\section*{',result[0],': \\begin{footnotesize}',s[1],s[2],'|',s[3],'\end{footnotesize} }'
		print '\\begin{enumerate}'
		for i in result[1]:
			print '\item',i[0],i[1]#,'\\\\'
		print '\end{enumerate}'
		#print '\\newpage'
		venn1 = sylnwp.syl([s[1],s[2],s[3]])
		print '\\begin{venndiagram3sets}['
		for k,j in enumerate(venn1[2]):
			if '+' in j:
				print labels[k]
		print 'labelNotABC={',venn1[0][0],'}]'
		if 'x' in venn1[2][0] and 'x' in venn1[2][3]:
			print '\\fillANotB'
		if 'x' in venn1[2][1] and 'x' in venn1[2][2]:
			print '\\fillBNotC'	
		if 'x' in venn1[2][2] and 'x' in venn1[2][5]:
			print '\\fillBNotA'
		if 'x' in venn1[2][3] and 'x' in venn1[2][6]:
			print '\\fillCNotB'	
		if 'x' in venn1[2][5] and 'x' in venn1[2][6]:
			print '\\fillCNotA'
		
		if 'x' in venn1[2][1] and 'x' in venn1[2][4]:
			print '\\fillACapB'
		if 'x' in venn1[2][3] and 'x' in venn1[2][4]:
			print '\\fillACapC'
		if 'x' in venn1[2][4] and 'x' in venn1[2][5]:
			print '\\fillBCapC'
 		print '\end{venndiagram3sets}'
		venn2 = sylwp.syl([s[1],s[2],s[3]])
		print '\\begin{venndiagram3sets}['
		for k,j in enumerate(venn2[2]):
			if '+' in j:
				print labels[k]
		print 'labelNotABC={',venn2[0][0],'}]'
		#print ']'
		if 'x' in venn2[2][0] and 'x' in venn2[2][3]:
			print '\\fillANotB'
		if 'x' in venn2[2][1] and 'x' in venn2[2][2]:
			print '\\fillBNotC'	
		if 'x' in venn2[2][2] and 'x' in venn2[2][5]:
			print '\\fillBNotA'
		if 'x' in venn2[2][3] and 'x' in venn2[2][6]:
			print '\\fillCNotB'	
		if 'x' in venn2[2][5] and 'x' in venn2[2][6]:
			print '\\fillCNotA'
		
		if 'x' in venn2[2][1] and 'x' in venn2[2][4]:
			print '\\fillACapB'
		if 'x' in venn2[2][3] and 'x' in venn2[2][4]:
			print '\\fillACapC'
		if 'x' in venn2[2][4] and 'x' in venn2[2][5]:
			print '\\fillBCapC'
 		print '\end{venndiagram3sets}'
	print '\end{multicols}'
	print '\end{document}'
#pretty_print()	
#print syl('Disamis')
#print syl('Camestres')
#print syl('Bamalip')
#print premises('Bamalip')
#print clue_one('Brrrrarmarrlip')
