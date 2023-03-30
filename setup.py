# %%
import platform
from setuptools import setup
import urllib.request, json 
import zipfile
import io
from setuptools import setup
import os 

PACKAGE_NAME = 'pysu2'

with urllib.request.urlopen("https://api.github.com/repos/su2code/SU2/releases/latest") as url:
    data = json.load(url)
    version = data["tag_name"].replace("v","")

s = setup(
   name=PACKAGE_NAME,
   version=version,
   description='Python wrapper for SU2',
   packages=[PACKAGE_NAME],
   package_data={PACKAGE_NAME: ['*.so', "_pysu2.so.p/*"]}
)
with open("/etc/os-release", "r") as f:
    lines = f.readlines()
for line in lines:
    if line.startswith("VERSION_CODENAME="):
        debian_codename = line.strip().split("=")[1]
        break

python_version_values = platform.python_version().split('.')
url = f"https://github.com/Turbodesigner/pysu2/releases/download/{version}-python-{python_version_values[0]}.{python_version_values[1]}-{debian_codename}-develop/pysu2.zip"
install_dir = f"{os.getcwd()}/{PACKAGE_NAME}"

# Download and extract the ZIP file
with urllib.request.urlopen(url) as response:
    with zipfile.ZipFile(io.BytesIO(response.read())) as zip_file:
        for file_info in zip_file.infolist():
            # Extract the file to the extract directory
            file_info.filename = file_info.filename.replace(f"{PACKAGE_NAME}/", "/")
            zip_file.extract(file_info, install_dir)

files = [f for f in os.listdir(install_dir)]
print(os.getcwd())
print(files)
