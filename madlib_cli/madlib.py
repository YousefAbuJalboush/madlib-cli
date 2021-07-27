import re

def welcome_output():
    print(""" 
        Welcome to madlib game!
        all you need is to think of an example of the below vocabs 
    """)

voc_list=['Adjective','Adjective','A First Name','Past Tense Verb','A First Name','Adjective','Adjective',
'Plural Noun','Large Animal','Small Animal',"A Girl's Nam",'Adjective','Plural Noun','Adjective','Plural Noun',
'Number 1-50',"First Name's",'Number','Plural Noun','Number','Plural Noun']

input_list=[]

def input_voc():
    for i in range (len(voc_list)):
        input_val=input('>> Enter %s  '%(voc_list[i]))
        input_list.append(input_val)




def read_template(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError :
        raise FileNotFoundError('The file not found')
   

def parse_template(read_script):
    modified_script=re.sub('{[^}]+}','{}',read_script)
    removed_str_parts=tuple(re.findall("{(.*?)}",read_script))
    return  modified_script, removed_str_parts


def merge(parsed_script,user_input):
    return parsed_script.format(*user_input)


def script_copy(merged_script):
    with open('./assets/script_copy.txt','wb') as script_write:
         return script_write.write(bytes(merged_script,'utf-8'))


if __name__== '__main__':

    welcome_output()
    input_voc()
    with open('assets/make_me_a_video_game_template.txt' , 'r') as file:
        text = file.read()
    text = re.sub(r"\{(.*?)\}", "{}", text)
    for word in input_list:
        text = text.replace("{}", word, 1)
    with open('assets/game_results.txt' , 'w') as file:
        file.write(text)
    print("************ Game Results ************")
    print(text)
