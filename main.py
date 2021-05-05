from git import Repo
import os
import os.path

path = '.'
commit = 'test'
site_path = 'https://awieczarek.github.io/StudentsGames/Classes'
classes_path = '.\\classes'
title = '# StudentsGames'
description = 'Games made by my students in Construct 3.'

class Games():
    def git_push(self):
        try:
            repo = Repo(path)
            repo.git.add('.')
            repo.index.commit(commit)
            origin = repo.remote(name='origin')
            origin.push()
        except:
            print('Error')

    def dir_list(self, path):
        final_path = classes_path + '\\' + path
        dir_list = next(os.walk(final_path))[1]
        return dir_list

    def make_index(self, path):
        dir = self.dir_list('')
        for x in dir:
            if not self.if_exists(x):
                f = open(classes_path+ '\\' + x + '\\'+ "index.htm", "a")
                template = open('start_html.txt', 'r')
                lines = template.readlines()
                for y in lines:
                    f.write(y+'\n')
                template.close()
                f.write(classes_path+ '\\' + x)
                template = open('end_html.txt', 'r')
                lines = template.readlines()
                for y in lines:
                    f.write(y+'\n')
                template.close()
                f.close()

    def add_to_readme(self):
        f = open('README.md', 'w')
        dirs = self.dir_list('')
        f.write(title + '\n')
        f.write(description + '\n')
        for dir in dirs:
            f.write('- [' + dir + '](' + site_path + '/' + dir + '/index.htm)\n')


    def if_exists(self, path):
        try:
            f = open(classes_path+ '\\'+ path + '\\'+ "index.htm")
            f.close()
            return True
        except IOError:
            return False


if __name__ == "__main__":
    g = Games()
    g.add_to_readme()
    g.git_push()