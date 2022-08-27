import os

working_dir_name = input("Name of working dir: ")
working_dir = os.fsencode(working_dir_name)

saving_dir_name = working_dir_name + "_parsed"
if not os.path.exists(f"./{saving_dir_name}"):
    os.makedirs(f"./{saving_dir_name}")

file_names = []
files = []

for file in os.listdir(working_dir):
    file_name = os.fsdecode(file)
    if file_name != "init.py":
        file_names.append(file_name)
        with open(f"./{working_dir_name}/{file_name}", 'r') as f:
            files.append([])
            for line in f:
                files[-1].append(line)

file_dict = {}
for i in range(len(file_names)):
    file_dict[file_names[i]] = files[i]

txt_for_init = [f"files={str(file_dict)}", f"for k in files:", "\twith open(f'./{k}', 'w') as f:", "\t\tf.write('\\n'.join(files[k]))", "exec('./main.py')"]

with open(f"./{saving_dir_name}/init.py", "w") as f:
    f.writelines('\n'.join(txt_for_init))