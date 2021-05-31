# Python 3.9
# Sezgin YILDIRIM
# Ver : 0.4

import bit
import re
import random
import argparse
import time
import sys

t_1 = int(time.time())

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', help = 'ADDRESS', required = True)
#parser.add_argument('-str', '--stride',  help = 'STRIDE', required = True)
#parser.add_argument('-s', '--start', help = 'START', required = True)
#parser.add_argument('-e', '--end', help = 'END', required = True)
args = parser.parse_args()

A=str(args.address)
#x=int(args.start)
#y=int(args.end)
#d=int(args.stride)

ilk1 = 9223372036854775807
ilk2 = 9923372036854775807
son1 = 17446744073709551615
son2 = 18446744073709551615

# DEPO
arti = '+'
eksi = '-'
alt = '\n'
sayac = 0
bulundu = (alt + '\033[92m ------------BULUNDU------------' + alt + '\033[92m *********ADRES BULUNDU*********' + alt + '\033[92m ------------BULUNDU------------')

try:
	while True:
		sayac = sayac + 1
		x=random.randint(ilk1,ilk2)
		y=random.randint(son1,son2)
		print(f'___________{sayac}. AŞAMA___________' + alt + 'Başlangıç : ' + str(x) + alt + 'Bitiş     : ' + str(y))
		# ------------ 1. AŞAMA BAŞLANGIÇ ------------
		yuzde = int(y - x)//2
		for dongu in range(100):
			x_i = str(dongu)
			yuzdeler = int(yuzde * dongu)//100
			yuzde_x = int(x + yuzdeler)
			yuzde_y = int(y - yuzdeler)
			d_x = 'x_' + x_i + '=' + str(yuzde_x)
			d_y = 'y_' + x_i + '=' + str(yuzde_y)
			exec(d_x)
			exec(d_y)
		for r in range(99):
			ran_a = int(r + 1)
			x_i = str(r)
			x_a = str(ran_a)
			r_x = 'r_x_' + x_i + '=random.randint(' + 'x_' + x_i + ', ' + 'x_' + x_a + ')'
			r_y = 'r_y_' + x_i + '=random.randint(' + 'y_' + x_a + ', ' + 'y_' + x_i + ')'
			exec(r_x)
			exec(r_y)
		for p in range(99):
			x_i = str(p)
			px_X = 'p_x_'+x_i+'=bit.Key.from_int('+'x_'+x_i+')'
			py_X = 'p_y_'+x_i+'=bit.Key.from_int('+'y_'+x_i+')'
			pr_x = 'pr_x_'+x_i+'=bit.Key.from_int('+'r_x_'+x_i+')'
			pr_y = 'pr_y_'+x_i+'=bit.Key.from_int('+'r_y_'+x_i+')'
			exec(px_X)
			exec(py_X)
			exec(pr_x)
			exec(pr_y)
		for a in range(99):
			x_i = str(a)
			a_1 = 'p_x_' + x_i + '.address'
			a_2 = 'p_y_' + x_i + '.address'
			a_3 = 'pr_x_' + x_i + '.address'
			a_4 = 'pr_y_' + x_i + '.address'
			addr = str(eval(a_1) + eval(a_2) + eval(a_3) + eval(a_4))
			if re.search (A,addr):
				f=open('BULUNDU.txt', 'a')
				b_1 = "f.write('p_x_: <--> ' + " + "p_x_" + x_i + ".to_wif() + ' <--> ' + " + "p_x_" + x_i + ".address + alt)"
				b_2 = "f.write('p_y_: <--> ' + " + "p_y_" + x_i + ".to_wif() + ' <--> ' + " + "p_y_" + x_i + ".address + alt)"
				b_3 = "f.write('pr_x_: <--> ' + " + "pr_x_" + x_i + ".to_wif() + ' <--> ' + " + "pr_x_" + x_i + ".address + alt)"
				b_4 = "f.write('pr_y_: <--> ' + " + "pr_y_" + x_i + ".to_wif() + ' <--> ' + " + "pr_y_" + x_i + ".address + alt)"
				exec(b_1)
				exec(b_2)
				exec(b_3)
				exec(b_4)
				print(bulundu)
				f.close()
				sys.exit()
		# ------------ 1. AŞAMA BİTİŞ ------------
		# ------------ 2. AŞAMA BAŞLANGIÇ ------------
		yuzde = int(x_1 - x_0)//2
		for dongu in range(100):
			x_i = str(dongu)
			d_x = 'x_' + x_i
			d_y = 'y_' + x_i
			x_X1 = 'x_X1_' + x_i + '_'
			y_X1 = 'y_X1_' + x_i + '_'
			x_Y1 = 'x_Y1_' + x_i + '_'
			y_Y1 = 'y_Y1_' + x_i + '_'
			x_Xp = 'x_Xp1_' + x_i + '_'
			y_Xp = 'y_Xp1_' + x_i + '_'
			x_Yp = 'x_Yp1_' + x_i + '_'
			y_Yp = 'y_Yp1_' + x_i + '_'
			for dongu_22 in range(100):
				x_ii = str(dongu_22)
				yuzdeler = int(yuzde * dongu_22)//100
				x_Xd = x_X1 + x_ii + '=int(' + d_x + arti + str(yuzdeler) + ')' + arti + str(1)
				y_Xd = y_X1 + x_ii + '=int(' + d_x + eksi + str(yuzdeler) + ')' + eksi + str(1)
				x_Yd = x_Y1 + x_ii + '=int(' + d_y + arti + str(yuzdeler) + ')' + arti + str(1)
				y_Yd = y_Y1 + x_ii + '=int(' + d_y + eksi + str(yuzdeler) + ')' + eksi + str(1)
				exec(x_Xd)
				exec(y_Xd)
				exec(x_Yd)
				exec(y_Yd)
				px_X = x_Xp + x_ii + '=bit.Key.from_int(' + x_X1 + x_ii + ')'
				py_X = y_Xp + x_ii + '=bit.Key.from_int(' + y_X1 + x_ii + ')'
				px_Y = x_Yp + x_ii + '=bit.Key.from_int(' + x_Y1 + x_ii + ')'
				py_Y = y_Yp + x_ii + '=bit.Key.from_int(' + y_Y1 + x_ii + ')'
				exec(px_X)
				exec(py_X)
				exec(px_Y)
				exec(py_Y)
				a_1 = x_Xp + x_ii + '.address'
				a_2 = y_Xp + x_ii + '.address'
				a_3 = x_Yp + x_ii + '.address'
				a_4 = y_Yp + x_ii + '.address'
				addr_2 = str(eval(a_1) + eval(a_2) + eval(a_3) + eval(a_4))
				if re.search (A,addr_2):
					f=open('BULUNDU.txt', 'a')
					b_1 = "f.write('b_1: <--> ' + " + x_Xp + x_ii + ".to_wif() + ' <--> ' + " + x_Xp + x_ii + ".address + alt)"
					b_2 = "f.write('b_2: <--> ' + " + y_Xp + x_ii + ".to_wif() + ' <--> ' + " + y_Xp + x_ii + ".address + alt)"
					b_3 = "f.write('b_3: <--> ' + " + x_Yp + x_ii + ".to_wif() + ' <--> ' + " + x_Yp + x_ii + ".address + alt)"
					b_4 = "f.write('b_4: <--> ' + " + y_Yp + x_ii + ".to_wif() + ' <--> ' + " + y_Yp + x_ii + ".address + alt)"
					exec(b_1)
					exec(b_2)
					exec(b_3)
					exec(b_4)
					print(bulundu)
					f.close()
					sys.exit()

		# AŞAMA 2 RANDOM
		for dongu_1 in range(100):
			x_i = str(dongu_1)
			x_X1d = 'x_Xr_' + x_i + '_'
			y_X1d = 'y_Xr_' + x_i + '_'
			x_Y1d = 'x_Yr_' + x_i + '_'
			y_Y1d = 'y_Yr_' + x_i + '_'
			x_X2d = 'x_X1_' + x_i + '_'
			y_X2d = 'y_X1_' + x_i + '_'
			x_Y2d = 'x_Y1_' + x_i + '_'
			y_Y2d = 'y_Y1_' + x_i + '_'
			x_Xp2 = 'x_Xp1_' + x_i + '_'
			y_Xp2 = 'y_Xp1_' + x_i + '_'
			x_Yp2 = 'x_Yp1_' + x_i + '_'
			y_Yp2 = 'y_Yp1_' + x_i + '_'
			for dongu_3 in range(99):
				x_ii = str(dongu_3)
				x_ar = int(dongu_3 + 1)
				x_a = str(x_ar)
				x_Xd = x_X1d + x_ii + '=random.randint(' + x_X2d + x_ii + ', ' + x_X2d + x_a + ')'
				y_Xd = y_X1d + x_ii + '=random.randint(' + y_X2d + x_a + ', ' + y_X2d + x_ii + ')'
				x_Yd = x_Y1d + x_ii + '=random.randint(' + x_Y2d + x_ii + ', ' + x_Y2d + x_a + ')'
				y_Yd = y_Y1d + x_ii + '=random.randint(' + y_Y2d + x_a + ', ' + y_Y2d + x_ii + ')'
				exec(x_Xd)
				exec(y_Xd)
				exec(x_Yd)
				exec(y_Yd)
				px_X = x_Xp2 + x_ii + '=bit.Key.from_int(' + x_X1d + x_ii + ')'
				py_X = y_Xp2 + x_ii + '=bit.Key.from_int(' + y_X1d + x_ii + ')'
				px_Y = x_Yp2 + x_ii + '=bit.Key.from_int(' + x_Y1d + x_ii + ')'
				py_Y = y_Yp2 + x_ii + '=bit.Key.from_int(' + y_Y1d + x_ii + ')'
				exec(px_X)
				exec(py_X)
				exec(px_Y)
				exec(py_Y)
				a_1 = x_Xp2 + x_ii + '.address'
				a_2 = y_Xp2 + x_ii + '.address'
				a_3 = x_Yp2 + x_ii + '.address'
				a_4 = y_Yp2 + x_ii + '.address'
				addr_r3 = str(eval(a_1) + eval(a_2) + eval(a_3) + eval(a_4))
				if re.search (A,addr_r3):
					f=open('BULUNDU.txt', 'a')
					b_1 = "f.write('r1: <--> ' + " + x_Xp2 + x_ii + ".to_wif() + ' <--> ' + " + x_Xp2 + x_ii + ".address + alt)"
					b_2 = "f.write('r2: <--> ' + " + y_Xp2 + x_ii + ".to_wif() + ' <--> ' + " + y_Xp2 + x_ii + ".address + alt)"
					b_3 = "f.write('r3: <--> ' + " + x_Yp2 + x_ii + ".to_wif() + ' <--> ' + " + x_Yp2 + x_ii + ".address + alt)"
					b_4 = "f.write('r4: <--> ' + " + y_Yp2 + x_ii + ".to_wif() + ' <--> ' + " + y_Yp2 + x_ii + ".address + alt)"
					exec(b_1)
					exec(b_2)
					exec(b_3)
					exec(b_4)
					print(bulundu)
					f.close()
					sys.exit()
		"""
		# ------------ 3. AŞAMA BAŞLANGIÇ ------------
		yuzde = int(x_X1_0_1 - x_X1_0_0)//2
		for dongu in range(100):
			iii = int(dongu + 1)
			x_i = str(dongu)
			x_X1 = 'x_X1_' + x_i + '_'
			y_X1 = 'y_X1_' + x_i + '_'
			x_Y1 = 'x_Y1_' + x_i + '_'
			y_Y1 = 'y_Y1_' + x_i + '_'
			x_X2 = 'x_X2_' + x_i + '_'
			y_X2 = 'y_X2_' + x_i + '_'
			x_Y2 = 'x_Y2_' + x_i + '_'
			y_Y2 = 'y_Y2_' + x_i + '_'
			x_Xp = 'x_Xp1_' + x_i + '_'
			y_Xp = 'y_Xp1_' + x_i + '_'
			x_Yp = 'x_Yp1_' + x_i + '_'
			y_Yp = 'y_Yp1_' + x_i + '_'
			for dongu_1 in range(100):
				x_ii = str(dongu_1)
				x_X1d = x_X1 + x_ii
				y_X1d = y_X1 + x_ii
				x_Y1d = x_Y1 + x_ii
				y_Y1d = y_Y1 + x_ii
				x_X2d = x_X2 + x_ii + '_'
				y_X2d = y_X2 + x_ii + '_'
				x_Y2d = x_Y2 + x_ii + '_'
				y_Y2d = y_Y2 + x_ii + '_'
				x_Xp2 = x_Xp + x_ii + '_'
				y_Xp2 = y_Xp + x_ii + '_'
				x_Yp2 = x_Yp + x_ii + '_'
				y_Yp2 = y_Yp + x_ii + '_'
				for dongu_3 in range(100):
					x_iii = str(dongu_3)
					yuzdeler = int(yuzde * dongu_3)//100
					x_Xd = x_X2d + x_iii + '=int(' + x_X1d + arti + str(yuzdeler) + ')' + arti + str(1)
					y_Xd = y_X2d + x_iii + '=int(' + y_X1d + eksi + str(yuzdeler) + ')' + eksi + str(1)
					x_Yd = x_Y2d + x_iii + '=int(' + x_Y1d + arti + str(yuzdeler) + ')' + arti + str(1)
					y_Yd = y_Y2d + x_iii + '=int(' + y_Y1d + eksi + str(yuzdeler) + ')' + eksi + str(1)
					exec(x_Xd)
					exec(y_Xd)
					exec(x_Yd)
					exec(y_Yd)
					px_X = x_Xp2 + x_iii + '=bit.Key.from_int(' + x_X2d + x_iii +')'
					py_X = y_Xp2 + x_iii + '=bit.Key.from_int(' + y_X2d + x_iii + ')'
					px_Y = x_Yp2 + x_iii + '=bit.Key.from_int(' + x_Y2d + x_iii + ')'
					py_Y = y_Yp2 + x_iii + '=bit.Key.from_int(' + y_Y2d + x_iii + ')'
					exec(px_X)
					exec(py_X)
					exec(px_Y)
					exec(py_Y)
					a_1 = x_Xp2 + x_iii + '.address'
					a_2 = y_Xp2 + x_iii + '.address'
					a_3 = x_Yp2 + x_iii + '.address'
					a_4 = y_Yp2 + x_iii + '.address'
					addr_3 = str(eval(a_1) + eval(a_2) + eval(a_3) + eval(a_4))
					if re.search (A,addr_3):
						f=open('BULUNDU.txt', 'a')
						for b in range(1):
							b_1 = "f.write('x_Xp: <--> ' + " + x_Xp2 + x_iii + ".to_wif() + ' <--> ' + " + x_Xp2 + x_iii + ".address + alt)"
							b_2 = "f.write('y_Xp: <--> ' + " + y_Xp2 + x_iii + ".to_wif() + ' <--> ' + " + y_Xp2 + x_iii + ".address + alt)"
							b_3 = "f.write('x_Yp: <--> ' + " + x_Yp2 + x_iii + ".to_wif() + ' <--> ' + " + x_Yp2 + x_iii + ".address + alt)"
							b_4 = "f.write('y_Yp: <--> ' + " + y_Yp2 + x_iii + ".to_wif() + ' <--> ' + " + y_Yp2 + x_iii + ".address + alt)"
							exec(b_1)
							exec(b_2)
							exec(b_3)
							exec(b_4)
						print(bulundu)
						f.close()
						sys.exit()
					x_Xd = 'del [' + x_X2d + x_iii + ']'
					y_Xd = 'del [' + y_X2d + x_iii + ']'
					x_Yd = 'del [' + x_Y2d + x_iii + ']'
					y_Yd = 'del [' + y_Y2d + x_iii + ']'
					exec(x_Xd)
					exec(y_Xd)
					exec(x_Yd)
					exec(y_Yd)
					px_X = 'del [' + x_Xp2 + x_iii + ']'
					py_X = 'del [' + y_Xp2 + x_iii + ']'
					px_Y = 'del [' + x_Yp2 + x_iii + ']'
					py_Y = 'del [' + y_Yp2 + x_iii + ']'
					exec(px_X)
					exec(py_X)
					exec(px_Y)
					exec(py_Y)
					addr_3 = 'del [addr_3]'
					exec(addr_3)
			print("", end=f"\rİlerleme  : %{iii}")
		print(alt)
		# ------------ 3. AŞAMA BİTİŞ ------------
		"""
except ValueError:
	t_2 = int(time.time())
	elapsed = int(t_2 - t_1)
	formatNumber = lambda n: n if n%1 else int(n)
	formatNumber(elapsed)
	print(alt + 'Geçen Süre: {} s.'.format(elapsed))
	print('***********BULUNAMADI***********')
