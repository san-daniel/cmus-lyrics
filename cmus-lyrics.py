import subprocess, os, time

def main():
    oldtitle = ""
    os.system('cls' if os.name == 'nt' else 'clear')

    while (True):
        query = subprocess.Popen(['cmus-remote', '-Q'], stdout=subprocess.PIPE)
        output =  query.stdout

        for line in output:
            if "tag artist" in str(line):
                artist = line.decode('utf-8').strip('\n')[10:]
            elif "tag title" in str(line):
                title = line.decode('utf-8').strip('\n')[10:]
        if oldtitle != title:
            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.call(['glyrc', 'lyrics', '--artist', artist, '--title', title])
            oldtitle = title
        time.sleep(10)

if __name__ == "__main__": 
    main()
