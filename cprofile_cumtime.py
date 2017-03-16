import os

root = '/group/vlsiarch/wangyu/bayesian/profiling/edward/'
code_path = os.path.join(root, "examples")
files = os.listdir(code_path)
output = os.path.join(root, "outputs/cprofile_cumtime")
tool = "python tmp.py > " 

head = "import cProfile \n\
pr = cProfile.Profile() \n\
pr.enable()\n"

tail = "\npr.disable() \n\
pr.print_stats(sort='cumtime')\n"

os.chdir(code_path)
for f in files:
  if not ".py" in f:
    continue
  name = f[:-3]
  outname = name + ".cprof"

  fopen = open(f, 'r')
  outfile = open('tmp.py','w')
  state = 0
  for line in fopen:
    if 'import' in line and 'edward' in line:
      outfile.write(head)
      outfile.write(line)
    else:
      outfile.write(line)
  fopen.close()
  outfile.write(tail)
  outfile.close()
    
  command = tool + outname
  os.system(command)
  print f
  os.system('mv ' + outname + " " + os.path.join(output, outname))
  #os.system('rm tmp.py')
  break
