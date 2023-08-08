try:
  import subprocess
  import argparse, os
  import json
  parser = argparse.ArgumentParser(description='Process cURL requests by script in a directory')
  parser.add_argument('-d', '--directory', type=str, help='Directory', required=True)
  parser.add_argument('-f', '--file', type=str, help='File name', required=True)
  parser.add_argument('-e', '--env', type=str, help='Environment')
  args = parser.parse_args()
  dir = args.directory
  file = args.file
  env = args.env
  if env is None:
    env = ""

  root = os.getcwd()
  env_file_path=env+".env"
  script_path = root + "/"+ dir + '/' + file
  if not os.path.isfile(script_path):
    print("Script not exist")
    exit()
  if not os.path.isfile(env_file_path):
    print("Environment not exist")
    exit()
  completed_process = subprocess.run(['bash', script_path, env_file_path],stdout=subprocess.PIPE,check=True)
  output = completed_process.stdout.decode('utf-8')
  try:
    output = json.loads(output)
    print(json.dumps(output, indent=4))
  except:
    print(output)
except Exception as e:
  print("Error", e)