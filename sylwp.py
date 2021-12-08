#!/usr/bin/env python
# coding: utf-8

def wff(L): # dummy for now
	return True
def revert(A):
	if 'o' in A:
		return 'SaP'
	if 'i' in A:
		return 'SeP'
	if 'a' in A:
		return 'SoP'
	if 'e' in A:
		return 'SiP'
def syl(L):
	mark = ['0']*7
	val = ''
	conc = revert(L[2])
	count = 1
	order = ['']*3
	if wff(L):
		if L[0] == 'PaM':
			mark[0] = 'x'
			mark[3] = 'x'
			order[0] = count
			count = count+1
		if L[0] == 'MaP':
			mark[2] = 'x'
			mark[5] = 'x'
			order[0] = count
			count = count+1
		if L[1] == 'MaS':
			mark[1] = 'x'
			mark[2] = 'x'
			order[1] = count
			count = count+1
		if L[1] == 'SaM':
			mark[3] = 'x'
			mark[6] = 'x'
			order[1] = count
			count = count+1
		#if conc == 'SaP':
		#	mark[5] = 'x'
		#	mark[6] = 'x'
		if 'e' in L[0]:
			mark[1] = 'x'
			mark[4] = 'x'
			order[0] = count
			count = count+1
		if 'e' in L[1]:
			mark[4] = 'x'
			mark[5] = 'x'
			order[1] = count
			count = count+1
		#if 'e' in conc:
		#	mark[3] = 'x'
		#	mark[4] = 'x'
		if 'i' in L[0]:
			#if mark[1] == 'x' and mark[4] == 'x':
			#	val = 'valid'
			#	mark[1] = 'x+'
			#	mark[4] = 'x+'
			if mark[1] == 'x':
				mark[4] = '+'
			elif mark[4] == 'x':
				mark[1] = '+'
			else:
				mark[1] = '+'
				mark[4] = '+'
			order[0] = count
			count = count+1
		if 'i' in L[1]:
			#if mark[4] == 'x' and mark[5] == 'x':
			#	val = 'valid'
			#	mark[4] = 'x+'
			#	mark[5] = 'x+'
			if mark[4] == 'x':
				mark[5] = '+'
			elif mark[5] == 'x':
				mark[4] = '+'
			else:
				mark[4] = '+'
				mark[5] = '+'
			order[1] = count
			count = count+1
		#if 'i' in conc:
		#	if mark[3] == 'x' and mark[4] == 'x':
		#		val = 'valid'
		#		mark[3] = 'x+'
		#		mark[4] = 'x+'
		#	elif mark[3] == 'x':
		#		mark[4] = '+'
		#	elif mark[4] == 'x':
		#		mark[3] = '+'
		#	else:
		#		mark[3] = '+'
		#		mark[4] = '+'
		if L[0] == 'PoM':
			#if mark[0] == 'x' and mark[3] == 'x':
			#	val = 'valid'
			#	mark[0] = 'x+'
			#	mark[3] = 'x+'
			if mark[0] == 'x':
				mark[3] = '+'
			elif mark[3] == 'x':
				mark[0] = '+'
			else:
				mark[0] = '+'
				mark[3] = '+'
			order[0] = count
			count = count+1
		if L[0] == 'MoP':
			#if mark[2] == 'x' and mark[5] == 'x':
			#	val = 'valid'
			#	mark[2] = 'x+'
			#	mark[5] = 'x+'
			if mark[2] == 'x':
				mark[5] = '+'
			elif mark[5] == 'x':
				mark[2] = '+'
			else:
				mark[2] = '+'
				mark[5] = '+'
			order[0] = count
			count = count+1
		if L[1] == 'SoM':
			#if mark[3] == 'x' and mark[6] == 'x':
			#	val = 'valid'
			#	mark[3] = 'x+'
			#	mark[6] = 'x+'
			if mark[3] == 'x':
				mark[6] = '+'
			elif mark[6] == 'x':
				mark[3] = '+'
			else:
				mark[3] = '+'
				mark[6] = '+'
			order[1] = count
			count = count+1
		if L[1] == 'MoS':
			#if mark[1] == 'x' and mark[2] == 'x':
			#	val = 'valid'
			#	mark[1] = 'x+'
			#	mark[2] = 'x+'
			if mark[1] == 'x':
				mark[2] = '+'
			elif mark[2] == 'x':
				mark[1] = '+'
			else:
				mark[1] = '+'
				mark[2] = '+'
			order[1] = count
			count = count+1
		#if conc == 'SoP':
		#	if mark[5] == 'x' and mark[6] == 'x':
		#		val = 'valid'
		#		mark[5] = 'x+'
		#		mark[6] = 'x+'
		#	elif mark[5] == 'x':
		#		mark[6] = '+'
		#	elif mark[6] == 'x':
		#		mark[5] = '+'
		#	else:
		#		mark[5] = '+'
		#		mark[6] = '+'
		if L[1] == 'PoS':
			#if mark[0] == 'x' and mark[1] == 'x':
			#	val = 'valid'
			#	mark[0] = 'x+'
			#	mark[1] = 'x+'
			if mark[0] == 'x':
				mark[1] = '+'
			elif mark[1] == 'x':
				mark[0] = '+'
			else:
				mark[0] = '+'
				mark[1] = '+'
			order[1] = count
			count = count+1
	#if mark[3] == 'x' and mark[4] == 'x' and mark[5] == 'x' and mark[6] == 'x':
	#	val = 'valid'
	#if mark[0] == 'x' and mark[1] == 'x' and mark[3] == 'x' and mark[4] == 'x':
	#	val = 'valid'
	#if mark[1] == 'x' and mark[2] == 'x' and mark[4] == 'x' and mark[5] == 'x':
	#	val = 'valid'
	#if val == '':
	#	val = 'invalid'
		if L[2] == 'SaP' and mark[5] == 'x' and mark[6] == 'x':
			val = 'valid'
		elif L[2] == 'SeP' and mark[3] == 'x' and mark[4] == 'x':
			val = 'valid'
		elif L[2] == 'SiP':
			if (mark[0] == 'x' and mark[1] == 'x' and mark[4] == 'x') or (mark[0] == 'x' and mark[1] == 'x' and mark[3] == 'x') or (mark[3] == 'x' and mark[5] == 'x' and mark[6] == 'x') or (mark[2] == 'x' and mark[3] == 'x' and mark[5] == 'x') or (mark[1] == 'x' and mark[2] == 'x' and mark[5] == 'x'):
				val = 'valid'
			if mark[4] == '+':
				if mark[5] == 'x' and mark[1] == '0':
					val = 'valid'
				elif mark[1] == 'x' and mark[5] == '0':
					val = 'valid'
				else:
					mark[4] = '0'
			if mark[3] == '+':
				if mark[0] == 'x' and mark[4] == 'x':
					val = 'valid'
				elif mark[4] == 'x' and mark[0] == '0' and mark[6] != '+':
					val = 'valid'
				else:
					mark[3] = '0'
		elif L[2] == 'SoP':
			if (mark[3] == 'x' and mark[4] == 'x' and mark[5] == 'x') or (mark[3] == 'x' and mark[4] == 'x' and mark[6] == 'x') or (mark[1] == 'x' and mark[2] == 'x' and mark[4] == 'x'):
				val = 'valid'
			if mark[5] == '+':
				if mark[2] == 'x' and mark[4] == '0':
					val = 'valid'
				elif mark[4] == 'x' and mark[2] == '0':
					val = 'valid'
				else:
					mark[5] = '0'
			if mark[6] == '+':
				if mark[3] == 'x' and mark[5] == '0':
					val = 'valid'
				elif mark[5] == 'x' and mark[3] == '0':
					val = 'valid'
				else:
					mark[6] = '0'
		if val == '':
			val = 'invalid'
	return val, L, mark, order

# returns all and  valid syllogisms

def all_syl():
	majorp = ['PaM','MaP','PeM','MeP','PiM','MiP','PoM','MoP']
	minorp = ['SaM','MaS','SeM','MeS','SiM','MiS','SoM','MoS']
	conclusion = ['SaP','SeP','SiP','SoP']
	alls = []
	allsyl = []
	for i in majorp:
		for j in minorp:
			for k in conclusion:
				alls.append([i,j,k])
#print len(alls)
	valids = []
	for i in alls:
		v,s,d,o = syl(i)
		if v == 'valid':
			valids.append(i)
		allsyl.append([v,s,d,o])
	return allsyl, valids
#print valids
def pretty_print():
	allsyl, valids = all_syl()
	#print len(allsyl)
	labels = ['labelOnlyA={\\footnotesize \\textbf{+}},','labelOnlyAB={\\footnotesize \\textbf{+}},','labelOnlyB={\\footnotesize \\textbf{+}},','labelOnlyAC={\\footnotesize \\textbf{+}},','labelABC={\\footnotesize \\textbf{+}},','labelOnlyBC={\\footnotesize \\textbf{+}},','labelOnlyC={\\footnotesize \\textbf{+}},']
	#labels1 = ['\\fillOnlyA','\\fillACapB','\\fillOnlyB','\\fillACapC','\\fillACapBCapC','\\fillBCapC','\\fillOnlyC']
	print '\documentclass[16pt,a4paper]{article}'
	print '\usepackage[utf8]{inputenc}'
	print '\usepackage[T2A,T1]{fontenc}'
	print '\usepackage{graphicx}'
	print '\usepackage{pbox}'
	#print '\usepackage{amssymb}'
	print '\usepackage{longtable}'
	print '\usepackage{venndiagram}'
	print '\pagenumbering{gobble}'
	#print '\usepackage[cm]{fullpage}'
	print '\usepackage[lmargin=0cm,rmargin=0cm, bottom=0cm, top=0cm]{geometry}'
	#print '\usepackage{hyperref}'
	print '\\begin{document}'
	print '\\begin{longtable}{| c c | c c | c c | c c |}'
	print '\hline'
	
	for i in allsyl:

		if (allsyl.index(i)+1)%4 != 0:
			#print ' & & & & & & & \\\\'
			#print ' & & & & & & & \\\\'
			print '\pbox{20cm}{ '
			count = 0
			for k in i[1]:
				if count == 2:
					print '------\\\\'
				print k,'\scalebox{.5}{',i[3][i[1].index(k)],'} \\\\'
				count=count+1
			print '} &'
			#print 'syl here &'
			print '\\begin{venndiagram3sets}['
			for k,j in enumerate(i[2]):
				if '+' in j:
					print labels[k]
			print 'labelNotABC={',i[0][0],'}]'
			#print ']'
			if 'x' in i[2][0] and 'x' in i[2][3]:
				print '\\fillANotB'
			if 'x' in i[2][1] and 'x' in i[2][2]:
				print '\\fillBNotC'	
			if 'x' in i[2][2] and 'x' in i[2][5]:
				print '\\fillBNotA'
			if 'x' in i[2][3] and 'x' in i[2][6]:
				print '\\fillCNotB'	
			if 'x' in i[2][5] and 'x' in i[2][6]:
				print '\\fillCNotA'
			
			if 'x' in i[2][1] and 'x' in i[2][4]:
				print '\\fillACapB'
			if 'x' in i[2][3] and 'x' in i[2][4]:
				print '\\fillACapC'
			if 'x' in i[2][4] and 'x' in i[2][5]:
				print '\\fillBCapC'
 			print '\end{venndiagram3sets} &'
		else:
			print '\pbox{20cm}{ '
			count = 0
			for k in i[1]:
				if count == 2:
					print '------\\\\'
				print k,'\scalebox{.5}{',i[3][i[1].index(k)],'} \\\\'
				count=count+1
			print '} &'
			print '\\begin{venndiagram3sets}['
			for k,j in enumerate(i[2]):
				if '+' in j:
					print labels[k]
			print 'labelNotABC={',i[0][0],'}]'
			#print ']'
			if 'x' in i[2][0] and 'x' in i[2][3]:
				print '\\fillANotB'
			if 'x' in i[2][1] and 'x' in i[2][2]:
				print '\\fillBNotC'	
			if 'x' in i[2][2] and 'x' in i[2][5]:
				print '\\fillBNotA'
			if 'x' in i[2][3] and 'x' in i[2][6]:
				print '\\fillCNotB'	
			if 'x' in i[2][5] and 'x' in i[2][6]:
				print '\\fillCNotA'
			
			if 'x' in i[2][1] and 'x' in i[2][4]:
				print '\\fillACapB'
			if 'x' in i[2][3] and 'x' in i[2][4]:
				print '\\fillACapC'
			if 'x' in i[2][4] and 'x' in i[2][5]:
				print '\\fillBCapC'
 			print '\end{venndiagram3sets} \\\\ \hline'
	print '\end{longtable}'
	print '\end{document}'

#pretty_print()
#print syl(['MeP','SiM','SoP'])
#print revert('SoP')
#a,b = all_syl()
#print b
