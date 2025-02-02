PLACEHOLDER="[name]"

with open(r"Mail Merge Project Start\Input\Letters\starting_letter.txt",mode='r') as blueprint:
    data=blueprint.read()

with open(r"Mail Merge Project Start\Input\Names\invited_names.txt",mode='r') as list:
    names=list.readlines()
    for i in names:
        new_i=i.strip()
        data1=data.replace('[name]',new_i)
        with open(f"Mail Merge Project Start\Output\ReadyToSend\letter_for_{new_i}.docx",'w') as letter:
            letter.write(data1)


