# Simple txt to README.md
# Just download txt and png after updating from
# https://coggle.it/diagram/Wf5mYoJbsgABUF9P and
# run this script
head='# Deep Architecture Genealogy\n' \
     'There are so many new models and archtectures. ' \
     'If you find something inetresting and worth to pay attention, please let us know.\n' \
     '## Mindmap Coggle Link\n' \
     'https://coggle.it/diagram/Wf5mYoJbsgABUF9P\n' \
     '![https://coggle.it/diagram/Wf5mYoJbsgABUF9P](Neural_Net_Arch_Genealogy.png)\n' \
     '## Text Version\n' \
     'This is automatically generated. Please send a PR on the `Neural Net Arch Genealogy.txt` file.\n'

tail = '\n## Contributions\nYour pull requests and issues are always welcome.' \

with open('Neural Net Arch Genealogy.txt') as fin, open('README.md', 'w') as fout:
    fout.write(head)
    for line in fin:
        tab_count = line.count('\t')
        if not tab_count:
            continue

        spaces = ['  ' for i in range(tab_count-1)]
        fout.write(''.join(spaces) + '* ' + line.replace('\t', ''))

    fout.write(tail)
