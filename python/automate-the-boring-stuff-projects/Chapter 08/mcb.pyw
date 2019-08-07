 Loads all keywords to clipboard.

import sys, pyperclip, shelve

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    try:
        del mcb_shelf[sys.argv[2]]
    except KeyError:
        print("Error \nKey not found")
        sys.exit()
elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
        elif sys.argv[1].lower() == 'delete':
            for i in mcb_shelf:
                mcb_shelf.clear()


mcb_shelf.close()


