import os
import shutil

def copy_project_structure(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    guide_lines = []
    
    for root, dirs, files in os.walk(src):
        for dir in dirs:
            src_dir = os.path.join(root, dir)
            dest_dir = os.path.join(dest, os.path.relpath(src_dir, src))
            os.makedirs(dest_dir)
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest, os.path.relpath(src_file, src))
            shutil.copyfile(src_file, dest_file)
            
            if file.endswith('.cs'):
                guide_lines.append(os.path.relpath(src_file, src))
    
    guide_path = os.path.join(dest, 'guide.txt')
    with open(guide_path, 'w') as guide_file:
        for line in guide_lines:
            guide_file.write(line + '\n')

# Example usage
if __name__ == "__main__":
    source_project = 'projects/csharp_project'
    destination_project = 'projects/python_project-Py'
    copy_project_structure(source_project, destination_project)
