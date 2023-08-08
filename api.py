import subprocess
import argparse, os
import json
AVAILABLE_ENV = ["stg", "uat", "local"]
parser = argparse.ArgumentParser(description='Process cURL requests by script in a directory')
parser.add_argument('-d', '--directory', type=str, help='Directory', required=True)
parser.add_argument('-f', '--file', type=str, help='File name', required=True)
parser.add_argument('-e', '--env', type=str, help='File name', required=True)
args = parser.parse_args()
dir = args.directory
file = args.file
env = args.env
if env is None:
  env = "local"
if env not in AVAILABLE_ENV:
  print("Invalid environment")
  exit()
root = os.getcwd()
script_path = root + "/"+ dir + '/' + file
if not os.path.isfile(script_path):
  print("Script not exist")
  exit()
env_file_path="."+env+".env"
completed_process = subprocess.run(['bash', script_path, env_file_path],stdout=subprocess.PIPE,check=True)
output = completed_process.stdout.decode('utf-8')
try:
  output = json.loads(output)
  print(json.dumps(output, indent=4))
except:
  print(output)