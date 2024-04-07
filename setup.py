from setuptools import find_packages,setup
hypen_e='-e .'

__version__ = "0.0.0"
def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace('\n','') for r in requirements]
    if hypen_e in requirements:
        requirements.remove(hypen_e) 
    return requirements    

setup(
    name="Text -Summarization-project",
    author="Atheeq",
    author_email="syed21ad067@rmkcet.ac.in",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)