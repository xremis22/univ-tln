def moy_I31(cc, ct) :
	note = 0.4*cc + 0.6*ct
	return(note)

def moy_I32(tp, ct) :
	note = (tp+ct)/2
	return(note)

def moy_I33(cc, ct, tp) :
	note = (0.2*cc) + (0.5*ct) + (0.3*tp)
	return(note)

def moy_sem(m_I31, m_I32, m_I33) :
	note = (m_I31 + m_I32 + m_I33)/3
	return(note)

def moy_I41(cc, ct, tp):
	note = (0.2*cc) + (0.5*ct) + (0.3*tp)
	return(note)

def moy_I42(CT1, CT2):
	note = (CT1 + CT2)/2
	return(note)

def moy_I43(ct, tp):
	note = (ct+tp)/2
	return(note)

def bonif(note) :
	if(note>10):
		point = (note - 10)/20
		return(point)
	else :
		return(0)


print("***CALCULATEUR DE MOYENNES***\n")
print("Pour I31\n")
n_i31_cc = float(input("Donnez la note du CC : \n"))
n_i31_ct = float(input("Donnez la note du CT : \n"))
print("La moyenne en I31 est de : \n")
A = moy_I31(n_i31_cc, n_i31_ct)
print(A)

print("Pour I32\n")
n_i32_tp = float(input("Donnez la note de TP : \n"))
n_i32_ct = float(input("Donnez la note du CT : \n"))
print("La moyenne en I32 est de :\n")
B = moy_I32(n_i32_tp, n_i32_ct)
print(B)

print("Pour I33\n")
n_i33_cc = float(input("Donnez la note du CC : \n"))
n_i33_ct = float(input("Donnez la note du CT : \n"))
n_i33_tp = float(input("Donnez la note de TP : \n"))
print("La moyenne en I33 est de :\n")
C = moy_I33(n_i33_cc, n_i33_ct, n_i33_tp)
print(C)

print("Vous avez déjà validé UE34 : Compétences (10/20)\n")
n_cmp = 10.0



print("La moyenne du 1er semestre est de : \n")
first = moy_sem(A, B, C) 
print(first)

print("Pour I41\n")
n_i41_cc = float(input("Donnez la note du CC : \n"))
n_i41_ct = float(input("Donnez la note du CT : \n"))
n_i41_tp = float(input("Donnez la note de TP : \n"))
print("La moyenne en I41 est de :\n")
D = moy_I41(n_i41_cc, n_i41_ct, n_i41_tp)
print(D)


print("Pour I42\n")
n_i42_ct1 = float(input("Donnez la note du CT1 : \n"))
n_i42_ct2 = float(input("Donnez la note du CT2 : \n"))
print("La moyenne en I42 est de :\n")
E = moy_I42(n_i42_ct1, n_i42_ct2)
print(E)

print("Pour I43\n")
n_i43_tp = float(input("Donnez la note de TP : \n"))
n_i43_ct = float(input("Donnez la note du CT : \n"))
print("La moyenne en I43 est de :\n")
F = moy_I43(n_i43_tp, n_i43_ct)
print(F)


print("La moyenne du 2e semestre est de : \n")
sec = moy_sem(D, E, F)
print(sec)

print("La moyenne de l'année est de : \n")
y = (first + sec)/2
print(y)

k = int(input("Donnez la note de bonification :\n"))
p = bonif(k)

print("Ce qui donne : ")
print(y + p)
