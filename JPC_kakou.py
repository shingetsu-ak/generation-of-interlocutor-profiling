#coding: utf8

import openpyxl
import misc


def JPC2txt():
	
	original_name = "japanese_persona_chat.xlsx"
	text_name = "persona_chat.txt"

	wb = openpyxl.load_workbook(original_name, data_only=True)
	ws = wb["対話"]
	dialog = []
	log_num = "0"
	for lines in ws:
		lines = list(lines)
		if lines[0].value == "No":
			continue
		if lines[0].value != log_num:
			dialog.append("@@@")
			log_num=lines[0].value
		sid, spk, utt = [v.value for v in lines][1:4]
		utt = utt.replace("\n", "")
		dialog.append(utt)
	misc.write_txt_str(text_name,"\n".join(dialog))

def make_utts_id():
	
	text_name = "persona_chat.txt"
	utt_and_id_filename = "utts_and_ids.txt"

	lines=misc.open_txt(text_name)
	context_num=2
	dialogs=[]
	context_num=context_num
	dialog=[]
	for line in lines:
		if line=="@@@":
			if len(dialog)!=0:
				dialogs.append(dialog)
			dialog=[]
			continue
		dialog.append(line)
	dialogs.append(dialog)

	###対話形式（persona_chat.txtを参照）から、三つづつの発話に加工
	three_utts=make_uttwithcontexts(context_num,dialogs)

	###三つづつの発話を「Aの発話：～」の形に加工
	formed_utts=set_form(three_utts)
	misc.write_txt_str(utt_and_id_filename,"\n".join(formed_utts))

	utts_with_id={}
	for l in formed_utts:
		u,i = l.split("@@@")
		utts_with_id[i]=u
	
	return utts_with_id
   
def make_uttwithcontexts(context_num:int =2,dialogs:list =[]):
	##2発話を文脈として
	utt_with_context=[]
	for dialog in dialogs:
		for i, _ in enumerate(dialog):
			s=i-context_num
			if s<0:
				s=0
			utt_with_context.append(dialog[s:i+1])
	return utt_with_context

def set_form(dialogs:list[list] = []):
	prompts=[]
	utts_id=0
	for utts in dialogs:
		prompt=""
		for i,u in enumerate(reversed(utts)):
			if i==0:
				prompt = "Aの最後の発話: " + u + "" + prompt
			elif i%2==0:
				prompt = "Aの発話: " + u + "\t" + prompt
			else:
				prompt = "Bの発話: " + u + "\t" + prompt
		
		prompts.append(prompt+"@@@"+str(utts_id))
		utts_id+=1
	return prompts

if __name__ == "__main__":
	JPC2txt()
	utts_with_id=make_utts_id()
	