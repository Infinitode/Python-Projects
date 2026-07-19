import os

def numput(prompt, default=0, do=int,use=input):
  try:
    got = use(prompt)
    if got == 'exit':
       raise KeyboardInterrupt
    res = do(got)
  except ValueError:
    print(f"Non-numberic value - Going to parent directory ...")
    res = default
  return res

def filter_dir(listdir):
  files = []
  folders = []
  for obj in listdir:
    if os.path.isfile(obj):
      files.append(obj)
    else:
      folders.append(obj)
  return files, folders

def select_where_to_go(folders):
  if not folders:
     print("- No folders found")
     return ".."
  built = []
  for num in range(1, len(folders) + 1):
    built.append(f"{num}. Folder `{folders[num - 1]}`")
  nums = len(folders) + 1
  built.append(f"{nums}. Parent directory")
  folders.append("..")
  print("\n".join(built))
  return folders[numput(f"Where to go (1~{nums})? ", default=nums) - 1]

def listdirs():
  alls = os.listdir()
  files, folders = filter_dir(alls)
  print("Files:")
  print(("- " + "\n- ".join(files)) if files else "- No files found")
  print("Folders:")
  try:
    os.chdir(select_where_to_go(folders))
  except NotADirectoryError:
    print("ERROR: Selected directory has invalid name or it's not directory")

print("Welcome to file explorer!")
print("Ctrl-C to exit, or type 'exit' to exit")
print()

while True:
  try:
    print(f"\nYou're at {os.getcwd()}")
    listdirs()
  except KeyboardInterrupt:
    print("Exit received")
    break
