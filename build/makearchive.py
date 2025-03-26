import os

def main():
    package = input('Package: ')
    os.system(f'mkdir {package}')
    os.system(f'zip -9 -s 64M {package}/{package}.zip {package}.deb')

if __name__ == '__main__':
    main()
