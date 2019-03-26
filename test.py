import os
import shutil
import sys
import zipfile


if len(sys.argv) not in [2, 3]:
    print("Usage: ./scripts/kattis_open problemname [language]")
    print("The language is cpp by default and can be either 'cpp' or 'py'")
    exit(0)

language = 'cpp'
if len(sys.argv) == 3 and sys.argv[2] == "py":
    language = 'py'

problemname = sys.argv[1]
#  problem_test = os.path.join('tests', problemname)
problem_test = os.path.join(problemname)

exists = False

try:
    os.mkdir(problem_test)
except FileExistsError:
    exists = True
    print("Test folder already exists")

if exists == False:
    sample_url = 'https://open.kattis.com/problems/{}/file/statement/samples.zip'
    url = sample_url.format(problemname)
    # For some reason python http lib gets 403 forbidden ??? Just use wget instead -.-
    os.system('wget -q {}'.format(url))
    try:
        local_zip = 'samples.zip'
        f = zipfile.ZipFile(local_zip)
        f.extractall(problem_test)
        os.remove(local_zip)
        print("Samples fetched from kattis and put into tests folder")
    except:
        print('Could not download sample input.' \
            + ' Perhaps none exist on Kattis or you do not have internet connection?')

#  problem_dir = os.path.join('kattis', problemname)

RED = '\x1b[38;5;1m'
GREEN = '\x1b[38;5;2m'
NULL = '\x1b[0m'

#  is_python = os.path.isfile(os.path.join(problem_dir, '{}.py'.format(problemname)))
is_cpp = os.path.isfile(os.path.join('{}.cpp'.format(problemname)))

test_dir = os.path.join(problemname)
testing_items = os.listdir(test_dir)
def ends_in(x):
    return lambda string: string.endswith(x)
ans = list(sorted(filter(ends_in('.ans'), testing_items)))
ins = list(sorted(filter(ends_in('.in'), testing_items)))
testing_tuples = zip(ins, ans)

try:
    os.mkdir('tmp')
except OSError:
    pass

#  items = os.listdir(problem_dir)
if is_cpp:
    CC = 'g++ -std=c++14 -O2 -Wall -pedantic -o tmp/prg -I{}'.format(problemname)
    os.system('{} {}'.format(CC, os.path.join('{}.cpp'.format(problemname))))

    def test_for(in_file):
        os.system('./tmp/prg < {} > tmp/output'.format(os.path.join(test_dir, in_file)))

#  elif is_python:
#      path = os.path.join(problem_dir, '{}.py'.format(problemname))
#      with open(path, 'r') as f:
#          firstline = f.readline().strip()
#      if 'python3' in firstline:
#          cmd = 'python3'
#      else:
#          cmd = 'python2'
#
#      def test_for(in_file):
#          os.system('{} {} < {} > tmp/output'.format(cmd, path, os.path.join(test_dir, in_file)))


no_bad_ones = True
for in_file, ans_file in testing_tuples:
    test_for(in_file)
    try:
        os.system('diff -Z tmp/output {} > tmp/diff'.format(os.path.join(test_dir, ans_file)))
    except:
        os.system('diff tmp/output {} > tmp/diff'.format(os.path.join(test_dir, ans_file)))
    res = os.stat('tmp/diff')
    if res.st_size > 0:
        no_bad_ones = False
        print('{}===> {} {}'.format(RED, in_file, NULL).rstrip())
        with open('tmp/diff', 'r') as f:
            for line in f:
                print(line.rstrip())

if no_bad_ones:
    print("{}✔ - AC{}".format(GREEN, NULL))
os.system('rm -rf tmp')

