def open_txt(filename):
	with open(filename, "r", encoding="utf-8") as f:
		l_strip = [s.rstrip() for s in f.readlines()]
	return l_strip

def write_txt_str(filename,sentence:str):
	with open(filename, mode='w',encoding="utf-8") as f:
		f.write(sentence)

import openpyxl

def save_excel(filename,sheetname,savedata):#dataは2x2のリスト	
	wb = openpyxl.Workbook()
	wb.create_sheet(sheetname)
	#print(self.wb.sheetnames)
	#filename="dataset/excel_data/random_data_0.xlsx"
	sheet = wb[sheetname]
	wb.remove(wb['Sheet'])
	for i,data in enumerate(savedata):
		for j,d in enumerate(data):
			#print(savedata[i][j])
			#print(i)
			#print(j)
			sheet.cell(row=i+2,column=j+1,value=savedata[i][j])


	sheet.cell(row=1,column=1,value="AとBの発話")
	sheet.cell(row=1,column=2,value="抽出した情報")
	sheet.cell(row=1,column=3,value="合っているか(o,p,l)")

	from openpyxl.styles.alignment import Alignment
	# write in sheet
	for row in sheet:
		for cell in row:
			if cell.row == 1:

				cell.alignment = Alignment(horizontal = 'center', 
											vertical = 'center',
											wrap_text = False)
			else:
				cell.alignment = Alignment(wrap_text = True)
	for k in range(len(savedata)):
		# 行の高さを変更
		sheet.row_dimensions[k+2].height = 63
	# 列の幅を変更
	sheet.column_dimensions['A'].width = 125
	# 列の幅を変更
	sheet.column_dimensions['B'].width = 25
	# 列の幅を変更
	sheet.column_dimensions['C'].width = 25

	wb.save(filename)

def load_excel(filename):
	
	wb = openpyxl.Workbook()
	wb = openpyxl.load_workbook(filename)
	ws=wb['personas']
	out=[]
	for row in ws.iter_rows():
		out_row=[]
		for cell in row:
			out_row.append(cell.value)
		out.append(out_row)
	return out
	

