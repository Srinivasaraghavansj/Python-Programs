"https://www.deviantart.com/cookiecat123456/art/Japanese-Alphabet-251191618"
translation = "A = chi B = tsu C = te D = to E = na F = ni G = nu H = ne I = no J = ha K = hi L = fu M = he N = ho O = ma P = mi Q = mu R = me S = mo T = ya U = yu V = yo W = ra X = ri Y = ru Z = re 1 = a 2 = i 3 = u 4 = u 5 = o 6 = ka 7 = ki 8 = ku 9 = ke 0 = --"
translation = translation.replace(' = ',':').split(' ')
translation_dict = {}
for i in translation:
    t = i.split(':')
    translation_dict[t[0]] = t[1]
translation_dict[" "] = " "
name_orig = input("Enter english Name")
name_jap = ""
for i in name_orig:
    name_jap += translation_dict[i.upper()]
print("Japanese Name is",name_jap.capitalize())